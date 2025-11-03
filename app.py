# app.py
import os # <-- Import inutilisé, mais flake8 le verra déjà.
une_variable_totalement_inutilisee = "ceci est une erreur" # <-- Ajoutons cette ligne

from flask import Flask, render_template, request, flash
from typing import Tuple, Union
import cmath

# --- 1. Logique métier ---


def resoudre_equation_second_degre(
    a: float, b: float, c: float
) -> Union[str, Tuple[complex, complex]]:
    """Résout l'équation ax² + bx + c = 0."""
    if a == 0:
        return "Le coefficient 'a' ne peut pas être nul."

    delta = (b**2) - (4 * a * c)
    racine1 = (-b - cmath.sqrt(delta)) / (2 * a)
    racine2 = (-b + cmath.sqrt(delta)) / (2 * a)
    return (racine1, racine2)


# --- NOUVELLE FONCTION D'AIDE POUR LE FORMATAGE ---
def formater_racine(racine: complex) -> str:
    """Formate un nombre complexe pour un affichage lisible."""
    # Arrondit à 2 décimales pour éviter les imprécisions de float
    real_part = round(racine.real, 2)
    imag_part = round(racine.imag, 2)

    if imag_part == 0:
        # C'est un nombre réel
        return f"{real_part:.2f}"
    else:
        # C'est un nombre complexe, on le formate joliment
        signe = "+" if imag_part > 0 else "-"
        return f"{real_part:.2f} {signe} {abs(imag_part):.2f}j"


# --- 2. Application Flask ---

app = Flask(__name__)
# Clé secrète nécessaire pour utiliser `flash` (messages d'erreur)
app.secret_key = "une-cle-secrete-tres-difficile-a-deviner"


@app.route("/")
def index() -> str:
    """Affiche la page d'accueil avec le formulaire."""
    return render_template("index.html")


@app.route("/resoudre", methods=["POST"])
def resoudre() -> str:
    """Traite les  données du  formulaire et affiche  le résultat."""
    try:
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
    except (ValueError, KeyError):
        flash("Entrée invalide. Veuillez fournir trois nombres .", "error")
        return render_template("index.html")

    resultat = resoudre_equation_second_degre(a, b, c)

    if isinstance(resultat, str):
        flash(resultat, "error")
        return render_template("index.html", a=a, b=b, c=c)
    else:
        # Affiche la page de résultat en passant la fonction de formatage
        return render_template(
            "resultat.html",
            a=a,
            b=b,
            c=c,
            resultat=resultat,
            formater_racine=formater_racine,  # <-- L'ajout important est ici
        )


# --- 3. Point d'entrée ---

if __name__ == "__main__":
    app.run(debug=True)
