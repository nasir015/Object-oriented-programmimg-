# class

class animation :
    pass


ob1 = animation()
ob2 = animation()

ob1.name = "mina"
ob1.age= 10
ob2.name = "statistics"
ob2.age= 20

print(ob1.name)
print(ob1.age)
print()
print(ob2.name)
print(ob2.age)





class animation :
    series = "Tv series"  #! class variable


ob1 = animation()
ob2 = animation()

ob1.name = "mina"
ob1.age= 10
ob2.name = "statistics"
ob2.age= 20

print(ob1.name)
print(ob1.age)
print(ob1.series)
print()
print(ob2.name)
print(ob2.age)
print(ob2.series)


# __init__()/ constructor
'''class er vitore kono kichu duke tahole ta recive korbe'''
class animation :
    series = "Tv series"#! class variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10)
ob2 = animation("statistics", 20)


print(ob1.name)
print(ob1.age)
print(ob1.series)
print()
print(ob2.name)
print(ob2.age)
print(ob2.series)



# self peramiter

class animation :
    series = "Tv series"#! class variable
    def __init__(self,name,age):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10)
ob2 = animation("statistics", 20)


print(ob1.name)
print(ob1.age)
print(ob1.series)
print()
print(ob2.name)
print(ob2.age)
print(ob2.series)



# method

class animation :
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

ob1.folafol()
ob2.folafol()
ob3.folafol()


# print(ob1.name)
# print(ob1.age)
# print(ob1.series)    #! function er baire print koraiche 
# print()
# print(ob2.name)
# print(ob2.age)
# print(ob2.series)


# modify object priperties


class animation :
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

ob1.age = 50  #! poriborton kora hoiche 

ob1.folafol()
ob2.folafol()
ob3.folafol()


# delete object properties

class animation :
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

del ob1.age  #! aikhane object ob1 er age variable ke  delete kore dewa hoiche 

# ob1.folafol() #! jodi ob1 ke comment kore dewa hoy tahole baki duida print kore dekhabe 
ob2.folafol()
ob3.folafol()


# delete object 

class animation :
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

del ob1

ob1.folafol()
ob2.folafol()
ob3.folafol()




#!                                buld in method 

# __doc__

class animation :
    "this is a animation class"
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''

print(animation.__doc__) #! ai class ta ki ki jonno class ta create kora hoiche ta bornona korar jonno ai method use kora hoy 


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

ob1.folafol()
ob2.folafol()
ob3.folafol()


# __dict__

class animation :
    def __init__(self,name,age,series):  #!self peramitar er jaygay  jekono name dewa jabe tobe ta object hisebe kaj korbe
        self.name = name
        self.age = age
        self.series = series
    def folafol(self):
        print(self.name)
        print(self.age)
        print(self.series)
'''aikhane self holo object recive korbe and name,age holo peramiter '''


ob1 = animation("mina", 10, "tv series")
ob2 = animation("statistics", 20, "tv series")
ob3 = animation("book", 40, "tv series")

print(ob1.__dict__)  #! ai class ta diya object gulake dictionary akare print korabe 
print(ob2.__dict__)
print(ob3.__dict__)

ob1.folafol()
ob2.folafol()
ob3.folafol()




# !                   - - - - - - - - - - - - - - - -method


#! instance method

class info:
    def __init__(self, name):
        self.name = name
    # instance method     object ke jodi pore abar call diya access newa hoy tahole seta instance method 
    def show(self):            # #ob1 diye akta object create kkora hoiche and aitar modde value diye dewa hoiche init function aita recive korche  porobortite ob1 call diche def  show re and aita print kore diche 
        print(self.name)
    def name_show(hey):
        print(hey.name)

ob1 = info("nasir")

ob1.show()

ob1.name_show()


#!  class method    
"""kono object create na kore class access kora jayna jodi korte hoy 
tahole class method er sahjjo newa lagbo"""

class info:
    def __init__(self,name):
        self.name = name
    def output(self):     #! aikhane class er maddome call diche 
        print(self.name)    
    @classmethod
    def output_print(cls):
        print("nasir")

ob1 = info("class method ")

ob1.output()

info.output_print()



