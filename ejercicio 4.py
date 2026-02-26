import os
os.system("cls")

# Costos base por destino
COSTOS_DESTINOS = {
    "Centro": 5000,
    "Marbella": 10000,
    "Torices": 25000,
    "Bicentenario": 70000
}

# Costos adicionales
COSTO_POR_ITEM = 500
COSTO_POR_KG = 2000

def calcular_tarifa(destino="Centro", cantidad_items=1, peso_kg=1.0):

    destino = destino.strip().capitalize()
    
    # Validar destino
    if destino not in COSTOS_DESTINOS:
        print(f" Destino '{destino}' no válido")
        print(f"Destinos válidos: {', '.join(COSTOS_DESTINOS.keys())}")
        return 0
    
    # Calcular tarifa
    costo_base = COSTOS_DESTINOS[destino]
    costo_items = cantidad_items * COSTO_POR_ITEM
    costo_peso = peso_kg * COSTO_POR_KG
    
    tarifa_total = costo_base + costo_items + costo_peso
    
    # Mostrar desglose
    print(f"\n{'='*50}")
    print(f"CÁLCULO DE TARIFA - {destino}")
    print(f"{'='*50}")
    print(f"Costo base (destino):     ${costo_base:,.0f}")
    print(f"Items ({cantidad_items}):              ${costo_items:,.0f}")
    print(f"Peso ({peso_kg} kg):                ${costo_peso:,.0f}")
    print(f"{'-'*50}")
    print(f"TARIFA TOTAL:              ${tarifa_total:,.0f}")
    print(f"{'='*50}")
    
    return tarifa_total


print("Destinos disponibles: Centro, Marbella, Torices, Bicentenario")
print("(Presiona Enter para usar valores por defecto)\n")

destino = input("Destino : ").strip()
cantidad = input("Cantidad de items : ").strip()
peso = input("Peso en kg : ").strip()

# Convertir a valores o None si está vacío
try:
    cantidad = int(cantidad) if cantidad else 1
    peso = float(peso) if peso else 1.0
    destino = destino if destino else "Centro"
    
    calcular_tarifa(destino, cantidad, peso)
except ValueError:
    print("Error: Ingresa números válidos para cantidad y peso")


