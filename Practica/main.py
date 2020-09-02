import json
import webbrowser

print("Bienvenido...")
print("Escriba su comando...")
print('NOTA: Para separar, no utilizar "," solo utilizar ESPACIO')
comando1 = input()
suma = 0
arreglostring = comando1.split()
tam = len(arreglostring)
#CARGA LOS ARCHIVOS A LA MEMORIA
for espacio in range(1, tam):
    with open(arreglostring[espacio]) as file:
        data = json.load(file)
print('Los archivos fueron cargados con éxito')
print('......................................')
print('Escriba su comando...')
comando2 = input()

arreglostring2 = comando2.split()
tam2 = len(arreglostring2)
#SELECCIONA LOS ELEMENTOS DESEADOS Y LOS IMPRIME EN CONSOLA
if comando2 == "SELECCIONAR*":
    for espacio in range(1, tam):
        with open(arreglostring[espacio]) as file:
            data = json.load(file)
    for registros in data:
        print('nombre: ', registros['nombre'])
        print('edad: ', registros['edad'])
        print('activo: ', registros['activo'])
        print('promedio: ', registros['promedio'])
        print('................................')
if len(arreglostring2) == 2:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            print(registros[arreglostring2[1]])
if len(arreglostring2) == 3:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            print(registros[arreglostring2[1]])
            print(registros[arreglostring2[2]])
if len(arreglostring2) == 4:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            print(registros[arreglostring2[1]])
            print(registros[arreglostring2[2]])
            print(registros[arreglostring2[3]])
if len(arreglostring2) == 5:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            print(registros[arreglostring2[1]])
            print(registros[arreglostring2[2]])
            print(registros[arreglostring2[3]])
            print(registros[arreglostring2[4]])

print('Escriba su comando...')
comando3 = input()

arreglostring3 = comando3.split()
tam3 = len(arreglostring3)
#SELECCIONA ENTRE EL MAXIMO, MINIMO O SUMA DE EDADES O PROMEDIO
if arreglostring3[0] == 'MAXIMO':
    if arreglostring3[1] == 'edad':
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            lista = [registros['edad']]
        minimo = min(lista)
        print(minimo)

    else:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            lista = [registros['edad']]
        minimo = min(lista)
        print(minimo)


if arreglostring3[0] == 'MINIMO':
    if arreglostring3[1] == 'edad':
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            lista = [registros['edad']]
        minimo = min(lista)
        print(minimo)
    else:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            lista = [registros['promedio']]
        minimo = min(lista)
        minimo_lista = minimo
        print(min(minimo_lista))

if arreglostring3[0] == 'SUMA':
    if arreglostring3[1] == 'edad':
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            Lista = (registros['edad'])
            suma = suma + Lista
        print(suma)
    else:
        for espacio in range(1, tam):
            with open(arreglostring[espacio]) as file:
                data = json.load(file)
        for registros in data:
            Lista = (registros['promedio'])
            suma = suma + Lista
        print(suma)

print('Escriba su comando...')
comando4 = input()
if comando4 == 'CUENTA':
    for espacio in range(1, tam):
        cargar_archivos = 2 * (tam - 1)
    print(cargar_archivos)

print('Escriba su comando...')
comando5 = input()
print('Espere, se abrirá el reporte en un instante...')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
for espacio in range(1, tam):
    with open(arreglostring[espacio]) as file:
        data = json.load(file)
print('El reporte está abriendo')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
new_webpage = open('reporte.html', 'w')
new_webpage.write(str(data))
new_webpage.close()
print('..............................................')
print('..............................................')
print('..............................................')
print('..............................................')
print('El reporte se ha abierto')
webbrowser.open_new_tab('reporte.html')