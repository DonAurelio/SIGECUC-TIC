class Calificacion:

    def __init__(self, Cohorte, ActividadEvaluacion, notaActividad):
        self.Cohorte = Cohorte
        self.ActividadEvaluacion = ActividadEvaluacion
        self.notaActividad = notaActividad

    def getCohorte(self):
        return self.Cohorte

    def getActividad(self):
        return self.ActividadEvaluacion

    def getLeaderTeacher(self):
        return self.LeaderTeacher

    def getNota():
        pass

    def setCohorte(self, Cohorte):
        self.Cohorte = Cohorte

    def setActividad(self, ActividadEvaluacion):
        self.ActividadEvaluacion = ActividadEvaluacion

    def setLeaderTeacher(self, LeaderTeacher):
        self.LeaderTeacher = LeaderTeacher

    def setNota(self, notaActividad):
        self.notaActividad = notaActividad


