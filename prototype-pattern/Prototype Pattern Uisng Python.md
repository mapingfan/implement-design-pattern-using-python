# Prototype Pattern Uisng Python

标签（空格分隔）： StackOverflow

---

今天这个设计模是原型模式。乍听不好理解，反复琢磨几天有所得。
按照惯例先给代码，最后说一下自己的理解。
今天的代码实现来源于[这个地方][1]，我基本上就是照着敲，实现了下，重点是理解原型模式的含义。

---
```
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

```
---

一开始接触原型模式真的是一头雾水。原型这个概念很早就接触过，比如说常见的函数原型。后来我慢慢了解到原型模式
主要用在创建对象代价很大地方。为了减少成本，原型模式采用了一种深拷贝机制，克隆了已有对象，从而达到了获得一个对象的目的。
所以归根结底来说，还是为了创建对象，但是创建对象的成本比较高或者有一些特殊情况，根本就不能创建第二个对象，这个时候采用原型模式或许是正确的。其实以前学习`C++中的拷贝机制`时，底层的实现应该就运用了原型模式。
在`Python`中，我们要借助于第三方`copy库`实现深拷贝的功能，因为据我了解Python中对象之间的复制都是引用模型，也就是相当于给一个对象起来多个别名（可以类比C++中的引用机制）。因为我们把对象当作参数传进函数，必然会涉及到对象的拷贝工作。
今天就到此为止，以后有新的发现会继续更新。


  [1]: https://gist.github.com/pazdera/1122366