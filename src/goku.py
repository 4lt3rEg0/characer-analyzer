# src/goku.py
# -*- coding: utf-8 -*-

def goku_transformacion():
    """
    Simula la transformación y aumento de poder de Goku.
    ¡Demuestra el uso de funciones y variables!
    """
    poder_base = 1000
    nivel_ki = 5  # Nivel de enojo/ki (1-10)

    # Lógica de transformación (if/else)
    if nivel_ki >= 7:
        poder_final = poder_base * 50  # Super Saiyan
        forma = "Super Saiyan 🟡"
    elif nivel_ki >= 5:
        poder_final = poder_base * 10  # Kaioken
        forma = "Kaioken 🔴"
    else:
        poder_final = poder_base
        forma = "Base ⚪"

    # Usamos un f-string para formatear el texto
    print(f"[GOKU] ¡Poder de pelea: {poder_final}! | Forma: {forma}")

# Ejecuta la función para ver el resultado
if __name__ == "__main__":
    goku_transformacion()