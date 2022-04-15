import random
l=[]
l1=[]
c=0
#n=int(input("enter no"))
cows=0
bulls=0
def makeno():
    while len(l1)<5:
          x=random.randrange(0,9)
          if x not in l1:
             l1.append(x)
    print(l1)
    # if len(l1)>len(set(l1)):
        # l1.clear()
makeno()
#for i in range(4):
# n=int(input("enter no"))
lives=10
for i in range(lives):
    # l.append(i)    

    # print("enter an element to insert")
    n=int(input("enter guessing no = ")) 
    p=int(input("enter position no = "))
#for n  in l1:
    #if n==l1[p]:
    if n in l1 and n==l1[p]:
       l.insert(p,n)
       print("it will return bulls",l)
    if len(l1)==len(l):
       break
    elif n in l1 and n!=l1[p]:
       print("number is correct but position is not")

        # lives-=1

    elif n not in l1:
       print("number is not correct")
    else:
       print("congratulation you are winner")
#if len(l1)==len(l):
#    print()
#else:
 #  print("oops you are the looser")


#if l1==bulls:
  #  print(")     
                      
                           

    #       if l1==l:
    #          cows+=1
    #          print("congratulation",n,"You are the winner") 
    #       else:
    #          print("opps you are looser") 
    #    else:
    #        print("bulls count") 
    # else:
    #     print("it will not return bulls")                   
   


    
                      
                


  