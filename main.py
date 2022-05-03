#from Class_livro import livro
#from Class_usuario import usuario
import cadastro as cad

print("--"*5+" VARIAVEL GLOBAL - SISTEMA BIBLIOTECARIOS "+ "--"*5)

def main():
    #Variaveis de listas inicializadas
    biblioteca = []
    usuarios = []
    alugueis = []

#Alimentando o banco
#gambiarra para pular um indice, para começar no 1., listas biblioteca,usuarios e alugueis.
    l1 = cad.livro(0,"$$$$",0000,"$$$$")
    biblioteca.append(l1)
    cliente=cad.usuario(0,"$$$$",0000,0)
    usuarios.append(cliente)
    aluga_0=cad.alugar(0,0)
    alugueis.append(aluga_0)
    
    #print("chamando função de cadastro de livro: cad_livro(passando como parametro uma lista biblioteca\n)")
    #cad.cad_livro(biblioteca)
    l1 = cad.livro(1,"METRO2033", 2016, "Dmitriy Glukhovskiy")
    l2 = cad.livro(2,"Orgulho e Preconceito",'1813', "Jane Austen")
    biblioteca.append(l1)
    biblioteca.append(l2)
    l1 = cad.livro(3,"Cinco Minutos", 1856, "Jose de Alencar")
    biblioteca.append(l1)
    l1 = cad.livro(4,"A Viuvinha", 1857, "Jose de Alencar")
    biblioteca.append(l1)
    
    #chamando função de cadastro de usuario: cadastra_usuario(passando como parametro uma lista usuarios)    
    cliente=cad.usuario(1,"wescley",90051816805,0)
    usuarios.append(cliente)
    cliente=cad.usuario(2,"Arruda",635328425000,1)
    usuarios.append(cliente)
    
    #Fim da alimentação
    menu_n1(biblioteca,usuarios,alugueis)

def menu_n1(biblioteca,usuarios,alugueis):
    while True:
        opcao=None
        # Vamos au menu nivel 1 onde fica cadastro de livors e clientes
        print("&"*60+"\n"+"&"*23+" MENU NIVEL 1 "+"&"*23+"\n"+
        "&"*20 + "  1 - LIVROS        " +"&"*20+"\n"+
        "&"*20 + "  2 - CLIENTES      "+"&"*20+"\n"+
        "&"*20 + "  3 - ALUGUEIS       " +"&"*20+"\n"+
        "&"*20 + " exit- para sair.   " +"&"*20+"\n"+
        "&"*60) 
        opcao=str(input("Escolha uma opção: "))
        if (opcao=='1'):
            while True:
                menu_n2("LIVROS ")
                opcao=str(input("Escolha uma opção: "))
                if(opcao== '1'):
                    cad.cad_livro(biblioteca)
                elif(opcao=='2'):
                    index=cad.pesquisa_livro_titulo(biblioteca)
                    if not (index):
                        print("Livro não encontrado no acervo da biblioteca!!!")
                    else:
                        biblioteca[index].mostrar()
                        index=None
                    
                elif(opcao=='3'):
                    cad.remove_livro(biblioteca)
                elif(opcao=='4'):
                    for i in range(1,len(biblioteca)):
                        biblioteca[i].mostrar()
                elif(opcao.lower()=='exit'):
                    break
                else:
                    print("entrada invalida!")
                input("Pressione <enter> para continuar")
                print("\n"*10)
                
        elif(opcao=='2'):
            while True:
                menu_n2("CLIENTES")
                opcao=str(input("Escolha uma opção: "))
                if (opcao=='1'):
                    cad.cadastra_usuario(usuarios)
                elif(opcao=='2'):
                    #nome=input("@"*59+"\nCadastro de usuarios.\n Informe o nome:")
                    index=cad.pesquisa_usuario_nome(usuarios)
                    if(index):
                        usuarios[index].identidade()
                elif(opcao=='3'):
                    cad.remove_usuario(usuarios)
                elif(opcao=='4'):
                    for i in range(1,len(usuarios)):
                        usuarios[i].identidade()
                elif(opcao.lower()=="exit"):
                    break
                else:
                    print("entrada invalida!")
                input("Pressione <enter> para continuar")
        
        elif (opcao=='3'):
            while True:
                print("\n"*5+"_"*60+"\n"+"_"*23+" MENU ALUGUEIS "+"&"*23+"\n"+
            "_"*20 + "  1 - EMPRESTAR LIVRO       " +"_"*20+"\n"+
            "_"*20 + "  2 - DEVOLUÇÃO             "+"_"*20+"\n"+
            "_"*20 + "  3 - LISTAR ALIGUEIS       " +"_"*20+"\n"+
            "_"*20 + "  4 - PESQUISA POR CLIENTES " +"_"*20+"\n"+
            "_"*20 + "  5 - PESQUISA POR TITULO   " +"_"*20+"\n"+
            "_"*20 + " exit- para sair.   " +"_"*20+"\n"+
            "_"*60)
                opcao=str(input("Escolha uma opção: "))
                if (opcao == '1'):
                    cad.cadasto_aluguel(alugueis,biblioteca,usuarios)
                elif (opcao == '2'):
                    cad.devolucao(alugueis,biblioteca)
                
                elif (opcao == '3'):
                    cad.listar_alugados(alugueis,biblioteca,usuarios)
                elif(opcao.lower()=="exit"):
                    break
                elif(opcao == '4'):
                    cad.listar_alugados_clientes(alugueis,biblioteca,usuarios)
                elif(opcao == '5'):
                    cad.listar_alugados_titulo(alugueis,biblioteca,usuarios)
                else:
                    print("entrada invalida!")
                input("Pressione <enter> para continuar")
        
        elif (opcao=='4'):
            pass
        elif(opcao.lower()=="exit"):
            break
        
        else:
            print("entrada invalida!")
        input("Pressione <enter> para continuar")
        print("\n"*10)

def menu_n2(auxiliar):
    print("*"*60+"\n|"+"_"*22+" MENU {} ".format(auxiliar)+"_"*23+"|\n|"+
            "_"*15 + " 1 - CADASTRO DE {} ".format(auxiliar) +"_"*19+"|\n|"+
            "_"*15 + " 2 - PESQUISA DE {} ".format(auxiliar)+"_"*19+"|\n|"+
            "_"*15 + " 3 - REMOVER {}     ".format(auxiliar) +"_"*19+"|\n|"+
            "_"*15 + " 4 - LISTAR {}      ".format(auxiliar) +"_"*19+"|\n|"+
            "_"*15 + " exit - para sair.        " +"_"*19+"|\n"+
            "*"*60)
    
if __name__ == '__main__':
    main()