#! object er maddome call dite hole poddoti

class info:
    def __init__(self,name):
        self.name = name
    def output(self):
        print(self.name)    
    @classmethod
    def output_print(cls):
        print("nasir")

ob1 = info("class method ")
# ob1.output()

info.output_print()

ob1.output_print()

#! indtant method e object carry kore but class method e class carry kore 




# Static method
'''jodi amon akta method toiri kora hoy jekhane kono object ba 
class thakbe na arokom method ke bola hoy static method 
'''
class faltu:
    @staticmethod
    def emnei():
        print("nasir")

faltu.emnei()




class info:
    def __init__(self,name):
        self.name = name
    def output(self):
        print(self.name)    
    @staticmethod           #! jokhon class diye call dewa hoy tokhon aitar modde @staticmethod dewa lagena jokhon object diya call dewa hoy tokhon aitar modde @staticmethod dewa lagbe 
    def output_print():
        print("nasir")

ob1 = info("class method ")
ob1.output()

info.output_print()

ob1.output_print()




#!              variable


# class variable

''''jodi method er baire kintu class er vitore 
kono variabke deglar kora hoy tahole take class variable bole
$$ ai method normally instance method and class method e access kora jay
kintu staticmethod e use kora jayna '''


class info:
    
    bangladesh = "amar desh"
    def __init__(self,name):
        self.name = name
    def output(self):
        print(self.name)
        print(self.bangladesh)    
    @classmethod
    def output_print(cls):
        print(cls.bangladesh)
    
    @staticmethod
    def amnetei():
        print("Allah")

ob1 = info("class method ")
ob1.output()

ob1.output_print()

info.amnetei()




# instance variable
'''object er sahajje kono kichuke akta variable er 
modde set korake instant variable bole
$$ ai variable normally instant method er sathe bebohito hoy '''

class info:
    
    bangladesh = "amar desh"
    
    def __init__(self,name):
        # instant variable
        self.name = name
    def output(self):
        print(self.name)
        print(self.bangladesh)    
    @classmethod
    def output_print(cls):
        print(cls.bangladesh)
    
    @staticmethod
    def amnetei():
        print("Allah")

ob1 = info("class method ")
ob1.output()

ob1.output_print()

info.amnetei()



#!                      inheritance 
'''dui ba totodik class er modde relation toiri kore
$$ 4 doroner inheritance ache 
1 single inheritance 
2 multiple inheritance
3 hiearirchical inheritance
4 multilevel inheritance'''

# single inheritance

class Doremon:
    def doremon(self):
        print ("i am doremon")
    def gadget(self):
        print("take gadget", end="\n\n")
''' aikhane duita object nobita and doremon,gadget. nobita Doremon 
class ke inheritance korche tar jonno nobita doremon 
class er sobgula object access kkorte parbe '''

class Nobita(Doremon):
    def nobita(self):
        print("i am sleeping")

doremon = Doremon
nobita =Nobita
nobita.gadget(1)



# multilevel inheritance

class Doremon:
    def doremon(self):
        print ("i am doremon")
    def gadget(self):
        print("take gadget", end="\n\n")

class Nobita(Doremon):
    def nobita(self):
        print("i am sleeping")

class Shizuka(Nobita):
    def sizuka(self):
        print("i am singging")

doremon = Doremon
nobita =Nobita
sizuka = Shizuka

nobita.gadget(1)
sizuka.gadget(1)


# hiearirchical inheritance

""" jodi dui ba totadic class jodi aktake 
inheritance kore tahole take hiearirhical inheritance bole  """

class Doremon:
    def doremon(self):
        print ("i am doremon")
    def gadget(self):
        print("take gadget", end="\n\n")

class Nobita(Doremon):
    def nobita(self):
        print("i am sleeping")

class Shizuka(Doremon):
    def sizuka(self):
        print("i am singging")

doremon = Doremon
nobita =Nobita
sizuka = Shizuka

nobita.gadget(1)
sizuka.gadget(1)




#!            multiple inheritance

class Doremon:
    def doremon(self):
        print ("i am doremon")
    def gadget(self):
        print("take gadget", end="\n\n")

class Nobita:
    def nobita(self):
        print("i am sleeping")

