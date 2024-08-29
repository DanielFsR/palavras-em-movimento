import random
from wordscrapper import get_words
from utils import print_red, print_green, print_blue, print_yellow
from utils import communsWords
palavras2 = get_words()
final_word = []

for i in range(4):
  final_word.append(random.choice(communsWords))

wordList = ['casa']
palavra = wordList[-1]
while(len(final_word) > 0):
    x = 0
    print('...............................................')
    if (palavra in final_word):
        print_green('Parabéns!!, você acertou a palavra:')
        print('',palavra)
        final_word.remove(palavra)
        continue
    print_blue('Objetivo:')
    print('',final_word)
    print('Palavra atual: ', end= '')
    print_yellow(palavra)
    print()
    variavel = input()[:4]

    if variavel == '1':
      print(wordList[-5:])
      continue

    if variavel == '2':
       wordList.remove(palavra)
       palavra = wordList[-1]
       continue
    #verifica se a palavra digitada existe
    if variavel not in palavras2:
        print_red('Palavra inválida, tente novamente')
        continue

    #verifica se a palavra digitada é um anagrama da palavra atual
    if sorted(variavel) == sorted(palavra):
        palavra = variavel
        if palavra != wordList[-1]:
          wordList.append(palavra)
        continue
    #verifica se a palavra digitada somente tem uma letra diferente da palavra atual
    for i in range(4):
        if variavel[i] != palavra[i]:
            x = x + 1
    if x <= 1:
        palavra = variavel
        if palavra != wordList[-1]:
          wordList.append(palavra)
        continue
    else:
        print_red('Palavra inválida, tente novamente')
        continue
print_green('PARABÉNS!!!!!!!!, você acertou todas as palavras')
