        
from collections import namedtuple

ventas = namedtuple("ventas", "registro consulta_fecha decripcionProducto cantidadPiezas precioVenta subtotal iva total")

ventasDiccionario = {}

while True:
    print("*" * 30)
    print("Bienvendio al menú principal")
    print("Por favor eliga la opcion que quiera realizar \n")
    opcion = int(input("1- Registrar una venta | 2- Consultar una venta | 3- Salir: \n"))
    print("*" * 30)
    if opcion == 1:      
        while True:
            registro = input("Ingrese su número de folio: \n")
            if registro in ventasDiccionario.keys():
                print("Este número de folio ya esta registrado, ingrese uno nuevo por favor")
            else:
                consulta_fecha = input("Ingrese la fecha en la que se realizo la venta DD/MM/AA: \n")
                decripcionProducto = input("Por favor ingrese la descrpcion de todos sus producto: \n")
                cantidadPiezas = int(input("Por favor ingrese la cantidad total de piezas: \n"))
                precioVenta =int(input("Por favor ingrese el precio total de la venta: "))
                print(f"Su número de registro es : {registro} \n la fecha es : {consulta_fecha}\n la descripcion es : {decripcionProducto}\n la cantidad de peizas es : {cantidadPiezas}\n el precio de venta es : {precioVenta}")
                subtotal = (cantidadPiezas * precioVenta)
                iva = (0.16 * subtotal)
                total = (subtotal + iva)
                print(f"SUBTOTAL: {subtotal}")
                print(f"IVA: {iva}")
                print(f"TOTAL: {total}")
                break

       
        
        nuevaVenta = ventas(registro, consulta_fecha, decripcionProducto, cantidadPiezas, precioVenta, subtotal, iva, total)

        ventasDiccionario[registro] = nuevaVenta
        
    elif opcion == 2:
        consultarVenta= input("Ingrese su número de folio que desea buscar: ")
        for ventas in ventasDiccionario.keys():
            if consultarVenta in ventasDiccionario.keys():
                print(f"Datos de la venta:\n Número de registro: {ventasDiccionario[consultarVenta].registro}\n Fecha de la venta: {ventasDiccionario[consultarVenta].consulta_fecha}\n Descripcion del producto o productos: {ventasDiccionario[consultarVenta].decripcionProducto}\n Total de cantidad de piezas: {ventasDiccionario[consultarVenta].cantidadPiezas}\n Precio total de venta: {ventasDiccionario[consultarVenta].precioVenta}\n Subtotal:{ventasDiccionario[consultarVenta].subtotal}\n Iva:{ventasDiccionario[consultarVenta].iva}\n Total:{ventasDiccionario[consultarVenta].total} ")
                break

            else:
                print("Número de folio no encontrado, por favor ingrese un número de folio que ya este registrado.")
    elif opcion == 3:
        break
      