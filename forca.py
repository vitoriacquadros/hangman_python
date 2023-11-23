from random import choice
import datetime
from time import sleep
'''
O código foi desenvolvido com finalidade de mensurar as dificuldades encontradas em lógica de programação simples utilizando a linguagem Python 
Este é bem simples e intuitivo e sua jogabilidade se dá através do terminal. 
Algumas atribuições ainda vão ser inseridas neste código para melhorar seu desempenho e criar uma interface gráfica para se tornar mais atrativo. 
Estudos no momento relativos a este código: como implementar uma API capaz de tornar possível a jogabilidade atráves de uma interface gráfica  visualmente agradável ao usuário e como adiconar mais opções de entrada como menus e barras de seleção.'''

'''
Duas funções, uma para introdução e outra para o menu do jogador.
'''
def introduction():
    linhas = "=" * 80
    introducao = "Prezado(a), seja bem-vindo(a) ao jogo da forca"
    print(linhas)
    print("")
    print(introducao.center(80, "*"))
    print("")
    print(linhas)
    

def inicial_forca():
    print("""Para iniciar, um breve texto explicativo de jogabilidade, leia atentamente às instruções:
            1° O número limite de tentativas é igual a 06 vezes por rodada
            2° Este jogo baseia-se em critérios de níveis de dificuldades aplicados à cada
            rodada.
            3° Caso deseje adivinhar a palavra completamente, digite "."(ponto)
            4º A cada erro será preenchido algum membro de seu enforcado, até que você seja totalmente enforcado.
            
            MAY THE LUCK OR STRENGTH BE WITH YOU! 
            
            
        
---------
|       |
|
|
|
------


          """)
    
introduction()
hora_atual = datetime.datetime.now() #mostra hora atual
agora_string = hora_atual.strftime("%A %d %B %y %I:%M")#Dia e hora atual
print(agora_string)
sleep(2)

inicial_forca()


"""
Primeiro nível de palavras selecionadas, ditas cujas como fáceis.
"""
with open('palavras.txt', 'r') as arquivo:
    lista = [linha.strip() for linha in arquivo]    
"""
Segundo nível de palavras selecionadas, ditas cujas como médias
"""
with open("medias.txt", "r") as arq:
    lista_2 = [linha.strip() for linha in arq]
"""
Terceiro nível de palavras selecionadas, ditas cujas como difíceis

"""
with open("dificeis.txt", "r") as arq2:
    lista_3 = [linha.strip() for linha in arq2]
"""MONTAGEM DO BONECO DA FORCA """

valido = False

while not valido:
    nivel = input("Escolha um nível de dificuldade: fácil = 1, médio = 2 ou difícil = 3: ")

    if nivel == '1':
        valido = True
        lista_palavras = choice(lista)
        espaços = ["_"]*len(lista_palavras)
        print(" ".join(espaços))
    if nivel == '2':
        valido = True
        lista_palavras = choice(lista_2)
        espaços = ["_"]*len(lista_palavras)
        print(" ".join(espaços))
    if nivel == '3':
        valido = True
        lista_palavras = choice(lista_3)
        espaços = ["_"]*len(lista_palavras)
        print(" ".join(espaços))

'''Aqui foi criada uma condição onde o usuário determinará qual o nível de dificuldade a ser jogado.
nivel é uma variável que armazenará o valor, e dentro da estrutura condicional (if) será validada qual opção o jogador escolheu
se, nivel for igual a fácil, é criada uma váriavel que contém uma lista de palavras com o método choice da função random, a fim de obter palavras aleatórias.
Isso é válido para os três níveis.
Caso, nenhuma das opções sejam válidas, o loop while irá executar indefinidas vezes até que o usuário digite corretamente.
A variável valido, em primeiro momento, é difinida como False, indicando que o nivel selecionado ainda não é valido
Se, for digitado um nivel valido, a variavel "valido" é definida com True.
'''





cabeca = """
            0 0
             _
"""

tronco = """
            0 0
             =
             ()
             ()
             ()

"""

braco_esquerdo = """

            0 0
             =
          \  ()
             ()
             ()
"""

braco_direito = """

            0 0
             =
          \  () /
             ()
             ()
"""

perna_esquerda = """

            0 0
             =
          \  () /
             ()
             ()
            / 
"""

perna_direita = """

            
            0 0
             =
          \  () /
             ()
             ()
            /  \\
"""





chances = 6
'''
Explicativo:
Primeiro, posso dizer que enquanto chances for maior que zero e enquanto há espaços vazios em espaços... 
Inicialmente há um input que pede ao usuário uma letra para poder verificar se essa letra está na palavra ou não.
Após, se a letra for igual a '.', cria-se  uma nova variável solicitando toda palavra ao usuário
se palpite está em lista_palavras(palavras aleatorias selecionadas)
o usuário receberá na tela: acertou no bug! (bug de inseto, compiuters entenderão)
e a execução é pausada.
senão, o usuário receberá na tela que a palavra está incorreta e o jogo se encerrará
O loop for percorre cada índice da string lista_palavras e compara o caractere no indice com a letra inserida pelo jogador
Se a letra estiver na posição 'i', o  caractere na posicao 'i' da lista 'letras' é atualizado na letra inserida.
Neste caso, o for irá percorrer cada índice da palavra secreta e encontrará a letra obtida no input, sendo assim
o caractere na posição encontrada da lista letras será atualizado.
chances -=1 se torna útil para reduzir o número de chances do jogador quando ele errar uma letra
essa variável é inicializada com o número 6, a cada erro, irá diminuir 1 chance do usuário
é o mesmo que:
chances = chances - 1
de modo simples chances -=1
'''

while chances > 0 and "_" in espaços:
    letra = input('digite uma letra: ')
    if letra == ".":
        palpite = input('Digite toda palavra: ')
        if palpite in lista_palavras:
            print("Acertou no bug!")
            break
        else:
            print("Palavra incorreta")
            break
    
    if letra in lista_palavras:
        for i in range(len(lista_palavras)): 
            if lista_palavras[i] == letra: 
                espaços[i] = letra    
        print(" ".join(espaços))
    else:
        chances -= 1
        print("Você errou. Quantidade de vidas:", chances)
        if chances == 5:
            print(cabeca)
        if chances == 4:
            print(tronco)
        if chances == 3:
            print(braco_esquerdo)
        if chances == 2:
            print(braco_direito)
        if chances == 1:
            print(perna_esquerda)
        if chances == 0:
            print(perna_direita)
        
if "_" not in espaços:
    print("Parabéns, você ganhou o Jogo da Forca!")
else:
    print("Fim de jogo. A palavra era:", lista_palavras)

        
