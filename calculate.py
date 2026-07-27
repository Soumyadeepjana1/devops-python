# def cal_cul():
#     for i in range(1,10):
#         if  i % 2 == 0:
#             print("number is even:",i)
#         else:
#             print("number is odd:",i)
            
def vote_ing():
    for i in range(1,100):
        if i >= 18 and i <= 50:
            print("you are eligible for voting:",i)
            
        elif i < 18:
            print("you are teeager you are not eligible for votting:", i)
        else:
            print("you are  too old you are not eligible for votting",i)
vote_ing()