# with open("knowledge.txt","r") as f,  open("vector.txt","w") as v:
with open("knowledge.txt", "r") as f, \
     open("vector.txt", "w") as v:
    lis=[]
    c=0
    for line in f:
        c+=1
        if c%2!=0:
            lis.append(line.strip())
        else:
            lis.append(line.strip())
            s=" ".join(lis)

            v.write(s+"\n")
            lis=[]
    user=input("enter input:").lower()
    v.flush()
    with open("vector.txt", "r") as vr:
        maxi=0
        s=""
        for i in vr:
            m=i.lower().split()
            c=0
            for j in m:
                if j in user.split():
                    c+=1
            if c>maxi:
                maxi=c
                s=i
        print(s)

            

        
        
            # s=" ".join(lis)
        
    # for i in lis:
    #     s="".join(i)
    #     v.write(s.join(" ",))
        

