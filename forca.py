from arquivos.telas import entrada_de_dados
from arquivos.regras_do_jogo import tratamento_palavra
from arquivos.telas import desenhar_boneco
from arquivos.telas import saida_de_dados
def divisao():
    print('-'*60)

saida_de_dados.boas_vindas()
def jogar():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    palavra = tratamento_palavra.pegar_palavra()
    letras_adivinhadas = []
    tentativas = 6
    erro = 0
    adivinhada = False

    print('\nA palavra possui', len(palavra), 'letras.')
    print(len(palavra) * '_ ')
    while adivinhada == False and tentativas > 0:
        print('Você tem ' + str(tentativas) + ' vidas')
        tentativa = input('\nPor favor digite uma letra ou a palavra inteira: ').lower()
        #1 - Usuario coloca a letra
        if len(tentativa) == 1:
            if tentativa not in alfabeto:
                divisao()
                print('Você não digitou uma letra.')
            elif tentativa in letras_adivinhadas:
                divisao()
                print(f'As letras digitadas foram: {letras_adivinhadas}')
                print('Você ja tentou essa letra anteriormente.')
            elif tentativa not in palavra:
                divisao()
                print('Desculpe mas essa letra não faz parte da palavra')
                letras_adivinhadas.append(tentativa)
                print(f'As letras digitadas foram: {letras_adivinhadas}')
                tentativas -=1
                erro += 1
                desenhar_boneco.desenho(erro)
            elif tentativa in palavra:
                divisao()
                print('Essa letra faz parte da palavra!')
                letras_adivinhadas.append(tentativa)
                print(f'As letras digitadas foram: {letras_adivinhadas}')
                desenhar_boneco.desenho(erro)
            else:
                divisao()
                print('Realmente, não sei como você chegou aqui.')

        #2 - Usuario chuta toda a palavra
        elif len(tentativa) == len(palavra):
            if tentativa == palavra:
                print('Muito bem, você adivinhou a palavra!')
                adivinhada = True
            else:
                print('Desculpe, você errou a palavra!')
                print(f'As letras digitadas foram: {letras_adivinhadas}')
                tentativas -= 1
                erro += 1
                desenhar_boneco.desenho(erro)

        #3 - Usuario chuta uma palavra maior ou menor do que a proposta.  
        else:
            divisao()
            print('A largura do seu chute não é do tamanho da palavra que estamos procurando!.')
            print(f'As letras digitadas foram: {letras_adivinhadas}')
            tentativas = False
            erro = 6
            desenhar_boneco.desenho(erro)

        status = ''
        if adivinhada == False:
            for letra in palavra:
                if letra in letras_adivinhadas:
                    status += letra
                else:
                    status += '_ '
            print(status)

        #4 - Fim de jogo
        if status == palavra:
            divisao()
            print('Muito bem, você adivinhou a palavra!')
            desenhar_boneco.desenho(erro)
            adivinhada = True
        elif tentativas == 0:
            divisao()
            print('Acabaram suas tentativas e você não adivinhou a palavra!')
            print(f'A palavra era {palavra}')
            print(f'As letras digitadas foram: {letras_adivinhadas}')
            desenhar_boneco.desenho(6)
        elif tentativas == False:
            divisao()
            print('Infelizmente você chutou a palavra errada!')
            print(f'A palavra era {palavra}')
            desenhar_boneco.desenho(erro)
            adivinhada = True

    if entrada_de_dados.jogar_novamente():
        jogar()

jogar()