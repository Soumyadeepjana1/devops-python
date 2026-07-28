def odd_even():
    n = int(input("enter a value to che number is odd or even: "))
    if n %2 == 0:
        print("number is even")
    else:
        print("number is odd")
    return(n)
odd_even()