class Shizuka(Nobita,Doremon):
    def sizuka(self):
        print("i am singging")

doremon = Doremon()
nobita =Nobita()
sizuka = Shizuka()

# nobita.gadget(1)
sizuka.gadget(1)
sizuka.sizuka(1)



# super (build in method)

class Robot :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)

class Nasir:
    def __init__(self,name,age,food):
        self.name = name
        self.age = age
        self.food = food
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)
    def show_food(self):
        print(self.food)


robot = Robot("sofiya", 5)
nasir = Nasir("nasir",21, "rosmolai")


print("----- robot-------")
robot.show_name()
robot.show_age()

print("----- human-------")

nasir.show_name()
nasir.show_age()
nasir.show_food()




class Robot :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)

class Nasir(Robot):
    def __init__(self,name,age,food):
        self.name = name
        self.age = age
        self.food = food
    def show_food(self):
        print(self.food)


robot = Robot("sofiya", 5)
nasir = Nasir("nasir",21, "rosmolai")


print("----- robot-------")
robot.show_name()
robot.show_age()

print("----- human-------")

nasir.show_name()
nasir.show_age()
nasir.show_food()




class Robot :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def show_name(self):
        print(self.name)
    def show_age(self):
        print(self.age)

class Nasir(Robot):
    def __init__(self,name,age,food):
        super().__init__(name,age)
        self.food = food
    def show_food(self):
        print(self.food)

class Rayhan(Nasir,Robot):
    def __init__(self,name,age,food,animal):
        super().__init__(name,age,food)
        self.animal = animal
    
    def show_animal(self):
        print(self.animal)


robot = Robot("sofiya", 5)
nasir = Nasir("nasir",21, "rosmolai")
rayhan = Rayhan("rayhan",22,"noodles","kobutor")

print("----- robot-------")
robot.show_name()
robot.show_age()

print("-----nasir-------")

nasir.show_name()
nasir.show_age()
nasir.show_food()

print("-----rayhan-------")

rayhan.show_name()
rayhan.show_age()
rayhan.show_food()
rayhan.show_animal()


#!          import class 


# single class   # multiple calss

from frist_module import Robot as r
from frist_module import Nasir as n

robot = r("sofiya", 5)
nasir = n("nasir",20,"rosmolai")


robot.show_name()
robot.show_age()
print("----Nasir----")
nasir.show_name()
nasir.show_age()
nasir.show_food()



# Entir module

import frist_module as f

robot = f.Robot("sofiya", 5)
nasir = f.Nasir("nasir",20,"rosmolai")


robot.show_name()
robot.show_age()
print("----Nasir----")
nasir.show_name()
nasir.show_age()
nasir.show_food()



# Module into module

from frist_module import Robot as r
from frist_module import Nasir as n
from Secound_module import Rayhan

robot = r("sofiya", 5)
nasir = n("nasir",20,"rosmolai")
rayhan = Rayhan("rayhan",22,"rosmolai","kobutor")


print("----robot-----")
robot.show_name()
robot.show_age()
print("----Nasir----")
nasir.show_name()
nasir.show_age()
nasir.show_food()
print("----rayhan-----")
rayhan.show_name() ,rayhan.show_age(),rayhan.show_food(),rayhan.show_animal()




#!                nested class

# create nested class

class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name(self):  # aikhane Nasir class er vitore  rayhan class ke access kor a hoyeche 
            print(self.name)


nasir = Nasir("nasir")
rayhan = nasir.Rayhan("rayhan")

nasir.show_name()
rayhan.show_name()


# multiple nested class

class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name(self):  # aikhane Nasir class er vitore  rayhan class ke access kor a hoyeche 
            print(self.name)
    class Anas:
        def __init__(self,name):
            self.name = name
        def show_name(self):
            print(self.name)

nasir = Nasir("nasir")
rayhan = nasir.Rayhan("rayhan")
anas = nasir.Anas("anas")

nasir.show_name()
rayhan.show_name()
anas.show_name()


# multilevel nested class

class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name(self):  # aikhane nasir er vitor rayhan , rayhan er vitor anas , anas ke access korte hole ai poddoti use kora lage .
            print(self.name)
        class Anas:
            def __init__(self,name):
                self.name = name
            def show_name(self):
                print(self.name)

