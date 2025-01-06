class ExampleClass:
    #Every function belonging to a class must be indented equality
    def __init__(self):
        name = "example"

    def someFunction(self, a):
        #Notice everything belonging to a function must be indented
        if a > 5:
            return True
        else:
            return False

    def separateFunction(b):
        for i in b:
        #Loops are also indented and nested conditions start a new indetation
            if i == 1:
                return True
        return False

    separateFunction([2, 3, 5, 6, 1])
