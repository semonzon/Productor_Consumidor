# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 11:21:59 2023

@author: USUARIO
"""

from multiprocessing import Process
from multiprocessing import Semaphore
from multiprocessing import Value
from multiprocessing import current_process
import random as random
from time import sleep
from numpy import inf


NPROD = 4    #numero de procesos
n_elem = 5   #numero de veces que un proceso produce un numero



def producir(empty, non_empty, num):
    num_aleatorio = random.randint(0,10)
    for _ in range(n_elem):
        num_aleatorio += random.randint(1,10)
        #Entramos a una sección critica
        empty.acquire()   #esperamos a que el semáforo empty esté libre
        print(f'Proceso {current_process().name} va a producir')
        num.value = num_aleatorio
        print(f'Proceso {current_process().name} produce el valor {num.value}')
        sleep(random.random()/3)
        non_empty.release()   #liberamos el semáforo non_empty
        #Salimos de la sección critica
    #Entramos a una sección critica
    empty.acquire()
    num.value = -1  #Cuando hemos acabado, añadimos un -1
    print(f'Proceso {current_process().name} ha acabado y tiene el valor final {num.value}')
    non_empty.release()
    #Salimos de la sección critica





def consumir(empty, non_empty, nums,  buffer):

    for i in range(NPROD):   #Vemos que todos los productores hayan producido
        non_empty[i].acquire()


    no_todos_seleccionados = True
    while no_todos_seleccionados:
        minimo = inf
        valor = None
        for i in range(NPROD):   #calculamos el minimo elemento de todos los disponibles
            numero = nums[i].value
            if numero < minimo and numero != -1 and numero != -2:
                minimo = numero
                valor = i
        
        if minimo == inf:    #si no hay ningun elemento mas para seleccionar, entonces el minimo sigue siendo infinito y paramos
            no_todos_seleccionados = False
        else:     #si hay un elemento disponible, entonces
            nums[valor].value = -2  #añadimos el valor -2 al correspondiente productor
            buffer.append(minimo)    #añadimos al buffer el minimo seleccionado
            print(f'El consumidor ha cogido del productor{valor+1} el valor {minimo}')
            print('el buffer en este momento es:', buffer, '\n')
            print(f'El productor {valor+1} ahora esta vacío, tiene el valor {nums[valor].value} ')
            empty[valor].release()   #liberamos el semáforo del productor para que pueda producir
            sleep(random.random()/3) 
            non_empty[valor].acquire()   #para la siguiente vuelta del bucle, esperamos a que el productor poduzca un número
    print('El buffer final es: ', buffer)


def main():
    buffer = []
    semaphore_empty = [Semaphore(1) for _ in range(NPROD)]
    semaphore_non_empty = [Semaphore(0) for _ in range(NPROD)]
    nums = [Value('i', -2) for _ in range(NPROD)]

    processes = [Process(target = producir, args=(semaphore_empty[i],semaphore_non_empty[i], nums[i])) for i in range(NPROD)]
    consumidor = Process(target = consumir, args=(semaphore_empty, semaphore_non_empty, nums, buffer))
    processes.append(consumidor)
    for p in processes:
        p.start()
    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
