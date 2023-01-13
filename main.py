import random
import numpy as np
import matplotlib.pyplot as plt
from evaluacion import Evaluacion
from functionaptitud import Aptitud

#* Objetos 
class Individuo:
    def __init__(self, cromosoma, aptitud):
        self.cromosoma = cromosoma
        self.aptitud = aptitud
    def __getitem__(self, index):
        return self.genes[index]

def Poblacion(tamPoblacionInicial):

    poblacionInicial = []
    
    for i in range(tamPoblacionInicial):

        #Genera un arreglo de 18 digitos lleno con 0 y 1 aleatoriamente
        cromosoma = np.array(np.random.randint(2, size=18))

        if(np.array_equal(cromosoma[11:13],[1,1])):
            cromosoma[11:13] = random.choice([[0,1],[1,0],[0,0]])
        
        if(np.array_equal(cromosoma[14:16],[1,1])):
            cromosoma[14:16] = random.choice([[0,1],[1,0],[0,0]])

        if(np.array_equal(cromosoma[16:18],[1,1])):
            cromosoma[16:18] = random.choice([[0,1],[1,0],[0,0]])
            
        aptitud = Aptitud(cromosoma)
        individuo = Individuo(cromosoma,aptitud)
        poblacionInicial.append(individuo)

    #for i in range (tamPoblacionInicial):
    #    print("Individuo: " + str(i+1)+ " " + str(poblacionInicial[i].cromosoma) + " " + str(poblacionInicial[i].aptitud))

    return poblacionInicial 

def Torneo(poblacion,tamMuestra):

    poblacionTorneo = []

    if (tamMuestra < len(poblacion)):

        for i in range(len(poblacion)):
            muestra = random.sample(poblacion, tamMuestra)
            mejorIndividuo = muestra[0]

            for i in range(len(muestra)):
                if muestra[i].aptitud > mejorIndividuo.aptitud:
                    mejorIndividuo = muestra[i]
                
            poblacionTorneo.append(mejorIndividuo)

        print(" -- TORNEO -- ")
        #for i in range (len(poblacionTorneo)):
        #    print("Individuo: " + str(i+1)+ " " + str(poblacionTorneo[i].cromosoma) + " " + str(poblacionTorneo[i].aptitud))
        print("Se generaron " + str(len(poblacionTorneo)) + " individuos del torneo")
    else:
        poblacionTorneo = poblacion

    return poblacionTorneo


def Cruza(poblacion,probabilidadCruza):

    poblacionCruza = []
    contadorCruzados = 0

    if(probabilidadCruza == 0):
        poblacionCruza = poblacion
    else:
        while(len(poblacionCruza) < len(poblacion)):
            
            individuo1 = random.choice(poblacion)
            individuo2 = random.choice(poblacion)

            aleatorio = random.random()

            nuevoIndividuo1Generado = False
            nuevoIndividuo2Generado = False

            if(aleatorio < probabilidadCruza):
                rangoCorte1 = np.arange(1,16,1)
                punto1 = np.random.choice(rangoCorte1)
                
                rangoPunto2 = np.arange(punto1+1,17,1)
                punto2 = np.random.choice(rangoPunto2)

                #Corta el cromosoma en el punto seleccionado
                corte1Individuo1 = individuo1.cromosoma[0:punto1]
                corte2Individuo1 = individuo1.cromosoma[punto1:punto2]
                corte3Individuo1 = individuo1.cromosoma[punto2:18]
                
                corte1Individuo2 = individuo2.cromosoma[0:punto1]
                corte2Individuo2 = individuo2.cromosoma[punto1:punto2]
                corte3Individuo2 = individuo2.cromosoma[punto2:18]

                #Crea el nuevo cromosoma
                nuevoCromosoma1 = np.concatenate((corte1Individuo1,corte2Individuo2,corte3Individuo1),axis=0)
                nuevoCromosoma2 = np.concatenate((corte1Individuo2,corte2Individuo1,corte3Individuo2),axis=0)

                if not(np.array_equal(nuevoCromosoma1[11:13],[1,1]) or (np.array_equal(nuevoCromosoma1[14:16],[1,1])) or np.array_equal(nuevoCromosoma1[16:18],[1,1])):
                    aptitud1 = Aptitud(nuevoCromosoma1)
                    nuevoIndividuo1 = Individuo(nuevoCromosoma1,aptitud1)
                    poblacionCruza.append(nuevoIndividuo1)
                    nuevoIndividuo1Generado = True
                else:
                    nuevoIndividuo1Generado = False
                         
                if not(np.array_equal(nuevoCromosoma2[11:13],[1,1]) or (np.array_equal(nuevoCromosoma2[14:16],[1,1])) or np.array_equal(nuevoCromosoma2[16:18],[1,1])):
                    aptitud2 = Aptitud(nuevoCromosoma2)
                    nuevoIndividuo2 = Individuo(nuevoCromosoma2,aptitud2)
                    poblacionCruza.append(nuevoIndividuo2)
                    nuevoIndividuo2Generado = True
                else:
                    nuevoIndividuo2Generado = False

                if((nuevoIndividuo1Generado == True) and (nuevoIndividuo2Generado == True)):
                    contadorCruzados = contadorCruzados +2
                else:
                    if((nuevoIndividuo1Generado == True) and (nuevoIndividuo2Generado == False)):
                        poblacionCruza.append(individuo2)
                        contadorCruzados = contadorCruzados + 1
                            
                    if((nuevoIndividuo1Generado == False) and (nuevoIndividuo2Generado == True)):
                        contadorCruzados = contadorCruzados +1
                        poblacionCruza.append(individuo1)
            else:
                poblacionCruza.append(individuo1)
                poblacionCruza.append(individuo2)
            
    print(" -- CRUZA -- ")
    #for i in range (len(poblacionCruza)):
    #    print("Individuo: " + str(i+1)+ " " + str(poblacionCruza[i].cromosoma) + " " + str(poblacionCruza[i].aptitud))
    print("Se generaron " + str(len(poblacionCruza)) + " individuos de la cruza")
    print("Se cruzaron " + str(contadorCruzados) + " individuos")

    return poblacionCruza

