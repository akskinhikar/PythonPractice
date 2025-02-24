class ClassVariableConcept:
    #Static variable or Class Variable
    wheel = 4
    #instance variables
    def __init__(self):
        self.model = 'X5'
        self.Company = 'BMW'


c1 = ClassVariableConcept()
c2 = ClassVariableConcept()

ClassVariableConcept.wheel = 5

print(c1.Company, c1.model, ClassVariableConcept.wheel)
print(c2.Company, c2.model, ClassVariableConcept.wheel)