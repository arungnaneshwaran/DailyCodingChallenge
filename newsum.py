def fun(s,k):
	s=set(s)
	s=list(s)
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

s=int(list(input("Enter the list: ")))
k=int(input("Enter The sum value: "))
a=fun(s,k)
print(a)