# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для
#     получания значений этого атрибута нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий

class Car:
    transmission = 'Automatic'

    def __init__(self, brand, model, fuel_type):
        self.__brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def run(self):
        return 'Im fast'

    def get_brand(self):
        return f'this is {self.__brand}'

    def set_brand(self, new_brand):
        self.__brand = new_brand

car1 = Car('Toyota', 'Camry', 'Gasoline')
car2 = Car('Honda', 'Civic', 'Electric')

# print(car1.brand)
# print(car1.get_brand())
# print(car1.fuel_type)
# print(car1.transmission)
# print(car2.get_brand())
# print(car2.transmission)


class Motorcycle(Car):

    def __init__(self, brand, model, fuel_type, color):
        super().__init__(brand, model, fuel_type)
        self.color = color

    def give_me_a_power(self):
        return 'Just press the button'

    def run(self):
        return 'Im super fast'

car3 = Motorcycle('Ducati', 'DesertX', 'Gasoline', 'White')

print(car3.get_brand())
print(car3.transmission)
print(car3.give_me_a_power())
print(car2.run())
print(car3.run())
print(car3.__dict__)
print(car2.set_brand('Mazda'))
print(car2.get_brand())

print(car2.__dict__)
print(car2._Car__brand)

