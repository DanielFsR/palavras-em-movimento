import unicodedata

def print_red(text):
    print(f"\033[31m{text}\033[0m")

def print_green(text):
    print(f"\033[32m{text}\033[0m", end='')

def print_yellow(text):
    print(f"\033[33m{text}\033[0m", end='')

def print_blue(text):
    print(f"\033[34m{text}\033[0m", end='')


def remove_accents(text):
    normalized_text = unicodedata.normalize('NFD', text)
    text_without_accents = ''.join(char for char in normalized_text if not unicodedata.combining(char))
    return text_without_accents

communsWords = [
    "amor", "bola", "casa", "dado", "fato", "gato", "hora", "jogo", "lado", "muro",
    "nove", "ovo", "arco", "rato", "sapo", "teia", "foca", "vaca", "", "alvo",
    "bico", "cima", "eixo", "fera", "gala", "hino", "jato", "lona", "oito", "pera",
    "raro", "sede", "teto", "uva", "vela", "bate", "colo", "dica", "fuma", "gelo",
    "liso", "mapa", "neto", "onda", "pino", "sopa", "tela", "unha", "vida", "zelo",
    "roma", "boia", "cola", "dona", "fino", "lago", "cola", "ouro", "pico", "mato"]