class HistorialAcademico:

    def __init__(self, zona_labor_docente, caracter_educacion_media,
         etnia_educatica, max_nivel_alcanzado, niveles_escolares_laborados,
         niveles_escolares_desempeniados, areas_formacion,
         especialidades_tecnicas):
        self.zona_labor_docente = zona_labor_docente
        self.caracter_educacion_media = caracter_educacion_media
        self.etnia_educatica = etnia_educatica
        self.max_nivel_alcanzado = max_nivel_alcanzado
        self.niveles_escolares_laborados = niveles_escolares_laborados
        self.niveles_escolares_desempeniados = niveles_escolares_desempeniados
        self.areas_formacion = areas_formacion
        self.especialidades_tecnicas = especialidades_tecnicas

    def getZona_labor_docente(self):
        return self.zona_labor_docente

    def getCaracter_educacion_media(self):
        return self.caracter_educacion_media

    def getEtnia_educatica(self):
        return self.etnia_educatica

    def getMax_nivel_alcanzado(self):
        return self.max_nivel_alcanzado

    def getNiveles_escolares_laborados(self):
        return self.niveles_escolares_laborados

    def getNiveles_escolares_desempeniados(self):
        return self.niveles_escolares_desempeniados

    def getAreas_formacion(self):
        return self.areas_formacion

    def getEspecialidades_tecnicas(self):
        return self.especialidades_tecnicas

    def setZona_labor_docente(self, zona_labor_docente):
        self.zona_labor_docente = zona_labor_docente

    def setCaracter_educacion_media(self, caracter_educacion_media):
        self.caracter_educacion_media = caracter_educacion_media

    def setEtnia_educatica(self, etnia_educatica):
        self.etnia_educatica = etnia_educatica

    def setMax_nivel_alcanzado(self, max_nivel_alcanzado):
        self.max_nivel_alcanzado = max_nivel_alcanzado

    def setNiveles_escolares_laborados(self, niveles_escolares_laborados):
        self.niveles_escolares_laborados = niveles_escolares_laborados

    def setNiveles_escolares_desempeniados(self,
    niveles_escolares_desempeniados):
        self.niveles_escolares_desempeniados = niveles_escolares_desempeniados

    def setAreas_formacion(self, areas_formacion):
        self.areas_formacion = areas_formacion

    def setEspecialidades_tecnicas(self, especialidades_tecnicas):
        self.especialidades_tecnicas = especialidades_tecnicas


