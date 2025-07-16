class Estudiante:
    def _init_(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion):
        calificacion.estudiantes.append(self)
        self.calificaciones.append(calificacion)
    
    def calcular_promedio_general(self):
        if not self.calificaciones:
            return 0.0
        return sum(cal.valor for cal in self.calificaciones) / len(self.calificaciones)
    
    def calcular_promedio_por_materia(self, materia):
        total = 0
        contador = 0
        
        for cal in self.calificaciones:
            if cal.materia == materia:
                total += cal.valor
                contador += 1
        
        return total / contador if contador > 0 else 0.0
    
    def mostrar_calificaciones(self):
        print(f"\nCalificaciones de {self.nombre} ({self.matricula}):")
        for cal in self.calificaciones:
            cal.mostrar()
    
    def esta_aprobado(self):
        return self.calcular_promedio_general() >= 6.0
    
    def materia_con_peor_promedio(self):
        if not self.calificaciones:
            return 
        
        promedios = {}
        
        for cal in self.calificaciones:
            materia = cal.materia
            if materia not in promedios:
                promedios[materia] = {"total": 0, "contador": 0}
            promedios[materia]["total"] += cal.valor
            promedios[materia]["contador"] += 1
        