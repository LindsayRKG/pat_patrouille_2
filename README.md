# Projet Solveur d'Équations

Bienvenue sur le projet ! Il s'agit d'une application web développée avec **Flask** qui permet de résoudre des équations du second degré.

Pour garantir la qualité, la cohérence et la robustesse de notre code, nous utilisons un système de **hooks pre-commit** qui exécute des vérifications automatiques avant chaque commit.

## Stack Technique

*   **Langage** : Python 3
*   **Framework Web** : Flask
*   **Qualité du code** : `pre-commit` avec les hooks suivants :
    *   `black` : Formatage automatique du code.
    *   `flake8` : Détection des erreurs de style (linting).
    *   `mypy` : Vérification du typage statique en mode strict.

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

Installez toutes les dépendances du projet, y compris Flask et les outils de développement, en une seule commande.

```bash
pip install -r requirements.txt
```

### 3. Activation des hooks Git

Installez les hooks dans votre configuration Git locale. `pre-commit` se chargera de les exécuter automatiquement avant chaque commit.

```bash
pre-commit install
```
Et c'est tout ! Votre environnement est prêt.

## 💻 Utilisation au quotidien

### 1. Lancer l'application web

Pour démarrer le serveur de développement Flask :

```bash
# Assurez-vous que votre environnement virtuel est activé
python app.py
```
L'application sera accessible dans votre navigateur à l'adresse `http://127.0.0.1:5000`.

### 2. Workflow de commit

1.  **Travaillez comme d'habitude** : Modifiez votre code, puis utilisez `git add` pour préparer vos fichiers.

2.  **Faites votre commit** :
    ```bash
    git commit -m "Votre message de commit"
    ```

3.  **Observez le résultat** :
    *   **Si tout est bon** : Les vérifications (`black`, `flake8`, `mypy` ) passent (`...Passed`) et votre commit est créé.
    *   **S'il y a une erreur** : Un ou plusieurs hooks échoueront (`...Failed`). Le commit sera **bloqué** et un message clair vous indiquera les erreurs à corriger.

4.  **Corrigez et recommencez** :
    *   **Erreur `black`** : `black` a déjà reformaté les fichiers pour vous. Il suffit d'ajouter ses modifications avec `git add <fichier_modifié>`.
    *   **Erreur `flake8` ou `mypy`** : Lisez le message d'erreur, corrigez le problème dans votre code, puis faites `git add <fichier_corrigé>`.
    *   Relancez ensuite la commande `git commit`.

## Commandes utiles

- **Exécuter les hooks sur tous les fichiers du projet** (utile pour tout vérifier d'un coup) :
  ```bash
  pre-commit run --all-files
  ```

- **Mettre à jour les hooks** vers les dernières versions compatibles :
  ```bash
  pre-commit autoupdate
  ```

- **Passer outre les vérifications (non recommandé)** :
  Si vous devez absolument faire un commit en urgence, vous pouvez utiliser l'option `--no-verify`. À utiliser avec une extrême prudence !
  ```bash
  git commit -m "Message" --no-verify
  ```

---
