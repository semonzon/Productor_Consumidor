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


def producir(empty, non_empty, num, NPROD):
    for _ in range(NPROD):
        empty.acquire()
        num.value = random.randint(0, 10)
        non_empty.release()
    empty.acquire()
    num.value = -1 
    non_empty.release()
    
def consumir(empty, non_empty, nums,  buffer, NPROD):
    for i in range(NPROD):
        non_empty[i].acquire()
        
    minimo = 100
    for i in range(NPROD):
        numero = nums[i].value
        if numero < minimo and numero != -1:
            minimo = numero
                
        empty[i].release()
        buffer.append(minimo)
        non_empty[i].acquire()
        
    print(buffer)
        


if __name__ == '__main__':
    n = NPROD
    buffer = []
    semaphore_empty = [Semaphore(1) for i in range(n)]
    semaphore_non_empty = [Semaphore(0) for i in range(n)]
    nums = [Value('i', -2) for _ in range(n)]
    
    processes = [Process(target=producir, args=(semaphore_empty[i],semaphore_non_empty[i], nums[i], NPROD)) for i in range(n)]
    consumidor = Process(target = consumir, args=(semaphore_empty, semaphore_non_empty, nums, buffer, NPROD))
    for p in processes:
        p.start()
    consumidor.start()
    



