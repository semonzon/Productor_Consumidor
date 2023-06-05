# Productor_Consumidor

Esta es la práctica 1 de la asignatura de PRPA de la Universidad Complutense de Madrid. 

1. EXPLICACIÓN DE LA PRÁCTICA
Tenemos NPROD procesos que producen n_elem numeros positivos en orden ascendente. 
Cuando un proceso esta vacio, se le asigna el valor -2 y cuando ha terminado de pro-
ducir, el valor -1. También tenemos un consumidor, el cual tiene que escoger el minimo
entre todos los valores disponibles de los productores y añadirlo al buffer. Para ello,
los productores solo podrán producir un elemento cuando su "casilla" este vacia, es decir, 
el consumidor haya cogido el elemento que le corresponde al productor.

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
![VirtualBox_ubuntu23_05_06_2023_11_15_56](https://github.com/semonzon/Productor_Consumidor/assets/124071911/635f8c58-f2bc-44f0-bf26-1d840fd6295e)
![VirtualBox_ubuntu23_05_06_2023_11_16_12](https://github.com/semonzon/Productor_Consumidor/assets/124071911/ff247a01-e073-48ec-9b4a-a6ea3fbe0a03)
