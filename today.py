



n=int(input())
list1 = [n]
while n>-1:
    n=int(input())
    list1.append(n)
    if n==0:
        #put list1 reverse in list2
        list2=list1[::-1]
        #remove index 0 (first element or etc)
        list2.remove(0)
        #printing the list using * operator separated
        #print(*list2)
        # print in new line
        print(*list2,sep="\n")
        break