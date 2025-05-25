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

# В Python всё является объектами, в том числе
# и сами классы

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
print(Person.print_info)                        # <function Person.print_info at 0x00000148C1B88220>
print(type(Person.print_info))                  # функция (<class 'function'>)

# Вызовем её для объектов alex и john
Person.print_info(alex)                        # Alex is 18
Person.print_info(john)                        # John is 20

# Метод -- это функция, привязанная к объекту. Все атрибуты класса, являющиеся функциями, описывают соответствующие методы экземпляров
# данного класса.

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
# MyClass.method()              # TypeError: outer_method() missing 1 required positional argument: 'self'





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
        return 'Rectangle(%.1f, %.1f)' % (self.side_a, self.side_b)


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
    print(rectangle)
    circle1 = Circle(1)
    print(circle1)
    circle2 = Circle.from_rectangle(rectangle)
    print(circle2)


if __name__ == '__main__':
    main()

# не злоупотредлять classmethod, если нужно описать просто staticmethod то classmethod использовать не имеет смысла







..[end]
