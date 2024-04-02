class Human:
    def __init__(self,name):
        self.__name=name

    def setname(self, name):
        self.__name = name

    def getname(self):
       return self.__name

    @property
    def Name2(self):
        return self.__name
    @Name2.setter
    def name(self,name):
        self.__name=name
    def __str__(self):
        return f'{self.__name} Object of Human'
    def __len__(self):
        return len(self.__name)
class Employee(Human):
    #class variable
    count=0
    def __init__(self,id,name):
        #instance varaibles
        self._id=id
        # self.__name='test'
        super(Employee,self).__init__(name)
        # self.name=name
        Employee.count+=1
        # print(self.count)

    def eat(os):
        print('eat')


    @classmethod
    def makefualt(cls):
        cls.count

    @staticmethod
    def mesuretemp(temp):
        print(f'static')


