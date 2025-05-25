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

# MyClass -- это класс, но также он является и объектом, экземпляром метакласса type,
# являющегося абстракцией понятия типа данных
print(type(MyClass))                # <class 'type'>

# Соответственно, с классами работать как с объектами, например, копировать
AnotherClass = MyClass
print(type(AnotherClass))           # <class 'type'>

# Как видим, теперь AnotherClass -- это то же самое, что и MyClass,
# и obj является и экземпляром класса AnotherClass
print(isinstance(obj, AnotherClass))  # True





##########################################################################################################################
###  CLASSES ATTRIBUTES  ###

# Все члены класса в терминологии Python называются атрибутами

# Объявление класса MyClass с двумя атрибутами int_field и str_field. Атрибуты класса, являющиеся переменными,
# примерно соответствуют статическим полям класса в других языках программирования
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

# Однако, аналогично глобальным и локальным переменным, присвоение значение атрибуту объекта не изменяет значение
# атрибута класса, а ведёт к созданию атрибута данных (нестатического поля)
object1.str_field = 'another string'
print(MyClass.str_field)            # string
print(object1.str_field)            # another string
print(object2.str_field)            # string







..[end]
