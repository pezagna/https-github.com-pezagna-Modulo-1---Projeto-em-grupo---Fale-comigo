
##################################################################
#  SENAC/RESILIA - Formação em Análise de Dados (FAD)            #
#  Projeto individual 1 - Módulo 2 - Deu match!                  #
#  Data de criação: 08/02/2023                                   #
#  Criação e edição:  Robson da Silva                            #
#  versão = '3.11'                                               #
##################################################################
##########################################################################################
#                                      Contexto                                          #           
#                                                                                        #
#    Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade         #
#    de um candidato com uma vaga de acordo com seu resultado nas etapas do              #   
#    processo seletivo.                                                                  #
#    Para isso foi criado um teste que devolve uma string no seguinte formato:           #
#    eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em             #
#    uma das etapas do processo - entrevista, teste teórico, teste prático e             #
#    avaliação de soft skills).                                                          #
#                                                                                        #           
#    Seguindo as informações do contexto, toda a linha de código seguinte foi projetada. #   
#                                                                                        #
##########################################################################################

import os
os.system("cls")
i= []
notas = ["Candidato1","Candidato2","Candidato3","Candidato4"]
entrevista = [6,3,5,8]
teorica = [6,3,4,6]
pratica = [8,6,7,10]
softskill = [8,5,8,7]
opcao=(1)

def menu(): #Menu Principal
    os.system("cls")
    opcao=0
    while opcao !="3":
        print("\n     Candidatos App""\n""\n""1. Cadastrar candidato""\n""2. Buscar/Listar candidatos""\n""3. Sair")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if  (opcao==1):
            cadastrar()
        elif(opcao==2):
            submenu()
        elif(opcao==3):
            print("\n""Aplicativo encerrado.""\n")
            break
        else:
            print ("\n""Opcão inválida, tente novamente.")
            
def submenu(): #Submenu
    opcao=1
    while opcao !="3": 
        print("\n     Submenu""\n""1. Buscar candidato por nota""\n""2. Listar todos""\n""\n""3. Retornar ")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if(opcao==1):
            pesquisar()
        elif(opcao==2):
            print("\nExibindo todos os candidatos:")          
            for i in range(len(notas)):
                    print("",notas[i],(f"= e{entrevista[i]}_t{teorica[i]}_p{pratica[i]}_s{softskill[i]}"))
        elif(opcao==3):
            break
        else:
            print ("\n""Opcão inválida, tente novamente.")
            
def cadastrar(): #Função para cadastrar candidatos.
    os.system("cls")
    while True:
        try:
            nome =(input("Digite o nome do candidato: "))
        except:
            print ("\nOpcão inválida, tente novamente.\n")
            continue
        notas.append(nome)   
        notaE = int(input("Digite a nota da entrevista: "))
        entrevista.append(notaE)
        notaT = int(input("Digite a nota da avaliação teórica: "))
        teorica.append(notaT)
        notaP = int(input("Digite a nota da avaliação prática: "))
        pratica.append(notaP)
        notaS = int(input("Digite a nota da avaliação soft skill: "))
        softskill.append(notaS)
        print("\nCandidato cadastrado.")
        break
    
def pesquisar(): # Função para buscar candidatos.
    os.system("cls")
    while True:
        checkE = int(input("Digite a nota da entrevista: "))
        checkT = int(input("Digite a nota da avaliação teórica: "))
        checkP = int(input("Digite a nota da avaliação prática: "))
        checkS = int(input("Digite a nota da avaliação soft skill: "))
        print("\nExibindo resultado dos candidatos com a melhor avaliação:")
        for i in range(len(notas)):
            if entrevista[i] >= checkE and teorica[i] >= checkT and pratica[i] >= checkP and softskill[i] >= checkS:           
                print("",notas[i],(f": e{entrevista[i]}_t{teorica[i]}_p{pratica[i]}_s{softskill[i]}"))

        break
menu()