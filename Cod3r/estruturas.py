#!\User\AppData\Local\Programs\Python\Python38-32\python.exe
import math
import sys

#Math
"""
import math
raio = 5
print(f'area de {math.pi*raio}')
"""
#Lista
"""
pj_horda = ['Ayer', 'Byern']

print(f'\nForam criados {len(pj_horda)} personagens na horda, {pj_horda[-1]} e {pj_horda[-2]}')

pj_conclave = ['Vayer', 'Sephera', 'Lyra']

pj_horda.extend(pj_conclave)

print(f'\nVou adicionar {pj_conclave} aos personagens da Horda, ficando então {pj_horda}')

print(f'It\'s {pj_conclave==pj_horda[2:5]} that Conclave is in Horda' )
"""
#Tupla
'''
Membros = tuple()
Membros = ('Membros Inferiores', 'Membros Superiores')
humanbody = tuple()
humanbody = ('Cabeça', 'Tronco', Membros)

print(f'\nOs mebros do corpo humano são {humanbody[0:3]}')
''' 
#Dicionário
"""
pessoa = {'nome': 'Berninson', 'idade': 22, 'Corpo': Membros}

print(f'\nEste é {pessoa["nome"]}, ele tem {pessoa["idade"]} anos.')

del pessoa['Corpo']

pessoa.update({'Sexo': 'Homem Cis', 'Região': 'Polo Norte'})

print(f'O sr.{pessoa["nome"]} é do {pessoa["Região"]}.')
"""
#Conjuntos
'''
Humano = set()
Humano = {humanbody, 'lógica', 'sociedade', 'sentimentos', 'espírto'}
'''
#Argumentos

def metodo(raio):
    return math.pi*raio**2

def help():
    print('Não foi efetuado uma entrada')
    print(f"Sintaxe: {(sys.argv[0][2:])} <raio>")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = metodo( raio )
        print(f'A area é { area }') 