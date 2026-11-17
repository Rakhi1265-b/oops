f=open("transaction","r")
m=open("clean","w")
# print(f.readlines())
# f.seek(0)
# print(f.tell())
k=f.readlines()
for i in k:
    if int(i)<=0:
        print("Invalid Transactions")
    else:
        print(i)
# m=open("clean","w")

        m.write(i)

        

# for i in f:
#     print([i])

