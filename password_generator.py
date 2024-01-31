# 1 - input para um usuário dar um ENTER e gerar a senha
# 2 - a senha deve ter 7 caracteres / conter número, uma letra maiúscula e um caractere especial

import random # importa o modo de escolhas aleatórias
import re # expressões regulares
from random import randint #importando o randint que é a escolha de números inteiros

user = str(input("Digite ENTER para gerar uma senha aleatória: ")) #input para usuário der o ok e gerar a senha

capital_letter = chr(randint(65,90)) #escolha das maiúsculas através da tabela ASCII
special_character = chr(33) #escolha dos caracteres especiais através da tabela ASCII

list = [] #criação da lista

for c in range(0,5): # for para gerar 5 números aleatórios
    number = chr(randint(48,57)) #escolha dos números através da tabela ASCII
    list.append(number) #adicionando a variável "number" dentro da lista

list.append(special_character) #adicionando a variável "special_character" dentro da lista
list.append(capital_letter) #adicionando a variável "capital_letter" dentro da lista
random.shuffle(list) #pegar os números, maiúscula e caractere especial e misturar tudo, deixando bem aleatório

sem_aspas = "[{0}]".format(', '.join(map(str, list))) #tirando as aspas da lista

junto = "[{0}]".format(', '.join(map(str, list)))[1:-1] #tirando os colchetes da lista

sem_virgulas = re.sub(",", "", junto) #tirando as vírgulas da lista
print(sem_virgulas) #print final com todas as modificações necessárias
print('OBS: Contém 7 caracteres com 1 letra maiúscula e 1 caractere especial') #observação sobre a personalização da senha








