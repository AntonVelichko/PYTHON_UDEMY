##########################################################################################################################
###  SIMPLE CLASS  ###

# Объявление пустого класса MyClass
class MyClass:
    pass

# Создание экземпляра класса
obj = MyClass()

# Вывод типа obj
print(type(obj))





##########################################################################################################################
###  CLASSES AS OBJECTS  ###

# В Python всё является объектами, в том числе и сами классы

# Объявление пустого класса MyClass
class MyClass:
    pass

# Создание экземпляра класса
obj = MyClass()

# Объект obj -- это экземпляр класса MyClass, то есть он имеет тип MyClass
print(type(obj))                    # <class '__main__.MyClass'>

# MyClass -- это класс, но также он является и объектом, экземпляром метакласса type, являющегося абстракцией понятия типа данных
print(type(MyClass))                # <class 'type'>

# Соответственно, с классами работать как с объектами, например, копировать
AnotherClass = MyClass
print(type(AnotherClass))           # <class 'type'>

# Как видим, теперь AnotherClass -- это то же самое, что и MyClass, и obj является и экземпляром класса AnotherClass
print(isinstance(obj, AnotherClass))  # True





##########################################################################################################################
###  CLASSES ATTRIBUTES  ###

# Все члены класса в терминологии Python называются атрибутами

# Объявление класса MyClass с двумя атрибутами int_field и str_field. Атрибуты класса, являющиеся переменными, примерно соответствуют статическим полям класса в других языках программирования
class MyClass:
    int_field = 8
    str_field = 'string'


# Обращение к атрибутам класса
print(MyClass.int_field)            # 8
print(MyClass.str_field)            # string

# Создание двух экземпляров класса
object1 = MyClass()
object2 = MyClass()

# Обращение к атрибутам класса через его экземпляры
print(object1.int_field)            # 8
print(object2.str_field)            # string

# Все вышеперечисленные обращения к атрибутам на самом деле относятся ко двум одним и тем же переменным

# Изменение значения атрибута класса
MyClass.int_field = 10
print(MyClass.int_field)            # 10
print(object1.int_field)            # 10
print(object2.int_field)            # 10

# Однако, аналогично глобальным и локальным переменным, присвоение значение атрибуту объекта не изменяет значение атрибута класса, а ведёт к созданию атрибута данных (нестатического поля)
object1.str_field = 'another string'
print(MyClass.str_field)            # string
print(object1.str_field)            # another string
print(object2.str_field)            # string





##########################################################################################################################
###  DATA ATTRIBUTES  ###
# Атрибуты-данные аналогичны полям в терминологии большинства распространённых языков программирования.
# Атрибуты-данные не нужно описывать: как и переменные, они создаются в момент первого присваивания.

# Класс, описывающий человека
class Person:
    pass

# Создание экземпляров класса
alex = Person()
alex.name = 'Alex'
alex.age = 18

john = Person()
john.name = 'John'
john.age = 20

# Атрибуты-данные относятся только к отдельным экземплярам класса и никак не влияют на значения соответствующих атрибутов-данных других экземпляров
print(alex.name, 'is', alex.age)
print(john.name, 'is', john.age)





##########################################################################################################################
###  METHODS  ###
# Атрибутами класса могут быть и функции

# Класс, описывающий человека
class Person:
    # Первый аргумент, который указывает на текущий экземпляр класса, принято называть self
    def print_info(self):
        print(self.name, 'is', self.age)

# Создание экземпляров класса
alex = Person()
alex.name = 'Alex'
alex.age = 18

john = Person()
john.name = 'John'
john.age = 20

# Проверим, чем является атрибут print_info класса Person
print(Person)                                   # <class '__main__.Person'>
print(Person.print_info)                        # <function Person.print_info at 0x00000148C1B88220>
print(type(Person.print_info))                  # функция (<class 'function'>)

# Вызовем её для объектов alex и john
Person.print_info(alex)                        # Alex is 18
Person.print_info(john)                        # John is 20

# Метод -- это функция, привязанная к объекту. Все атрибуты класса, являющиеся функциями, описывают соответствующие методы экземпляров данного класса.

print(alex)                                       # <__main__.Person object at 0x77fd6548fb90>
print(alex.print_info)                            # <bound method Person.print_info of <__main__.Person object at 0x0000017351116A50>> (привязанный метод который лежит уже по другому адресу)
print(type(alex.print_info))                      # метод (<class 'method'>)

# Вызов метода print_info
alex.print_info()                                 # Alex is 18
john.print_info()                                 # John is 20





##########################################################################################################################
###  __init__  ###
# Начальное состояние объекта следует создавать в специальном методе-конструкторе __init__, который вызывается автоматически после создания экземпляра класса
# Его параметры указываются при создании объекта

