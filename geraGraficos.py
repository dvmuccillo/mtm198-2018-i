import numpy as np
import matplotlib.pyplot as plt
import math


def sequencia(formula, max, label_sequencia):
    sequencia = []
    for i in range(max):
        sequencia.append(math.pow(formula,(i+1)))

    x = 1 + np.array(range(max))

    plt.plot(x, sequencia, 'go', label=label_sequencia)  # green bolinha
    #   plt.plot(x, data1, 'k:', color='orange')  # linha pontilha orange

    ''' dois primeiros valores, intervalo eixo X, e os dois ultimos, intervalo eixo Y
        plt.axis([-10, 60, 0, 11])'''
    plt.title("Gráficos Sequências")

    plt.subplot().legend(loc='best', shadow=False, fontsize='large')
    plt.grid(True)
    plt.xlabel("n E N")
    plt.ylabel("R")
    plt.show()


if __name__ == "__main__":

    sequencia((1/2), 10, 'Sequencia convergente')

    sequencia((-2), 8, 'Sequencia divergente')