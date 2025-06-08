import string

# aqui conseguimos uma string com todas as letras do alfabeto
todas_as_letras = string.ascii_letters
print(todas_as_letras)
print()

# tambem podemos pegar apenas as letras maiusculas
print(string.ascii_uppercase)
print()

# tambem podemos pegar apenas as letras minusculas
print(string.ascii_lowercase)
print()

# tambem podemos pegar todos os numeros
print(string.digits)
print()

# tambem podemos pegar todos os caracteres de pontuação
print(string.punctuation)
print()

# até mesmo a representação de espaços em branco 
print(repr(string.whitespace))
print()
