# Productor_Consumidor

Esta es la práctica 1 de la asignatura de PRPA de la Universidad Complutense de Madrid. 

1. EXPLICACIÓN DE LA PRÁCTICA
Tenemos NPROD procesos que producen n_elem numeros positivos en orden ascendente. 
Cuando un proceso esta vacio, se le asigna el valor -2 y cuando ha terminado de pro-
ducir, el valor -1. También tenemos un consumidor, el cual tiene que escoger el minimo
entre todos los valores disponibles de los productores y añadirlo al buffer. Para ello,
los productores solo podrán producir un elemento cuando su "casilla" este vacia, es decir, 
el consumidor haya cogido el elemento que le corresponde al productor.
El consimidor espera a que todos los productores tengan un elemento producido y añade al buffer
el menor de todos ellos. 

Para su correcto funcionamiento, se le asigna un semáforo a cada productor.

2. FUNCIONAMIENTO
En el archivo .py estan todos los pasos que realizan los productores y el 
consumidor explicados. 

3. EJECUCIÓN
Para ejecutar el programa, es necesario introducir en la terminal el siguiente comando:
>> python3 productor_consumidor_mejorada.py
En la salida se mostrará todas las veces que el productor produce y el consumidor
obtiene un número. 
Se adjuntan capturas de pantalla de un ejemplo al ejecutar el programa.

![prod_cons_captura1](https://github.com/semonzon/Productor_Consumidor/assets/124071911/4b5b2e3a-47c8-41a2-ba7c-6c031bc4578a)
![prod_cons_captura2](https://github.com/semonzon/Productor_Consumidor/assets/124071911/c129877a-244c-4647-a3ec-dd17d89ce8df)
