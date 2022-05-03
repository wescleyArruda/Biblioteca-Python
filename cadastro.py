from Class_livro import livro
from Class_usuario import usuario
from Class_alugar import alugar
#https://raccoon.ninja/pt/dev-pt/pesquisando-propriedades-de-objetos-em-uma-lista-python/
def pesquisa_livro(biblioteca,titulo):
    for i in range(1,len(biblioteca)):
        if (titulo.upper() == biblioteca[i].titulo.upper()):
            return i
    #return 0
    
    print("Livro não encontrado!!!")
  
def pesquisa_livro_titulo(biblioteca):
    titulo=input("Sistema de buscas por titulos :)\n Informe o titulo do livro que busca:")
    return pesquisa_livro(biblioteca,titulo)

def cad_livro(biblioteca):
    titulo=input("Titulo?")
    
    
    if (pesquisa_livro(biblioteca,titulo)):
        print("LIVRO COM ESSE TITULO JÁ CADASTRADO!!!")
    else:
        ano=int(input("Ano de lancamento?"))
        autor=input("Autor?")
        if (len(biblioteca)==1):
            id_livro=1 #outra forma "l" +str(1), mas teria de fazer um tratamento para incrementar.
        else:
            id_livro=(biblioteca[-1].id_livro+1)
        novo_livro=livro(id_livro,titulo.upper(),ano,autor.upper())
        biblioteca.append(novo_livro)
        if not (novo_livro in biblioteca):
            print("Não foi possivel cadastrar novo livro!!!\n"+"="*100)
            print("Novo livro cadastrado!")

def remove_livro(biblioteca):
    print("Remoção de livros:")
    index=pesquisa_livro_titulo(biblioteca)
    if (index):
        print("O livro que deseja é esse?")
        biblioteca[index].mostrar()
        if not (pesquisa_alugar(biblioteca[index].id_livro,alugueis)):
            print("Deseja remover da biblioteca?")
            resposta =str(input("sim ou não \n"))
            if(resposta.upper()=="SIM"):
                aux=biblioteca[index]
                biblioteca.remove(biblioteca[index])
                if (aux not in biblioteca):
                    print("Livro removido!!!")
                else:
                    print("Não foi possivel remover o livro")
        else:
            print("O livro foi alugado! Aguarde devolução para remover.")
        
  
#Cadastro de Usuarios/Clientes   
def cadastra_usuario_nivel(usuarios,nome,nivel):
    if(not pesquisa_usuario(usuarios,nome)):
        cpf=input("Informe o CPF:")
        if (usuarios):
            id_usuario=(usuarios[-1].id_usuario+1)
        else:
            id_usuario=1 #outra forma "u" +str(1), mas teria de fazer um tratamento para incrementar.
        novo_usuario=usuario(id_usuario,nome.upper(),cpf,nivel)
        usuarios.append(novo_usuario)
        if(novo_usuario in usuarios):
            print("usuario cadastrado com sucesso!!!")
        else:
            print("falha ao cadastrar usuario.:`(")
    else:
        print("Cliente ja cadastrado com o mesmo nome.:`(")
    
def cadastra_usuario(usuarios):
    nome=input("@"*59+"\nCadastro de usuarios.\n Informe o nome:")
    nivel=0
    if (len(usuarios)==1):
        nivel=1
    else:
        nivel=0
    cadastra_usuario_nivel(usuarios,nome,nivel)

def pesquisa_usuario_nome(usuarios):
    nome=input("#"*59+"\nBusca de Clientes por nome.\n Informe nome: ")
    index=pesquisa_usuario(usuarios,nome)
    return index
    
def pesquisa_usuario(usuarios,nome):
    for i in range(len(usuarios)):
        if (nome.upper() == usuarios[i].nome.upper()):
            return i
    print("Cliente não encontrado!")

def remove_usuario(usuarios):
    nome=input("@"*59+"\nRemoção de usuarios.\n Informe o nome:")
    index=pesquisa_usuario(usuarios,nome)
    if not(index==0):
        usuarios.remove(usuarios[index])
        print("Cliente removido.")

