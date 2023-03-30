import Portafolio as p
class PortafolioOrganizado(p.Portafolio):
    def __init__(self, capacity):
        super().__init__(capacity)

    def agregarServicio(self, servicio1):
        if self.contadorNumeroServicios < len(self.listadoServicios):
            super().agregarServicio(servicio1)
        elif servicio1.numero > self.listadoServicios[self.contadorNumeroServicios  - 1].numero:
            self.listadoServicios[self.contadorNumeroServicios - 1] = servicio1

        if self.contadorNumeroServicios > 1:
            temp = self.contadorNumeroServicios - 1
            while temp > 0 and self.listadoServicios[temp].numero > self.listadoServicios[temp-1].numero:
                self.listadoServicios[temp] = self.listadoServicios[temp - 1]
                self.listadoServicios[temp - 1] = servicio1
                temp  -= 1
    
        