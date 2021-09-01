from unidade_federativa import UnidadeFederativa

print("Unidades Federativas Brasileiras")

unidades_federativas = UnidadeFederativa.get_lista_uf()

for counter, value in enumerate(unidades_federativas):
    print(counter, "-", value)

sigla = input('Digite a sigla do estado')
uf = UnidadeFederativa.get_UF(sigla)
print("A UF da sigla " + sigla + " é " + uf)
