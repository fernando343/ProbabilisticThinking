# INTRODUCCION AL PENSAMIENTO PROBABILISTICO

* La programación probabilística utiliza probabilídades y modelos probabilísticos para ejecutar cómputos.
* Se utiliza en una gran cantidad de campos: 
    * Inventigación científica
    * Inteligencia artificial 
    * Medicina, etc.
* Exiten lenguajes y librerias especializadas para ejecutar este tipo de cómputo, como Pyro de Uber

Cuando tenemos dos probabilidades unidas por la letra **Y** o **AND** en ingles nos indica que la probabilidad que las dos condiciones se cumplan se reduce

## Donde se utiliza
**UBER**: Lo utiliza por que necesita constantemente unir a sus conductores con sus clientes y necesita poder determinar el tiempo estimado que se va a demorar el conductor en llegar del punto A al punto B 

**FILTROS DE SPAM**: Son una de las primeras aplicaciones reales de gran escala de machine lerning se genero en los años 80 con programacion probabilistica y de la manera que lo implementaron fue que los usuarios hiban diciendo que era span y que no era espan 

## PROBABILIDAD CONDICIONAL
La **probabilidad condicional** es la probabilidad de que ocurra un evento A, sabiendo que también sucede otro evento B. La probabilidad condicional se escribe P(A|B), y se lee «la probabilidad de A dado B».

No tiene por qué haber una relación causal o temporal entre A y B. A puede preceder en el tiempo a B, sucederlo o pueden ocurrir simultáneamente. A puede causar B, viceversa o pueden no tener relación causal. Las relaciones causales o temporales son nociones que no pertenecen al ámbito de la probabilidad. Pueden desempeñar un papel o no, dependiendo de la interpretación que se le dé a los eventos.

Es decir la **probabilidad condicional** cuando evento depende de otro evento

Las formulas que podemos usar son:

    P(A and B) = P(A) * P(B | A)
    P(B) = P(A) * P(B | A) + P(~A) * P(B | ~A)

Un ejemplo de esto puede ser la probabilidad que una persona tenga cáncer, luego de realizar pruebas.

    P(cancer) = P(positivo) * P(cancer | positivo) + P(negativo) * P(cancer | negativo)


Otro ejemplo es cual es la probabilidad de que una persona use drogas, pero como dato adicional esta persona es músico.

    P(drogas) = P(musico) * P(drogas | no musico) + P(~musico) + P(drogas | no musico)

## TEOREMA DE BAYES

Fue planteado por el matemático **Thomas Bayes** al querer saber la probabilidad de aventar un balon si saber en donde cayo como mejorar su probabilidad de que caiga en la mesa. Es probablemente uno de los teoremas mas importantes dentro de las matemáticas

![Formula](https://i.postimg.cc/CxrL8sWt/teorema-De-Bayes.png)


Nos dice que la probabilidad de una hipotesis que la vamos a llamar **A** dada alguna evidencia que sera **B** es simplemente 
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