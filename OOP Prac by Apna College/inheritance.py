# Single inheritance
class Car:
    @staticmethod
    def start():
        print("car started ... ")
    
    @staticmethod
    def stop():
        print("car stopped .")

class New(Car):
    def __init__(self,name):
        self.name = name

c1 = New("toyota")
c2 = New("Lambo")
c3 = New("farari")

c1.start()
c2.start()
c3.start()

c1.stop()
c2.stop()
c3.stop()


# multilevel inhertance
class Grandpa:
    @staticmethod
    def behaviour():
        print("NICE AND GOOD FOR EVERYONE AND RESPECTFULL")
    
class Papa(Grandpa):
    def __init__(self):
        pass

class Child(Papa):
    def __init__(self):
        pass

c1 = Child()
c1.behaviour()


# multiple inheritance
class Mom:
    @staticmethod
    def look():
        print("calm person")

class Dad:
    @staticmethod
    def behavior():
        print("respectfull  person")

class Child(Mom , Dad):
    def __init__(self):
        pass

child1 = Child()
child1.behavior()
child1.look()

        