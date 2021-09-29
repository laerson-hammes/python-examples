# O que são?
# F-stings são uma forma diferente e atualizada do .format
# Para a utilização, basta colocar um f (upper ou lowercase) antes da string e, dentro da string, 
# onde você deseja imprimir uma variável, abrir e fechar {} e dentro deles colocar diretamente a variável

# Exemplos:
print(f"{2}")
print(F"{2}")

# Operações dentro dos {}
print(f"{4 + 5}")

# Imprimindo variáveis
number = 5
print(f"{number}")

# Imprimindo o nome da variável e o seu respectivo valor
name = "Angelina"
print(f"{name = }")


# Chamando funções dentro dos {}
def mul(x, y):
   return x * y

print(f"{mul(2, 5)}")


# Mostrando somente duas casas decimais
print(f"{mul(2.1235, 3.1415):.2f}")