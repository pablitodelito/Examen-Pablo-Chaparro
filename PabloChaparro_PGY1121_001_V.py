
pisos = 10
departamentos_por_piso = 4
total_departamentos = pisos * departamentos_por_piso

precios = {
'A':3800,
'B':3000,
'C':2800,
'D':3500
}

venta_de_departamentos = ['-' for _in range(departamentos_por_piso)][for _in range(pisos)]:

compradores = []
 
def mostrar_menú():
    print("xxxxxxxxxxxxxx Menú xxxxxxxxxxxxx")
    print("1.- Comprar departamento")
    print("2.- Mostrar departamentos disponibles")
    print("3.- Ver lista de compradores")
    print("4.- Mostrar ganancias totales")
    print("5.- Salir")

def comprar_departamento():
        print("xxxxxxxxxxxxxx Comprar departamento xxxxxxxxxxxxxx")
        piso = int(input("Ingrese el numero de piso (1-10):"))
        tipo = input("Ingrese el tipo de departamento (A, B, C, D): ")
        tipo = tipo.upper()

        if piso < 1 or pisos or tipo not in precios:
            print("Error tipo o departamento inválido")
            return
        departamento = tipo + str(piso)
        if venta_de_departamentos[piso-1][ord(tipo)-ord('A')] != '-':
            print("Departamento", departamento, "No disponible")
            return
        run = input("Ingrese el rut del comprador sin guiones ni puntos: ")
        if not run.isdigit():
            print("Error el Run es incorrecto" )
            return
        venta_de_departamentos[piso-1][ord(tipo)- ord ('A')] = 'X'
        compradores.append((run,departamento))
        print("La operacion ah sido exitosa")

def mostrar_departamentos_disponibles():
    print("xxxxxxxxxxxxxxxxxxxxxx Departamentos disponibles xxxxxxxxxxxxxxxxxxxxxxx")
    for piso in range (pisos):
        for tipo in precios:
            estado = venta_de_departamentos[piso][ord(tipo)-ord ('A')]
            departamento = tipo + str (piso + 1)
            print("Departamento", departamento, "Departamento disponible" if estado == '-'else "Vendido" )

def ver_listado_compradores():
    print("xxxxxxxx Listado de compradores xxxxxxxxx"):
    compradores_ordenados = sorted(compradores, key=lambda x: x[0])
    for comprador in compradores_ordenados:
        print("run:", comprador [0], " - Departamento:", comprador [1])

def mostrar_ventas_totales():
    print("xxxxxxxxxxxxx Total ventas xxxxxxxxxxx")
    total_ventas = sum(precios[tipo]for fila in venta_de_departamentos for tipo in fila if tipo == 'X')
    print("Ganancias totales:", total_ventas , "UF")

def salir():
    print("Hasta luego")
    print("Nombre, [Tu nombre]")
    print("Apellido: [Tu Apellido]" )
    print("Fecha actual:",().strftime("%Y-%M-%D"))

def main():
    while True:
        mostrar_menú()
        opcion = input("Ingrese una opcion: ")

        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        if opcion == '3':
            ver_listado_compradores()
        if opcion == '4':
            mostrar_ventas_totales()
        elif opcion == '5':
            salir()
            break
        else:
            print("¡Error!, opcion invalida. Por favor intentar nuevamente")    

        if _name_ == "_main_":
            main()

def _name_():





    