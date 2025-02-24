class A:
    def __init__(self):
        print("In Class A constructor")

    def feature1(self):
        print("feature one working")

    def feature2(self):
        print("feature two working")



class B(A):
    def __init__(self):
        #super().__init__()
        print("In Class B constructor")

    def feature3(self):
        print("feature three working")

    def feature4(self):
        print("feature four working")

class C(B):
    def __init__(self):
        super().__init__()
        print("In Class C constructor")


s2 = C()


