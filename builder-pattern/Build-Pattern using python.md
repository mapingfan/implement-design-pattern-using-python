# Build-Pattern using python

标签（空格分隔）： Desing-Pattern

---

今天这个模式是构造模式，也是属于创造模式中的一种。主要目的是用来创建对象。按照惯例，先给上代码，然后下面讲下自己的理解。

---
```
# Implement builder pattern using python .
# Assume we want to build a car , but we have many options .
# Car : wheels , color, seats, brand ,style etc.

# one way to produce a vehicle instance .

class Vehicle:
    # This is normal car with four wheels  .
    def __init__(self, wheels, color, seats, brand, style):
        self.wheels = wheels
        self.color = color
        self.seats = seats
        self.brand = brand
        self.style = style


    # But we want to produce a car without brand . how to do this ?
    # A possible way .
    def __init__(self, wheels, color, seats, style):
        self.wheels = wheels
        self.color = color
        self.seats = seats
        self.style = style

    # Ok, we do it .But someone want a moto without style and style  . How to dow this ?
    # definite another constructor .
    def __init__(self, wheels, color, seats):
        self.wheels = wheels
        self.color = color
        self.seats = seats

    # if we have too many requests ,we must define too many constructors .
    # so we have builder pattern .


class Vehicle_:

    def __init__(self):
        self.wheels = None
        self.color = None
        self.seats = None
        self.brand = None
        self.style = None


class BuildVehicle:
    def __init__(self):
        self.vehicle = Vehicle_()

    def set_wheels(self,wheels):
        self.vehicle.wheels = wheels

    def set_color(self, color):
        self.vehicle.color = color

    def set_seats(self, seats):
        self.vehicle.seats = seats

    def set_brand(self, brand):
        self.vehicle.brand = brand

    def set_style(self, style):
        self.vehicle.style = style

    def getVehicle(self):
        return self.vehicle


def main():
    # we want a car with color red .
    build_vehicle = BuildVehicle()
    build_vehicle.set_color("red")
    build_vehicle.set_brand("ModelX")
    build_vehicle.set_seats(4)
    build_vehicle.set_style("normal")
    build_vehicle.set_wheels(2) # two wheels , brand: ModelX, four sets normal style .

    vehicle = build_vehicle.getVehicle()

    print vehicle, vehicle.brand, vehicle.color, vehicle.wheels, vehicle.style, vehicle.seats


if __name__ == '__main__':
    main()
```
---
忽略蹩脚的英语做了注释。
构造模式一开始并不像工厂模式，单例模式那么好理解，我查了一些资料才有点眉目。
首先我们要把握一个核心思想，**这个模式用来创建对象的**。考虑如下一种情况：
我们想想定制车辆：
方案一：
两个轮子+真皮座椅+红色喷漆
方案二：
三个轮子+宝马样式+全景天窗
方案三：
四个轮子别的啥也没有（我就是喜欢奇怪的车）
方案N:
...
我们有如此多的方案，那么当我要用`车类`产生一个类对象时，我们怎么办？正常想法肯定是根据方案个数写多少个`构造器`。这样写多了肯定会有麻烦，比如你记不住参数顺序，记不住参数个数等。
接着我们的构造模式出现了。顾名思义，我们一步步的构造出车辆，从而实现定制。
废话到此为止。
总而言之，`构造器的核心思想就是当我们要写多个构造器的时候，不妨考虑使用构造模式，把构造器拆分到多个构造模式类中，从而减轻构造器的负担`。