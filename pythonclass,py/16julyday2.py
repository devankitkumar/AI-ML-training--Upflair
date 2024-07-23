#int   , float,
#data type
##        string

# st ="upflairs"
# print(st)
# print(st[2])
# print(st[-6])
# print(st[4:7])
# print(st[:7])  #strating default called as 0
# print(st[4:])   #stopping ==end
# #print([starting]:[stopping]:[jump])
# print(st[::1])
# print(st[::2])

# st="upflairs"
# print(st.upper())  #functions built in or inbuilt

st="UPFLAIRS PVT LTD JAIPUR"
print(st.lower()) 
#title
#capitalize
#count
#len
print(len(st))  #number of characters counted
print(st.count('J')) # specific characters can be counted in the list
print(st.find('P')) #index of the first occurence
#how can be find the index of the second chractrer p
print(st.find('JAIPUR')) #wherever the first time jaipur is written it will be printing the charcaters
print(st.split())  #bydefault split the function with the help of commas
print(st.replace(',',''))
print(st.replace('UPFLAIRS','flipkart'))
print(st.endswith('R'))
print(st.startswith('u'))


##data type ___boolean ___


# var1 =True
# var2= False
# print(var1, var2)
# print(type(var1), type(var2))
# # var = False
# #print(var)

#list
ls= [10,20,30,4.5,50,80.4,True]  #single variable stored multiple item
print(ls)
print(type(ls))
print(ls[-4])
print(ls[-4:-7])

lis= [10,20,30,40,50,60,70]
print(lis[1:2])

print(student_name)

#manshi
# student_name.append('manshi')
print(student_name)
student_name.pop() #if we give the index position then it will remove the particular element from the lsit
print(student_name)  #it will remove by default by the last position remove the last element

