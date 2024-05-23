""" Universidad Del Valle de Guatemala
    Departamento de Computación
    Análisis y diseño de algoritmos
    Proyecto 3
    Diana Lucía Fernández Villatoro
    21747
"""

configuracion = [0, 1, 2, 3, 4]
secuencia1= [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
secuencia2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
secuencia3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
secuencia4 = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
secuencia5 = [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
secuencia51 = [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

def MTF(configuracion, secuencia):
    costo = 0

    print("Lista de configuración: ", configuracion)
    print(f"Solicitudes: {secuencia}")
    print("-----------------------------------------------------------------------------------------------------\n")

    for solicitud  in secuencia:
        configuracion1 = configuracion.copy()
        posicionSolicitud = configuracion.index(solicitud)
        costoSolicitud = posicionSolicitud + 1
        costo += costoSolicitud

        configuracion.pop(posicionSolicitud)
        configuracion.insert(0, solicitud)

        print(f"Lista de configuración: {configuracion1} con solicitud {solicitud} y coste {costoSolicitud} -> Lista con MTF {configuracion}")

    print("-----------------------------------------------------------------------------------------------------\n")
    print(f"Costo total de la secuencia: {costo}")
    
# MTF(configuracion, secuencia1) #Primera secuencia
# MTF(configuracion, secuencia2) #Segunda secuencia
# MTF(configuracion, secuencia3) #Tercera secuencia
# MTF(configuracion, secuencia4) #Cuarta secuencia
# MTF(configuracion, secuencia5) #Quinta secuencia
MTF(configuracion, secuencia51) #Segunda parte del quinto punto