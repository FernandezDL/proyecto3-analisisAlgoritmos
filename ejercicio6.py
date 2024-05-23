""" Universidad Del Valle de Guatemala
    Departamento de Computación
    Análisis y diseño de algoritmos
    Proyecto 3
    Ejercicio 6
    Diana Lucía Fernández Villatoro
    21747
"""

configuracion = [0, 1, 2, 3, 4]
secuenciaWorst = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
secuenciaBest = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def IMTF(configuracion, secuencia):
    costo = 0

    print("Lista de configuración: ", configuracion)
    print(f"Solicitudes: {secuencia}")
    print("-----------------------------------------------------------------------------------------------------\n")

    for idx, solicitud  in enumerate(secuencia):
        configuracion1 = configuracion.copy()
        posicionSolicitud = configuracion.index(solicitud)
        costoSolicitud = posicionSolicitud + 1
        costo += costoSolicitud

        if(idx + 1 + (posicionSolicitud - 1)) < len(secuencia):
            lookAhead = secuencia[idx + 1 : idx + 1 + (posicionSolicitud - 1)]
        else:
            lookAhead = secuencia[idx + 1 : len(secuencia)]

        if solicitud in lookAhead:
            configuracion.pop(posicionSolicitud)
            configuracion.insert(0, solicitud)
            print(f"Elemento movido -> lista de configuración: {configuracion1} con solicitud {solicitud} y coste {costoSolicitud} -> Lista con MTF {configuracion}")

        else:
            print(f"Elemento no movido -> lista de configuración: {configuracion1} con solicitud {solicitud} y coste {costoSolicitud} -> Lista con MTF {configuracion}")

    print("-----------------------------------------------------------------------------------------------------\n")
    print(f"Costo total de la secuencia: {costo}")

# IMTF(configuracion, secuenciaBest) #Best-case scenario
IMTF(configuracion, secuenciaWorst) #Worst-case scenario