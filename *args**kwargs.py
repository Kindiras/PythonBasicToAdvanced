""" *args non keyword arguments and **kwargs keyword arguments, the former passes arguments are tuple"""

def adder(*args):
    return sum(args)


def myIntro(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} is {value}')

if __name__ == "__main__":
    print(adder(10.0,10.0,30,60))  
    myIntro(FirstName="Indiras",LastName = "Khatri", age = 35, zipcode = 43614)  


