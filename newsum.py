def fun(s,k):
    s=sorted(s)
    print(s)
    if len(s)>=2 and sum(s)>=k:
        i=0
        j=len(s)-1
        while i!=j:
            if s[i]+s[j]==k:
                return True
            elif s[i]+s[j]>k:
                    j-=1
            else:
                i+=1
    return False
s = input('Enter your list: ')
s = [int(x) for x in s.split(',')]
k=int(input("Enter The sum value: "))
a=fun(s,k)
print(a)
