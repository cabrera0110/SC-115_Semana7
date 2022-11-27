# VARIABLES
tipo = ""
cantidad = 0
subtotal = 0
porcentaje_descuento = 0.0
descuento = 0
iva = 0


# FUNCION CALCULO
def calculo_neumaticos(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal


# FUNCION DESCUENTO
def aplicar_descuento(subtotal, descuento):
    subtotal_con_descuento = subtotal - (subtotal * descuento)
    return subtotal_con_descuento


# FUNCION IVA
def aplicar_iva(subtotal, subtotal_con_descuento):
    subtotal = subtotal - subtotal_con_descuento
    iva = subtotal * 0.13
    return iva


# FUNCION FACTURA
def imprimir_factura(tipo, cantidad, subtotal, descuento, iva, total):
    print("\nGracias por su compra. A continuación, su factura:\nTipo..............", tipo, "\nCantidad..........",
          cantidad, "\nSubtotal..........", subtotal, "\nDescuento.........", descuento, "\nIVA...............",
          iva, "\nMonto por Pagar...", total)


# CICLO MENU
while True:
    menu = input(
        "\nGracias por utilizar nuestro programa. A continuación, el menú de opciones: \n\n1. Cálculo neumáticos. "
        "\n2. Aplicar descuento.\n3. Cálculo deL IVA.\n4. Imprimir Factura.\n5. Salir. \n"
        "\nDigite el número de la opción que desea ejecutar: \n")

    # OPCION MENU 1: CALCULO MONTO
    if menu == "1":
        tipo = input(
            "\nDe acuerdo. A continuación podrá seleccionar el tipo de neumáticos que desea comprar:\n"
            "\n1. Digite '1' para neumáticos sintéticos.\n2. Digite '2' para neumaticos híbridos."
            "\n3. Digite '3' para neumáticos naturales.\n")

        cantidad = int(input("\nDigite la cantidad de neumáticos que desea comprar: \n"))

        # DEFINICION TIPO SINTENTICO
        if tipo == "1":
            tipo = "Sintéticos"
            if cantidad > 10:
                porcentaje_descuento = 0.95
                porcentaje = "5%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 12000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

        # DEFINICION TIPO HIBRIDO
        if tipo == "2":
            tipo = "Híbridos"
            if cantidad > 10:
                porcentaje_descuento = 0.90
                porcentaje = "10%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 25000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

        # DEFINICION TIPO NATURAL
        if tipo == "3":
            tipo = "Naturales"
            if cantidad > 8:
                porcentaje_descuento = 0.93
                porcentaje = "7%"
            else:
                porcentaje_descuento = 1
                porcentaje = "0%"
            subtotal = calculo_neumaticos(cantidad, 45000)
            print("Subtotal..........", subtotal)
            print("Descuento aplicable...", porcentaje)
            continue

    # OPCION MENU 2: DESCUENTO
    if menu == "2":
        descuento = aplicar_descuento(subtotal, porcentaje_descuento)
        print("Descuento.........", descuento)
        continue

    # OPCION MENU 3: IVA
    if menu == "3":
        iva = aplicar_iva(subtotal, descuento)
        print("IVA...............", iva)
        continue

    # OPCION MENU 4: FACTURA
    if menu == "4":
        total = subtotal - descuento + iva
        imprimir_factura(tipo, cantidad, subtotal, descuento, iva, total)
        continue

    # SALIDA MENU
    else:
        print("Adios!")
        break
