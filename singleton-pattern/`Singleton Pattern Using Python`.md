# `Singleton Pattern Using Python`

标签（空格分隔）： Desing-Pattern

---

这个模式是单例模式，也是属于很常见的设计模式。但是Python中实现确实有点困难，因为这可能需要某些特性的支持。我们无法创建一个类外无法访问的构造器。要想实现的话可能需要一些奇技淫巧。

### 适用场景： `类外无法创建类实例，但是必须要有一个实例。`
最下面Python实现的代码我是谷歌到的，借鉴一下。

![设计模式图][1]
```
#Java中的单例模式实现
public class SingleObject {

   //create an object of SingleObject
   private static SingleObject instance = new SingleObject(); #这一句是重点。

   //make the constructor private so that this class cannot be
   //instantiated
   private SingleObject(){}  #重点，类外无法访问私有的构造器。

   //Get the only object available
   public static SingleObject getInstance(){
      return instance;
   }  # 返回唯一实例。注意是静态函数。

   public void showMessage(){
      System.out.println("Hello World!");
   }
}

public class SingletonPatternDemo {
   public static void main(String[] args) {

      //illegal construct
      //Compile Time Error: The constructor SingleObject() is not visible
      //SingleObject object = new SingleObject();

      //Get the only object available
      SingleObject object = SingleObject.getInstance();

      //show the message
      object.showMessage();
   }
}

# Output： Hello World！ 。
```

----

```
# implement singleton pattern using python .


class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from.

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


@Singleton
class Foo:
    def __init__(self):
        print 'Foo created'

Foo() #TypeError: Singletons must be accessed through `Instance()`.
a_instance = Foo.Instance() #<__main__.Foo instance at 0x02D83670> 内存地址一致。
b_instance = Foo.Instance() #<__main__.Foo instance at 0x02D83670> 内存地址一致。

print a_instance, "\n"
print b_instance
```
这个地方用到了很多`Python`的高级特性，有些地方我目前也没搞懂，所以暂时不做解释。

---
下面简单写下思路和理解：
顾名思义，单例，单一实例。一个类只能拥有一个实例，而且这个实例是无法在类外创建的。但是我们在类里是可以调用私有的构造器，故而可以创建出类实例。所以不要问，构造器是私有，那么唯一的实例是哪里来的。


  [1]: http://www.tutorialspoint.com/design_pattern/images/singleton_pattern_uml_diagram.jpg