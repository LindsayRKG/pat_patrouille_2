# app.py

"""
Module principal de l'application Flask pour le solveur d'équations.
Définit les routes et la logique de l'interface web.
"""

from flask import Flask, render_template, request
from typing import Dict, Union, Callable

from solveur_equation import resoudre_equation


# --- Initialisation de l'application ---
app = Flask(__name__)


# --- Définition des routes ---

@app.route("/")
def index() -> str:
    """Affiche la page d'accueil avec le formulaire."""
    return render_template("index.html")


@app.route("/resoudre", methods=["POST"])
def resoudre() -> str:
    """Traite les données du formulaire et affiche le résultat."""
    try:
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
    except (ValueError, KeyError):
        erreur = "Veuillez entrer des nombres valides pour les coefficients a, b et c."
        return render_template("index.html", erreur=erreur)

    resultat = resoudre_equation(a, b, c)
    return render_template("resultat.html", a=a, b=b, c=c, resultat=resultat)


def formater_racine(racine: Union[float, complex]) -> str:
    """Formate une racine (réelle ou complexe) pour l'affichage."""
    if isinstance(racine, complex):
        partie_reelle = f"{racine.real:.2f}"
        partie_imaginaire = f"{abs(racine.imag):.2f}"
        signe = "+" if racine.imag >= 0 else "-"
        return f"{partie_reelle} {signe} {partie_imaginaire}i"
    else:
        return f"{racine:.2f}"


@app.context_processor
def inject_utils() -> Dict[str, Callable[[Union[float, complex]], str]]:
    """Injecte des fonctions utiles dans le contexte des templates."""
    return dict(formater_racine=formater_racine)


# --- Point d'entrée pour l'exécution directe ---
if __name__ == "__main__":
    app.run(debug=True)
