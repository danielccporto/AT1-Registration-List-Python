# Uma possível solução
```python
# Armazenamento dos cadastros
nomes = []
cpfs = []
nascimentos = []

# Se não há nenhum cadastro, imprime mensagem informando
if len(nomes) == 0:
  print('Nenhum cadastro')
else:
  # Para cada cadastro...
  for i in range(len(nomes)):
    # Imprime os dados do cadastro
    print()
    print('ID:', i + 1)
    print('Nome:', nomes[i])
    print('CPF:', cpfs[i])
    print('Data de nascimento:', nascimentos[i])
```