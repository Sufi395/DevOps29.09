# -*- coding: utf-8 -*-
"""
Jhonatan Teodoro - RA: 1700081
Alan Poveda - RA: 1520274

"""
def gravar():
    agenda_arquivo = open ('agenda.txt','r+')
    texto = agenda_arquivo.readlines()
    requisitos = ['Nome:', 'Rua:', 'Cep:', 'Bairro:', 'Estado:', 'Telefone:']
    formulario = []
    gravar =[]
    for x in requisitos:
        formulario.append(input(x))
    for x in range(len(requisitos)):
        gravar.append(requisitos[x]+formulario[x]+' ')
    texto.append(gravar)
    agenda_arquivo.writelines(texto[-1])
    agenda_arquivo.writelines("\n")
    agenda_arquivo.close()

def consulta():
    nome = str(input("Digite um nome para pesquisa: "))
    agenda_arquivo = open('agenda.txt','r+')
    texto = agenda_arquivo.readlines()
    for x in texto:
        if nome in x:
            return print(x)
    agenda_arquivo.close()
    return"Cadastro não localizado"

while True:
    print("Bem vindo á Agenda")
    escolha = int(input(print("Para cadastrar um contato Digite 1 e para consultar Digite 0")))
    if escolha == 1:
        gravar()
    elif escolha == 0:
        consulta()
    else:
        print("operação invalida, reiniciando sistema")



    