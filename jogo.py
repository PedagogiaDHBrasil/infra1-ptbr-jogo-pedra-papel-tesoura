#encoding:UTF-8
import random

while True: 
    aleatorio = random.randrange(0, 3)
    escolhePc = ""
    print("1)Pedra")
    print("2)Papel")
    print("3)Tesoura")
    print("4)Sair do Programa")
    opcao = int(input("O que você escolhe: "))
    
    if opcao == 1:
        escolhaUsuario = "Pedra"
    elif opcao == 2:
        escolhaUsuario = "papel"
    elif opcao == 3:
        escolhaUsuario = "Tesoura"
    elif opcao == 4:
        print ("Ate a proxima!")
        break
    else:
        print ("Valor Invalido")
        continue
        
    print("Você escolhe: ", escolhaUsuario)   
    if aleatorio == 0:
        escolhePc = "Pedra"
    elif aleatorio == 1:
        escolhePc = "Papel"
    elif aleatorio == 2:
        escolhePc = "Tesoura"
    print("PC escolheu: ", escolhePc)
    print("...")
    
    if escolhePc == "Pedra" and escolhaUsuario == "Papel":
        print("Você ganhou, papel envolve pedra!")
    elif escolhePc == "papel" and escolhaUsuario == "Tesoura":
        print("Você ganhou, tesoura corta papel")
    elif escolhePc == "Tesoura" and escolhaUsuario == "Pedra":
        print("Você ganhou, Pedra esmaga Tesoura")
        
    if escolhaUsuario == "Pedra" and escolhePc == "papel":
        print("Você perdeu, papel envolve Pedra")
    elif escolhaUsuario == "papel" and escolhePc == "Tesoura":
        print("Você perdeu, Tesoura corta papel")
    elif escolhaUsuario == "Tesoura" and escolhePc == "Pedra":
        print("Você perdeu, Pedra esmaga Tesoura")
    elif escolhePc == escolhaUsuario:
        print("Empate")
    again = input("Jogamos de novo? s/n: ")
    if 's' in again:
        continue
    elif 'n' in again:
        print("Até a próxima!")
        break
    else:
        print("Valor Invalido")
