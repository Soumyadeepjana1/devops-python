def show(n):
    if n >10:
        return
    print(n)
    show(n + 1)
    
show(5)


def show(n):
    if n > 10:
        return
    print(n)
    show(n + 1)

show(5)

def king(j):
    if  j == 1:
        return
    print(j)
    king(j-1)
king(5)


def jod(j):
    if j == 10:
        return
    print(j)
    jod (j +1)
jod(1)

def cobra(n):
    if n <= 10:
        return
    print(n)
    cobra(n -1)
cobra(20)


def dog(n):
    if n > 100:
        return
    print(n)
    dog( n + 1)
dog(1)