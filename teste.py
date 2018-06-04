#coding : utf-8
import os
import math
import matplotlib.pyplot as plt #importando a biblioteca de criação de gráficos

def menu(): #criando o menu por função
    print ('Bem vindo ao programa de difração de luz')
    print ('Escolha as opções de cores de luz e insira os dados:')
    print('Azul -> 1')
    print('Laranja -> 2')
    print('Verde -> 3')
    print('Vermelha -> 4')


def cor(color_n): #definindo o título do gráfico pela cor selecionada
    print(color_n)
    if(color_n == '1'):
        return "Figura de difração para a cor azul"
    elif (color_n == '2'):
         return "Figura de difração para a cor laranja"
    elif (color_n == '3'):
         return "Figura de difração para a cor verde"
    elif (color_n == '4'):
          return "Figura de difração para a cor vermelha"

def erro(): #verificação de erro na seleção das cores
    opcoes = ['1', '2', '3', '4']
    y = input('Digite o número referente a cor escolhida:')
    while not (y in opcoes):
        print("Insira um valor válido!")
        y = input('Digite o número referente a cor escolhida:')
    return y 



def comprimento(num): #definição do comprimento de onda de cada cor
    if(num=='1'):
      return 637e-09
    elif(num== '2'):
       return 496e-09
    elif(num == '3'):  
     return 566e-09
    elif(num == '4'):
     return 442e-09 

def difracao(comp,larg): #função que efetua o cálculo em si
   posicoes = []
   for n in range(1, 6):
      x= (n*comp)/(larg*(10**-6))
      if(x > 1):
         posicoes.append(0) #caso o valor de x ultrapasse 1 pois não existe seno maior que 1
      else:
         posicoes.append(math.degrees(math.asin(x)))
   return posicoes   
      


if __name__ == '__main__': #o main onde as funções são chamadas
 

 while (True): #laço que "roda" o programa
    menu()
    num=erro()

    largura = float(input("Insira a largura da fenda(em micrometros) "))

    pos = difracao(comprimento(num),largura)
    var = [1,2,3,4,5]
    plt.plot(var,pos) #criando o gráfico de linha
    plt.scatter(var,pos) #criando o gráfico de dispersão

    plt.title(cor(num)) #criando o título usando a função cor
    plt.xlabel('Mínimos') #nome do eixo x
    plt.ylabel('Posição do feixe (em graus)') #nome do eixo y

    plt.show() #exibindo o gráfico
    

    p = input ('Deseja terminar o programa?  ') #finalizando o programa
    if p == 'sim':
     break
     os.system('cls') #apagando a tela
 os.system('cls') #apagando a tela


    


