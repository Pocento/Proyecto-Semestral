from django.forms import ValidationError

class TamañoMaximoValidator:
    def __init__(self, maxfile=3) :
        self.maxfile = maxfile
    
    def __call__ (self, value):
        tamaño = value.size
        maxfileT = self.maxfile * 1048576

        if tamaño > maxfileT:
            raise ValidationError (f"El tamaño maximo del archivo debe ser {self.maxfile} ")

