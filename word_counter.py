text = "the quick brown fox the lazy dog the fox runs the dog sleeps the quick fox"
a={}
text=text.lower().split(" ")
for i in text:
    if i not in a:
         a[i]=1
    elif i in a:
        a[i]+=1

keys=[]
a=a.items()
a = sorted(a, key=lambda x: x[1],reverse=True)
for i in a[0:5]:
    a,b=i
    print(f"{a} встретилось {b} раз")