import numpy as np

def Aptitud(individuo):

    edad = individuo[0:2]
    ocupacion = individuo[2:5]
    estudios = individuo[5:7]
    estadoCivil = individuo[7:9]
    vivienda = individuo[9:11]
    ingresos = individuo[11:13]
    deudas = individuo[13:14]
    historial = individuo[14:16]
    formaPago = individuo[16:18]

    if(np.array_equal(edad,[0,0]) or np.array_equal(edad,[1,1])):
        ponderacionEdad = 6
    elif(np.array_equal(edad,[1,0])):
        ponderacionEdad = 8
    elif(np.array_equal(edad,[0,1])):
        ponderacionEdad = 10
    
    if(np.array_equal(ocupacion,[0,0,1])):
        ponderacionOcupacion = 0
    elif(np.array_equal(ocupacion,[0,0,0])):
        ponderacionOcupacion = 4
    elif(np.array_equal(ocupacion,[1,0,0]) or np.array_equal(ocupacion,[1,1,1])):
        ponderacionOcupacion = 6
    elif(np.array_equal(ocupacion,[0,1,0]) or np.array_equal(ocupacion,[1,0,1]) or np.array_equal(ocupacion,[1,1,0])):
        ponderacionOcupacion = 8
    elif(np.array_equal(ocupacion,[0,1,1])):
        ponderacionOcupacion = 10

    if(np.array_equal(estudios,[0,0])):
        ponderacionEstudios = 4
    elif(np.array_equal(estudios,[0,1])):
        ponderacionEstudios = 6
    elif(np.array_equal(estudios,[1,0])):
        ponderacionEstudios = 8
    elif(np.array_equal(estudios,[1,1])):
        ponderacionEstudios = 10

    if(np.array_equal(estadoCivil,[1,1])):
        ponderacionEstadoCivil = 6
    elif(np.array_equal(estadoCivil,[1,0])):
        ponderacionEstadoCivil = 4
    elif(np.array_equal(estadoCivil,[0,0])):
        ponderacionEstadoCivil = 8
    elif(np.array_equal(estadoCivil,[0,1])):
        ponderacionEstadoCivil = 10

    if(np.array_equal(vivienda,[0,0])):
        ponderacionVivienda = 10
    elif(np.array_equal(vivienda,[0,1])):
        ponderacionVivienda = 6
    elif(np.array_equal(vivienda,[1,0])):
        ponderacionVivienda = 8
    elif(np.array_equal(vivienda,[1,1])):
        ponderacionVivienda = 6

    if(np.array_equal(ingresos,[0,0])):
        ponderacionIngresos = 10
    elif(np.array_equal(ingresos,[0,1])):
        ponderacionIngresos = 8
    elif(np.array_equal(ingresos,[1,0])):
        ponderacionIngresos = 0

    if(np.array_equal(deudas,[0])):
        ponderacionDeudas = 5
    elif(np.array_equal(deudas,[1])):
        ponderacionDeudas = 10

    if(np.array_equal(historial,[1,0])):
        ponderacionHistorial = 6
    elif(np.array_equal(historial,[0,1])):
        ponderacionHistorial = 8
    elif(np.array_equal(historial,[0,0])):
        ponderacionHistorial = 10

    if(np.array_equal(formaPago,[0,1])):
        ponderacionFormaPago = 6
    elif(np.array_equal(formaPago,[0,0])):
        ponderacionFormaPago = 8
    elif(np.array_equal(formaPago,[1,0])):
        ponderacionFormaPago = 10

    aptitud = (ponderacionEdad*0.07) + (0.3*((ponderacionOcupacion+ponderacionEstudios+ponderacionDeudas)/3)) + (0.05*ponderacionEstadoCivil) + (0.08*ponderacionVivienda) + (0.3*((ponderacionIngresos+ponderacionFormaPago)/2)) + (0.2*ponderacionHistorial)
    return aptitud