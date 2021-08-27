n=int(input())
for i in range(0,n):
    rating=int(input())
    if(rating>=2000):
        print(1)
    elif(rating >= 1600) and (rating < 2000):
        print(2)
    else:
        print(3)
