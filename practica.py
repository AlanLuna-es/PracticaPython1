import pandas as pd

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Ingresa el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        try:
            calificaciones = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(',')))
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: Ingresa solo números separados por comas.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(calificaciones)/len(calificaciones) for nombre, calificaciones in estudiantes.items()}
    return promedios

def encontrar_mejor_estudiante(promedios):
    mejor = max(promedios, key=promedios.get)
    return mejor, promedios[mejor]

def guardar_resultados(estudiantes, promedios, mejor_estudiante, mejor_promedio):
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados de los estudiantes:\n")
        for nombre, calificaciones in estudiantes.items():
            archivo.write(f"{nombre}: {calificaciones}, Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nMejor estudiante: {mejor_estudiante} con promedio de {mejor_promedio:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    if estudiantes:
        promedios = calcular_promedios(estudiantes)
        mejor_estudiante, mejor_promedio = encontrar_mejor_estudiante(promedios)
        guardar_resultados(estudiantes, promedios, mejor_estudiante, mejor_promedio)
        print("Datos guardados en resultados.txt")
    else:
        print("No se ingresaron datos.")

if __name__ == "__main__":
    main()
