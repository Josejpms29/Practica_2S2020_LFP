# Practica_2S2020_LFP
Practica 
MANUAL DE USUARIO 

INTRODUCCIÓN:
SimpleQL es un programa elaborado con Python en el IDE PyCharm. El programa realizado consiste en una serie de comandos los cuales funcionan
al ingresarlos en la consola del IDE. La función principal de SimpleQL es guardar en la memoria archivos en formato JSON, los cuales contienen
diferentes registros. El programa deberá acceder a los registros para posteriormente poder generar un reporte en formato HTML el cuál se generará
al terminar el programa con un comando. El reporte generado se abrirá en el navegador predeterminado del sistema.

OBJETIVO:
El usuario aprenderá a utilizar un programa a base de comandos, SimpleQL es un programa elaborado en Python que tiene como funcion principal
ser manejado a base de comandos. En este manual se enseñarán los distintos comandos que fueron programados, además, se enseñará a como utilizar 
los distintos comandos y como emplearlos según sea el caso.

CONTENIDO:
En el programa SimpleQL existen distintos comandos a utilizar, estos comandos tienen distintas funciones las cuales iremos analizando a continuación.
Es importante agregar que estos comandos se tienen que ir escribiendo según el orden en el que se van explicando los comandos:

  1) Comando CARGAR: Este comando puede escribirse tanto "CARGAR", como "cargar", seguido de esto, se debrá colocar el nombre de archivo que se desee
                     cargar. Para separar los archivos no se utiliza coma, solo se utiliza un espacio, los nombres de los archivos deberán colocarse 
                     tal y como se escribieron y deben colocarse en la carpeta en la que se encuentre el proyecto. Podemos ver la estructura del comando:
                        
                                                        CARGAR Archivo1.json Archivo2.json Archivo3.json
                                                        cargar Archivo4.json Archivo5.json
                                                        
  2) Comando SELECCIONAR: Este comando tiene distintas funciones, se puede utilizar el comando "SELECCIONAR*" para seleccionar e imprimir todos los registros
                          que se encuentren en los archivos cargados a memoria. Además, también podremos seleccionar las características que querramos ver
                          es decir, podemos utilizar el comando "SELECCIONAR" ó "seleccionar" seguido de un atributo en específico. A continuación podemos
                          ver distintas estructuras del comando mencioncionado
                                                      
                                                        SELECCIONAR*
                                                        SELECCIONAR nombre 
                                                        seleccionar promedio
                                                        
  3) Comando MAXIMO, MINIMO ó SUMA: Estos comandos tienen distintas funciones, el comando "MAXIMO" busca un atributo máximo en los registros, es decir, si 
                                    ponemos el comando seguido de un atributo, ya sean estos edad o promedio, el programa buscará la edad máxima o más grande,
                                    por el contrario, buscará el promedio máximo o más grande. El comando "MINIMO", a diferencia del comando anterior, busca
                                    los atributos mínimos en los distintos registros. Además, el comando "SUMA" suma los distintos promedios o edades según el
                                    usuario indique en consola. A continuación, podemos observar la estructura de los comandos:
                                    
                                                        MAXIMO edad
                                                        MINIMO promedio
                                                        SUMA edad
                                                        
  4) comando CUENTA: Este comando tiene una función más sencilla, cuando se ingresa el comando "CUENTA", el programa contará cuantos registros existen en los
                     distintos archivos de formato JSON, la estructura del comando es la siguiente:
                     
                                                        CUENTA
                                                        
  5) Comando REPORTAR: Al igual que el comando anterior, la función de este comando es sencilla, cuando se ingresa el comando "REPORTAR" este genera un reporte
                       en el cual se encuentran los distintos registros. Este reporte se ecuentra en formato html y se abre al terminar el programa en el 
                       navegador predeterminado del sistema. La estructura del comando es el siguiente:
                        
                                                        REPORTAR  
