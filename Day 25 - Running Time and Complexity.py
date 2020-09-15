def es_divisible(dividendo, divisor):
    if(dividendo % divisor == 0):
        print('por el numero {}'.format(divisor))
        return(True)
    else:
        return(False)

def es_primo(numero):
    if(numero > 3 and numero % 2 == 0):
        return(False)
    elif(numero > 9 and numero % 5 == 0):
        return(False)
    else:
        inicio = 2
        for x in range(inicio, numero):
            if(x > 1000):
                #Hago el supuesto que si no es divisible por nada hasta el 1000 entonces es un numero primo. No he comprobado lo contrario.
                return(True)
            elif(es_divisible(numero, x) is True):
                return(False)
        else:
            return(True)

N = int(input()) #se ingresa cuantos numeros se evaluaran
for x in range(N):
    numero = int(input()) #inserta por teclado un numero a evaluar
    if(es_primo(numero) and numero != 1):
        print('Prime')
    else:
        print('Not prime')