# Класс, описывающий человека
class Person:
    # Конструктор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Метод из прошлого примера
    def print_info(self):
        print(self.name, 'is', self.age)


# Создание экземпляров класса
alex = Person('Alex', 18)
john = Person('John', 20)

# Вызов метода print_info
alex.print_info()                # Alex is 18
john.print_info()                # John is 20

Person.print_info(alex)			 # Alex is 18
Person.print_info(john)			 # John is 20





##########################################################################################################################
###  METHOD OUTSIDE A CLASS  ###
# Атрибуты класса, которые являются функциями, -- это такие же  атрибуты класса, как и переменные. Это можно увидеть на следующем примере

def outer_method(self):
    print('I am a method of object', self)

class MyClass:
    method = outer_method

obj = MyClass()
obj.method()                    # I am a method of object <__main__.MyClass object at 0x000001E1215C6A50>
print(MyClass.method)           # <function outer_method at 0x000001B7C7573EC0>

MyClass.method()                # TypeError: outer_method() missing 1 required positional argument: 'self'
MyClass().method()				# I am a method of object <__main__.MyClass object at 0x000001B1E7DA8A50>





##########################################################################################################################
###  STATIC METHOD  ###
# Методы, которые являются общими для класса и всех экземпляров класса и не имеют доступ к данным экземпляров классов, называются статическими методами.
# Для создания статических методов используется декоратор staticmethod.
# Декоратор – это специальная функция, которая изменяет поведение функции или класса. Для применения декоратора следует перед
# соответствующим объявлением указать символ @, имя необходимого декоратора и список его аргументов в круглых скобках.
# Если передача параметров декоратору не требуется, скобки не указываются.

class MyClass:
    # Объявление атрибута класса
    class_attribute = 8

    # Конструктор
    def __init__(self):
        self.data_attribute = 42

    # Статический метод. Обратите внимание, что у него нет параметра self, поскольку он не связан ни с одним из экземпляров класса не имеет доступа к атрибутам-данным
    @staticmethod
    def static_method():
        print(MyClass.class_attribute)

    # Обычный метод
    def instance_method(self):
        print(self.data_attribute)


if __name__ == '__main__':
    # Вызов статического метода
    MyClass.static_method()                 # 8
    # Инстанцирование объекта
    obj = MyClass()
    # Вызов метода
    obj.instance_method()                   # 42
    # Аналогично атрибутам класса, доступ ко статическим методам можно получить и через экземпляр класса
    obj.static_method()                     # 8



'''
In the below example, we have both data and class attributes with the same name, and it works the same way as the above code
'''

class MyClass:
    # Объявление атрибута класса
    data_attribute = 8

    # Конструктор
    def __init__(self):
        self.data_attribute = 42

    # Статический метод. Обратите внимание, что у него нет параметра self, поскольку он не связан ни с одним из экземпляров класса не имеет доступа к атрибутам-данным
    @staticmethod
    def static_method():
        print(MyClass.data_attribute)

    # Обычный метод
    def instance_method(self):
        print(self.data_attribute)


if __name__ == '__main__':
    # Вызов статического метода
    MyClass.static_method()                 # 8
    # Вызов обычного метода
    MyClass().instance_method()				# 42

    # Инстанцирование объекта
    obj = MyClass()
    # Вызов метода
    obj.instance_method()                   # 42
    # Аналогично атрибутам класса, доступ ко статическим методам можно получить и через экземпляр класса
    obj.static_method()                     # 8






##########################################################################################################################
###  CLASS METHOD  ###
# Так как классы тоже являются объектами, то помимо атрибутов-функций они могут иметь и собственные методы. 
# Для создания методов класса используется декоратор classmethod. В таких методах первый параметр принято называть не self, а cls.
#
# Методы класса обычно используются в двух случаях:
# •	для создания фабричных методов, которые создают экземпляры данного класса альтернативными способами;
# •	статические методы, вызывающие статические методы:  поскольку данный класс передаётся как первый аргумент функции, не нужно вручную указывать имя класса для вызова статического метода.

class Rectangle:
    """
    Класс, описывающий прямоугольник
    """

    def __init__(self, side_a, side_b):
        """
        Конструктор класса
        :param side_a: первая сторона
        :param side_b: вторая сторона
        """
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        """
        Метод, который возвращает строковое представление объекта
        """
        return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)			# new version --> f'Rectangle({self.side_a:.1f}, {self.side_b:.1f})'


