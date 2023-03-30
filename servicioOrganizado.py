import Servicio as s
class ServicioOrganizado(s.Servicio):
    def __init__(self, codigo, descripcion, valor , numero):
       super().__init__(codigo, descripcion, valor)
       self.numero = numero
    

    


    
    