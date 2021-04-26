dictionary={1:10,2:20,3:30,4:40,5:50,6:60}
print('dictionary:',dictionary)
print('key\t','value\t','item')
for key in dictionary:
    print(key,'\t',dictionary[key],'\t',key)


lista=['red','green','blue']
Listb = ['#FF0000','#008000', '#0000FF']
x=dict()
for i in range (len(lista)):
    x[lista[i]]=Listb[i]
print(x)