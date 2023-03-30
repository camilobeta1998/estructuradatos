import numpy as np

class Portafolio():
    def __init__(self, capacity):
        self.listadoServicios=np.empty(capacity, dtype=object)
        self.contadorNumeroServicios = 0

    @property
    def listadoServicios(self):
        return self.__listadoServicios

    @listadoServicios.setter
    def listadoServicios(self,listadoServicios):
        self.__listadoServicios=listadoServicios

    def __str__(self):
        return self.listadoServicios
    
    def agregarServicio(self, servicio1):
        if self.contadorNumeroServicios < len(self.listadoServicios):
            self.listadoServicios[self.contadorNumeroServicios] = servicio1
            self.contadorNumeroServicios += 1
        
    def buscarServicio(self, codigo):
        if self.contadorNumeroServicios==0:
            return None
        else:
            temp = 0
            while temp<self.contadorNumeroServicios and self.listadoServicios[temp].codigo != codigo:
                temp += 1
            if temp==self.contadorNumeroServicios:
                return None
            else:
                return self.listadoServicios[temp]
            
    def eliminarServicio(self, codigo):
        if self.contadorNumeroServicios==0:
            return None
        else:
            temp = 0
            while temp<self.contadorNumeroServicios and self.listadoServicios[temp].codigo != codigo:
                temp += 1
            if temp==self.contadorNumeroServicios:
                return None
            else:
                registroTemp = self.listadoServicios[temp]
                for i in range(temp, self.contadorNumeroServicios-1):
                    self.listadoServicios[temp] = self.listadoServicios[temp+1]
                self.listadoServicios[self.contadorNumeroServicios - 1] = None
                self.contadorNumeroServicios -=1
                return f'se elimino con exito {registroTemp}'
            

    def solicitarServicios(self, codigo):
        variable = self.buscarServicio(codigo)
        if variable != None:
            variable.contadorNumeroServiciosSolicitados +=1


    def toFile(self):
        try:
            archivo = open("PortafolioActualizado.csv" , "w")
            temp = 0
            while temp < self.contadorNumeroServicios:
                archivo.write(str(self.listadoServicios[temp]) + '\n')
                temp += 1
            archivo.close()
        except:
            print("ha ocurrido un error en la escritura del archivo")

            
   