class Circle:
    """
    Класс, описывающий окружность
    """

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle(%.1f)' % self.radius

    @classmethod
    def from_rectangle(cls, rectangle):
        """
        Мы используем метод класса в качестве фабричного метода, который создаёт экземпляр класса Circle из экземпляра класса Rectangle как окружность, вписанную в данный прямоугольник.
        :param rectangle: Rectangle instance
        :return: Circle instance
        """
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)
        # если мы напишем Circle.from_rectangle - то cls будет равно Circle
        # если опишем class Disc который наследуется от class Circle -  Disc.from_rectangle - то cls будет Disc и экземпляр класса будет Disc

        """
        Если бы мы написали вот так:
        @staticmethod
        def from_rectangle(rectangle):
            radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
            return Circle(radius)
        Здесь мы получаем экземпляр класса Circle. Например если бы у нас был бы class Disc и он наследовался бы от класса Circle
        """

def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)                                  # Rectangle(3.0, 4.0)
    circle1 = Circle(1)
    print(circle1)                                    # Circle(1.0)
    disc = Circle.from_rectangle(rectangle)
    print(disc)                                       # Circle(2.5)


    print(Circle)								      # <class '__main__.Circle'>
    print(Circle.from_rectangle)					  # <bound method Circle.from_rectangle of <class '__main__.Circle'>>


if __name__ == '__main__':
    main()

# не злоупотредлять classmethod, если нужно описать просто staticmethod то classmethod использовать не имеет смысла


'''
In the below example, we don't use @classmethod
'''


class Rectangle:
    """
    Класс, описывающий прямоугольник
    """

    def __init__(self, side_a, side_b):
        """
        Конструктор класса
        :param side_a: первая сторона
        :param side_b: вторая сторона
        """
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        """
        Метод, который возвращает строковое представление объекта
        """
        return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)			# new version --> f'Rectangle({self.side_a:.1f}, {self.side_b:.1f})'


class Circle:
    """
    Класс, описывающий окружность
    """

    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return 'Circle(%.1f)' % self.radius

    def from_rectangle(rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return Circle(radius)
        # Здесь мы получаем экземпляр класса Circle. Например если бы у нас был бы class Disc и он наследовался бы от класса Circle



def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)                                  # Rectangle(3.0, 4.0)
    circle1 = Circle(1)
    print(circle1)                                    # Circle(1.0)
    disc = Circle.from_rectangle(rectangle)
    print(disc)                                       # Circle(2.5)

    print(Circle)								      # <class '__main__.Circle'>
    print(Circle.from_rectangle)					  # <function Circle.from_rectangle at 0x00000193729BC180>


if __name__ == '__main__':
    main()




##########################################################################################################################
###  PRIVAT MEMBERS  ###
# Атрибуты, имена которых начинаются, но не заканчиваются, двумя символами подчёркивания, считаются приватными. К ним применяется механизм
# «name mangling», суть которого заключается в том, что изнутри класса и его экземпляров к этим атрибутам можно обращаться по тому имени,
# было задано при объявлении, однако на самом деле к именам слева добавляется подчёркивание и имя класса. Этот механизм не предполагает защиты данных от
# изменения извне, так как к ним всё равно можно обратиться, зная имя класса и то, как Python изменяет имена приватных атрибутов, однако позволяет
# защитить их от случайного переопределения в классах-потомках.

class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def get_private(self):
        return self.__private_attribute


obj = MyClass()
print(obj.get_private())  # 42
print(obj.__private_attribute)  # ошибка
# print(obj._MyClass__private_attribute)  # 42





##########################################################################################################################
###  ???  ###

class MyObject:
    def __init__(self):
        self.__private_attribute = 0

    def get_attribute(self):
        return self.__private_attribute

    def set_attribute(self, value):
        if value < 10:
            self.__private_attribute = value
            return self.__private_attribute
        else:
            return self.__private_attribute

obj = MyObject()            # creating an example of class MyObject

print(obj.get_attribute())                          # 0
print(obj.set_attribute(9))                         # 9
print(obj.set_attribute(11))                        # 9


print(MyObject().get_attribute())                   # 0
print(MyObject().set_attribute(9))                  # 9
print(MyObject().set_attribute(11))                 # 0  <-- this doesn't change

print(MyObject.get_attribute())         # TypeError: MyObject.get_attribute() missing 1 required positional argument: 'self'




--- same but with methods ---




class MyObject:
    def __init__(self):
        self.__attribute = 0

    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        if value < 10:
            self.__attribute = value
            return self.__attribute
        else:
            return self.__attribute


obj = MyObject()            # creating an example of class MyObject

# calling @property method, not private '__attribute'
print(obj.attribute)                                    # 0

# calling method @attribute.setter
obj.attribute = 9

# calling method @property
print(obj.attribute)                                    # 9

obj.attribute = 11
print(obj.attribute)                                    # 9



print(MyObject().attribute)                             # 0

MyObject().attribute = 9
print(MyObject().attribute)                             # 0

MyObject().attribute = 11
print(MyObject().attribute)                             # 0


