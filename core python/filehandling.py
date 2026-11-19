# # f=open("test.txt","w")
# # f.write("hello world\n")
# # f.writelines(["how are you\n","whats up\n"])
#
# # f=open("test.txt","rb")
# # print(f.read())
# # f.seek(0)
# # print("----------------------------")
# # print(f.readline())
# # print(len(f.readlines()))
#
# # with open("test.txt","r") as f:
# #     print(f.read())
# #     f.seek(0)
# #     print(f.closed)#false
# #     print(f.readline())
# # print(f.closed)#true
#
#
# # class A:
# #     def __init__(self,fn,m):
# #         self.fn = fn
# #         self.m = m
# #     def __enter__(self):
# #         print("entering")
# #         self.f=open(self.fn,self.m)
# #         return self.f
# #     def __exit__(self, a,b,c):
# #         print("exiting")
# #         self.f.close()
# # obj=A("test.txt","r")
# # with obj as f:
# #     print(f.read())
# # print(f.closed)
# from contextlib import contextmanager
# @contextmanager
# def fun(fn,m):
#     print("enter")
#     f=open(fn,m)
#     try:
#         yield f
#     finally:
#         print("exiting")
#         f.close()
# with fun("test.txt","r") as f:
#     print(f.closed)
# print(f.closed)
#

with open("transaction",'r') as f, \
    open("clean.txt","w") as c, \
        open("error.txt","a") as e:
    headers=f.readline()
    total_line=0
    clean_line=0
    error_line=0
    total_amount=0
    category_amount={}
    for line in f:
        try:
            total_line+=1
            u,amount,cat=line.split(",")
            if u=='' or amount=='' or cat=='':
                raise ValueError("values cannot be empty")
            amount=int(amount)
            if amount<0:
                raise ValueError("amount cannot be negative\n")

            c.write(line)
            clean_line+=1
            total_amount+=amount
            category_amount[cat]=category_amount.get(cat,0)+amount
        except ValueError as err:
            error_line+=1
            e.write(f"{line} -> {err}\n")
#     print(total_amount)
#     print(category_amount)
#     print(error_line)
#     print(clean_line)
#     print(total_line)

with open("report.txt","w") as report:
    report.write(f"Error lines = {error_line}\n")
    report.write(f"clean lines {clean_line}\n")
    report.write(f"{total_line}\n")
    report.write(f"{total_amount}\n")
    report.write(f"{category_amount}\n")