import numpy as np
import matplotlib.pyplot as plt


def sequencia_limitada(self):
    pass

def sequencia_monotona(self):
    pass

def sequencia_convergente(self):
    pass


if __name__ == "__main__":
    sequencia = []
    data1 = [10, 5, 2, 4, 6, 8]
    data2 = [1, 2, 4, 8, 7, 4]
    x = 10 * np.array(range(len(data1)))

    plt.plot(x, data1, 'go')  # green bolinha
#    plt.plot(x, data1, 'k:', color='orange')  # linha pontilha orange

    plt.plot(x, data2, 'r^')  # red triangulo
#    plt.plot(x, data2, 'k--', color='blue')  # linha tracejada azul

#    plt.axis([-10, 60, 0, 11])    dois primeiros valores, intervalo eixo X, e os dois ultimos, intervalo eixo Y.
    plt.title("Gráficos Sequências")

    plt.grid(True)
    plt.xlabel("n E N")
    plt.ylabel("R")
    plt.show()