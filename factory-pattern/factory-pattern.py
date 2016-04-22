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