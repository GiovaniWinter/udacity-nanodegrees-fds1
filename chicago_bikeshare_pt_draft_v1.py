# coding: utf-8

# Importando os Modulos.

import csv
import matplotlib.pyplot as plt



# configurando path
caminho = '/Users/gpacheco/Documents/Udacity/Nanodegree_Fundamentos_Data_ScienceI/ProjetoI/pj01/dados/'
arquivo = caminho + 'chicago.csv'

# Abrindo o arquivo
print('Lendo o arquivo...\n')
with open(arquivo,'r') as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: \n")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: \n")
print(data_list[1])

# TAREFA 1 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...\n")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras\n")

# Vamos mudar o data_list para remover o cabeçalho dele.
print(data_list[1:21])

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# TAREFA 2 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...\n")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras\n")

for linha in data_list[0:21]:
    print(linha[6])

# TAREFA 3 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...\n")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista

    for i in data:
        column_list.append(i[index])

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])
print(len(column_to_list(data_list, -2)))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."

# TAREFA 4 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

for linha in data_list[1:]:
    if linha[6].lower() == 'male':
        male +=1

    if linha[6].lower() == 'female':
        female +=1

## Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

# TAREFA 5 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = 0
    female = 0

    for linha in data_list[1:]:
        if linha[6].lower() == 'male':
            male += 1

        if linha[6].lower() == 'female':
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------


# TAREFA 6 -------------------------------------------------------------------------------------------------------------------------------------


input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    male = 0
    female = 0
    answer = ""

    if linha[6].lower() == 'male':
        male += 1

    if linha[6].lower() == 'female':
        female += 1

    if male > female:
        answer = "Masculino"
    else:
        answer = "Feminino"


    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)


# TAREFA 7 -------------------------------------------------------------------------------------------------------------------------------------
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_list(data_list,index,name):
    cout_name = 0

    for linha in data_list[1:]:
        if linha[index].lower() == name.lower():
            cout_name += 1

    return cout_name

qtn = []
qtn.append(count_list(data_list,5,"Customer"))
qtn.append(count_list(data_list,5,"Subscriber"))

user_list = column_to_list(data_list, -2)
types = ["Customer", "Subscriber"]
quantity = qtn
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Type')
plt.xticks(y_pos, types)
plt.title('Quantidade por Type')
plt.show(block=True)

# TAREFA 8 -------------------------------------------------------------------------------------------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
total_gender = male + female
qtreg = len(data_list)
diferenca = qtreg - total_gender
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque ha {} registros não preenchidos (Null) no campo Gender".format(diferenca)
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------
