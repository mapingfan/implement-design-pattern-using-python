# `Factory Design Pattern Using Python `

标签（空格分隔）： Desing-Pattern

---

尝试用`Python`实现一些简单的设计模式。第一个实现的工厂模式。尽量尝试把23个模式都实现。
适用情景： `推迟类对象的实例化过程，根据需求动态的创建实例。`
先上代码，底下讲讲自己的理解。图片中是用`Java`实现的，我盗用了别人的图片。

![设计模式图][1]
```
# implement the factory pattern using python .


class Shape:

    def __init__(self):
        pass

    def draw(self):
        pass


class Circle(Shape):

    def draw(self):
        print "Drawing a circle ."


class Rectangle(Shape):

    def draw(self):
        print "Drawing a rectangle ."


class Square(Shape):

    def draw(self):
        print "Drawing a square ."


class ShapeFactory:

    def __init__(self):
        pass

    @staticmethod
    def getShape(shape_type):

        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "rectangle":
            return Rectangle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            return None


class FactoryPatternDemo:

    def __init__(self):
        pass

    @staticmethod
    def test_factory_pattern():
        # test circle .
        result = ShapeFactory.getShape("circle")
        result.draw()

        # test rectangle .
        result = ShapeFactory.getShape("rectangle")
        result.draw()

        # test square .
        result = ShapeFactory.getShape("square")
        result.draw()

        # test others
        result = ShapeFactory.getShape("wrong_type")
        print result

FactoryPatternDemo.test_factory_pattern()
```
有些地方明明可以不用写类，但是设计模式毕竟是和`OOP`相关的，感觉都写成类比较合适。

---
*下面总结下自己对工厂模式的理解：*
工厂模式其实以前我就接触过，但是我不知道它的名字。第一次看感觉可能很惊奇，工厂模式是什么鬼？
其实这个名字起的很贴切。
考虑如下场景：
现在有很多手机厂商，但是很多厂商都没自己的工厂。所以手机厂商负责设计手机，然后交给第三方进行代工。这个模式和我们的工厂模式很相似。
在工厂模式中，各个手机厂商设计手机的原型，可以等价于上面例子中的圆形，矩形，正方形。
手机厂商把原型交给代工厂进行生产，而上面的例子中也是如此，我们在工厂类中创建了矩形等形状的实例。
上面这两个步骤还是很相似的，所以从这一点来说取名为工厂模式还是很贴切的。

*核心思想：*
我对工厂模式的理解就是推迟类的实例化。把实例化过程放到工厂函数中进行处理，我们可以根据参数动态创建类的实例对象，并返回。总而言之，要把实例化的过程放到工厂函数中。


  [1]: http://www.tutorialspoint.com/design_pattern/images/factory_pattern_uml_diagram.jpg