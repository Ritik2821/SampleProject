st="a4b3z1"
ans1=""

for i in st:
    if i.isalpha():
        x=i
    else:
        ch=int(i)
        ans1+=x*ch
print("Expand String is --->",ans1)

s="aaaabbbccz"
ans2=""
prev=s[0]
ans=""
c=1
i=1
while i< len(s):
    if s[i]==prev:
        c+=1
    else:
        ans2+=prev+str(c)
        prev=s[i]
        c=1
    i+=1
print("Compressed String--->",ans2)


