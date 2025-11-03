# solveur_equation.py

"""
Module dédié à la logique de résolution des équations du second degré.
"""

import cmath
from typing import Tuple, Dict, Any, Union  # On réintroduit Union

# Définition d'un type pour représenter le résultat
ResultatEquation = Dict[str, Any]


def resoudre_equation(a: float, b: float, c: float) -> ResultatEquation:
    """
    Résout une équation du second degré de la forme ax² + bx + c = 0.

    Args:
        a (float): Le coefficient de x².
        b (float): Le coefficient de x.
        c (float): Le terme constant.

    Returns:
        Un dictionnaire contenant le discriminant et les racines.
    """
    # On définit la variable une seule fois avec un type qui couvre tous les cas
    racines: Union[Tuple[float, ...], Tuple[complex, ...], str]

    if a == 0:
        if b == 0:
            return {"discriminant": None, "racines": "Pas une équation valide."}
        else:
            racine = -c / b
            racines = (racine,)
            return {"discriminant": None, "racines": racines}

    delta = (b**2) - (4 * a * c)

    if delta > 0:
        racine1 = (-b - delta**0.5) / (2 * a)
        racine2 = (-b + delta**0.5) / (2 * a)
        racines = (racine1, racine2)
    elif delta == 0:
        racine = -b / (2 * a)
        racines = (racine,)
    else:
        racine1 = (-b - cmath.sqrt(delta)) / (2 * a)
        racine2 = (-b + cmath.sqrt(delta)) / (2 * a)
        racines = (racine1, racine2)

    return {"discriminant": delta, "racines": racines}
