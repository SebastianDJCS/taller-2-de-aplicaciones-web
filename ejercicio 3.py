import os
os.system("cls")

# Repartidores y sus destinos permitidos
REPARTIDORES = {
    "Luis": ["Centro"],
    "Roy": ["Torices", "Marbella"],
    "Donacel": ["Bicentenario", "Centro"],
    "Juan": ["Centro", "Marbella", "Torices", "Bicentenario"]
}

def buscar_repartidores(destino):
    """Busca qué repartidores pueden ir a un destino específico"""
    destino = destino.strip().capitalize()
    
    disponibles = []
    for repartidor, destinos_permitidos in REPARTIDORES.items():
        if destino in destinos_permitidos:
            disponibles.append(repartidor)
    
    print(f"Destino: {destino}")
    
    if disponibles:
        print(f"✓ Repartidores disponibles: {', '.join(disponibles)}")
    else:
        print(f" No hay repartidores para '{destino}'")
        print("Destinos válidos: Centro, Marbella, Torices, Bicentenario")

# MENÚ INTERACTIVO
print("Destinos disponibles: Centro, Marbella, Torices, Bicentenario\n")

destino = input("¿A qué destino necesitas un repartidor?: ").strip()
buscar_repartidores(destino)






