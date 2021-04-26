# INTRODUCCIÓN AL PENSAMIENTO PROBABILISTICO

## Tabla de contenido
* [**Programación Probabílistica**]()
    * [Programación Probabílistica](##programacion-probabilistica)
        * [Donde se utiliza](#Donde-se-utiliza)
    * [Probabilidad condicional](#probabilidad-condicional)
    * [Teorema de bayes](#Teorema-de-bayes)
* [**Mentiras estadísticas**]()
    * [Garbage in, Garbage out (GIGO)](##Garbage-in-Garbage-out-(GIGO)-o-Principio-gaigo)
    * [Imágenes engañosas](#Imágenes-engañosas)
    * [Cum Hoc Ergo Propter Hoc](#Cum-Hoc-Ergo-Propter-Hoc)
    * [Prejuicio en el muestreo](#Prejuicio-en-el-muestreo)
    * [Falacia del francotirador de Texas](#Falacia-del-francotirador-de-Texas)
    * [Porcentajes confusos](#Porcentajes-confusos)
    * [Falacia de regresión](#Falacia-de-regresión)
* [**Introducción a Machine Learning**](#Introducción-a-Machine-Learning)
    * [Historia](#Historia)
    * [Feature vectors](#Feature-vectors)
    * [Métricas de distancia](#Métricas-de-distancia)
* [**Agrupamiento**]()
    * [Introducción al agrupamiento](#Introducción-al-agrupamiento)
    * [Clustering](#Clustering)
        * [Algoritmo de agrupamiento jerárquico](#Algoritmo-de-agrupamiento-jerárquico)
        * [Algoritmo de Agrupamiento K-means](#Algoritmo-de-Agrupamiento-K-means)
* [**Clasificación**]()
    * [Introducción a la clasificación](#Introducción-a-la-clasificación)
        * [Algoritmo K-nearest neighbors](#Algoritmo-K-nearest-neighbors)





## Programación probabilistica

### Programación probabilistica
---
* La programación probabilística utiliza probabilídades y modelos probabilistico para ejecutar cómputos.
* Se utiliza en una gran cantidad de campos: 
    * Investigación científica
    * Inteligencia artificial 
    * Medicina, etc.
* Existen lenguajes y librerías especializadas para ejecutar este tipo de cómputo, como Pyro de Uber

Cuando tenemos dos probabilidades unidas por la letra **Y** o **AND** en ingles nos indica que la probabilidad que las dos condiciones se cumplan se reduce

### Donde se utiliza
**UBER**: Lo utiliza por que necesita constantemente unir a sus conductores con sus clientes y necesita poder determinar el tiempo estimado que se va a demorar el conductor en llegar del punto A al punto B 

**FILTROS DE SPAM**: Son una de las primeras aplicaciones reales de gran escala de machine lerning se genero en los años 80 con programación probabilistica y de la manera que lo implementaron fue que los usuarios iban diciendo que era span y que no era spam 

### Probabilidad condicional
---
La **probabilidad condicional** es la probabilidad de que ocurra un evento A, sabiendo que también sucede otro evento B. La probabilidad condicional se escribe P(A|B), y se lee «la probabilidad de A dado B».

No tiene por qué haber una relación causal o temporal entre A y B. A puede preceder en el tiempo a B, pueden ocurrir simultáneamente. A puede causar B, viceversa o pueden no tener relación causal. Las relaciones causales o temporales son nociones que no pertenecen al ámbito de la probabilidad. Pueden desempeñar un papel o no, dependiendo de la interpretación que se le dé a los eventos.

Es decir la **probabilidad condicional** cuando evento depende de otro evento

Las formulas que podemos usar son:

    P(A and B) = P(A) * P(B | A)
    P(B) = P(A) * P(B | A) + P(~A) * P(B | ~A)

Un ejemplo de esto puede ser la probabilidad que una persona tenga cáncer, luego de realizar pruebas.

    P(cáncer) = P(positivo) * P(cáncer | positivo) + P(negativo) * P(cáncer | negativo)


Otro ejemplo es cual es la probabilidad de que una persona use drogas, pero como dato adicional esta persona es músico.

    P(drogas) = P(músico) * P(drogas | no músico) + P(~músico) + P(drogas | no músico)

### Teorema de bayes
---

Fue planteado por el matemático **Thomas Bayes** al querer saber la probabilidad de aventar un balón si saber en donde cayo como mejorar su probabilidad de que caiga en la mesa. Es probablemente uno de los teoremas mas importantes dentro de las matemáticas

![Formula](https://i.postimg.cc/CxrL8sWt/teorema-De-Bayes.png)


Nos dice que la probabilidad de una hipótesis que la vamos a llamar **A** dada alguna evidencia que sera **B** es simplemente 
la probabilidad de **A and B** sobre la probabilidad de **B**

traducido esto a lo que tenemos es 

![FORMULA](https://i.postimg.cc/Z5XzZskT/BAYES.png)

    P(H) = prior
    p(H|E)= posteriorph

Para poder visualizar esto vamos a usar un **eikosograma**

#### Eikosograma
Un Eikosograma es una representación gráfica de una tabla de recuentos de dos factores (o probabilidades conjuntas) que hace que los tamaños relativos de los recuentos en cada tabla sean claramente visibles al hacer que el área de cada celda sea proporcional al recuento.

![eikosogram](https://i.postimg.cc/RCtkQLn8/eikosogram.jpg)

#### Ejemplo con un ejercicio del teorema de bayes
* En un acuario se tienen solo 2 especies de
peces. El 40 % de los peces del acuario son de la
especie azul y el 60% son de la especie roja. De
la especie azul, el 30 % son machos; mientras
que, de la especie roja, el 40% son hembras. Si
se selecciona un pez al azar,
a) y resulta que es hembra, ¿cuál es la
probabilidad de que sea de la especie azul?

![arbolgrafico](https://i.postimg.cc/BvVx6DSc/bayes-Arbol.jpg)
![resoluciongrafico](https://i.postimg.cc/J7PRBqVL/Ejercico-bayes.jpg)

![eikosogramaejercicio](https://i.postimg.cc/gcSP028c/grafico.jpg)

#### Llevando el problema a codigo
    def calc_bayes(prio_A, prob_B_dado_A, prob_B):
        return (prio_A * prob_B_dado_A) / prob_B

    if __name__ == '__main__':
        prob_azul = 40 / 100
        prob_hembra_dado_azul = 70 / 100
        prob_rojo = 60 /100
        prob_hembra_dado_rojo = 40 /100 
        prob_de_hembra = (prob_azul * prob_hembra_dado_azul) + (prob_rojo * prob_hembra_dado_rojo)
        probabilidad = round(calc_bayes(prob_azul, prob_hembra_dado_azul, prob_de_hembra), 3) 
        total = round(probabilidad * 100, 2)
        print(f'{total} %')

## Mentiras estadísticas

### Garbage in, Garbage out (GIGO) o Principio gaigo
---
* La calidad de nuestros datos es igual de fundamental que la precisíon de nuestros cómputos.
* Cuando los datos son errados, aunque tengamos un cómputo prístino nuestros resultados serán erróneos.
* En pocas palabras: con datos errados las conclusiones serán erradas

**Ejemplo**
Unos de los ejemplos mas importantes es en el censo de 1840 en Estados Unidos estos censos aun se hacían a mano esto fue previo a las maquinas a hacer censos y el problema es que el error ya era demasiado grande para llegar a conclusiones reales con métodos manuales. Uno de los errores mas importantes es que el el censo arrojaba que las personas de color que habían sido liberadas eran 10 veces mas probables de volverse locos que las personas de color que aun eran esclavos

### Imágenes engañosas 
---

* Las visualizaciones son muy importantes para entender un conjunto de datos
* Sin embrago, cuando se juega con la escala se puede llegar a conclusiones incorrectas.
* Nunca se debe confiar en una gráfica sin escalas o etiquetas 

![imagenesenga](https://i.postimg.cc/kgdVzXTs/iamgensenga.png)

Viendo la imagen del lado izquierdo podríamos llegar a la conclusión que los Yankees son mucho mejores que los Red Sox pero si nos fijamos en la imagen solo tiene una diferencia de 107 puntos y esto se debe a que tiene una escala incorrecta a diferencia de la gráfica del lado derecho 

### Cum Hoc Ergo Propter Hoc
---
* Dos variables están positivamente correlacionadas cuando se mueven en la misma dirección y negativamente correlacionadas cuando se mueven en direcciónes opuestas
* Correlación no implica casualidad.
* Pueden existir variables escondidas que generen la correlación 
* *Después de esto, eso; entonces a consecuencia de esto, eso.*

### Prejuicio en el muestreo
---

* Para que un muestro pueda servir como base para la inferencia estadística tiene que ser aleatorio y representativo.
* El prejuicio en el muestreo elimina la representativas de las muestras
* A veces conseguir muestras es difícil. por lo que se utiliza a la probación de mas fácil acceso

**Ejemplo**

Uno de los errores mas comunes es pensar que todos nuestros ante pasados sean hombres de cavernas y es que es muy difícil por cuestión de evidencias ya que se encuentran las muestras dentro de cavernas pero esto no quiere decir que haya sido asi 

Lo importante es recordar que para poder generar una inferencia estadística válida necesitas aleatoriedad y también necesitamos una muestra representativa 

### Falacia del francotirador de Texas
---
* Esta falacia se da cuando no se toma la aleatoriedad en consideración 
* También sucede cuando uno se enfoca en la similitudes e ignora las diferencias 
* Cuando fallamos al tener una hipótesis antes de recolectar datos estamos en alto riesgo de caer en esta falacia(***muy común en Data Science***).

Una forma muy común de caer en este error es comenzar a recolectar datos sin una hipótesis 

### Porcentajes confusos 
---

* Cuando no sabemos la cuenta total del cual se obtiene un porcentaje tenemos el riesgo de concluir falsos resultados.
* Siempre es importante ver el contexto
* Los porcentajes, en vació, no significan mucho

**Ejemplo**

* La escuela A incremento su rendimiento en 25%
* La escuela B incremento su rendimiento en 10%
* La escuela C incremento su rendimiento en un 5%
¿Que escuela tuvo un mejor desempeño global solo viendo estos porcentajes* 
Sin contexto esto no sirve de nada 

|   |Rendimiento 2018|Rendimiento 2019|Incremento|Incremento Porcentajes   |
|:-:|:-:|:-:|:-:|:-:|
|Escuela A| 20 | 25 | 5 | 25% |
|Escuela B| 50 | 55 | 5 | 10% |
|Escuela C| 95 | 100 | 5 | 5% |

Cuando tenemos los datos podemos observar que la escuela que mejor desempeño tiene es la escuela C

**Ejemplo**
* En 1970, 12.5 millones de jóvenes vivían con sus padres
* En 2015 esta cifra se incrementó a 18.6 millones
¿esto representa un 48%?

||Jóvenes viviendo con sus padres|Población del país| Porcentaje de jóvenes viviendo con sus padres|
|:-:|:-:|:-:|:-:|  
|1970|12.5|234.38|5.33%|
|2015|18.6|309.98|6.01%|
|Diferencia|¿48?||NO 48%|

En realidad si hubo de un del 0.7% pero no del 48%

### Falacia de regresión 
---

* Muchos eventos fluctuá naturalmente, por ejemplo, la temperatura promedio de una ciudad, el rendimiento de un atleta, los rendimientos de un portafolio de inversión etc.
* Cuando algo fluctúa y se aplican medidas correctivas se puede creer que existe un lugar de una regresión a la media.

**Ejemplos**
* Un atleta que le fue muy mal durante una semana y cambia de alimentación y entonces le comienza a ir como antes, el puede atribuir esto a su alimentación y no una regresión a la media
* Cuando tienes un estudiante que le esta yendo una racha mala y lo castigas y luego vuelve a ser el estudiante que era antes puedes caer en el error que tus medidas correctivas es lo que le esta haciendo mejorar 

## Introducción a Machine Learning
### Introducción a Machine Learning
---
**¿Que es?**
> Es el campo de estudio que le da a las computadoras la habilidad de aprender sin ser explícitamente programadas. *Arthur Samuel, 1959*

Son algoritmos matemáticos muy inteligentes en el sentido de cleverness de que son astutos que nos permiten llegar a las conclusiones de manera automática como si un humano se hubiera puesto a pensar y reflexionar 

### Historia
---

Todo empezó con **Thomas Bayes** que nos otorgo una forma de pensar matemáticamente en como incorporar la evidencia, como incorporar los datos que tenemos del mundo real para poder llegar a conclusiones cada vez mas correctas de manera recursiva es decir mientras mas datos obtengamos del mundo real mas correctas van a ser nuestras aproximaciones.

**Alan Turing** no solo descubrió que todos los algoritmos son el mismo algoritmo y nos dio la base para crear las computadoras modernas y si no también nos dio las bases para que estas computadoras aprendan 

**Marvil Minsky** creo la primera red neuronal la cual por la epoca solo contaba de una capa 

En 1952 **Arthur Samuel** genera el primer programa que sabe jugar damas chinas y la forma en que lo general es calculando los siguientes movimientos. Este programa nos permitió entender que aprender desde una perspectiva humana significaba 2 cosas:
* **Memorizar**: Los humanos memorizamos los datos 
* **Generealizar** 

En 1960 **Donald Michie** genera la primera la primera red adversarial en donde se permite que las computadoras puedan jugar constantemente para poder entender como automatizar las reglas de un juego

En 1967 se inventa el algoritmo de **K-nearest neighbor** que es la primera aproximación para detectar patrones a través de datos que ya preexisten y su primera aplicación fue para calcular rutas 

En 1969 **Marvin Minsky** escribe el libro de **Perceptrons** y este libro fue un hito dentro del Machine Lerning por que detuvo en seco toda la investigación relacionada con redes neuronales por que Marvin demostró matemáticamente que las redes que el mismo había diseñado no permitían seguir adelante dentro del desarrollo del IA. Pero el error del cual el no se había dado cuenta es que dentro de las redes podíamos tener redes de mas de una capa pero el estaba hablando de solo de una capa la cual tiene varias limitantes 

En 1979 se genero el **Stanford Car** fue una forma en la cual los estudiantes de Stanford generaron algoritmos para lograr mover un carro que ellos habían hecho para que pudiera evitar obstáculos 

1997 Fue el gran año que marco el paso a la inteligencia artificial moderna, fue el año en que la computadora **Deep Blue** derroto a Gary Kasparov el gran campeón durante muchos años de ajedrez 

* Machine learning se utiliza cuando : 
    * Programar un algoritmo es imposible
    * El problema es muy complejo o no se conocen algoritmos para resolverlos
    * Ayuda los humanos a entender patrones (*data ming*)
* Aprendizaje supervisado vs no  supervisado bs semi supervisado
* Batch vs online learning 

### Feature vectors
---

* Se utiliza para representar características simbólicas o numéricas llamadas *features*.
* Permite analizar un objeto desde una perspectiva matemática.
* Los algoritmos de machine learning típicamente requieren representaciones numéricas para poder ejecutar el computo
* Uno de los *feature* vectores mas conocidos es la presentación del color a través de RGB.
    * color = [R, G, B]

**Ejemplos**
* Procesamiento de imágenes:
    * Gradientes
    * Bordes
    * Áreas
    * Colores
* Reconocimiento de voz:
    * Distancia de sonidos
    * Nivel de ruido
    * Razón ruido
    * Señal
* Spam:
    * Dirección IP
    * Estructura del texto,
    * Frecuencia de palabras
    * Encabezados 

### Métricas de distancia
---

* Muchos de los algoritmos de machine learning pueden clasificarse como algoritmos de optimización.
* lo que desean optimizar es una función que en muchas ocasiones se refiere a la distancia entre features  
x = (a, b), y = (c, d)

* **Distancia euclidiana**:
Una de las distancias más conocidas y utilizadas es la distancia euclídea. Ya que es la que se utiliza en el día a día para medir la separación entre dos puntos. La distancia euclídea en un espacio de n dimensiones se define mediante la siguiente ecuación

    * ![formula](https://latex.codecogs.com/gif.latex?\bg_white&space;d(a,&space;b)&space;=&space;\sqrt{\sum_{i&space;=&space;1}^{n}(\frac{a_{i}}{\sigma&space;_{i}}-\frac{b_{i}}{\sigma_{i}&space;})^{2}})

* **Distancia de Manhattan**:  Otra distancia de interés en algunos problemas es la Manhattan o geometría del taxista. El nombre hace referencia al diseño de cuadriculado de las calles de la isla de Manhattan, lo que obliga a moverse en los ejes que definen las calles. Así la distancia más corta entre dos puntos es la suma de los tramos de las calles. Esto es lo que se muestra en la siguiente figura donde la línea negra representa la distancia euclídea y el resto son la distancia Manhattan se define mediante la siguiente ecuación
    * ![formula](https://latex.codecogs.com/gif.latex?\bg_white&space;d(a,&space;b)&space;=&space;\sqrt{\sum_{i&space;=&space;1}^{n}|a_{i}&space;-&space;b_{i}|})

* **Distancia de Minkowsky**: La distancia de Minkowsky es una generalización de las vistas anteriormente. Esto se realiza mediante un parámetro pp con el que se puede reproducir los valores de las anteriores. Matemáticamente se define como
    * ![formula](https://latex.codecogs.com/gif.latex?\bg_white&space;d(a,&space;b)&space;=&space;\sqrt{\sum_{i&space;=&space;1}^{n}&space;|a_{i}&space;-&space;b_{i}|^{p}})


## Agrupamiento 
### Introducción al agrupamiento 
Existen muchas formas de clasificar los algoritmos de machine learning supervisados, no supervisados, en batch, en online pero una de las formas mas facil de agruparlo es en algoritmos de agrupamiento o ***Clustering***  y algoritmos de clasificación o ***classification algorithms***

### Clustering

* Es un proceso mediante el cual se agrupan objetos similares en clusters que los identifica.
* Se clasifica como aprendizaje no supervisado ya que no requiere la utilización de etiquetas.
* Permite entender la estructura de los datos y la similitud entre los mismos.
* Es utilizado en motores de recomendación, análisis de redes sociales, análisis de riesgo crediticio, clasificación de genes, riesgos médicos, etc

#### **Algoritmo de agrupamiento jerárquico**
* Es un algoritmo que agrupa objetos similares en grupos llamados clusters.
* El algoritmo comienza tratando a cada objeto como un cluster individual y luego realiza los siguientes pasos de manera recursiva:
    * Identifica los dos clusters con menos distancia *los mas similares*.
    * Agrupa los dos clusters en uno nuevo.

* El output final es un dendrograma que muestra la relación entre objetos y grupos.
*Es importante determinar qué medida de distancia vamos a utilizar y los puntos a utilizar en cada cluster *(linkage criteria)*

#### **Algoritmo de Agrupamiento K-means**
* Es un algoritmo que agrupa utilizando centroides.
* El algoritmo funciona signado puntos al azar(*K define el número inicial de clusters*) y después:
    * En cada iteración el punto se ajusta a su nueva centroide y cada punto se re calcula con la distancia con respecto de los centroides. 
    * Los puntos se reasignan al nuevo centro
    * El algoritmo se repite de manera iterativa hasta que ya no existen mejoras

## Clasificación 
### Introducción a la clasificación 
* Es el proceso mediante el cual se predice la clase de cierto dato.
* Es un tipo de aprendizaje supervisado ya que para que funcione, se necesitan etiquetas con los datos(*labels*)
* Se utiliza en muchos dominios, incluyendo la medicina, aprobación crediticia, reconocimiento de imágenes, vehículos autónomos, entre otros.
* Sigue dos pasos:
    * Aprendizaje (*creación del modelo*)
    * Clasificación

#### Algoritmo K-nearest neighbors 
Es uno de los algoritmos mas importante dentro del machine learning
* Parte del supuesto de que ya tenemos un conjunto de datos clasificados.
* Trata de encontrar los "vecinos más cercanos"
* k se refiere a la cantidad de vecinos que se utilizaran para clasificar un ejemplo que aún no ha sido clasificado.
* Es sencillo de implementar y tiene aplicaciones en medicina, finanzas, agricultura, etc.
* Es computacionalmente muy costoso y no sirve con datos de alta dimensionalidad. 
