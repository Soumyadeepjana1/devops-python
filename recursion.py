# def show(n):
#     if n >10:
#         return
#     print(n)
#     show(n + 1)
    
# show(5)


# def show(n):
#     if n > 10:
#         return
#     print(n)
#     show(n + 1)

# show(5)

# def king(j):
#     if  j == 1:
#         return
#     print(j)
#     king(j-1)
# king(5)


# def jod(j):
#     if j == 10:
#         return
#     print(j)
#     jod (j +1)
# jod(1)

# def cobra(n):
#     if n <= 10:
#         return
#     print(n)
#     cobra(n -1)
# cobra(20)


# def dog(n):
#     if n > 100:
#         return
#     print(n)
#     dog( n + 1)
# dog(1)




# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fac(n - 5) * n
# print(fac(10))


# def odd_even(n):
#     if n == 0:
#         print("stp")
#         return
    
#     if n % 2 == 0:
#         print("number is even",n)
#     else:
#         print("number is odd",n)
#     odd_even(n  - 1)
# odd_even(10)


# def nat(n):
#     if n == 0:
#         return 0
#     return n + nat(n-1)
# print(nat(7))


# def n_f(i):
#     if i > 10:
#         return
#     print(i)
#     n_f(i + 1)
    
# n_f(1)


# def p(i):
#     if i < 1:
#         return
#     print(i)
#     p(i-1)
# p(10)


# def sum_di(n):
#     if n > 10:
#         return 1
#     return sum_di(n+1)+ n
# print(sum_di(1))


# def cal(n):
#     if n == 0:
#         return 0
#     return(cal(n-1)+n)

# print(cal(5))

def print_list(lst, idx=0):
    if idx == len(lst):
        return

    print(lst[idx])
    print_list(lst, idx + 1)

print_list(["apple", "banana", "cherry"])

