
import random
import time

def erro():
    print("\nEssa não é uma opção válida!")
    voltar()

ganha = ["oponente: putz, ta com sorte hoje",
    "oponente: putz , mais um pouco e eu ganhava",
    "oponente: ainda bem que eu não apostei",
    "oponenet: uma hora eu ganho",
    "oponente: nem queria ganhar mesmo",
    "Oponente: fosse truco eu ganhava",
    "oponente: uma hora eu ganho",
    "oponente: onde aprendeu a jogar assim?",
    
]

ganha = random.choice(ganha)

perde = [
    "oponente: eu falei que eu era o melhor",
    "oponente: mais uma vez? só pra não dizer que foi sorte",
    "oponente: depois te ensino a jogar assim",
    "oponente: que pena que eu não apostei",
    "oponente: mais sorte na proxima"
    
]

perde = random.choice(perde)

def creditos():
    print("\neste jogo foi feito por: SpaceX")


def voltar():
    restart = input("\nJogar de novo (1) ou voltar pro menu (2)? ")
    if restart == "1":
        jogo()
    elif restart == "2":
        menu()
    else:
        erro()

def jogo():

    dificuldade = random.randint(1, 3)
    
    if dificuldade == 1:
        dificuldade = 18
    elif dificuldade == 2:
        dificuldade = 19
    if dificuldade == 3:
        dificuldade = 20
    
    j1 = random.randint(1, 10)
    j2 = random.randint(1, 10)
    jogador1 = j1 + j2

    c1 = random.randint(1, 10)
    c2 = random.randint(1, 10)
    jogador2 = c1+c2

    print(" ___________________")
    print("|                   |")
    print("| A                 |")
    print("| ♦ _____________   |")
    print("|  |             |  |")
    print("|  | MODO DE JOGO|  |")
    print("|  |             |  |")
    print("|  |1 = normal   |  |")
    print("|  |2 = jackblack|  |")
    print("|  |3 = voltar   |  |")
    print("|  |             |  |")
    print("|  |_____________|  |")
    print("|                 ♦ |")
    print("|                 Ɐ |")
    print("|___________________|\n")

    modo = input("\nselecione modo de jogo: ")
    if modo == "1":
        print("\nVocê escolheu o modo: normal")
    elif modo == "2":
        print("\nVocê escolheu o modo: blackjack")
    elif modo == "3":
        menu()
    else:
        print("\nisso não é um modo de jogo válido")
        time.sleep(1)
        print("\ncarregando...")
        time.sleep(2)
        jogo()
        
    print("\ncarregando...")
    time.sleep(1)
    print("\ncontroles:desistir - 1")
    print("pegar uma carta - qualquer tecla")
    time.sleep(2)
    print("\n[Embaralhando as cartas...]")
    time.sleep(1)
    print("\n[rodada 1]")
    print()
    print("  suas    __    __        ")
    print(f" cartas  |{j1:^2}|  |{j2:^2}|")
    print("  são:   |__|  |__|")
    print("\n   Você tem:",jogador1)

    if modo == "2" and j1 == 1 and j2 == 10:
        print("\n[Você ganhou]")
        print("\noponente: Meu deus fez 21 de cara")      
        print("\n minhas   __    __        ")
        print(f" cartas  |{c1:^2}|  |{c2:^2}|")
        print("  eram:  |__|  |__|")

    elif modo == "2" and j2 == 1 and j1 == 10:
        
        print("\noponente: Meu deus fez 21 de cara")      
        print("\n minhas   __    __        ")
        print(f" cartas  c|{c1:^2}|  |{c2:^2}|")
        print("  eram:  |__|  |__|")
        voltar()
              
    elif modo == "2" and c2 == 10 and c1 == 1:
        print("\noponente:haha, fiz 21")      
        print("\n minhas   __    __        ")
        print(f" cartas  |{c1:^2}|  |{2:^2}|")
        print("  eram:  |__|  |__|")
        voltar()

    elif modo == "2" and c2 == 1 and c1 == 10:
        print()
        print(ganha)    
        print("\n minhas   __    __        ")
        print(f" cartas  |{c1:^2}|  |{c2:^2}|")
        print("  eram:  |__|  |__|")
        voltar()
        
    elif jogador2 >= dificuldade and jogador1 > jogador2:
        print("\nOponente: eu desisto")
        print("\nContando os pontos...")
        time.sleep(1)
        print()
        print(ganha)      
        print("\n minhas   __    __        ")
        print(f" cartas  |{c1:^2}|  |{c2:^2}|")
        print("  eram:  |__|  |__|")
        voltar()

    elif jogador2 >= dificuldade and jogador1 < jogador2:
        print("\nOponente: eu desisto")
        print("\nContando os pontos...")
        time.sleep(1)
        print("[Você ganhou]")
        print("\noponente:", ganha)          
        print("  minhas  __    __        ")
        print(f" cartas  |{c1:^2}|  |{c2:^2}|")
        print("   eram: |__|  |__|")
        voltar()
    else:
        continuar = input("\nDesistir de cara ou Pegar uma carta: ")
        if continuar == "1" and jogador1 > jogador2:
            print("\nvocê desistiu")
            print("\nContando os pontos...")
            time.sleep(1)
            print("\noponente:", ganha)            
            print("\n  minhas  __    __        ")
            print(f" cartas  |{c1:^2}|  |{c2:^2}|")
            print("   eram: |__|  |__|")
            voltar()

        elif continuar == "1" and jogador1 < jogador2:
            print("\nvocê desistiu")
            print("\nContando os pontos...")
            time.sleep(1)
            print("\noponente:", perde)        
            print("  minhas  __    __        ")
            print(f" cartas  |{c1:^2}|  |{c2:^2}|")
            print("   eram: |__|  |__|")
            voltar()

        elif continuar == "1" and jogador1 == jogador2:
            print("\nOponente: empatamos\nEu também tenho",jogador2)
            print("mais uma pra desempatar?")
            voltar()
            
        #rodada 1/jogador 1                
        else:
            print("\nVocê está pegando uma carta...")
            time.sleep(1)
            
            j3 = random.randint(1, 10)
            jogador1 = jogador1 + j3
            
            if jogador1 > 21:


                print("\n  você   __  ")
                print(f" tirou  |{c1:^2}|")
                print("  um:   |__|  ")
                print("\nOponente: você estourou")
                print("\nVocê fez um total de",jogador1)
                voltar()
    
                
            elif jogador1 == 21:

                print("\n [rodada 2]")
                print()
                print("\n  você   __  ")
                print(f" tirou  |{c1:^2}|")
                print("  um:   |__|  ")
                print("\nOponente:", ganha)
                print("\nVocê tirou 21")
                print("\n   minhas cartas eram:"     )            
                print("  minhas  __    __        ")
                print(f" cartas  |{c1:^2}|  |{c2:^2}|")
                print("   eram: |__|  |__|")
                voltar()
               
            else:
                print("\n [rodada 2]")
                print("\n  você   __  ")
                print(f" tirou  |{c1:^2}|")
                print("  um:   |__|  ")
                print("\nAgora você tem:",jogador1)
                
                continuar = input("Desistir (1) ou Continuar jogando? ")
                if continuar == "1" and jogador1 > jogador2:
                    print("você desistiu")
                    print("Contando os pontos...")
                    time.sleep(1) 
                    print("\noponente:", ganha)          
                    print("  minhas  __    __        ")
                    print(f" cartas  |{c1:^2}|  |{c2:^2}|")
                    print("   eram: |__|  |__|")
                    voltar()

                elif continuar == "1" and jogador1 < jogador2:
                    print("você desistiu")
                    print("Contando os pontos...")
                    time.sleep(1)
                    print("\noponente:", perde)          
                    print("  minhas  __    __        ")
                    print(f" cartas  |{c1:^2}|  |{c2:^2}|")
                    print("   eram: |__|  |__|")

                elif continuar == "1" and jogador1 == jogador2:
                    print("você desistiu")
                    print("Contando os pontos...")
                    time.sleep(1)
                    print("\nOponente: empatamos\nEu também tenho",jogador2)
                    print("mais uma pra desempatar?")
                    voltar()
                #rodada 2, computador
                else:
                    print("\nSeu oponente está pegando uma carta...")
                    time.sleep(1)
                    print("\nSeu oponente está pensando...")
                    time.sleep(3)                  
                    c3 = random.randint(1, 10)
                    jogador2 = jogador2 + c3
                    
                    if jogador2 > dificuldade and jogador1 > jogador2:
                        print("\nOponente: eu desisto")
                        print("Contando os pontos...")
                        time.sleep(1)
                        print("\noponente:", ganha)      
                        print("\n  minhas  __    __    __        ")
                        print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                        print("   eram: |__|  |__|  |__|")
                        voltar()


                    elif jogador2 == 21:
                        print("\nOponente: Meu Deus que sorte a minha\nTirei 21")
                        print("\n  minhas  __    __    __        ")
                        print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                        print("   eram: |__|  |__|  |__|")
                        print("mais uma sem perder a amizade?")
                        voltar()

                            
                    elif jogador2 > 21:
                        print("\noponente: putz, estourei")      
                        print("\n  minhas  __    __    __        ")
                        print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                        print("   eram: |__|  |__|  |__|")
                        voltar()
                        
                    #rodada - player
                    else:
                        print("\nOponente: pronto, é sua vez de novo")
                        print("\nVocê está pegando uma carta...")
                        time.sleep(1)            
                        j4 = random.randint(1, 10)
                        jogador1 = jogador1 + j4
                        if jogador1 > 21:
                            
                            print("\n [rodada 3]")
                            print("\n  você   __  ")
                            print(f" tirou  |{j4:^2}|")
                            print("  um:   |__|  ")
                            print("\nOponente: você estourou")
                            print("\n  minhas  __    __    __        ")
                            print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                            print("   eram: |__|  |__|  |__|")
                            print("\nVocê fez um total de",jogador1)
                            voltar()

                        elif jogador1 == 21:
                            print("\n [rodada 3]")
                            print("\n  você   __  ")
                            print(f" tirou  |{j4:^2}|")
                            print("  um:   |__|  ")
                            print("\nOponente:", ganha)
                            print("\nVocê tirou 21")
                            print("\n   minhas cartas eram:"     )            
                            print("\n  minhas  __    __    __        ")
                            print(f" cartas  |{c12:^2}|  |{c22:^2}|  |{c33:^2}|")
                            print("   eram: |__|  |__|  |__|")
                            voltar()
                            
                        else:
                            print("\n [rodada 3]")
                            print("\n  você   __  ")
                            print(f" tirou  |{j4:^2}|")
                            print("  um:   |__|  ")
                            print("\nAgora você tem:",jogador1)
                            
                            continuar = input("\nDesistir (1) ou Continuar jogando? ")
                            if continuar == "1" and jogador1 > jogador2:
                                print("você desistiu")
                                print("Contando os pontos...")
                                time.sleep(1)
                                print("\noponente:", ganha)      
                                print("\n  minhas  __    __    __        ")
                                print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                                print("   eram: |__|  |__|  |__|")
                                voltar()

                            elif continuar == "1" and jogador1 < jogador2:
                                print("você desistiu")
                                print("Contando os pontos...")
                                time.sleep(1)
                                print("\noponente:", perde)      
                                print("\n  minhas  __    __    __        ")
                                print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|")
                                print("   eram: |__|  |__|  |__|")

                            elif continuar == "1" and jogador1 == jogador2:
                                print("\nOponente: empatamos\nEu também tenho",jogador2)
                                print("mais uma pra desempatar?")
                                voltar()

                            else:
                                print("\nSeu oponente está pegando uma carta...")
                                time.sleep(1)
                                print("\nSeu oponente está pensando...")
                                time.sleep(3)

                                #computador
                                
                                c4 = random.randint(1, 10)
                                jogador2 = jogador2 + c4
                                if jogador2 > dificuldade and jogador1 > jogador2:
                                    print("\nOponente: eu desisto")
                                    print("Contando os pontos...")
                                    time.sleep(1)
                                    print("\noponente:", ganha)      
                                    print("\n  minhas  __    __    __    __        ")
                                    print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                    print("   eram: |__|  |__|  |__|  |__|")
                                    voltar()

                                elif jogador2 > 21:
                                    print("\noponente: putz, estourei")      
                                    print("\n  minhas  __    __    __    __        ")
                                    print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                    print("   eram: |__|  |__|  |__|  |__|")
                                    voltar()
                                    
                                elif jogador2 == 21:
                                    print("\nOponente: Meu Deus que sorte a minha\nTirei 21")
                                    print("\n  minhas  __    __    __    __        ")
                                    print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                    print("   eram: |__|  |__|  |__|  |__|")
                                    print("mais uma sem perder a amizade?")
                                    voltar()

                                else:
                                    #player
                                    print("\nOponente: Meu Deus, nós dois estamos azarados hoje\nE é a sua vez de novo")
                                    print("\nVocê está pegando uma carta...")
                                    time.sleep(1)
                                    j5 = random.randint(1, 10)
                                    jogador1 = jogador1 + j5
                                    if jogador1 > 21:
                                        print("\n [rodada 4]")
                                        print("\n  você   __  ")
                                        print(f" tirou  |{j5:^2}|")
                                        print("  um:   |__|  ")
                                        print("\nOponente: você estourou")
                                        print("\n  minhas  __    __    __    __        ")
                                        print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                        print("   eram: |__|  |__|  |__|  |__|")
                                        print("\nVocê fez um total de",jogador1)
                                        voltar()
        
                                    elif jogador1 == 21:
                                        print("\n [rodada 4]")
                                        print("\n  você   __  ")
                                        print(f" tirou  |{j5:^2}|")
                                        print("  um:   |__|  ")
                                        print("\nOponente:", ganha)
                                        print("\nVocê tirou 21")        
                                        print("\n  minhas  __    __    __    __        ")
                                        print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                        print("   eram: |__|  |__|  |__|  |__|")
                                        voltar()
                                        

                                    else:
                                        print("\n [rodada 4]")
                                        print("\n  você   __  ")
                                        print(f" tirou  |{j4:^2}|")
                                        print("  um:   |__|  ")
                                        print("\nAgora você tem:",jogador1)
                                        continuar = input("\nDesistir logo desse jogo longo (1) ou continuar (qualquer letra)? ")
                                        
                                        if continuar == "1" and jogador1 > jogador2:
                                            print("você desistiu")
                                            print("Contando os pontos...")
                                            time.sleep(1)
                                            print("\noponente:", ganha)      
                                            print("\n  minhas  __    __    __    __        ")
                                            print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                            print("   eram: |__|  |__|  |__|  |__|")
                                            voltar()
                                        elif continuar == "1" and jogador2 > jogador1:
                                            
                                            print("você desistiu")
                                            print("Contando os pontos...")
                                            time.sleep(1)
                                            print("\noponente:", perde)      
                                            print("\n  minhas  __    __    __    __        ")
                                            print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|")
                                            print("   eram: |__|  |__|  |__|  |__|")
                                            voltar()
                                        
                                        elif continuar == "1" and jogador1 == jogador2:
                                            print("\nOponente: empatamos\nEu também tenho",jogador2)
                                            print("mais uma pra desempatar?")
                                            voltar()

                                        else:
                                            print("\nSeu oponente está pegando uma carta...")
                                            time.sleep(1)
                                            print("\nSeu oponente está pensando...")
                                            time.sleep(3)

                                            
                                            c5 = random.randint(1, 10)
                                            jogador2 = jogador2 + c5
                                            if jogador2 > dificuldade and jogador1 > jogador2:
                                                print("\nOponente: eu desisto")
                                                print("Contando os pontos...")
                                                time.sleep(1)
                                                print("\noponente:", ganha)      
                                                print("\n  minhas  __    __    __    __    __        ")
                                                print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|  |{c2:^2}|  ")
                                                print("   eram: |__|  |__|  |__|  |__|  |__|")
                                                voltar()

                                            elif jogador2 > dificuldade and jogador1 < jogador2:
                                                print("\nOponente: eu desisto")
                                                print("Contando os pontos...")
                                                time.sleep(1)
                                                print("\noponente:", perde)      
                                                print("\n  minhas  __    __    __    __    __        ")
                                                print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|  |{c2:^2}|  ")
                                                print("   eram: |__|  |__|  |__|  |__|  |__|")
                                                voltar()

                                            elif jogador2 > 21:
                                                print("\noponente: putz estourei\n",ganha)      
                                                print("\n  minhas  __    __    __    __    __        ")
                                                print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|  |{c2:^2}|  ")
                                                print("   eram: |__|  |__|  |__|  |__|  |__|")
                                                voltar()
                                                voltar()

                                            else:
                                                print("\nTempo de jogo esgotado por azar de ambos dos competidores...")
                                                print("\nContando os pontos...")
                                                time.sleep(3)
                                                if jogador1 > jogador2:
                                                    print("\noponente:", ganha)      
                                                    print("\n  minhas  __    __    __    __    __        ")
                                                    print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|  |{c2:^2}|  ")
                                                    print("   eram: |__|  |__|  |__|  |__|  |__|")
                                                    voltar()

                                                elif jogador1 < jogador2:
                                                    print("\noponente:", perde)      
                                                    print("\n  minhas  __    __    __    __    __        ")
                                                    print(f" cartas  |{c1:^2}|  |{c2:^2}|  |{c3:^2}|  |{c4:^2}|  |{c2:^2}|  ")
                                                    print("   eram: |__|  |__|  |__|  |__|  |__|")
                                                    voltar()

                                                else:
                                                    print("se você estiver vendo isso, parabens você bugou o jogo")
                        



def menu():
    print()    
    print(" ___________________")
    print("|                   |")
    print("| A                 |")
    print("| ♦ _____________   |")
    print("|  |   SUPER 21  |  |")
    print("|  |    ARCADE   |  |")
    print("|  |             |  |")
    print("|  |1 = Iniciar  |  |")
    print("|  |2 = Regras   |  |")
    print("|  |3 = Créditos |  |")
    print("|  |4 = Sair     |  |")
    print("|  |_____________|  |")
    print("|                 ♦ |")
    print("|                 Ɐ |")
    print("|___________________|\n")

    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        print("\ncarregando...")
        time.sleep(2)
        jogo()
    elif opcao == '2':
        regras()
    elif opcao == "3":
        creditos()
    else:
        exit()


menu()