def Mutacion(poblacion,probabilidadMutacion,rangoMutacion):

    poblacionMutacion = []
    contadorMutados = 0
    rango = np.arange(1,rangoMutacion[0]+1)

    if(probabilidadMutacion == 0):
        poblacionMutacion = poblacion
    else:
        while(len(poblacionMutacion) < len(poblacion)):
            
            individuo = random.choice(poblacion)
            noAleatorio = random.random()

            if(noAleatorio < probabilidadMutacion):
                cromosoma = []

                for i in range (len(individuo.cromosoma)):
                    gen = individuo.cromosoma[i]
                    aleatorioGen = random.randint(1,rangoMutacion[1])

                    if(aleatorioGen in rango):                        
                        if(gen == 0):
                            gen = 1
                        else:
                            gen = 0
                    
                    cromosoma.append(gen)
                
                cromosoma = np.array(cromosoma)

                #print("Individuo original: " + str(individuo.cromosoma))
                #print("Cromosoma mutado: " + str(cromosoma))

                # if(np.array_equal(cromosoma,individuo.cromosoma)):
                #     #print("             El individuo no muto")
                #     poblacionMutacion.append(individuo)
                # else:
                if not(np.array_equal(cromosoma[11:13],[1,1]) or (np.array_equal(cromosoma[14:16],[1,1])) or np.array_equal(cromosoma[16:18],[1,1])):
                    #print("         EL INDIVIDUO MUTO")
                    aptitud = Aptitud(cromosoma)
                    individuoMutado = Individuo(cromosoma,aptitud)
                    poblacionMutacion.append(individuoMutado)
                    contadorMutados = contadorMutados + 1
            else:
                poblacionMutacion.append(individuo)

    print(" -- MUTACION -- ")
    print("Se generaron " + str(len(poblacionMutacion)) + " individuos de la mutacion")
    print("Mutaron " + str(contadorMutados) + " individuos")

    return poblacionMutacion

def siguienteGeneracion(poblacion,muestraTorneo,probabilidadCruza,probabilidadMutacion,rangoMutacion):
    torneo = Torneo(poblacion,muestraTorneo)
    cruza = Cruza(torneo,probabilidadCruza)
    mutacion = Mutacion(cruza,probabilidadMutacion,rangoMutacion)
    return mutacion 
    
