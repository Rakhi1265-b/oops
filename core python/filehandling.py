with open("transaction","r") as f,open("clean.txt","w") as m,open("error.log","w") as n , open("report.txt","w") as t:
# print(f.readlines())
# f.seek(0)
# print(f.tell())
    k=f.readlines()
    t.write("Toatl:")
    t.write(" \n")

    valid=[]
    invalid=[]
    totals=0
    for i in k:
        t.write(i)
        if int(i)<=0:
            print("Invalid Transactions")
            n.write(f"the Transactions should be above 0 and your transaction is {i}")  
        else:
            print(i)
            totals+=int(i)
    # m=open("clean","w")
            valid.append(i)
            
            m.write(i)
    t.write("\nValid:")
    t.write(" \n")
    for j in valid:
        t.write(j)
    t.write("\nToatl:")
    totals=str(totals)
    t.write(" \n")

    t.write(totals)

            

    # for i in f:
    #     print([i])