#Alugueis/Emprestimos de livros para clientes 

def pesquisa_alugar(livro,alugueis):
    for i in range(1,len(alugueis)):
            if (alugueis[i].id_livro==livro):
                return i

def cadasto_aluguel(alugueis,biblioteca,usuarios):
    index_livro=pesquisa_livro_titulo(biblioteca)
    if(index_livro):
        if not (alugueis==1):
            if (pesquisa_alugar(biblioteca[index_livro].id_livro,alugueis)):
                print("Livro ja alugado!!!")
            else:
                biblioteca[index_livro].mostrar()
                index_livro=biblioteca[index_livro].id_livro
                index_usuario=pesquisa_usuario_nome(usuarios)
                if(index_usuario):
                    print("indice id do usuario"+str(index_usuario))
                    usuarios[index_usuario].identidade()
                    index_usuario=usuarios[index_usuario].id_usuario
                    alugado=alugar(index_livro,index_usuario)
                    alugueis.append(alugado)
                else:
                    print("Não foi possivel completar o aluguel!")

def devolucao(alugueis,biblioteca):
    if(len(alugueis)==1):
        print("Ainda não foram feitos emprestimos!")
    else:
        index_livro=pesquisa_livro_titulo(biblioteca)
        if(index_livro):
            index=pesquisa_alugar(biblioteca[index_livro].id_livro,alugueis)
            if(index):
                print("O livro :")
                biblioteca[index_livro].mostrar()
                print("Foi devolvido.")
                alugueis.remove(alugueis[index])

def listar_alugados(alugueis,biblioteca,usuarios):
    if(len(alugueis)==1):
        print("Ainda não foram feitos emprestimos!")
    else:
        print("MOSTRANDO LISTAGEM DE LIVROS EMPRESTADOS E PARA QUEM:")
        for i in range(1,len(alugueis)):
            for j in range(1,len(biblioteca)):
                if( alugueis[i].id_livro==biblioteca[j].id_livro):
                    for z in range(1,len(usuarios)):
                        if (alugueis[i].id_cliente==usuarios[z].id_usuario):
                            print("+"*59)
                            biblioteca[j].mostrar()
                            usuarios[z].identidade()

def listar_alugados_clientes(alugueis,biblioteca,usuarios):
    if(len(alugueis)==1):
        print("Ainda não foram feitos emprestimos!")
    else:
        print("+"*59+"\n MOSTRANDO LISTAGEM DE LIVROS EMPRESTADOS PARA O CLIENTE:")
        index_usuario=pesquisa_usuario_nome(usuarios)
        if(index_usuario):
            for i in range(1,len(alugueis)):
                if(alugueis[i].id_cliente==usuarios[index_usuario].id_usuario):
                    print("LIVROS EMPRESTADOS POR: ")
                    usuarios[index_usuario].identidade()
                    print("LISTAGEM: ")
                    for j in range(1,len(biblioteca)):
                        if( alugueis[i].id_livro==biblioteca[j].id_livro):
                            biblioteca[j].mostrar()
                else:
                    print("O cliente nao possui livros emprestados!"+"."*59)
  
#que bagunça
def listar_alugados_titulo(alugueis,biblioteca,usuarios):
    if(len(alugueis)==1):
        print("Ainda não foram feitos emprestimos!")
    else:
        print("+"*59+"\n PESQUISAR LIVROS EMPRESTADOS POR TITULO: ")
        index_livro=pesquisa_livro_titulo(biblioteca)
        if(index_livro):
            for i in range(1,len(alugueis)):
                if(alugueis[i].id_livro==biblioteca[index_livro].id_livro):
                    print("LIVRO EMPRESTADO: ")
                    biblioteca[j].mostrar()
                    print("ALUGADO PARA: ")
                    for j in range(1,len(usuarios)):
                        if( alugueis[i].id_usuario==usuarios[j].id_usuario):
                            usuarios[j].identidade()  
                else:
                    print("O livro  nao foi emprestado!"+"."*59)

    