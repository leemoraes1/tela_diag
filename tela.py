from tkinter import *

def tecla(): #função do botão "Enviar"
    nome=caixa1.get()
    mensagem=caixa2.get()
    frase["text"]=nome,"diz",mensagem

def fechar (): #Função para fechar a página 1
    janela.destroy()

janela = Tk() #Função da janela 1
janela.geometry("450x200") #Tamanho da janela
janela.config(bg="#E6C3B7") #Cor do fundo da janela
janela.title("Entrada de mensagem") #Nome da página

frase1=Label(janela, text="Leticia Moraes - 2° Semestre - UNIVALE",fg="#591E18", font="arial 11 underline bold", bg="#E6C3B7") #Cabeçalho da página
frase1.place(x=89,y=10) #Lugar da posição do cabeçalho

nome1=Label(janela,text="Nome:",fg="black", font="Verdana 10 ", bg="#E6C3B7") #Texto indicativo para "Nome:"
nome1.place(x=99,y=40) #Lugar da posição do texto "Nome:"

caixa1=Entry(janela,bg="#F7AA7D") #Função para a primeira caixa de entrada
caixa1.place(x=99,y=58) #Lugar da posição da primeira caixa de texto

nome2=Label(janela,text="Mensagem:",fg="black", font="Verdana 10 ", bg="#E6C3B7") #Texto indicativo para "Mensagem:"
nome2.place(x=99,y=77) #Lugar da posição do texto "Mensagem:"

caixa2=Entry(janela,bg="#F7AA7D", width=30) #Função para a segunda caixa de entrada
caixa2.place(x=99,y=96) 

botao=Button(janela, text="Enviar", command=lambda:[tecla(),fechar()],width=30)
botao.place(x=99,y=130)

janela2=Tk()
janela2.title("Resposta da Entrada")
janela2.geometry("450x300")
janela2.config(bg="#E6C3B7")

frase=Label(janela2, text="Aguardando mensagem...", bg="#E6C3B7",fg="black", font="Verdana 15")
frase.place(x=100,y=100)

janela = mainloop()