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


NPROD = 10


def producir(empty, non_empty, num, NPROD,i):
    num.value = random.randint(0, 10)
    for _ in range(NPROD):
        empty.acquire()
        num.value += random.randint(1,10)
        print(f'Proceso {i} produce el valor {num.value}\n')
        non_empty.release()
    empty.acquire()
    num.value = -1 
    non_empty.release()
    
def consumir(empty, non_empty, nums,  buffer, NPROD):
    for i in range(NPROD):
        for i in range(NPROD):
            non_empty[i].acquire()
        for i in range(NPROD):
            minimo = 100
            numero = nums[i].value
            if numero < minimo and numero != -1:
                minimo = numero
                    
            empty[i].release()
            buffer.append(minimo)
            print(f'el consumidor consume {minimo} y el buffer es {buffer}\n')
            non_empty[i].acquire()


if __name__ == '__main__':
    n = NPROD
    buffer = []
    semaphore_empty = [Semaphore(1) for i in range(n)]
    semaphore_non_empty = [Semaphore(0) for i in range(n)]
    nums = [Value('i', -2) for _ in range(n)]
    
    processes = [Process(target=producir, args=(semaphore_empty[i],semaphore_non_empty[i], nums[i], NPROD,i)) for i in range(n)]
    consumidor = Process(target = consumir, args=(semaphore_empty, semaphore_non_empty, nums, buffer, NPROD))
    for p in processes:
        p.start()
    consumidor.start()
    for p in processes:
        p.join()
    print ("fin")
    



