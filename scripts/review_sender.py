# scripts/review_sender.py

import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Optional

# On utilise bien la bibliothèque 'google-generativeai'
# et on ignore les erreurs de type car elle n'a pas de stubs
from google import generativeai as genai  # type: ignore

# --- Configuration ---
GEMINI_API_KEY: str = os.environ.get("GEMINI_API_KEY", "")
GMAIL_APP_PASSWORD: str = os.environ.get("GMAIL_APP_PASSWORD", "")
SENDER_EMAIL: str = os.environ.get("SENDER_EMAIL", "")

if not all([GEMINI_API_KEY, GMAIL_APP_PASSWORD, SENDER_EMAIL]):
    print("Erreur: Un ou plusieurs secrets ne sont pas configurés.")
    sys.exit(1)

# --- Récupération des arguments ---
if len(sys.argv) < 3:
    print("Erreur: Email du destinataire et fichiers modifiés sont requis.")
    sys.exit(1)

RECIPIENT_EMAIL: str = sys.argv[1]
CHANGED_FILES: List[str] = sys.argv[2].split()
PREVIOUS_JOB_STATUS: Optional[str] = sys.argv[3] if len(sys.argv) > 3 else None


# --- Fonctions d'aide (inspirées de votre code) ---
def get_file_content(file_path: str) -> str:
    """Lit les 100 premières lignes d'un fichier."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = "".join(f.readlines()[:100])
        return f"--- Contenu du fichier: {file_path} ---\n{content}\n"
    except Exception as e:
        return f"--- Impossible de lire le fichier: {file_path} (Erreur: {e}) ---\n"


def generate_prompt(changed_files: List[str]) -> str:
    """Génère le prompt pour l'IA en incluant le contenu des fichiers."""
    prompt = (
        "Vous êtes un expert en revue de code. Votre tâche est d'analyser les changements de code suivants, "
        "en vous concentrant sur la qualité, la cohérence, les erreurs potentielles et les améliorations. "
        "Après l'analyse, vous devez générer une réponse **uniquement** sous forme de code HTML complet et esthétique "
        "pour un e-mail de feedback. L'e-mail doit être très beau, professionnel et convivial. "
        "Si le code est impeccable, dites-le. S'il y a des erreurs ou des suggestions, mentionnez-les clairement, "
        "en indiquant les lignes si possible, et proposez des corrections. "
        "Le code HTML doit être complet (avec <html>, <body>, etc.) et utiliser des styles en ligne (CSS) "
        "pour garantir un bon affichage dans tous les clients de messagerie. Utilisez une palette de couleurs agréable (par exemple, bleu, vert, gris clair)."
        "\n\n"
        "--- Fichiers Modifiés ---\n"
    )
    for file in changed_files:
        if file.startswith(".github/") or file.endswith(
            (".png", ".jpg", ".gif", ".bin")
        ):
            continue
        prompt += get_file_content(file)
    return prompt


# --- FONCTION CORRIGÉE SELON VOTRE CODE DE RÉFÉRENCE ---
def get_ai_review(prompt: str) -> str:
    """Appelle l'API Gemini pour obtenir la revue de code HTML."""
    try:
        # On utilise la syntaxe genai.Client() comme dans votre code
        client = genai.Client(api_key=GEMINI_API_KEY)

        # On utilise le nom de modèle de votre code, en ajoutant le préfixe 'models/'
        response = client.models.generate_content(
            model="models/gemini-1.5-flash",
            contents=prompt,
        )

        html_content: str = response.text.strip()
        if html_content.startswith("```html"):
            html_content = html_content.strip("```html").strip("```").strip()
        return html_content
    except Exception as e:
        return f"<h1>Erreur d'API Gemini</h1><p>Impossible d'obtenir la revue de code. Erreur: {e}</p>"


def send_email(recipient: str, subject: str, html_body: str) -> None:
    """Envoie l'email HTML via SMTP (Gmail)."""
    try:
        msg = MIMEMultipart("alternative")
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(html_body, "html"))
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        server.close()
        print(f"Succès: Email de revue de code envoyé à {recipient}")
    except Exception as e:
        print(f"Erreur: Échec de l'envoi de l'email à {recipient}. Erreur: {e}")
        print("\n--- Contenu HTML non envoyé (pour débogage) ---\n")
        print(html_body)
        print("\n----------------------------------------------------\n")


# --- Logique principale ---
if __name__ == "__main__":
    print(f"Début de l'analyse pour le push de: {RECIPIENT_EMAIL}")
    print(f"Statut du job de vérification: {PREVIOUS_JOB_STATUS}")

    if PREVIOUS_JOB_STATUS == "failure":
        email_subject = "❌ Action Requise : Votre push a échoué aux vérifications de qualité"
    elif PREVIOUS_JOB_STATUS == "success":
        email_subject = "✅ Revue de Code Automatisée - Push réussi"
    else:
        email_subject = "Revue de Code Automatisée - Push sur ai-projet-git"

    review_prompt = generate_prompt(CHANGED_FILES)
    html_review = get_ai_review(review_prompt)
    send_email(RECIPIENT_EMAIL, email_subject, html_review)
