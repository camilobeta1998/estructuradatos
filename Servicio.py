class Servicio():
    def __init__(self, codigo, descripcion, valor):
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__valor=valor
        self.__contadorNumeroServiciosSolicitados=0

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,descripcion):
        self.__descripcion=descripcion

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self,valor):
        self.__valor=valor

    @property
    def contadorNumeroServiciosSolicitados(self):
        return self.__contadorNumeroServiciosSolicitados

    @contadorNumeroServiciosSolicitados.setter
    def contadorNumeroServiciosSolicitados(self,contadorNumeroServiciosSolicitados):
        self.__contadorNumeroServiciosSolicitados=contadorNumeroServiciosSolicitados

    def __str__(self):
        return  self.__codigo+';'+self.__descripcion+';'+str(self.__valor)+";"+str(self.__contadorNumeroServiciosSolicitados)
    

