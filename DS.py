# # for i in range(1,6):
#     n=input("enter a name:")
#     a=int(input("enter the age:"))
#     if a>20:
#         with open("std.txt","a") as f:
#             f.write(f"{n},{a}")
#     print("student details saved")
# 
# 
# 
# 
# from collections import deque
# queue=deque(["Anu","Ammu","Arya"])
# queue.append("John")
# print(queue)
# print(queue.popleft())



# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

#         first=node(10)
#         second=node(20)
#         third=node(30)

#         first.next=second
#         second.next=third
       
        


def selsort(myarry,r):
    for x in range(r):
        min=x
        for y in range(x+1,r):
            if myarry[y]<myarry[min]:
                min=y
        myarry[x],myarry[min]=myarry[min],myarry[x]
mylist=[1,33,45,67,23]
r=len(mylist)
selsort(mylist,r)
print(mylist)


