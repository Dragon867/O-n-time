def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("When n is ",n,"iterations = ",iteration)
OnTime(10)
OnTime(20)
OnTime(40)
print("With every n the time taken and the iteration will increase")