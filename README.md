# Projet Solveur d'Équations & Revue de Code par IA

Bienvenue sur le projet ! Il s'agit d'une application web développée avec **Flask** qui résout des équations du second degré. Ce projet intègre également un système avancé de revue de code automatisée par une IA (Google Gemini) après chaque `push`.

Pour garantir la robustesse et la fiabilité du code, nous utilisons un système de **hooks pre-commit** et des **workflows GitHub Actions**.

## Stack Technique & Fonctionnalités

*   **Langage** : Python 3
*   **Framework Web** : Flask
*   **Qualité du code** :
    *   `mypy` : Un vérificateur de typage statique en mode strict, exécuté localement (`pre-commit` et `pre-push`) et côté serveur (GitHub Actions) pour prévenir les erreurs de type.
*   **Intégration Continue (CI)** :
    *   **GitHub Actions** :
        1.  **Vérification du Typage** : Valide automatiquement que tout le code poussé respecte les annotations de type.
        2.  **Revue de Code par IA** : Après un `push` réussi, un script analyse les modifications avec l'API Gemini, génère une revue de code et l'envoie par email à l'auteur du push.

## 🚀 Mise en place (à faire une seule fois)

Chaque collaborateur doit suivre ces étapes après avoir cloné le projet pour la première fois.

### 1. Prérequis

Assurez-vous d'avoir **Python 3** et **pip** installés. Il est **fortement recommandé** de travailler dans un environnement virtuel.

```bash
# Créez un environnement virtuel (si ce n'est pas déjà fait)
python -m venv .venv

# Activez-le
# Sur Windows (PowerShell/Git Bash)
source .venv/Scripts/activate
# Sur macOS/Linux
source .venv/bin/activate
```

### 2. Installation des dépendances

Installez toutes les dépendances du projet, y compris Flask, Mypy et les bibliothèques pour l'IA, en une seule commande.

```bash
pip install -r requirements.txt
```

### 3. Activation des hooks Git

Installez les hooks dans votre configuration Git locale. `pre-commit` se chargera d'exécuter `mypy` automatiquement avant chaque commit et chaque push.

```bash
pre-commit install

ou

python -m pre_commit install

```
python -m pre_commit run --all-files

Et c'est tout ! Votre environnement est prêt.

## 💻 Utilisation au quotidien

### 1. Lancer l'application web

Pour démarrer le serveur de développement Flask :

```bash
# Assurez-vous que votre environnement virtuel est activé
python app.py
```
L'application sera accessible dans votre navigateur à l'adresse `http://127.0.0.1:5000`.

### 2. Workflow de commit et de push

1.  **Travaillez comme d'habitude** : Modifiez votre code, puis utilisez `git add` pour préparer vos fichiers.

2.  **Faites votre commit** :
    ```bash
    git commit -m "Votre message de commit"
    ```
    `mypy` s'exécutera. S'il y a une erreur de type, le commit sera bloqué. Corrigez l'erreur, faites `git add`, puis recommencez.

3.  **Poussez votre code** :
    ```bash
    git push
    ```
    `mypy` s'exécutera une dernière fois comme filet de sécurité. Si tout est bon, le code est envoyé sur GitHub, ce qui déclenchera les GitHub Actions (vérification et envoi de l'email de revue IA ).

## ⚙️ Configuration Côté Serveur (Secrets)

Pour que la revue de code par IA et l'envoi d'email fonctionnent, les secrets suivants doivent être configurés dans les paramètres du dépôt GitHub (`Settings` > `Secrets and variables` > `Actions`) :

*   `GEMINI_API_KEY` : Votre clé d'API pour Google Gemini.
*   `GMAIL_APP_PASSWORD` : Un **mot de passe d'application** généré depuis votre compte Google (ne pas utiliser votre mot de passe principal).
*   `SENDER_EMAIL` : L'adresse email Gmail utilisée pour l'envoi.

## Commandes utiles

- **Exécuter `mypy` sur tous les fichiers du projet** :
  ```bash
  pre-commit run --all-files
  ```

- **Passer outre les vérifications (non recommandé)** :
  Si vous devez absolument faire un commit ou un push en urgence, vous pouvez utiliser l'option `--no-verify`. À utiliser avec une extrême prudence !
  ```bash
  git commit -m "Message" --no-verify
  git push --no-verify
  ```

---
