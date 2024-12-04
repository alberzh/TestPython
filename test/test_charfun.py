# test_charfun.py
import unittest
from app.scripts.charfun import esPalindromo

class TestCharfun(unittest.TestCase):
    def test_palindromo(self):
        self.assertTrue(esPalindromo("radar")) # Palíndromo Simple
        self.assertTrue(esPalindromo("A man, a plan, a canal, Panama")) # Palíndromo con espacios y mayúsculas
        self.assertFalse(esPalindromo("hola"))
        self.assertFalse(esPalindromo("python"))

    def test_cadena_vacia(self):
        self.assertFalse(esPalindromo("")) # Cadena vacía
        self.assertFalse(esPalindromo(" ")) # Espacio vacío
    
    def test_cadena_con_espacios(self):
        self.assertTrue(esPalindromo("Able was I ere I saw Elba"))

    def test_cadena_con_puntuacion(self):
        self.assertTrue(esPalindromo("A man, a plan, a canal, Panama."))

if __name__ == "__main__":

    unittest.main()
