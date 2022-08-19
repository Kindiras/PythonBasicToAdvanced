def add(a,b):
    try:
        return (a+b)
    except TypeError as err:
        print("enter number",err)
        return TypeError


def subtraction(a,b):
    try:
        return(a-b)
    except TypeError as err:
        print("enter numbers",err)
        return TypeError    

if __name__ == "__main__":
    print(add(2,3 + 4j))    