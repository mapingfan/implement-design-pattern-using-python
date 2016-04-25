# implement prototype pattern using python .
# we need to use copy library .

from copy import copy


class Prototype:
    _type = None
    _value = None

    def clone(self):
        pass

    def getType(self):
        return self._type

    def getValue(self):
        return self._value


class TypeOne(Prototype):

    def __init__(self, number):
        self._type = "Type1"
        self._value = number

    def clone(self):
        return copy(self)


class TypeTwo(Prototype):

    def __init__(self, number):
        self._type = "Type2"
        self._value = number

    def clone(self):
        return copy(self)


class ObjectFactory:

    __type1Value1 = None
    __type1Value2 = None

    __type2Value1 = None
    __type2Value2 = None

    @staticmethod
    def initialize():
        ObjectFactory.__type1Value1 = TypeOne(1)
        ObjectFactory.__type1Value2 = TypeOne(2)

        ObjectFactory.__type2Value1 = TypeTwo(1)
        ObjectFactory.__type2Value2 = TypeTwo(2)

    @staticmethod
    def getType1Value1():
        return ObjectFactory.__type1Value1.clone()

    @staticmethod
    def getType1Value2():
        return ObjectFactory.__type1Value2.clone()

    @staticmethod
    def getType2Value1():
        return ObjectFactory.__type2Value1.clone()

    @staticmethod
    def getType2Value2():
        return ObjectFactory.__type2Value2.clone()

def main():
    ObjectFactory.initialize()

    instance = ObjectFactory.getType1Value1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType1Value2()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType2Value1()
    print "%s: %s" % (instance.getType(), instance.getValue())

    instance = ObjectFactory.getType2Value2()
    print "%s: %s" % (instance.getType(), instance.getValue())

if __name__ == "__main__":
    main()

