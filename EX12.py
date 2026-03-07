a="hello,how are you?"
b=a.split();
c={}
print("after split",b)
for i in range(len(b)):
    c[i]=b[i]
print(c)
print("$".join(b))
