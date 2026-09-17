#PREDICADOS
estudiantes = {"Juan","Arturo","José"}
profesores = {"Alonso","Maria"}
clases = {"Calculo diferencial","Programacion logica"}
num_control = {"61720312", "61720313", "61720314"}
grupos = {"2SA", "2IA"}
salones = {"202", "404"}
carreras = {"Sistemas", "Industriales"}
num_empleado = {"19357218", "19357221"}

#UNIVERSO

#Estudiantes
pertenece_grupo = {
    ("Juan", "2SA"),
    ("Arturo", "2SA"),
    ("José", "2IA")
}

asiste_clase = {
    ("Juan", "Cálculo Diferencial"),
    ("Juan", "Programación Lógica"),
    ("Arturo", "Cálculo Diferencial"),
    ("Arturo", "Programación Lógica"),
    ("José", "Cálculo Diferencial")
}

asiste_salon = {
    ("Juan", "202"),
    ("Juan", "404"),
    ("Arturo", "202"),
    ("Arturo", "404"),
    ("José", "202")
}

tiene_num_control = {
    ("Juan", "61720312"),
    ("Arturo", "61720313"),
    ("José", "61720314")
}

cursa_carrera = {
    ("Juan", "Sistemas"),
    ("Arturo", "Sistemas"),
    ("José", "Industrial")
}

#Profesores
enseña_clase = {
    ("Alonso", "Cálculo Diferencial"),
    ("Maria", "Programación Lógica")
}

trabaja_salon = {
    ("Alonso", "202"),
    ("Maria", "404")
}

tiene_num_empleado = {
    ("Alonso", "19357218"),
    ("Maria", "19357221")
}

#FUNCIONES

def hacer_consulta(nombre, relacion):
    def funcion(x, y):
        resultado = (x, y)in relacion
        print(f"{nombre}({x}, {y}) = {'Verdadero' if resultado else 'Falso'}")
        return resultado
    return funcion

def es(nombre, categoria):
    categorias = {
        "estudiante": estudiantes,
        "profesor": profesores,
        "clase": clases,
        "grupo": grupos,
        "salon": salones,
        "carrera": carreras,
        "num_empleado": num_empleado,
        "num_control": num_control
    }
    resultado = nombre in categorias[categoria]
    boleano = "Verdadero" if resultado else "Falso"
    print(f"{categoria}({nombre}) = {boleano}")
    return resultado

Enseña = hacer_consulta("Enseña", enseña_clase)
AsisteClase = hacer_consulta("AsisteClase", asiste_clase)
TieneNumEmpleado = hacer_consulta("TieneNumEmpleado", tiene_num_empleado)
CursaCarrera = hacer_consulta("CursaCarrera", cursa_carrera)
TieneNumControl = hacer_consulta("TieneNumControl", tiene_num_control)
TrabajaSalon = hacer_consulta("TrabajaSalon", trabaja_salon)
PerteneceGrupo = hacer_consulta("PerteneceGrupo", pertenece_grupo)

#CONSULTAS

Enseña("Alonso", "Cálculo Diferencial")
Enseña("José", "Programación Lógica")

AsisteClase("Juan", "Cálculo Diferencial")
AsisteClase("Jose", "Programación Lógica")

TieneNumEmpleado("Maria", "19357221")
TieneNumEmpleado("Juan", "19357221")

CursaCarrera("Arturo", "Sistemas")
CursaCarrera("Juan", "Industriales")

TieneNumControl("José", "61720314")
TieneNumControl("Maria", "61720314")

TrabajaSalon("Alonso", "202")
TrabajaSalon("José", "404")

PerteneceGrupo("Juan", "2SA")
PerteneceGrupo("Alonso", "2IA")

es("José", "estudiante")
es("Maria", "estudiante")

es ("Alonso", "profesor")
es ("Juan", "profesor")

es("Calculo diferencial", "clase")
es("Sistemas", "clase")

es("2SA", "grupo")
es("202", "grupo")

es("404","salon")
es("Industriales", "salon")

es("Sistemas", "carrera")
es("Alonso", "carrera")

es("19357221", "num_empleado")
es("61720313", "num_empleado")

es("61720314", "num_control")
es("19357218", "num_control")