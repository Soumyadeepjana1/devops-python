age = int(input("enter your age: "))

if (age >= 18):
    if age >= 80:
        print("you are eligible for senior citizen discount")
    else:
        print("you are eligible for voting")
else:
    print("you are not eligible for voting")