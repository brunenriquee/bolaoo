
#Sistema para práticar python - Bolao da mega sena

#Menu da aplicação
menu = """ Menu:
        1 - Mostrar jogos
        2 - Adcionar jogo
        3 - deletar jogo 
        4 - sair
        """
#Lista de jogos feitos
jogos = []

#Função para adicionar jogo
def fazerjogo():
    novo = []
    i = 0

    while i < 6:

        numero = int(input("Digite um número de 0 a 60 : "))
        if numero > 0 and numero < 61:
            if numero not in novo:
                novo.append(numero)
                i = i + 1
            else:
                print("Número já está no jogo \n")
        else:
            print("valor invalidado \n")
    
    if novo in jogos:
        print("Jogo já existe \n")
    else:
        jogos.append(novo)
        print("Jogo adicionado \n")

#função para remover jogo
def removerjogo():
    novo = []
    i = 0

    while i < 6:

        numero = int(input("Digite um número de 0 a 60 : "))
        if numero > 0 and numero < 61:
            if numero not in novo:
                novo.append(numero)
                i = i + 1
            else:
                print("Número já está no jogo \n")
        else:
            print("valor invalidado \n")

    if novo in jogos:
        jogos.remove(novo)
        print("Jogo deletado \n")
    else:
        print("Jogo não exite \n")



#Apresentação do software
print("Bolão da mega sena \n")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=- \n")


#Loop da aplicação
while True:
    print(menu)

    opcao = input("escolha uma opção: ")

    if opcao.isnumeric(): #Verifica se é numero

        if opcao == '1':
            if len(jogos) == 0:
                print("Nenhum jogo feito")
            else:
                for x in jogos:
                    print(x)

        elif opcao == '2':
            fazerjogo()

        elif opcao == '3':
            removerjogo()
                            
        elif opcao == '4':
            print("Fechando...")
            break
        else :
            print("Digite uma opção valida \n")
        
    else :
        print("Digite uma opção valida \n")
