altura = float(input("Digite a altura"))
comprimento = float(input("Digite o comprimento"))
metros2 = altura*comprimento
cobertura= metros2 / 3
latas = (cobertura / 3.6)
preço = (latas * 107.0)
print("o preço com latas será:" , preço , "e a quantidade é:", latas)
