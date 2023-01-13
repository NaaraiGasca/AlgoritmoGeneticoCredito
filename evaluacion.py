import numpy as np

def Evaluacion(individuo):

    edad = individuo[0:2]
    ocupacion = individuo[2:5]
    estudios = individuo[5:7]
    estadoCivil = individuo[7:9]
    vivienda = individuo[9:11]
    ingresos = individuo[11:13]
    deudas = individuo[13:14]
    historial = individuo[14:16]
    formaPago = individuo[16:18]

    if(np.array_equal(edad,[0,0])):
        ponderacionEdad = "Entre 18 y 28 años de edad"
    elif(np.array_equal(edad,[1,0])):
        ponderacionEdad = "Entre 40 y 50 años de edad" 
    elif(np.array_equal(edad,[0,1])):
        ponderacionEdad = "Entre 29 y 39 años de edad"
    elif(np.array_equal(edad,[1,1])):
        ponderacionEdad = "Mayor de 51 años"
    
    if(np.array_equal(ocupacion,[0,0,1])):
        ponderacionOcupacion = "Desempleado"
    elif(np.array_equal(ocupacion,[0,0,0])):
        ponderacionOcupacion = "Ama de casa"
    elif(np.array_equal(ocupacion,[1,0,0])):
        ponderacionOcupacion = "Estudiante"
    elif(np.array_equal(ocupacion,[0,1,0])):
        ponderacionOcupacion = "Empleado de tiempo parcial"
    elif( np.array_equal(ocupacion,[1,0,1])):
        ponderacionOcupacion = "Independiente"
    elif(np.array_equal(ocupacion,[0,1,1])):
        ponderacionOcupacion = "Empleado de tiempo completo"
    elif(np.array_equal(ocupacion,[1,1,0])):
        ponderacionOcupacion = "Jubilado"
    elif(np.array_equal(ocupacion,[1,1,1])):
        ponderacionOcupacion = "Pensionado"

    if(np.array_equal(estudios,[0,0])):
        ponderacionEstudios = "Primaria"
    elif(np.array_equal(estudios,[0,1])):
        ponderacionEstudios = "Secundaria"
    elif(np.array_equal(estudios,[1,0])):
        ponderacionEstudios = "Carrea técnica"
    elif(np.array_equal(estudios,[1,1])):
        ponderacionEstudios = "Universidad"

    if(np.array_equal(estadoCivil,[1,1])):
        ponderacionEstadoCivil = "Viudo(a)"
    elif(np.array_equal(estadoCivil,[1,0])):
        ponderacionEstadoCivil = "Divodciado(a)"
    elif(np.array_equal(estadoCivil,[0,0])):
        ponderacionEstadoCivil = "Soltero(a)"
    elif(np.array_equal(estadoCivil,[0,1])):
        ponderacionEstadoCivil = "Casado(a)"

    if(np.array_equal(vivienda,[0,0])):
        ponderacionVivienda = "Propia"
    elif(np.array_equal(vivienda,[0,1])):
        ponderacionVivienda = "Rentada"
    elif(np.array_equal(vivienda,[1,0])):
        ponderacionVivienda = "Familiar"
    elif(np.array_equal(vivienda,[1,1])):
        ponderacionVivienda = "Compartida"

    if(np.array_equal(ingresos,[0,0])):
        ponderacionIngresos = "Ingresos fijos"
    elif(np.array_equal(ingresos,[0,1])):
        ponderacionIngresos = "Ingresos variables"
    elif(np.array_equal(ingresos,[1,0])):
        ponderacionIngresos = "Sin ingresos"

    if(np.array_equal(deudas,[0])):
        ponderacionDeudas = "Tiene deudas pendientes"
    elif(np.array_equal(deudas,[1])):
        ponderacionDeudas = "No tiene deudas pendientes"

    if(np.array_equal(historial,[1,0])):
        ponderacionHistorial = "Sin historial crediticio"
    elif(np.array_equal(historial,[0,1])):
        ponderacionHistorial = "Pagados a destiempo"
    elif(np.array_equal(historial,[0,0])):
        ponderacionHistorial = "Pagados a tiempo"

    if(np.array_equal(formaPago,[0,1])):
        ponderacionFormaPago = "Pago minimo"
    elif(np.array_equal(formaPago,[0,0])):
        ponderacionFormaPago = "Pago para no generar intereses"
    elif(np.array_equal(formaPago,[1,0])):
        ponderacionFormaPago = "Pago mayor para no generar intereses"

    print("Edad: ",ponderacionEdad)
    print("Ocupacion: ",ponderacionOcupacion)
    print("Estudios: ",ponderacionEstudios)
    print("Estado Civil: ",ponderacionEstadoCivil)
    print("Vivienda: ",ponderacionVivienda)
    print("Ingresos: ",ponderacionIngresos)
    print("Deudas: ",ponderacionDeudas)
    print("Historial crediticio: ",ponderacionHistorial)
    print("Forma de pago: ",ponderacionFormaPago)