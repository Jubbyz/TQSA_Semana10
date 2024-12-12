from numeroromano import converte

if __name__ == "__main__":
    try:
        numeroromano = input("Digite um número romano: ")
        resultado = converte(numeroromano)
        print(f"O equivalente inteiro de {numeroromano} é {resultado}.")
    except ValueError as e:
        print(f"Erro: {e}")