nasir = Nasir("nasir")
rayhan = nasir.Rayhan("rayhan")
anas = rayhan.Anas("anas")

nasir.show_name()
rayhan.show_name()
anas.show_name()



# inheritance in nested class

class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name(self):  
            print(self.name)

class Anas:
    def __init__(self,name):
        self.name = name
    def show_name(self):
            print(self.name)
    class Ramim:
        def __init__(self,name):
            self.name = name
        def show_name(self):
            print(self.name)

nasir= Nasir("nasir")
rayhan = nasir.Rayhan("rayhan")
anas = Anas("anas")
ramim = anas.Ramim("ramim")

nasir.show_name()
rayhan.show_name()
anas.show_name()
ramim.show_name()




class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name_nasir(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name_rayhan(self):  
            print(self.name)

class Anas(Nasir):
    def __init__(self,name):
        self.name = name
    def show_name_anas(self):
            print(self.name)
    class Ramim(Nasir.Rayhan):
        def __init__(self,name):
            self.name = name
        def show_name_ramim(self):
            print(self.name)

anas = Anas("anas")
ramim=anas.Ramim("ramim")


anas.show_name_anas()
anas.show_name_nasir()

ramim.show_name_ramim()
ramim.show_name_rayhan()





class  Nasir:
    def __init__(self,name):
        self.name = name
    def show_name_nasir(self):
        print(self.name)
    class Rayhan:
        def __init__(self,name):
            self.name = name
        def show_name_rayhan(self):  
            print(self.name)

class Anas(Nasir.Rayhan):
    def __init__(self,name):
        self.name = name
    def show_name_anas(self):
            print(self.name)
    class Ramim:
        def __init__(self,name):
            self.name = name
        def show_name_ramim(self):
            print(self.name)

anas = Anas("anas")
ramim=anas.Ramim("ramim")


anas.show_name_anas()
anas.show_name_nasir()
anas.show_name_rayhan()

ramim.show_name_ramim()
ramim.show_name_rayhan()




#!                   polymorphism
#!Method  overriding
class Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)

class Anas(Nasir):
    def __init__(self,name):
        self.name = name
    def show_name(self):        
        print(self.name)

nasir = Nasir("nasir")
anas = Anas("anas")

nasir.show_name()
anas.show_name()




class Nasir:
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print(self.name)

class Anas(Nasir):
    def __init__(self,name):
        self.name = name


nasir = Nasir("nasir")
anas = Anas("anas")

nasir.show_name()
anas.show_name()



# method overloading
#! diffrent method  (overloading)
""" ai method ta diffrent  take is carefully """
class profile():
    def name(self,frist,middle,last):
        if frist != None and middle != None and last != None:
            print(frist+" "+middle+" "+last)                     
        elif frist != None and middle != None:
            print(frist+" "+middle)
        else:
            print(frist)



profile.name(1, "nasir","uddin","pintu")




# !               Abstraction

# abstract
from abc import ABC , abstractmethod

class Nasir(ABC):
    def nasir_name(self):
        print("nasir")

class Pintu(Nasir):
    def pintu(self):
        print("pintu")
    def Uddin(self):
        print("uddin")

na = Nasir()
p= Pintu()

na.nasir_name()
p.pintu()
p.Uddin()


# abstractmethod

"""  abstractmethod toiri korar jonno ai method ke decorate 
kore dite hobe jei class ke decorate korbe oi 
class chaild class e rakhte hobe nahoy function error dekhabe ai function
faka rakhte hobe aita cheek korbe  ai function ta ki ai chaild class e ache naki nai  
multiple abstructmethod  method o use kora jabe same menner """

from abc import ABC , abstractmethod

class Nasir(ABC):
    @abstractmethod
    def nasir_name(self):
        pass  

class Pintu(Nasir):
    def nasir_name(self):
        print("nasir do work")
    def pintu(self):
        print("playing football")
    def Uddin(self):
        print("playing cricket")


p= Pintu()

p.nasir_name()
p.Uddin()
p.pintu()




# concrete method

