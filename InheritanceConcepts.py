class A:
    def feature1(self):
        print("feature one working")

    def feature2(self):
        print("feature two working")



class B(A):
    def feature3(self):
        print("feature three working")

    def feature4(self):
        print("feature four working")


class C():
    def feature5(self):
        print("feature five working")


class D(A,C):
    def feature6(self):
        print("feature six working")




s2 = B()
s2.feature1()
s2.feature2()
s2.feature3()
s2.feature4()


s3 = D()

s3.feature1()
s3.feature2()
s3.feature5()
s3.feature6()

