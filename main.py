# Armazenamento dos cadastros
cadastro = []
nomes = []
cpfs = []
nascimentos = []
data = []
CP = [] 

nome = input("Digite seu nome ou se quiser encerrar o programa digite a palavra terminou: ")

if nome.strip() != "terminou":
  data = input("Digite sua data de nascimento (no formato dd/mm/aaaa): ")
  CP = input("Digite seu CPF: ")

i = 0

while nome.strip() != "terminou": 
  cadastro.append(i+1)
  nomes.append(nome)
  nascimentos.append(data)
  cpfs.append(CP) 

  i = i +1 
  nome = input("Digite seu nome ou se quiser encerrar o programa digite a palavra terminou: ")
  if nome.strip() != "terminou":
    data = input("Digite sua data de nascimento (no formato dd/mm/aaaa): ")
    CP = input("Digite seu CPF: ")
  
  
if i != 0 : 
  print(f"Nomes : {nomes}, CPFs : {cpfs}, Datas de nascimento : {nascimentos}, IDs : {cadastro}")

else : 
  print("Não há nenhum cadastro")
      
  




  
  


  





  
  