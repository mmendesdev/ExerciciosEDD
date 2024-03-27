#ATIVIDADE PARA APRENDER LISTA EM PYTHON

#criando uma lista
thisList = ["apple", "banana", "cherry"]
#mostrar o elemento da lista, o primeiro elemento sempre começa com 0 
print(thisList[0])
# (LEN) saber quantos elementos tem na lista
print(len(thisList))

ages = [28, 10, 40, 50]
print(len(ages)) #4
print(ages[3]) #50

names = ["Matheus", "João", "Maria", "Felipe"]
print(names)

myList = list(("Apple", 5, "home"))
print(myList)
myList.pop(0)
print(myList)

#1. Write a Python program to sum all the items in a list.
## 1. Escreva um programa Python para somar todos os itens de uma lista.
def somar_lista(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma

# Exemplo de uso
lista_numeros = [1, 2, 3, 4, 5]
resultado = somar_lista(lista_numeros)
print("A soma dos números na lista é:", resultado)
