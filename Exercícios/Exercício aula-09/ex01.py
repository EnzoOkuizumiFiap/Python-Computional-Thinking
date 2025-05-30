# Ex 01 - Calculadora com todas as operações
import time # Importa o módulo time

em_execucao = True

while em_execucao:
    print('\nEscolha uma opção:\nA - Somar dois números\nB - Subtrair dois números\nC - Multiplicar dois números\nD - dividir dois números\nE - Mostrar tabuadas de desejada\nF - Encerrar programa')

    opcao = input("Digite a opção: ").upper()

    if opcao == 'A':
        x = float(input('Digite o primeiro valor para a soma:'))
        y = float(input('Digite o segundo valor para a soma:'))
        print('Resultado da soma:', x + y)
        time.sleep(3)

    elif opcao == 'B':
        x = float(input('Digite o primeiro valor para a subtração:'))
        y = float(input('Digite o segundo valor para a subtração:'))
        print('Resultado da subtração:', x - y)
        time.sleep(3)

    elif opcao == 'C':
        x = float(input('Digite o primeiro valor para a multiplicação:'))
        y = float(input('Digite o segundo valor para a multiplicação:'))
        print('Resultado da multiplicação:', x * y)
        time.sleep(3) 

    elif opcao == 'D':
        x = float(input('Digite o primeiro valor para a divisão:'))
        y = float(input('Digite o segundo valor para a divisão:'))
        if y != 0:
            print('Resultado da divisão:', x / y)
            time.sleep(3) 
        else:
            print('Erro: divisão por zero!')
            time.sleep(3) 

    elif opcao == 'E':
        numero = int(input("Qual a tabuada desejada? "))
        print(f'\nTabuada do {numero}:')

        multiplicador = 1
        while multiplicador <= 10:
            print(f'{numero} x {multiplicador} = {numero * multiplicador}')
            multiplicador += 1

        time.sleep(3)

    elif opcao == 'F':
        em_execucao = False
        print('Programa encerrado.')

    else:
        print('Opção inválida. Tente novamente.')
