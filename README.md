# Projet Pat'patrouille

Bienvenue sur le projet ! Pour garantir la qualité, la cohérence et la robustesse de notre code, nous utilisons un système de **hooks pre-commit**.

Ce système exécute automatiquement des vérifications sur le code avant que chaque commit ne soit finalisé.

## À quoi ça sert ?

L'objectif principal est d'automatiser les contrôles de qualité pour :
1.  **Garantir le typage statique** : Nous utilisons `mypy` pour vérifier que tout le code respecte les annotations de type Python. Cela permet de détecter de nombreux bugs avant même l'exécution.
2.  **Bloquer les commits non conformes** : Si une erreur de typage est détectée, le commit est automatiquement annulé, avec un message indiquant l'erreur à corriger.
3.  **Maintenir un code propre** : En nous assurant que seules des contributions de qualité sont intégrées à notre base de code.

## 🚀 Mise en place (à faire une seule fois)

Chaque collaborateur doit suivre ces étapes après avoir cloné le projet pour la première fois.

### 1. Prérequis

Assurez-vous d'avoir **Python** et **pip** installés sur votre machine. Il est fortement recommandé de travailler dans un **environnement virtuel**.

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

Installez les outils nécessaires, y compris le framework `pre-commit`.

```bash
pip install -r requirements.txt  # Si vous avez un fichier requirements.txt
pip install pre-commit mypy
```

### 3. Activation des hooks

Installez les hooks dans votre configuration Git locale. `pre-commit` se chargera de les exécuter automatiquement avant chaque commit.

```bash
pre-commit install

ou

python -m pre_commit install

```
python -m pre_commit run --all-files

Et c'est tout ! Votre environnement est prêt.

## Comment ça marche au quotidien ?

1.  **Travaillez comme d'habitude** : Modifiez votre code, puis utilisez `git add` pour préparer vos fichiers.

2.  **Faites votre commit** :
    ```bash
    git commit -m "Votre message de commit"
    ```

3.  **Observez le résultat** :
    *   **Si tout est bon** : Les vérifications passent (`...Passed`) et votre commit est créé normalement.
    *   **S'il y a une erreur** : Le hook échouera (`...Failed`), affichera un message d'erreur clair (par exemple, une erreur de type détectée par `mypy`), et **le commit sera bloqué**.

4.  **Corrigez et recommencez** :
    *   Corrigez l'erreur signalée dans votre code.
    *   Faites `git add` sur le fichier corrigé.
    *   Relancez la commande `git commit`.

## Commandes utiles

- **Exécuter les hooks sur tous les fichiers du projet** (utile pour tout vérifier d'un coup) :
  ```bash
  pre-commit run --all-files
  ```

- **Passer outre les vérifications (non recommandé)** :
  Si vous devez absolument faire un commit en urgence sans passer les vérifications, vous pouvez utiliser l'option `--no-verify`. À utiliser avec une extrême prudence !
  ```bash
  git commit -m "Message" --no-verify
  ```

---

