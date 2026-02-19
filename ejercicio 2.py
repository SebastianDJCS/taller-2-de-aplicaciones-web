import os
os.system("cls")
RUTAS = {
    ("Centro", "Marbella"): {"distancia": 10, "costo": 10000},
    ("Centro", "Torices"): {"distancia": 15, "costo": 25000},
    ("Centro", "Bicentenario"): {"distancia": 30, "costo": 70000},
    ("Marbella", "Torices"): {"distancia": 5},
    ("Torices", "Bicentenario"): {"distancia": 12},
    ("Marbella", "Bicentenario"): {"distancia": 18}
}

def motor_de_rutas(*destinos):
    distancia_radial = 0
    for d in destinos:
        distancia_radial += RUTAS[("Centro", d)]["distancia"] * 2
    distancia_circular = 0
    punto_actual = "Centro"
    
    for d in destinos:
        llave = tuple(sorted((punto_actual, d)))
        distancia_circular += RUTAS[llave]["distancia"]
        punto_actual = d

    distancia_circular += RUTAS[tuple(sorted((punto_actual, "Centro")))]["distancia"]

    print(f"Distancia Total Radial: {distancia_radial} km")
    print(f"Distancia Total Circular: {distancia_circular} km")
    
    if distancia_circular < distancia_radial:
        print(f"\n La mejor ruta es PASAR POR TODOS (Circular). Te ahorras {distancia_radial - distancia_circular} km.")
    else:
        print(f"\n La mejor ruta es IR Y VOLVER (Radial).")
motor_de_rutas("Marbella", "Torices", "Bicentenario")