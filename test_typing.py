# test_typing.py
def saluer(nom: str) -> None:
    print(f"Bonjour, {nom}")


# Erreur de type : on passe un entier au lieu d'une chaîne de caractères
saluer("Pat'patrouille")
