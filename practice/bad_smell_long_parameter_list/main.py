# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, speed, state, field, x, y):
        self.speed = speed
        self.state = state
        self.field = field
        self.x = x
        self.y = y

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')


    def move(self, direction):

        if direction == 'UP':
            self.field.set_unit(y=self.y + self._get_speed(), x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - self._get_speed(), x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - self._get_speed(), unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + self._get_speed(), unit=self)

