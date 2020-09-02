def evalua_pos(pos):
    if(pos%2==0):
        return(True)
    else:
        return(False)

N = int(input())
palabras = []
#El siguiente ciclo es para ir ingresando los N strings y se almacenan en el array
for c in range(N):
    S = input()
    palabras.append(S)

#El siguiente ciclo es para tomar cada string del array
for elemento in palabras:
    flag = 0
    Rp = '' #String que contendrá todos los caracteres de posiciones pares
    Ri = '' #String que contendrá todos los caracteres de posiciones impares
    for x in elemento:
        if(evalua_pos(flag)):
            Rp += x
        else:
            Ri += x
        flag += 1 #contador de loops que sirve como contador de posicion
    else:
        print('{} {}'.format(Rp, Ri)) #Se imprime los strings resultantes de la palabra trabajada
