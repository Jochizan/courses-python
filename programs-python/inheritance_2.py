class persona():

    def __init__(self, nombre, edad, lugar_residencia):
        
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def decription(self):

        print("Nombre: " , self.nombre, " Edad: " , self.edad, " Residencia: " , self.lugar_residencia)

class empleado(persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def decription(self):

        super().decription()

        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Joan = empleado(1500, 15, "Joan", 19, "Perú")

Joan.decription()

print(isinstance(Joan, persona))