def main():

    #* Parametros generales
    tamPoblacionInicial = 500
    noGeneraciones = 20

    #* Torneo
    muestraTorneo = 3
    #* Cruza
    probabilidadCruza = 0.3
    #* Mutacion
    probabilidadMutacion = 0.02
    rangoMutacion = [5,100000]

    ymejor = []
    ypeor = []
    ypromedio = []
    
    resultadoGeneraciones = []
    individuosAptos = []

    poblacion = Poblacion(tamPoblacionInicial)

    # print("Poblacion inicial")
    # for i in range(len(pob)):
    #     print("Individuo: " + str(i+1)+ " " + str(pob[i].cromosoma) + " " + str(pob[i].aptitud))
    # print(" ")

    for i in range(noGeneraciones):

        print("-----------------------------------")
        print("GENERACION NO. " + str(i+1))
        
        poblacion = siguienteGeneracion(poblacion,muestraTorneo,probabilidadCruza,probabilidadMutacion,rangoMutacion)
        
        #print(" -- POBLACION DE LA GENERACION " + str(i+1) + " --")
        #for i in range(len(poblacion)):
        #    print("Individuo: " + str(i+1)+ " " + str(poblacion[i].cromosoma) + " " + str(poblacion[i].aptitud))
        print("Se generaron " + str(len(poblacion)) + " individuos de la generacion " + str(i+1))

        peorIndividuo = min(poblacion, key=lambda poblacion: poblacion.aptitud)
        ypeor.append(peorIndividuo.aptitud)

            # #Obten el peor individuo de la generacion
        mejorIndividuo = max(poblacion, key=lambda poblacion: poblacion.aptitud)
        ymejor.append(mejorIndividuo.aptitud)

        suma = 0
        for j in range(len(poblacion)):
            suma = suma + poblacion[j].aptitud
                
        promedioGeneracion = suma/len(poblacion)
        ypromedio.append(promedioGeneracion)

        print(" ")
        print("El mejor individuo de la generacion " + str(i+1) + " es: " + str(mejorIndividuo.cromosoma) + " con aptitud: " + str(mejorIndividuo.aptitud))
        print("El peor individuo de la generacion " + str(i+1) + " es: " + str(peorIndividuo.cromosoma) + " con aptitud: " + str(peorIndividuo.aptitud))
        print("La aptitud promedio de la generacion " + str(i+1) + " es: " + str(promedioGeneracion))

        resultadoGeneraciones.append(mejorIndividuo)
        resultadoGeneraciones.append(peorIndividuo)

        print("-----------------------------------")
        print(" ")

    mejorIndividuoGeneraciones = max(resultadoGeneraciones, key=lambda resultadoGeneraciones: resultadoGeneraciones.aptitud)
    peorIndividuoGeneraciones = min(resultadoGeneraciones, key=lambda resultadoGeneraciones: resultadoGeneraciones.aptitud)
    
    print(" -- RESULTADOS FINALES DEL ALGORITMO GENETICO -- ")
    print("El mejor individuo de todas las generaciones fue " + str(mejorIndividuoGeneraciones.cromosoma) + " con aptitud: " + str(mejorIndividuoGeneraciones.aptitud))
    print("El peor individuo de todas las generaciones fue " + str(peorIndividuoGeneraciones.cromosoma) + " con aptitud: " + str(peorIndividuoGeneraciones.aptitud))
    print(" ")

    print(" -- LISTA DE CANDIDATOS APTOS PARA UN CREDITO --")
    for i in range(len(resultadoGeneraciones)):
        if(resultadoGeneraciones[i].aptitud >= 8.0):
            individuosAptos.append(resultadoGeneraciones[i])

    individuosAptos.sort(key=lambda individuosAptos: individuosAptos.aptitud, reverse=True)

    for i in range(len(individuosAptos)):
        print("Individuo " + str(i+1)+ ": " + str(individuosAptos[i].cromosoma) + " " + str(individuosAptos[i].aptitud))
    
    print(" ")

    print(" -- CARACTERISTICAS DE LA PERSONA MAS APTA PARA UN CREDITO --")
    Evaluacion(mejorIndividuoGeneraciones.cromosoma)
    print(" ")

    print(" -- CARACTERISTICAS DE LA PERSONA MENOS APTA PARA UN CREDITO --")
    Evaluacion(peorIndividuoGeneraciones.cromosoma)
    print(" ")

    # crea un arreglo de 0 a el tamaño de grafica
    x = np.arange(1,noGeneraciones+1,1)

    plt.plot(x,ymejor,"o-",label="Mejor individuo",color="green")
    plt.plot(x,ypeor,"o-",label="Peor individuo",color="red")
    plt.plot(x,ypromedio,"o-",label="Aptitud promedio",color="blue")
    plt.ylabel("Valor de la aptitud")
    plt.xlabel("No. de generaciones")
    plt.title("Resultados finales")
    plt.legend()
    #plt.savefig("Generaciones.png")
    plt.show()

if __name__ == "__main__":
    main()
