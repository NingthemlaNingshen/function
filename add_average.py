##Q1

def add(sum_mix):
    i=0
    sum=0
    while i<len(sum_mix):
        sum=sum+(int(sum_mix[i]))
        i=i+1
    print(sum,"is the total sum")
add(sum_mix=['5','0',9,3,2,1,'9',6,7])
add(sum_mix=['3',6,6,0,'5',8,5,'6',2,'0'])
add(sum_mix=[1,3,6,9,'4',8,'3'])

###Q2
def average(get_average):
    i=0
    sum=0
    count=0
    while i<len(get_average):
        sum=sum+get_average[i]
        count=count+1
        i=i+1
    a=sum//count
    print("sum is: ",sum,"  ","count is: ",count)
    print("average is: ",a)
average(get_average=[2, 2, 2, 2])
average(get_average=[1, 5, 87, 45, 8, 8])
average(get_average=[1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7])

##Q3
def num(l):
    i=0
    while i<len(l):
        b=str(l[i])
        j=0
        sum=0
        a=[]
        while j<len(b):
            sum=int(b[j])+sum
            a.append(sum)
            j=j+1
        i=i+1
    return a
print(num(l=[12,34,234,3671]))



##Q4
def num(a,b,c):
    sums=a+b+c
    count=3
    average=sums/count
    print(sums,average)
num(3,4,5)


##Q5
def num(user):
    i=1
    sum=0
    while i<=user:
        if(i%3==0 or i%5==0):
            sum=sum+i
            print(i)
        i=i+1
    print("the sum of all multiples of 3 and 5: ",sum)
user=int(input("enter your number: "))
num(user)

##Q6(h69ll79)
def charecter(a):
    i=0
    sum=0
    while i<len(a):
        if a[i]=="e" or a[i]=="o":
            b=a[i].upper()
            sum=sum+ord(b)
            print(ord(b),end="")
        else:
            print(a[i],end="")
        i=i+1
    print()
    print("Total of the ord = ",sum)
charecter( "hello")

##Q7(h15ll16)
def charecter(a):
    i=0
    while i<len(a):
        if a[i]=="e" or a[i]=="o":
            b=a[i].upper()
            c=ord(b)
            d=str(c)
            j=0
            sum=0
            while j<len(d):
                sum=sum+ int(d[j])
                j=j+1
            print(sum,end="")

        else:
            print(a[i],end="")
        i=i+1
charecter( "hello")