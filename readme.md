# Palavras em Movimento

Este é um jogo de palavras onde o desafio é mover-se de uma palavra para outra, mudando apenas uma letra ou reorganizando todas as letras. Mergulhe nas combinações de palavras com quatro letras e tente adivinhar todas as palavras finais propostas.

## Funcionalidades

- **Busca automática de palavras:** Coleta palavras de quatro letras através de web scraping.
- **Verificação de validade:** Utiliza um corretor ortográfico para garantir que as palavras inseridas sejam válidas.
- **Desafios de anagramas e alterações:** O jogador deve transformar a palavra atual em uma nova, mudando uma única letra ou reorganizando todas as letras.
- **Progresso visual:** Indicação clara de acertos e erros para ajudar o jogador a avançar no jogo.

## Requisitos

Antes de executar o jogo, instale as dependências necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```
## Como Jogar

1. Execute o jogo com o comando:

    ```bash
    python wordgame/game.py
    ```

2. O jogo irá gerar uma lista de palavras finais que você deve adivinhar.

3. A cada rodada, digite uma palavra que seja um anagrama da palavra atual ou que tenha apenas uma letra diferente.

4. Continue jogando até adivinhar todas as palavras finais.

## Exemplo de Jogo

O objetivo é chegar à palavra `bola`. Aqui está um exemplo de como você pode começar e evoluir no jogo:

- **Palavra inicial:** `casa`
  - Palavra inicial com a qual o jogo começa.

- **Mudança 1:** Anagrama para `saca`
  - Neste passo, a palavra `casa` é reorganizada para formar o anagrama `saca`.

- **Mudança 2:** Transforme `saca` em `soca`
  - Aqui, `saca` é alterada para `soca` mudando uma letra (de 'a' para 'o').

- **Mudança 3:** Altere `soca` para `boca`
  - `soca` é transformada em `boca` mudando uma letra (de 's' para 'b').

- **Objetivo final:** Chegue à palavra `bola`
  - Finalmente, `boca` é transformada em `bola` mudando uma letra (de 'c' para 'l').

Nesse exemplo, a primeira mudança é um anagrama e as mudanças seguintes envolvem a troca de uma única letra. Cada palavra intermediária é válida e tem uma relação com a palavra anterior, seja por mudança de uma única letra ou por reorganização das letras.


## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões, sinta-se à vontade para abrir uma [issue](https://github.com/DanielFsR/wordgame/issues) ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

