# charfun.py

"""
Programa que determina si una cadena proporcionada por el usuario es palíndroma.
Para ello se preguntará por teclado al usuario tantas veces como quiera hasta que
escriba la palabra salir.


Ultima Modificación: 03/12/2024
Autor: Gregorio Coronado Morón
Dependencias: Unicodedata
"""


import unicodedata

def esPalindromo(cadena):

    """
    Función que verifica si una cadena es palíndroma. Ignora espacios,
    mayúsculas y tildes.
    """

    # Convertir la cadena a minúsculas y eliminar caracteres no alfabéticos.
    # unicodedata.normalize('NFD',char) descompone los caracteres acentuados en
    # su equivalente base.

    if not ininstance(cadena, str):
        raise TypeError(f"La entrada debe ser una cadena de texto, pero se ha recibido {type(cadena).__name__}.")

    cadena_limpia = ''.join(unicodedata.normalize('NFD',char).encode('ascii','ignore').decode('utf-8').lower()
        for char in cadena if char.isalnum())

    # Comparar la cadena limpia con su reverso

    return cadena_limpia == cadena_limpia[::-1]
 