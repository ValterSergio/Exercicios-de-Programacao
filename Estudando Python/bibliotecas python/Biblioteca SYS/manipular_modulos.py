import sys
import types

# podemos criar um modulo falso para testes 
modulo_falso = types.ModuleType("modulo_falso") # criamos um modulo vazio

# podemos adicionar um atributo qualquer nesse modulo
modulo_falso.ele_existe = True

# adicionamos ele no dicionario de modulos
sys.modules['modulo_falso'] = modulo_falso

# vamos importar o modulo falso
import modulo_falso # type: ignore

# exibimos o valor do atributo criado no modulo falso
print("Modulo criado: ", modulo_falso.ele_existe)

# podemos apagar esse modulo já que não vamos mais usar
del sys.modules['modulo_falso']

# como vemos ele não existe mais
try:
    import modulo_falso # type: ignore
except ImportError as Error:
    print("\nModulo apagado com sucesso.")
    print(str(Error))