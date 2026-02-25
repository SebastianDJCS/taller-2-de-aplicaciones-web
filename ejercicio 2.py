import os
os.system("cls")
RUTAS = {
    ("Bicentenario", "Centro"): {"distancia": 30, "costo": 70000},
    ("Bicentenario", "Marbella"): {"distancia": 18, "costo": 40000},
    ("Bicentenario", "Torices"): {"distancia": 12, "costo": 30000},
    ("Centro", "Marbella"): {"distancia": 10, "costo": 10000},
    ("Centro", "Torices"): {"distancia": 15, "costo": 25000},
    ("Marbella", "Torices"): {"distancia": 5, "costo": 15000},
}


def motor_de_rutas(*destinos):
    # Validar que los destinos existan
    for d in destinos:
        if (("Centro", d) not in RUTAS) and ((d, "Centro") not in RUTAS):
            print(f"Error: {d} no existe en las rutas disponibles")
            return
    
    print(f"\n Visitando: {' → '.join(['Centro'] + list(destinos) + ['Centro'])}\n")
    
    # Ruta Ida y vuelta (viajes individuales)
    distancia_ida_vuelta = 0
    costo_ida_vuelta = 0
    for d in destinos:
        llave = ("Centro", d) if ("Centro", d) in RUTAS else (d, "Centro")
        distancia_ida_vuelta += RUTAS[llave]["distancia"] * 2
        costo_ida_vuelta += RUTAS[llave]["costo"] * 2
    
    # Ruta Recorrida completa (un viaje único)
    distancia_recorrida = 0
    costo_recorrida = 0
    punto_actual = "Centro"
    
    for d in destinos:
        llave = tuple(sorted((punto_actual, d)))
        distancia_recorrida += RUTAS[llave]["distancia"]
        costo_recorrida += RUTAS[llave]["costo"]
        punto_actual = d

    llave_final = tuple(sorted((punto_actual, "Centro")))
    distancia_recorrida += RUTAS[llave_final]["distancia"]
    costo_recorrida += RUTAS[llave_final]["costo"]

    print(f"Distancia Ida y vuelta: {distancia_ida_vuelta} km | Costo: ${costo_ida_vuelta:,}")
    print(f"Distancia Recorrida completa: {distancia_recorrida} km | Costo: ${costo_recorrida:,}")
    
    ahorro_km = distancia_ida_vuelta - distancia_recorrida
    ahorro_costo = costo_ida_vuelta - costo_recorrida
    
    if distancia_recorrida < distancia_ida_vuelta:
        print(f"\n✓ Mejor ruta: RECORRIDA COMPLETA. Ahorras {ahorro_km} km (${ahorro_costo:,})")
    else:
        print(f"\n✓ Mejor ruta: IDA Y VUELTA. Ahorras {-ahorro_km} km (${-ahorro_costo:,})")

# Menu interactivo
print("=== OPTIMIZADOR DE RUTAS ===")
print("Destinos disponibles: Marbella, Torices, Bicentenario\n")

destinos_usuario = input("Ingresa los destinos (separados por coma): ").strip()
destinos_lista = tuple([d.strip() for d in destinos_usuario.split(",")])

if destinos_lista:
    motor_de_rutas(*destinos_lista)