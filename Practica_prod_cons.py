#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:20:49 2023

@author: Sergio Monzon Garces
"""

from multiprocessing import Process
from multiprocessing import Semaphore
from multiprocessing import Value
import random as random





def producir(empty, non_empty, num, i, n_elem):
    num.value = random.randint(0,10)
    for _ in range(n_elem):
        empty.acquire()   #esperamos a que el semáforo empty esté libre
        num.value += random.randint(1,10)    #obtenemos un número mayor que el anterior
        print(f'Proceso {i} produce el valor {num.value}\n')
        non_empty.release()   #liberamos el semáforo non_empty
    empty.acquire()
    num.value = -2 
    non_empty.release()

    
def consumir(empty, non_empty, nums,  buffer, NPROD):
    while True:
        for i in range(NPROD):
            non_empty[i].acquire()   #vemos que el semáforo non_empty de los procesos esté libre
        minimo = 1000000
        valor = None
        for i in range(NPROD):   #calculamos el minimo 
            numero = nums[i].value
            if numero < minimo and numero != -1 and numero != -2:
                minimo = numero
                valor = i
        if minimo == 1000000:    #si no hay ningun elemento mas para seleccionar, paramos
            break
        else:
            buffer.append(minimo)    #añadimos al buffer el minimo
            print(f'El consumidor consume {minimo}\n')
            empty[valor].release()   #liberamos el semáforo empty
    print('El buffer final es: ', buffer)
            






if __name__ == '__main__':
    
    NPROD = 3    #numero de procesos
    n_elem = 5   #numero de veces que un proceso produce un numero
    buffer = []
    semaphore_empty = [Semaphore(1) for i in range(NPROD)]
    semaphore_non_empty = [Semaphore(NPROD*n_elem) for i in range(NPROD)]
    nums = [Value('i', -2) for _ in range(NPROD)]
    
    processes = [Process(target = producir, args=(semaphore_empty[i],semaphore_non_empty[i], nums[i], i, n_elem)) for i in range(NPROD)]
    consumidor = Process(target = consumir, args=(semaphore_empty, semaphore_non_empty, nums, buffer, NPROD))
    for p in processes:
        p.start()
    consumidor.start()
    for p in processes:
        p.join()
    print ("fin")
    
