### python 对象访问
- 私有成员：在类的外部不能直接访问，可在内部访问，形式上，两个下划线开头但是不以两个下划线结束则表示是私有成员,
- 对象名._类名__xxx 也可以在外部程序中访问私有成员。 self.__name = “name” 这是类中私有成员的书写方式
- 公有成员：可以公共访问的成员
- _xxx：受保护成员； _counts = 0     #受保护的变量
- xxx：系统定义的特殊成员；
- __xxx：私有成员，只有类对象自己能访问，子类对象不能直接访问到这个成员，但在对象外部可以通过“对象名._类名__xxx”这样的特殊方式来访问。
    
##
    def __init__(self, color, name):#这是构造方法，self类似Java里面的this，代表对象自己。在类中的方法里self永远是第一个参数
     @classmethod   #修饰器声明类方法
    def classShow(cls):#类方法，cls默认为其方法的参数
        print(cls._counts)
    @staticmethod       #修饰器，声明该方法为静态方法
    def staticShow():
         print(Person.__name1)
##