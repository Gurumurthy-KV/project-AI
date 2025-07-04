def selectionsort(a):
    n=len(a)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
        print(a)
a=[70,30,40,20,60,50,10,65,75,85,80,]
print("before sorting:",a)
selectionsort(a)
print("after sorting:",a)