# vrni seznam premešanih ševil od 1 do 10

import random

if __name__ == '__main__':
    e = int(input("Vnesi število:"))
    premetanka = []
    for number in range(e):
        premetanka.insert(random.randint(0, 10), number)

    print(premetanka)
