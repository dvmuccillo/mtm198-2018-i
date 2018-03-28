import math
import time


if __name__ == "__main__":
    '''
        Formula utilizada
        ----------------------------------------------
        |VALOR OBTIDO | VALOR DE N | TEMPO DECORRIDO |
        ----------------------------------------------
    '''

    #somatorio de 1/(n+k) > (13/24)
    print("Somatorio de 1/(n+k) > (13/24)")
    condicao = 13/24
    for n in range(1,11):
        inicio = time.time()
        valor = 0
        for k in range(1, (n+1)):
            valor += (1/(n+k))
        fim = time.time()
        if( valor > condicao ):
            resultado = round((fim - inicio), 4)
            print("Valor obtido => "+str(round(valor, 5))+"\t\tValor n => "+str(n)+"\t\tTempo => "+str(resultado))

    
    #somatorio de 1/k >= 2-(1/n)
    print("\nSomatorio de 1/k >= 2-(1/n)")
    for n in range(1, 11):
        inicio = time.time()
        valor = 0
        condicao = (2 - (1/n))
        for k in range(1, (n+1)):
            valor += (1/k)
        fim = time.time()
        if( valor >= condicao ):
            resultado = round((fim - inicio), 4)
            print("Valor obtido => " + str(round(valor, 5)) + "\t\tValor n => " + str(n) + "\t\tTempo => " + str(resultado))


    #somatorio de 1/(k**2) <= 2-(1/n)
    print("\nSomatorio de 1/(k**2) <= 2-(1/n)")
    for n in range(1, 11):
        inicio = time.time()
        valor = 0
        condicao = (2 - (1/n))
        for k in range(1, (n+1)):
            valor += (1/math.pow(k, 2))
        fim = time.time()
        if( valor <= condicao):
            resultado = round(( fim - inicio), 4)
            print("Valor obtido => " + str(round(valor, 5)) + "\t\tValor n => " + str(n) + "\t\tTempo => " + str(resultado))