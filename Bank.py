#(name:Odai afif)

#Question 1:(A)
l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
dictionary=dict(zip(l1,l2))
print(dictionary)

#Questaion 1:(B)
x=int(input("enter the number:"))
def fact(x):
    f=1
    if(x<0):
        return"error number"
    elif(x==0 or x==1):
        return 1
    elif(x>1):
        for i in range(1,x+1):
            f=f*i
        return f
print("fact",fact(x))

#Questaion 1:(c)
l=['Network','Bio','programming','physics','Music']
for i in range(len(l)):
    if l[i].startswith('B'):
        print("the items that sarts with B:",l[i],"index:",i)

#Questaion 1:(D)
l2=[0,1,2,3,4,5,6,7,8,9,10]
l3=[1,2,3,4,5,6,7,8,9,10,11]
d=dict(zip(l2,l3))
print(d)

#Questaion 2:
b=list(input("enter binary nummber"))
sum=0
b.reverse()
for i in range(len(b)):
    if b[i]=="1":
     sum+=2**i
    else:
        sum+=0
print(sum)

#Questions 3:

import json
questions={}
marks=0
num=0
f=open("question.txt",'r')
questions=json.load(f)
f.close()

name=input("Enter your name: ")
for q in questions.keys():
    print("Question",num,": ",q)
    ans=input("The answer is: ")
    if ans.upper() == questions[q].upper():
        marks+=1
        print("Correct")
    else:
        print("Wrong")
    num+=1
result={name:marks}
m=open("marks.txt",'w')
result=json.dump(result,m)
m.close()

#Questaion 4:
class Bank:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if value > self.balance:
            print(False, "money not enough")
        else:
            self.balance -= value

    def transfer(self, account, value):
        if value > self.balance:
            print(False, "money not enough")
        else:
            self.balance -= value
            account.deposit(value)
    def __str__(self):
        return (str(self.account) + "\n" + str(self.balance))

account1 = Bank("Bank Account", 1000)
account2 = Bank("Bank Account", 500)

account1.transfer(account2, 200)

print(account1)
print(account2)