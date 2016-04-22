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
