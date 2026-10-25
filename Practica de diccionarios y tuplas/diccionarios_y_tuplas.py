
#hechos con las caracteristicas de todos los animales
HECHOS = {
    ("guepardo", "TienePelo"),
    ("guepardo", "ComeCarne"),
    ("guepardo", "Leonado"),
    ("guepardo", "ManchasOscuras"),

    ("tigre", "TienePelo"),
    ("tigre", "ComeCarne"),
    ("tigre", "RayasNegras"),

    ("jirafa", "TienePelo"),
    ("jirafa", "TienePezunas"),
    ("jirafa", "CuelloLargo"),
    ("jirafa", "ManchasOscuras"),

    ("cebra", "TienePelo"),
    ("cebra", "TienePezunas"),
    ("cebra", "RayasNegras"),

    ("pinguino", "TienePlumas"),
    ("pinguino", "Nada"),
    ("pinguino", "BlancoYNegro"),

    ("albatros", "TienePlumas"),
    ("albatros", "VuelaMuyBien"),

    ("perro", "TienePelo"),
    ("perro", "DaLeche"),
    ("perro", "CuatroPatas"),
    ("perro", "ExcelenteOlfato"),
    ("perro", "Ladra"),
    ("perro", "Domesticado"),

    ("caballo", "DaLeche"),
    ("caballo", "TienePezunas"),
    ("caballo", "TieneCrin"),
    ("caballo", "TieneColaLarga"),
    ("caballo", "TienenOrejasErgidas"),
    ("caballo", "NoConsumeCarne")
}


REGLAS = (
    (("TienePelo",), "Mamifero"),
    (("DaLeche",), "Mamifero"),
    (("TienePlumas",), "Ave"),
    (("Vuela", "PoneHuevos"), "Ave"),

    (("ComeCarne", "Mamifero"), "Carnivoro"),
    (("TienePezunas", "Mamifero"), "Ungulado"),

    (("Carnivoro", "Leonado", "ManchasOscuras"), "Guepardo"),
    (("Carnivoro", "RayasNegras"), "Tigre"),

    (("Ungulado", "CuelloLargo", "ManchasOscuras"), "Jirafa"),
    (("Ungulado", "RayasNegras"), "Cebra"),

    (("Ave", "Nada", "BlancoYNegro"), "Pinguino"),
    (("Ave", "VuelaMuyBien"), "Albatros"),

    (("Mamifero", "CuatroPatas", "TienePelo", "ExcelenteOlfato"), "Perro"),
    (("Mamifero", "Ladra", "Domesticado"), "Perro"),

    (("Mamifero", "TieneCrin", "TieneColaLarga", "TienenOrejasErgidas", "TienePezunas"), "Caballo"),
    (("Mamifero", "NoConsumeCarne"), "Herbivoro")
)



def consultar_hechos():
    animales = {}

    for animal, predicado in HECHOS:
        if animal not in animales:
            animales[animal] = set()

        animales[animal].add(predicado)

    return animales


#inferimos a que categorias pertenece el animal en base a sus hechos

def inferir(animal):
    animales = consultar_hechos()

    if animal not in animales:
        return set(), []

    conocidos = animales[animal].copy()
    deducciones = []

    cambio = True

    while cambio:
        cambio = False

        for numero, (condiciones, conclusion) in enumerate(
            REGLAS, start=1
        ):
            if all(c in conocidos for c in condiciones):
                if conclusion not in conocidos:
                    conocidos.add(conclusion)

                    deducciones.append(
                        (numero, condiciones, conclusion)
                    )

                    cambio = True

    return conocidos, deducciones

#consultamos los hechos de un animal y mostramos los grupos a los que pertece
def consultar_animal(animal):
    animales = consultar_hechos()

    if animal not in animales:
        print("Animal no encontrado.")
        return

    conocidos, deducciones = inferir(animal)

    grupos = {
        "Mamifero", "Ave", "Carnivoro",
        "Ungulado", "Herbivoro"
    }

    especies = {
        "Guepardo", "Tigre", "Jirafa", "Cebra",
        "Pinguino", "Albatros", "Perro", "Caballo"
    }

    print("ANIMAL:", animal.upper())

    print("\nHechos registrados:")

    for predicado in sorted(animales[animal]):
        print("-", predicado)

    print("\nDeducciones:")

    if deducciones:
        for numero, condiciones, conclusion in deducciones:
            texto = " Y ".join(condiciones)

            print(
                f"Regla {numero}: "
                f"{texto} -> {conclusion}"
            )
    else:
        print("No se obtuvieron nuevas conclusiones.")

    print("\nClasificacion:")

    grupos_encontrados = sorted(conocidos & grupos)
    especies_encontradas = sorted(conocidos & especies)

    print("Grupos:", ", ".join(grupos_encontrados)
          if grupos_encontrados else "Ninguno")

    print("Especies:", ", ".join(especies_encontradas)
          if especies_encontradas else "Ninguna")

    input("\nPresiona ENTER para continuar...")


#mostramos la lista de los animales que tenemos registrados.

def mostrar_animales():
    animales = sorted(consultar_hechos().keys())

    print("\nANIMALES REGISTRADOS")

    for numero, animal in enumerate(animales, start=1):
        print(f"{numero}. {animal.capitalize()}")

    print("0. Regresar")

    opcion = input("\nSelecciona un animal: ")

    if not opcion.isdigit():
        print("Ingresa un numero valido.")
        return

    numero = int(opcion)

    if numero == 0:
        return

    if 1 <= numero <= len(animales):
        consultar_animal(animales[numero - 1])
    else:
        print("Opcion no valida.")


# Ponemos la lista de las reglas que hicimos en la consola

def mostrar_reglas():
    print("\nREGLAS DEL SISTEMA EXPERTO")

    for numero, (condiciones, conclusion) in enumerate(
        REGLAS, start=1
    ):
        print(f"\nRegla {numero}")
        print("SI", " Y ".join(condiciones))
        print("ENTONCES", conclusion)

    input("\nPresiona ENTER para continuar...")



def menu():
    while True:
        print("CONSULTA DE ANIMALES")
        print("Selecciona una opcion:")
        print("1. Consultar animales registrados")
        print("2. Ver reglas")
        print("0. Salir")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            mostrar_animales()

        elif opcion == "2":
            mostrar_reglas()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()
