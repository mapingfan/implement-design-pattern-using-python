# `Abstract Factory Desing Pattern Using Python`

标签（空格分隔）： Desing-Pattern

---

第二个设计模式是抽象工厂模式，听名字就知道和第一个工厂模式是亲戚。
适用情景： `推迟类对象的实例化过程，根据需求动态的创建实例。`


还是先给代码，然后总结写自己的理解。

![设计模式图][1]

```
# implements abstract factory pattern using python .


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


class Color:
    def __init__(self):
        pass

    def print_color(self):
        pass


class Red(Color):

    def print_color(self):
        print "The color is red ."


class Green(Color):

    def print_color(self):
        print "The color is green ."


class White(Color):

    def print_color(self):
        print "The color is white ."


class ShapeFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_shape(shape_type):

        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "rectangle":
            return Rectangle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            return None


# ColorFactory produce color instance . same as ShapeFactory .
class ColorFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_color(color_type):
        if color_type.lower() == "red":
            return Red()
        elif color_type.lower() == "white":
            return White()
        elif color_type.lower() == "green":
            return Green()
        else:
            return None


# This class is used to produce factory .
class ProduceFactory:
    # return ColorFactory or ShapeFactory based on factory_name .
    def __init__(self):
        pass

    @staticmethod
    def get_factory(factory_name):
        if factory_name.lower() == "colorfactory":
            return ColorFactory()

        elif factory_name.lower() == "shapefactory":
            return ShapeFactory()


class AbstractFactoryDemo:

    def __init__(self):
        pass

    @staticmethod
    def test_demo():
        result = ProduceFactory.get_factory("colorfactory")
        color = result.get_color("Red")
        color.print_color()

        result = ProduceFactory.get_factory("shapefactory")
        shape = result.get_shape("circle")
        shape.draw()

AbstractFactoryDemo.test_demo()

```

---
我还是沿用上一个例子，增加了一个颜色类工厂。
我对抽象工厂模式的理解就是运用两次工厂模式。第一次是创建类的实例，诸如`ShapeFactory`。第二次是对工厂类运用工厂模式。乍一听可能不好理解。既然工厂类也是类，而且可以实例化，那么为什么不可以对工厂类也运用工厂模式，把创建工厂类对象的过程移到另一个工厂函数中呢？
来一个具体的例子：
还是做手机，然后找代工。但是现在手机行情太好，代工厂急剧扩张，底下有很多字代工厂。现在订单来了，我们会怎么办？
我们肯定会分发订单，子代工厂一号负责代工苹果手机，子代工厂二号负责生产三星手机。
这个地方我们分发订单就等价于我们对工厂类实施工厂模式。由总代工厂分发订单（等价于产生子代工厂实例），然后子代工厂负责具体的生产事宜。
其实想想这个例子，感觉就是特喵的运用了两次工厂模式嘛，推迟类的实例化过程，移入到工厂类里。为什么叫抽象工厂类，可能就是因为我们进行了二次工厂。
例子中第一类工厂类是`ShapeFactory/ColorFactory`。第二类工厂是`ProduceFactory`。


  [1]: http://www.tutorialspoint.com/design_pattern/images/abstractfactory_pattern_uml_diagram.jpg