"""jesob class e abstractmethod er pore kono function thake tahole seta abstruct class hobe
ai class sob class e thakte hobe amon kono dorkar nai """

from abc import ABC , abstractmethod

class Nasir(ABC):
    @abstractmethod
    def nasir_name(self):
        pass  
    #concrete method
    def rayhan (self):
        print("I am rayhan")

class Pintu(Nasir):
    def nasir_name(self):
        print("nasir do work")
    def pintu(self):
        print("playing football")
    def Uddin(self):
        print("playing cricket")


p= Pintu()

p.nasir_name()
p.Uddin()
p.pintu()



# Encapsulation

""""specific data specific kichu manuser modde share 
korar je maddom seitai hole incapsulation atake data hiding o bole """


#!  Public data 
# access

class Nasir:
    def __init__(self):
        self.name = "nasir"
        self.no = 10
    def show(self):
        print(self.no)

class Rayhan(Nasir):
    def show_no(self):
        print("book name of rayhan : ",self.no)

class Anas(Nasir):
    def show_no(self):
        print("book name of anas : ",self.no) 

nasir = Nasir()
rayhan = Rayhan()
anas = Anas()

nasir.show()
rayhan.show_no()
anas.show_no()


# modify public data 


class Nasir:
    def __init__(self):
        self.name = "nasir"
        self.no = 10
    def show(self):
        print(self.no)

class Rayhan(Nasir):
    def show_no(self):
        print("book name of rayhan : ",self.no)

class Anas(Nasir):
    def show_no(self):
        print("book name of anas : ",self.no) 

nasir = Nasir()
rayhan = Rayhan()
anas = Anas()
""" modify korar jonno jei class er vitore chane korbe sei class 
er object.variable er name = () tarpor poriborton hobe  """

nasir.show()            
nasir.no= 50
nasir.show()
rayhan.show_no()
anas.show_no()



# Protected (_)


class Nasir:
    def __init__(self):
        self.name = "nasir"
        self.no = 10
        self._no = 20
    
    def show(self):
        print(self.no, self._no)

class Rayhan(Nasir):
    def show_no(self):
        print("book name of rayhan : ",self.no)

class Anas(Nasir):
    def show_no(self):
        print("book name of anas : ",self._no) 

nasir = Nasir()
rayhan = Rayhan()
anas = Anas()
""" modify korar jonno jei class er vitore chane korbe sei class 
er object.variable er name = () tarpor poriborton hobe  """

nasir.show()            
nasir.no= 50
nasir.show()
rayhan.show_no()
anas.show_no()



# modify protected data
class Nasir:
    def __init__(self):
        self.name = "nasir"
        self.no = 10
        self._no = 20
    
    def show(self):
        print(self.no, self._no)

class Rayhan(Nasir):
    def show_no(self):
        print("book name of rayhan : ",self.no)

class Anas(Nasir):
    def show_no(self):
        print("book name of anas : ",self._no) 

nasir = Nasir()
rayhan = Rayhan()
anas = Anas()
""" modify korar jonno jei class er vitore chane korbe sei class 
er object.variable er name = () tarpor poriborton hobe  """

nasir.show()            
nasir._no= 50
nasir.show()
rayhan.show_no()
anas.show_no()




# privet(__)


class Nasir:
    def __init__(self):
        self.name = "nasir"
        self.no = 10
        self._no = 20
        self.__no = 30
    
    def show(self):
        print(self.no, self._no)
    def protected(self):
        print("protect number :",self.__no)

class Rayhan(Nasir):
    def show_no(self):
        print("book name of rayhan : ",self._no)

class Anas(Nasir):
    def show_no(self):
        print("book name of anas : ",self._no) 
    def pro(self):
        print("book name of anas : ",self.__no)

nasir = Nasir()
rayhan = Rayhan()
anas = Anas()
""" modify korar jonno jei class er vitore chane korbe sei class 
er object.variable er name = () tarpor poriborton hobe  """

nasir.show()            
nasir.no= 50
nasir.show()
rayhan.show_no()
anas.show_no()
nasir.protected()





# spetial or magic method


a = 5
b = 6

print(a+b)

print(a.__add__(b))




























































