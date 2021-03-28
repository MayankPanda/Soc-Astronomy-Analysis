l=["AB","A","BC","ABCD","ABC","C","ABCDEFG","SS","FGH","HGKK","C"]
print("Unsorted List")
print(l)
i=0
while i<(len(l)-1):
    j=i+1
    #print("PRINTING J")
    #print(j)
    #print("CHECK")
    while j<len(l):
        #print("CHECK INNER")
        #print(j)
        if len(l[i])>len(l[j]):
            #print("CHECKIF")
            temp=l[j]
            l[j]=l[i]
            l[i]=temp
        j=j+1
    i=i+1
print("Sorted List")
print(l)


