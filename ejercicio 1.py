import os
os.system("cls")

def registro_pedidos(nombre="amigo", direccion="alguna", telefono="", **detalles_extra):
    print("Registro de Pedido")
    print(f"Nombre: {nombre}")
    print(f"Dirección: {direccion}")
    print(f"Teléfono: {telefono}")
    for key, value in detalles_extra.items():
        print(f"{key.capitalize()}: {value}")
    print("Pedido registrado exitosamente.")

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su teléfono: ")
registro_pedidos(nombre, direccion, telefono, producto="suavitel", cantidad=2, fecha_entrega="2024-07-01")