# treino.py
Calculando media ponderada no Python

def _calcular_media_ponderada(nota, peso):
  soma_das_notas = 0
  soma_dos_pesos = 0
  for nota,peso in zip(nota, peso):
      soma_das_notas += nota * peso
      soma_dos_pesos += peso
  media_ponderada = soma_das_notas / soma_dos_pesos
  if media_ponderada >= 7:
      print("Aprovado")
  return media_ponderada

nota = (10,5,7)
peso = (1,2,3)

print(f"A média ponderada é: {_calcular_media_ponderada(nota, peso)}")
