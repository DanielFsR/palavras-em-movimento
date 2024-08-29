import requests
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
from utils import remove_accents



def get_words():
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    words = []

    for letter in letter_list:
        print(f'Buscando palavras com a letra {letter}')
        response = requests.get(f'https://www.dicio.com.br/palavras-com-quatro-letras/?i=&e=&a=0&s={letter}___#resultsTitle')
        content = response.content

        # Transforma o conteúdo em um objeto BeautifulSoup
        site = BeautifulSoup(content, 'html.parser')

        # Encontra a div que contém o conteúdo que queremos
        div_content = site.find('div', attrs={'class': 'col-xs-12 col-md-8 card new-advanced-search-card mb20'})

        # Encontra todos os parágrafos dentro da div
        paragraphs = div_content.find_all('p')

        for p in paragraphs[4:]:
            texto = p.get_text(separator=' ') # Pega o texto do parágrafo e separa por espaço
            words.extend(texto.split()) # Adiciona as palavras na lista de palavras

    # Inicializa o corretor ortográfico em português
    spell = SpellChecker(language='pt')

    # Remove palavras que não existem no dicionário
    newWords = [remove_accents(word) for word in words if word in spell]
    return newWords

