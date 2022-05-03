class usuario:
#nivel 0 ou 1, onde quanto menor maior a priorirade
#ou seja, nive igual a 0 zero, pode cadastrar ou auterar
#
    def __init__(self,id_usuario, nome,cpf,nivel=1):
        self.id_usuario= id_usuario
        self.nome = nome
        self.cpf = cpf
        self.nivel = nivel
    
    def identidade(self):
        print("ID do Cliente: {} NOME: {} CPF: {} NIVEL: {}".format(self.id_usuario,self.nome.upper(), self.cpf, self.nivel))