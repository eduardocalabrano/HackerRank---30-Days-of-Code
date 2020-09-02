def concreta_busqueda(nombre, dic):
    elemento = ''
    elemento = ''.join(map(str, nombre))
    valor = dic.get(elemento)
    if(valor):
        print('{}={}'.format(elemento, valor))
    else:
        print('Not found')

n = int(input())
dic = {}
busqueda = []

for x in range(n):
    arr = list(input().rstrip().split())
    dic.setdefault(arr[0],arr[1])

while True:
    try:
        nombre_buscado = input().rstrip().split()
        if(len(nombre_buscado)>0):
            concreta_busqueda(nombre_buscado, dic)
        else:
            break
    except:
        break
