# Cadastro de funcionarios

# Estrutura dic
Funcionario = {'Nome':'', 'Salario':0.0, 'Ativo':False}

# Endradas
print('\n\t\t\t -- Registro de Funcionário --\n')

Funcionario['Nome'] = input('informe o nome: ')
Funcionario['Salario'] = float(input(('Informe o salario: ')))
Funcionario['Ativa'] = True

# Saída
print(f'\n\nNome......{Funcionario["Nome"]}')
print(f'Salario.........{Funcionario["Salario"]}')
print(f'Funcionario Ativa..........{Funcionario["Ativa"]}')
# print("*** Funciomario Ativa ***") if funcionario['Ativa'] eles print("*** Fuincionario Inativo ***")
