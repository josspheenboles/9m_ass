fornt=['html','css','js','anglure']
back=['c++','java','php','Bash','python']
courses=[]
# courses.extend(fornt)
# courses.extend(back)
print(fornt,back,fornt+back,sep='\n')
print(fornt*3)
"""
# name='ali'
# print(name[0:])
#array? task1 lab 12
#List collection of values of different  datatype
ml=[1,11]#,1.1,1+2j,"sdsdsd",[],(),{},True]
# ml[0]='ten'
# ml.pop(0)
# ml.remove(1.1)
# ml.remove(1)
# ml.append(10)
ml.insert(2,10)
print(ml)
# print(ml,type(ml),len(ml))
# print(ml[4:1:-1],ml.count(1))
# for value in enumerate(ml):
#     print(value,type(value))

num=eval(input('Enter number'))
# if(num.isdigit()):
#     num=int(num)

print(num,type(num))

for x in range(1,13,1):
    if(x==3):
        continue
    print(x)
else:#last iteration done
    print('else')




# while condirion:
#     body
count=1
while count<=3:
    print('hi os')
    count+=1

for x in range(1,13,2):
    print(x)

# range([start=0],end,[step=1])
months=range(1,13,1)#1,...11
print(months)
for month in months:
    print(month)

fname='mostafa'
index=0

for varname in fname:
    print(varname,index)#fname.index(varname))#,type(varname))#
    index+=1
for char in enumerate(fname):#[(0,m),(1,o)...(6,a)]
    print("index:",char[0],"letter:",char[1])

x=2
if x==2:
    print('two')


fname='mostf'
lname='ali'
print(fname.index('o'))
print(lname.find('a'))
print(fname+' '+lname)
print(fname*3)

x,y=10,20
x,y=y,x#x,y=20,10


# temp=x
# x=y
# y=temp
#print(values....,sep=' ',end='\n')
print(x,y,'one',sep='===>',end=' ')
print('plaplapl')


name='First name :{fname} \nLast Name:{lname} {lname}'
print(name.format(lname='ahmed',fname='ali')    )

print(name.format('ali','ahmed','ahmed'))
print(name.format('ahmed','ali','ahmed'))

name='mostafa aLi' #array of char
x='sd'
if(x.isdigit()):
    int(x)
else:
    print('invalid number ')

print(name,name.capitalize(),name.lower())
name=(name.replace('a','@'))
print(name.count('af'))
print(name)


name='mostafa' #array of char
print(name[0],name[-3])
#slicing    [start=0:end=length:step=1]
print(name[:5])
print(len(name))
print(name[4:1:-1])#4,3,2
#print(name[7])

print(min(1,2,3.3,4004,5995))

x,y,z=1,5.5,'ali' #unpacking sequnce
print(type(x),type(y),type(z))


x=1+2j
y=3+4j
print(type(x),x)
print(x+y)

#1='' 1=none 1=[] () {} False 0
#Falsy values ===>None,False,0,'',[],{},()
print(0 and 1)#1 and 3

x='A'
print(int(x))

x=1
print(type(x))
x=1.1
print(type(x))
x='dd'
print(type(x))
x=True
print(type(x))

X='one'
print(x,X)



#single line comment
print('leve1')#level1
if(True): #level1
    print('evel2')#level2
else:#level1
    if(True):
        print('level3')#
    print('leve;2') #level2
print('level1')

#string
x='sdsds'
y="sdssd"
z='''
line1
line2
'''

line1 
line2
"""