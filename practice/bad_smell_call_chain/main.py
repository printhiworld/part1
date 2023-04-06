# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_populatio, room):
        self.room = room
        self.city_populatio = city_populatio

    def get_person_room(self):
        return self.room

    def get_city_population(self):
        return self.city_populatio


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.