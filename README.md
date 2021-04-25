# INTRODUCCIÓN AL PENSAMIENTO PROBABILISTICO

## Tabla de contenido
 * [Programación Probabílistica]()
    * [Programación Probabílistica](##programacion-probabilistica)
        * [Donde se utiliza](#Donde-se-utiliza)
    * [Probabilidad condicional](#probabilidad-condicional)
    * [Teorema de bayes](#Teorema-de-bayes)


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
* Después de esto, eso; entonces a consecuencia de esto, eso.