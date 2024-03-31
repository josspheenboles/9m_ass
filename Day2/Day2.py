import myexperiance.mymath
from myexperiance.mymath import pi as modulepi
pi=3.1455565
print(pi)
print(modulepi)

# print(mymath.pi)
# mymath.amth.sum(1,2)
# #open
# f1=open('asd.txt','a')
# f1.write('sara sayed\n')
# # if(f1.readable()):
# #    # for line in f1:
# #    #     print(line)
# #    print(f1.readlines())
# #    # print(f1.read(2))
# #    # print(f1.read())
# #    # # print(type(s))
# #    # print(f1.readline())
# #    # print(f1.readline())
# #    # print(f1.readline())
# #close
# f1.close()
#
# # print(type(f1),f1)
# # #write
# # if(f1.writable()):
#     # f1.write('line1\nline2')
#     lines=['line1\n','line2']
#     f1.writelines(lines)
# import sys
# num=eval(input('enter num'))
# num2=eval(input('enter num2'))
# try:
#     # int('a')
#     print(num/num2)
# except ZeroDivisionError:
#     print('/0')
# except:
#     print(sys.exc_info()[1])
# else:
#     print('else ok')
# finally:
#     print('finally')
 # print('zero deivision')
# d={'id':10,'name':'ali'}
# for key in d:
#     if(key=='x'):
#         print(d['x'])
# else:
#     print('key not found')
# 'one' in [1,2.2,True]
# (1,'2') in d.items()
# #x=1
# for z in range(1,10):
#     x='ok'
#     print('ok')
# print(x)
# x=1#global scope
# def fun(): #scope
#    x='fun'#10
#    def fun2():
#        # x='fun2'
#        # nonlocal  x#accsess first local var & modified
#        global  x#accsess global var & modified
#        print(x)#2
#        x=10
#    fun2()
#    print(x)#3
# print(x)#1
# fun()
# print(x)
# min(1,2,3,5.7,834,43)
# '{nam} {id}'.format(id=1,nam='ali')
# def myformate(**arg):
#     pass
#     # print(arg,type(arg))
# myformate(k1='asas',k2=2323)
# def mymin(*var):
#     pass
# t=(1,2,3,4,5,6)
# mymin(1,2,3,4,5,6))#packing (1,2,3,4,5,6)
# x=1
# x=1.1
# def funcationame(val1,val2):
#     print('body')
# print(funcationame)
# def funcationame():
#     print('body')
# print(funcationame)
# funcationame(1,2)
# funcationame(1,2)
# funcationame(1.2,22.2)
# funcationame('s',22.2)

# students={
#     '1':{'id':1,'name':'ahmes','courses':('html','css')},
#     '2':{'id':2,'name':'alkasem','courses':('php','java')}
# }
# for key in students:
#     print(students[key]['courses'])
# students['2']['courses']
# name='mosatfa'
# print(name[::-1])#start=0 end=length
#Tuple --->collection of values differernt data types
#imputable list ()--->optional
# mt=1,1.1,True,[3,45],(),{},'os'
# mt[0]='ten'
# mt=('pd',[])#(ref1,ref2)
# mt[1].append('plplapl')
# # mt[0]= mt[0].replace('p','$')
# print(type(mt),mt)
# tfront=('html','css','js')#1000
# tback=('php','python','java')
# print(tfront+tback)
# print(tfront*3)
# tfront=(tfront*3)#2000
#set-->collection of differernt datatype
#{val1,val2} imutable ordered
# mset={1,5,6,3,2}
# print(type(mset),mset)
#dict collection of values diff types
#key:value
# student={'id':1,'name':'ahmed kamal','id':100}
# student['dept']='os'
# student['id']=10
# print(student,type(student))
# print(student['id'])
# for key,value in student.items():
#     print(key,value)#,student[x])
# t=(1,1.1,'fff',9232093,'kasem')
# x,y,*z=t
# print(x,y,z)
# l = []
# for n in range(1,11,1):
#     if(n%2==0):
#         l.append(n)
# # l=list(range(2,11,2))
# # l=[value loop  condition]
# # l=[n for n in range(1,11,1) if(n%2==0)]
# # print(l)
# largel=[]
# for tablenumber in range(1,4):#1
#     sl=[]
#     for val in range(1,tablenumber+1):#[1]
#         sl.append(val*tablenumber)
#     largel.append(sl)
# # largel=[[val*tablenumber for val in range(1,tablenumber+1)]
# #         for tablenumber in range(1, 4)]
# [    [val*tablenumber for val in range(1,tablenumber+1)
#       ]
#       for tablenumber in range(1,4)
# ]