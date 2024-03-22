import sys
from datetime import date
#LISTA DE SUITES
suites =[
    {
        "nombre":"Suite Junior",
        "capacidad": 2,
        "precio_noche": 150000,
        "disponibles":10
    },
    {
        "nombre":"Suite Doble",
        "capacidad": 4,
        "precio_noche": 220000,
        "disponibles":10
    },
    {
        "nombre":"Suite Presidencial",
        "capacidad": 6,
        "precio_noche": 300000,
        "disponibles":2
    }
]
 
#Realiza el registro de la reserva dentro de la lista "reservas[]"
reservas = [] 
def registroReserva(tipo_suite, fecha_llegada, fecha_salida, id_cliente, nombre_cliente, correo_cliente, num_personas):
    reservas.append(
        {
            "id_cliente": id_cliente,
            "nombre_cliente": nombre_cliente,
            "correo_cliente": correo_cliente,
            "fecha_llegada": fecha_llegada,
            "fecha_salida": fecha_salida,
            "num_personas": num_personas,
            "tipo_suite": tipo_suite
        }
    )
    print(f'Reserva realizada con exito para la suite {tipo_suite}')
    print(f'Información de la reserva: \n{reservas[-1]}')

#Valida la disponibilidad de las suites para su posterior elección RF03
def eleccionSuite(tipo_suite, fecha_llegada, fecha_salida, id_cliente, nombre_cliente, correo_cliente, num_personas):
    suite_elegida = None
    
    for suite in suites:
        #Validar nombre de suite
        if suite["nombre"] == tipo_suite:
            suite_elegida = suite
            break

    fecha_valida = False    
    
    #Luego de validar si la suite es correcta: 
    if suite_elegida:
        for reserva in reservas:
            #Buscar en las reservas la suite y hacer los debidos procesos
            if reserva["tipo_suite"] == tipo_suite:
                #Validar si hay forma de acomodar una reserva en una habitación una fecha antes o después de haber estado reservada
                if (reserva["fecha_llegada"] < fecha_llegada < reserva["fecha_salida"]) or (reserva["fecha_llegada"] < fecha_salida < reserva["fecha_salida"]):
                    print("SE ENCUENTRA OCUPADO POR LA RESERVA: ")
                    print(f"FECHA INICIO: {reserva["fecha_llegada"]} \n FECHA FIN: {reserva["fecha_salida"]}")
                    fecha_valida = False
                    break
                else:
                    fecha_valida = True

        #Caso por si hay suites disponibles     
        if suite_elegida["disponibles"] > 0:
            suite_elegida["disponibles"] -=1
            registroReserva(tipo_suite, fecha_llegada, fecha_salida, id_cliente, nombre_cliente, correo_cliente, num_personas)
        else:
            #Caso por si hay suites ocupadas pero se puede reservar en una fecha diferente
            if fecha_valida:
                registroReserva(tipo_suite, fecha_llegada, fecha_salida, id_cliente, nombre_cliente, correo_cliente, num_personas)
    else:
        print("La suite elegida no existe")

#MENU
while True:
    print(""" ----------- INGRESO DE RESERVAS V1.0 ALPHA -----------
          1. Realizar nueva reserva.
          2. Consultar reservas.
          3. Salir.
          ----------------------------------------------------------""")
    op = int(input("OPCIÓN: "))

    if op==1:

        #Solicitud de datos cliente
        id_cliente = input("Ingrese cedula: ")
        nombre_cliente = input("Ingrese su nombre: ")
        correo_cliente = input("Ingrese correo del cliente: ")

        #Fecha llegada
        año_llegada = int(input("Ingrese año llegada: "))
        mes_llegada = int(input("Ingrese mes de llegada: "))
        dia_llegada = int(input("Ingrese dia llegada: "))
        fecha_llegada = date(año_llegada, mes_llegada, dia_llegada)
        #Fecha salida
        año_salida= int(input("Ingrese año salida: "))
        mes_salida = int(input("Ingrese mes de salida: "))
        dia_salida = int(input("Ingrese dia salida: "))
        fecha_salida = date(año_salida, mes_salida, dia_salida)
        #Datos Suite
        num_personas = int(input("Ingrese numero de personas: "))
        tipo_suite = input("Ingrese tipo de suite deseada: ")

        eleccionSuite(tipo_suite.title(), fecha_llegada, fecha_salida, id_cliente, nombre_cliente, correo_cliente, num_personas)

    elif op == 2:
        i = 1
        if reservas:
            for reserva in reservas:
                print(f"\n RESERVA: {i}")
                for clave, valor in reserva.items():
                    print(f"{clave}: {valor}")
                i +=1
        else:
            print("No hay reservas por mostrar")
    elif op == 3:
        sys.exit()
    else:
        print("Opción incorrecta. INGRESE UNA VALIDA!!")