'''
The reason MyObject().attribute = 9 does not change it to 9 is because you are assigning the value to a new instance of MyObject, but you are not storing that instance anywhere.

Each time MyObject() is called, a brand-new object is created. So when you write:

------
MyObject().attribute = 9
print(MyObject().attribute)  # Still prints 0
------

Here's what's happening:
MyObject() creates a new instance of MyObject.

attribute = 9 sets the attribute value for that temporary instance.

Immediately after, MyObject().attribute creates another new instance, which still has its original value (0), since it is not the same instance as the one you just modified.

How to Fix It
If you want the modification to persist, you need to store the instance in a variable:

------
obj = MyObject()  # Store instance in a variable
obj.attribute = 9  # Modify stored instance
print(obj.attribute)  # Outputs: 9
------

Every time you call MyObject(), it creates a new object, so changes made to one instance do not carry over to others. Hope that clears it up! Let me know if you need more clarification.
'''




##########################################################################################################################
###  MAGIC/SPECIAL METHODS  ###

# Атрибуты, имена которых начинаются и заканчиваются двумя знаками подчёркивания, являются внутренними для Python и задают особые
# свойства объектов. С одним из подобных атрибутов мы уже имели дело ранее (документационная строка __doc__). Другим примером может служить атрибут __class__, в котором хранится класс
# данного объекта.
#
# Среди таких атрибутов есть методы. В документации Python подобные методы называются методами со специальными именами,
# однако в сообществе Python-разработчиков очень распространено название «магические методы». Также встречается и название
# «специальные методы». Они задают особое поведение объектов и позволяют переопределять поведение встроенных функций и
# операторов для экземпляров данного класса.
#
# Наиболее часто используемым специальным методом является метод-конструктор __init__.


class Complex:
    """
    Комплексное число
    """

    def __init__(self, real=0.0, imaginary=0.0):
        """
        Конструктор

        :param real:      действительная часть
        :param imaginary: мнимая часть
        """
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        """
        Метод __repr__ возвращает строковое представление объекта, которое,
        если это возможно, должно быть корректным выражением, создающим
        аналогичный объект, иначе содержать его описание;
        вызывается функцией repr.
        """
        return 'Complex(%g, %g)' % (self.real, self.imaginary)

    def __str__(self):
        """
        Метод __str__ возвращает предназначенное для человека строковое
        представление объекта; вызывается функциями str, print и format.
        """
        return '%g %c %gi' % (self.real,
                              '+' if self.imaginary >= 0 else '-',
                              abs(self.imaginary))

    # Арифметические операции

    def __add__(self, other):
        """
        Метод __add__ определяет операцию сложения.
        """
        return Complex(self.real + other.real,
                       self.imaginary + other.imaginary)

    def __neg__(self):
        """
        Операция отрицания
        """
        return Complex(-self.real, -self.imaginary)

    def __sub__(self, other):
        """
        Операция вычитания.
        Сложение и отрицание уже определены, поэтому вычитание
        можно определить через них
        """
        return self + (-other)

    def __abs__(self):
        """
        Модуль числа
        """
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    # Операции сравнения

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not (self == other)


def main():
    x = Complex(2, 3.5)
    print(repr(x))                          # Complex(2, 3.5)
    print('x =', x)                         # x = 2 + 3.5i

    y = Complex(5, 7)
    print('y =', y)                         # y = 5 + 7i

    print('x + y =', x + y)                 # x + y = 7 + 10.5i
    print('x - y =', x - y)                 # x - y = -3 - 3.5i

    print('|x| =', abs(x))                  # |x| = 4.031128874149275

    print('(x == y) =', x == y)             # (x == y) = False


if __name__ == '__main__':
    main()



x = 2
print(x.__neg__())                          # -2



class Custom:
    def __init__(self, num):
        self.num = num
    
    def __eq__(self, other):
        # return self.num == other.num
        return 'Works!'


num1 = Custom(1)
num2 = Custom(1)
print(num1.__eq__(num2))                    # Works!







##########################################################################################################################
###  SECRET DATA  ###
# В этом примере показано использование функции __getattribute__ для сокрытия данных

class MyClass:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        """
        Метод __getattribute__ вызывается при получении атрибутов
        """

        # Если запрошено поле secret_field и пароль верный
        if item == 'secret_field' and self.password == '9ea)fc':
            # то возвращаем значение
            return 'secret value'
        else:
            # иначе вызываем метод __getattribute__ класса object
            return object.__getattribute__(self, item)


# Создание экземпляра класса
obj = MyClass()

# Разблокирование секретного поля
obj.password = '9ea)fc'             # comment it ro see Error

# Вывод значения secret field.
# Значение будет получено, если раскомментировать предыдущую строку программного кода, иначе будет получена ошибка.
print(obj.secret_field)             # secret value






..[end]
