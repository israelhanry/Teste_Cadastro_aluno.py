# Teste_Cadastro_aluno.py
Teste de dois iniciantes
import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastro():
   print("________________________________")
   print("")
   nome=input("digite o nome do aluno:")  
   turma=input("digite a turma do aluno:")
   nota=float(input("digite a nota do aluno:"))
   print("")
   print("________________________________")
   lista_nome.append(nome)
   lista_turma.append(turma)
   lista_nota.append(nota)

lista_nome=[]
lista_turma=[]
lista_nota=[]

while True:
 print("________________________________")
 print("")
 print("operações disponiveis:")
 print("Cadastrar aluno: 1")
 print("listar alunos: 2")
 print("Deletar aluno: 3")
 print("Encerrar programa: 4")
 print("")
 print("________________________________")

 operacao=int(input("Digite o numero escolhido:"))
 if operacao==1:
   cadastro()
   input("Pressione ENTER...")
   limpar()
   
 elif operacao==2:
   
    print("\n--- LISTA DE ALUNOS ---\n")
    for i in range(len(lista_nome)):
     print(f"{i} - Nome: {lista_nome[i]}")
     print(f"    Turma: {lista_turma[i]}")
     print(f"    Nota: {lista_nota[i]}")
     print("---------------------------")
    input("Pressione ENTER...")
    limpar()

 elif operacao==3:
   apagar = input("Digite o nome do aluno: ")
   encontrado = False

   for i in range(len(lista_nome)):
      if lista_nome[i] == apagar:
         lista_nome.pop(i)
         lista_nota.pop(i)
         lista_turma.pop(i)
         print("Aluno removido!")
         encontrado = True
         break
      
      if not encontrado:
          print("Não há esse nome")
   input("Pressione ENTER...")
   limpar()

 elif operacao!=1 and operacao!=2 and operacao!=3 and operacao!=4:
   print("digite certo rapaize")
 
 elif operacao==4:
   print("processo encerrado")
   break
 
