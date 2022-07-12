import random
import string

tamanho = int(input("Digite o tamanho da senha que você deseja: ")) #tamanho da Senha a ser gerada. Numero pode ser recebido ou pré definido

chars = string.ascii_letters + string.digits + "ç!@#$%&*-=+?" #Gerarar letras maiusculas e minusculas + números + os caracteres escolhidos

rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(tamanho)))
#rnd.choice escolhe aleatoriamente dentro de Chars, roda o looping definindo o tamanho e o .join junta em uma linha str

