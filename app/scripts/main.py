from app.scripts.charfun import esPalindromo

def main():
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        try:
            if frase.lower() == "salir":
                print("Programa finalizado.")
                break
            else:
                # Comprobar si es palíndromo
                if esPalindromo(frase):
                    print("La frase es palíndroma.")
                else:
                    print("La frase no es palíndroma.")
        except Exception as e:
            print(f"Error: {e}")
