

import Servicio as s
import Portafolio as p
import portafolioOrganizado as po
import servicioOrganizado as so
contadorConsultaMedicaGeneral = 0
#arreglo serviciosCM
try:
    file1 = open("serviciosCM.csv" , "r")
    line = file1.readline()
    line = file1.readline()
    portafolio1 = p.Portafolio(10)

    while line != "":
        arrayServicios = line.split(";")
        codigo = arrayServicios[0]
        descripcion = arrayServicios[1]
        valor = arrayServicios[2]
        servicio1 = s.Servicio(codigo, descripcion, float(valor))
        portafolio1.agregarServicio(servicio1)
        line = file1.readline()
    file1.close()
except:
    print("ha ocurrido un error en la lectura")


try:
    file1 = open("solicitudes.csv" , "r")
    line = file1.readline()
    line = file1.readline()
    while line != "":
        arraySolicitudes = line.split(";")
        codigo = arraySolicitudes[0]
        portafolio1.solicitarServicios(codigo)
        line = file1.readline()
    file1.close()
except:
    print("ha ocurrido un error en la lectura")

#--------------------------------------------------------------------------------------------------------------------

portafolio1.toFile()



try:
    file2 = open("PortafolioActualizado.csv" , "r")
    line = file2.readline()
    portafolioOrganizado1 = po.PortafolioOrganizado(5)

    while line != "":
                arrayServiciosOrganizado = line.split(";")
                arrayServiciosOrganizado[-1] = arrayServiciosOrganizado[-1].strip()
                codigo = arrayServiciosOrganizado[0]
                descripcion = arrayServiciosOrganizado[1]
                valor = arrayServiciosOrganizado[2]
                numero = arrayServiciosOrganizado[3]
                servicio1 = so.ServicioOrganizado(codigo, descripcion, valor , numero)
                portafolioOrganizado1.agregarServicio(servicio1)
                line = file2.readline()
    file2.close()
except:
    print("ha ocurrido un error en la escritura ya")

print(portafolio1.buscarServicio('C59'))
portafolio1.solicitarServicios('C59')
print(portafolio1.eliminarServicio('G66'))

