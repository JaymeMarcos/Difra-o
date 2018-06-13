# coding : utf-8
import math
import os as os
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate
import numpy as np

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def color3(cor):
    if cor == 'blue':
        return 'Blues'
    elif cor == 'orange':
        return 'Oranges'
    elif cor == 'green':
        return 'Greens'
    elif cor == 'red':
        return 'Reds'

def negativo(x):
    y=[]
    for i in x:
        if i < 0:
            y.append(0)
        else:
            y.append(i)
    return y

def menu():  # criando o menu por função
    print('Bem vindo ao programa de difração de luz')
    print('Escolha as opções de cores de luz e insira os dados:')
    print('Azul -> 1')
    print('Laranja -> 2')
    print('Verde -> 3')
    print('Vermelha -> 4')

def montarimagem(x,cor,color):
    area= np.empty([len(x),len(x)])
    side= 1e-6
    dim = np.linspace(-side/2,side/2,len(x))
    for i in range (len(x)):
        for j in range(len(x)):
            if dim[i] == 0 and dim[j] ==0:
                area[j,i] = 0
            else:
                area[j,i] = x[i]
    plt.imshow(area, cmap=color)
    plt.title(cor)
    plt.colorbar()

def desenhaGrafico(x, y, cor, titulo):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    t, c, k = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(t, c, k, extrapolate=False)
    plt.figure('Gráfico 1')
    plt.title(titulo)
    plt.plot(xnew, negativo(suave(xnew)), color=cor)
    plt.scatter(xnew, negativo(suave(xnew)), color='#87CEFA')
    plt.ylabel("Intensidade da luz")

    plt.figure("Gráfico 2")
    montarimagem(negativo(suave(xnew)),titulo,color3(cor))
    plt.show()
    plt.show()


def cor(color_n):  # definindo o título do gráfico pela cor selecionada
    print('')
    if (color_n == '1'):
        return "Figura de difração para a cor azul"
    elif (color_n == '2'):
        return "Figura de difração para a cor laranja"
    elif (color_n == '3'):
        return "Figura de difração para a cor verde"
    elif (color_n == '4'):
        return "Figura de difração para a cor vermelha"


def cor2(color_n):  # definindo o título do gráfico pela cor selecionada
    print('')
    if (color_n == '1'):
        return "blue"
    elif (color_n == '2'):
        return "orange"
    elif (color_n == '3'):
        return "green"
    elif (color_n == '4'):
        return "red"


def erro():  # verificação de erro na seleção das cores
    opcoes = ['1', '2', '3', '4']
    y = input('Digite o número referente a cor escolhida:')
    while not (y in opcoes):
        print("Insira um valor válido!")
        y = input('Digite o número referente a cor escolhida:')
    return y


def comprimento(num):  # definição do comprimento de onda de cada cor
    if (num == '1'):
        return 637e-09
    elif (num == '2'):
        return 496e-09
    elif (num == '3'):
        return 566e-09
    elif (num == '4'):
        return 442e-09


def intensidade(comp, larg, ang):
    if (ang <= 1 and math.sin(ang) != 0.0):
        z = ((math.pi * comp) / (larg * (10 ** -6))) * ang
    else:
        return 0

    return ((math.sin(z) / z) ** 2)


def difracao(comp, larg):  # função que efetua o cálculo em si
    posicoes = []
    for n in range(-5, 6):
        x = n * (comp / (larg * (10 ** -6)))
        i = 'x'
        if x <= 1 and x >= -1:
            if ((n == -3) or (n == 3)):
                print('')
                print('')

            i = intensidade(comp, larg, x)

        if i != 'x' and larg >= comp:
            posicoes.append(1 - i)  # caso o valor de x ultrapasse 1 pois não existe seno maior que 1
        else:
            posicoes.append(0)

    return posicoes


if __name__ == '__main__':  # o main onde as funções são chamadas

    while (True):  # laço que "roda" o programa
        menu()
        num = erro()
        largura = float(input("Insira a largura da fenda(em micrometros) "))
        pos = difracao(comprimento(num), largura)
        var = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        desenhaGrafico(var, pos, cor2(num), cor(num))

        p = input('Deseja terminar o programa?  ')  # finalizando o programa
        if p == 'sim' or p == 'Sim' or p == 's' or p == 'S':
            break
            os.system('cls')  # apagando a tela
        else:
            os.system('cls')  # apagando a tela
