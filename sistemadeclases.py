# Clase para representar una materia
class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase para representar una calificación
class Calificacion:
    def __init__(self, materia, valor):
        self.materia = materia
        self.valor = valor

# Clase para representar un estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        total = 0
        for c in self.calificaciones:
            total += c.valor
        promedio = total / len(self.calificaciones)
        return promedio

    def obtener_estatus(self):
        promedio = self.calcular_promedio()
        if promedio >= 6:
            return "Aprobado"
        else:
            return "No Aprobado"

    def materia_mas_baja(self):
        if len(self.calificaciones) == 0:
            return None
        cal_menor = self.calificaciones[0]
        for c in self.calificaciones:
            if c.valor < cal_menor.valor:
                cal_menor = c
        return cal_menor

    def mostrar_reporte(self):
        print("Nombre:", self.nombre)
        print("Matrícula:", self.matricula)
        promedio = self.calcular_promedio()
        print("Promedio general:", promedio)
        print("Estatus:", self.obtener_estatus())
        cal_menor = self.materia_mas_baja()
        if cal_menor != None:
            print("Materia con menor promedio:", cal_menor.materia.nombre, "-", cal_menor.valor)
        print("                                 ")

# Clase para representar un docente
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones_asignadas = []

    def asignar_calificacion(self, estudiante, materia, valor):
        if valor >= 0 and valor <= 10:
            nueva = Calificacion(materia, valor)
            estudiante.agregar_calificacion(nueva)
            self.calificaciones_asignadas.append((estudiante, materia, valor))
        else:
            print("Calificación no válida. Debe estar entre 0 y 10.")


# Crear materias
proyecto = Materia("proyecto integrador")
programacion = Materia("programacion orientada a objetos")
topicos = Materia("topicos de calidad para el diseño de software")
ingles = Materia("ingles")
base = Materia("base de datos")
desarrollo = Materia("desarrollo del pensamiento y toma de decisiones")
calculo = Materia("calculo integral")

materias = [proyecto, programacion, topicos, ingles, base, desarrollo, calculo]

# Crear docentes
sindy = Docente("Profe Sindy")
fidel = Docente("Profe Fidel")
niko = Docente("Profe Niko")
gilbelto = Docente("Profe Gilbelto")
alatiel = Docente("Profe Alatiel")
bruno = Docente("Profe Bruno")

# Asignar docente a cada materia (punto extra solicitado)
docentes_por_materia = {
    "proyecto integrador": sindy,
    "programacion orientada a objetos": fidel,
    "topicos de calidad para el diseño de software": niko,
    "ingles": gilbelto,
    "base de datos": alatiel,
    "desarrollo del pensamiento y toma de decisiones": sindy,
    "calculo integral": bruno
}

# Crear estudiantes
alumnos = [
    Estudiante("Juan Gimenes", "E001"),
    Estudiante("Jassiel Perez", "E002"),
    Estudiante("Gadiel Mas", "465401"),
    Estudiante("Jhosua Delgado", "83132"),
    Estudiante("Genesis Suarez", "20051"),
    Estudiante("Dori Maria", "E00254"),
    Estudiante("Luis Angel", "E04401"),
    Estudiante("Zuleyma Martinez", "E44611002")
]

# Asignar calificaciones (a todos los alumnos la misma forma)
for alumno in alumnos:
    docentes_por_materia["proyecto integrador"].asignar_calificacion(alumno, proyecto, 9)
    docentes_por_materia["programacion orientada a objetos"].asignar_calificacion(alumno, programacion, 6)
    docentes_por_materia["topicos de calidad para el diseño de software"].asignar_calificacion(alumno, topicos, 8)
    docentes_por_materia["ingles"].asignar_calificacion(alumno, ingles, 8)
    docentes_por_materia["base de datos"].asignar_calificacion(alumno, base, 9)
    docentes_por_materia["desarrollo del pensamiento y toma de decisiones"].asignar_calificacion(alumno, desarrollo, 7)
    docentes_por_materia["calculo integral"].asignar_calificacion(alumno, calculo, 6)


# Mostrar reporte por estudiante
for alumno in alumnos:
    alumno.mostrar_reporte()

# Mostrar promedios por materia y docente
print("\n*** Promedio por materia y nombre del profesor ***")
calificaciones_por_materia = {}

for materia_nombre, docente in docentes_por_materia.items():
    calificaciones_por_materia[materia_nombre] = []

    for est, mat, val in docente.calificaciones_asignadas:
        if mat.nombre == materia_nombre:
            calificaciones_por_materia[materia_nombre].append(val)

for materia, lista_calif in calificaciones_por_materia.items():
    total = 0
    for val in lista_calif:
        total += val
    promedio = total / len(lista_calif)
    print(f"{materia} (Profesor: {docentes_por_materia[materia].nombre}) → Promedio: {promedio:.2f}")
