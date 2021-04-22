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
