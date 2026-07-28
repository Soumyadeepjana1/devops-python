# def avj_def(a,b,c):
#     sum = (a+b+c)/3
#     print(sum)
#     return(sum)
# avj_def(4,12,16)




# def find_len(b):
#     print(len(b))
#     print(type(b))
#     print(b)
#     return(len(b))
# find_len([1,4,5,6,8])

# find_len((12,13,15,16,17))


# def fact(n):
#     i = 1
#     fac = 1
#     while i <= n :
#         fac = fac *i
#         i = i + 1
#     print(fac)
#     return fac
# fact(14)

# fact(5)


def usd_inr(b):
    c = str(input("what you want to conver usd or iner: "))
    if c =="usd":
        print(b * 93)
    elif c == "inr":
        print(b / 93)
    else:
        print("plese enter right number")
    return (c)
usd_inr(1000)