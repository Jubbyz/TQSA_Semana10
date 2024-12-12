def converte(numeroromano):
  valores = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  }

  soma = 0
  valor_direita = 0

  # Verifica se o número romano viola a regra de repetição
  if "IIII" in numeroromano or "VV" in numeroromano or "XXXX" in numeroromano \
          or "LL" in numeroromano or "CCCC" in numeroromano or "DD" in numeroromano \
          or "MMMM" in numeroromano:
      raise ValueError("Número romano inválido: repetição excessiva de caracteres.")

  # Itera pelos caracteres do número romano em ordem inversa
  for indice in reversed(range(len(numeroromano))):
      valor_atual = valores.get(numeroromano[indice], 0)

      if valor_atual == 0:
          raise ValueError(f"Caractere inválido encontrado: {numeroromano[indice]}")

      if valor_atual < valor_direita:
          soma -= valor_atual
      else:
          soma += valor_atual

      valor_direita = valor_atual

  return soma