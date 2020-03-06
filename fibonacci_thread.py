import time
import sys
from threading import Thread


def rec_fib(n):
    if n > 1:
        return rec_fib(n - 1) + rec_fib(n - 2)
    return n

inicial = time.time()
if __name__ == '__main__':

    n = int(sys.argv[1])

    # Sem thread
    print("tempo inicial:", inicial)
    # print("res: ", rec_fib(n))
    # final = time.time()
    # print("tempo final:", final)
    # print("tempo gasto: ", final - inicio)

    # Com thread
    res1 = Thread(target=rec_fib, args=[rec_fib(n)])
    print("res1: ", res1)
    res2 = Thread(target=rec_fib, args=[rec_fib(n*2)])
    print("res2: ", res2)
    res3 = Thread(target=rec_fib, args=[rec_fib(n*3)])
    print("res3: ", res3)
    final = time.time()
    print("tempo final:", final)

    print("tempo gasto: ", final - inicial)
