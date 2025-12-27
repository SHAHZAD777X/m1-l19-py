def avgfun(num):
    list1=list(num)
    sum=0
    for x in list1:
        sum=sum+x
    return sum

n=(12,67,98,45,56,23,66,57,89,63)
print("Tuple:",n)
print("Average:",avgfun(n)/len(n))