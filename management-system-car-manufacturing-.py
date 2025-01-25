import doctest

from dataclasses import dataclass
from enum import Enum

class FuelType(Enum):
    """
    Класс, представляющий возможные виды топлива для автомобиля.
    Каждый тип топлива представлен строковым значением.

    Attributes:
        PETROL: Бензин.
        DIESEL: Дизель.
        ELECTRO: Электричество.

    """
    PETROL = 'Бензин'
    DIESEL = 'Дизель'
    ELECTRO = 'Электричество'

@dataclass
class MaxPower:
    """
    Класс, представляющий максимальную мощность (hp) автомобиля.

    Attributes:
        value (int | float): Значение максимальной мощности, коорое может быть
        представлено как целым, так и вещественным числом.
    """
    value: int | float
    def __post_init__(self):
        """
        Производит проверку значения (value) после его инициализации.
        Вызывает исключение ValueError, если значение < 1 или > 200.
        :raise: ValueError: Неверное значение hp.
        :return: None

        >>> max_power = MaxPower(150)
        >>> max_power.value
        150

        >>> MaxPower(0)
        Traceback (most recent call last):
            ...
        ValueError: Неверное значение hp.

        >>> MaxPower(250)
        Traceback (most recent call last):
            ...
        ValueError: Неверное значение hp.
        """
        if self.value < 1 or self.value > 200:
            raise ValueError('Неверное значение hp.')

class Engine:
    """
    Класс, представляющий двигатель автомобиля.
    """
    def __init__(self, max_power: MaxPower, fuel_type: FuelType):
        """
        Создание и подготовка к работе объекта класса Engine (Двигатель)

        :param max_power: MaxPower: Мощность двигателя в лошадиных силах
        :param fuel_type: FuelType: Тип топлива
        """
        self.max_power: MaxPower = max_power
        self.fuel_type: FuelType = fuel_type

    def __str__(self) -> str:
        """
        Возвращает информацию о двигателе авто (мощность и тип топлива).
        :return: MaxPower, FuelType: Мощность в hp, тип топлива.
        """
        return f'{self.max_power.value} hp, тип топлива: {self.fuel_type.value}.'

@dataclass
class BodyType:
    """
    Класс, представляющий тип кузова автомобиля.

    Attributes:
        value (str): Тип кузова автомобиля. Должен содержаться в списке body_type_list.
    """
    value: str
    body_type_list = [
        'внедорожник', 'джип', 'хетчбэк', 'кабриолет', 'фастбэк', 'кроссовер', 'универсал', 'купе',
        'спорткар', 'лимузин', 'седан', 'микроавтобус', 'родстер', 'минивэн', 'пикап'
    ]

    def __post_init__(self):
        """
        Производит проверку значения (value) после его инициализации.
        Вызывает исключение ValueError, если значение не входит в body_type_list.
        :raise: ValueError: Неверный тип кузова.
        :return: None

        >>> body_type = BodyType('лимузин')
        >>> body_type.value
        'лимузин'
        >>> BodyType('спортивный')
        Traceback (most recent call last):
        ...
        ValueError: Неверный тип кузова.
        """
        if self.value.lower().strip() not in self.body_type_list:
            raise ValueError('Неверный тип кузова.')

@dataclass
class Doors:
    """
    Класс, представляющий количество дверей авто.

    Attributes:
        value (int): Значение количества дверей авто. Может быть только целым числом.
    """
    value: int
    def __post_init__(self):
        """
        Производит проверку значения (value) после его инициализации.
        Вызывает исключение ValueError, если значение < 2 или > 5.
        :raise: ValueError: Неверное количество дверей.
        :return: None

        >>> number_of_doors = Doors(4)
        >>> number_of_doors.value
        4
        >>> Doors(6)
        Traceback (most recent call last):
        ...
        ValueError: Неверное количество дверей.
        >>> Doors(1)
        Traceback (most recent call last):
        ...
        ValueError: Неверное количество дверей.
        """
        if self.value < 2 or self.value > 5:
            raise ValueError('Неверное количество дверей.')

class CarBody:
    """
    Класс, представляющий кузов автомобиля (тип кузова и количество дверей авто).
    """
    def __init__(self, body_type: BodyType, number_of_doors: Doors):
        """
        Создание и подготовка к работе объекта класса CarBody (Кузов)

        :param body_type: BodyType: Вид кузова автомобиля
        :param number_of_doors: Doors: Количество дверей (шт.)
        """
        self.body_type: BodyType = body_type
        self.number_of_doors: Doors = number_of_doors

    def __str__(self) -> str:
        """
        Возвращает информацию о кузове автомобиля.
        :return: BodyType, Doors: Тип кузова, количество дверей.
        """
        return f'Тип кузова - {self.body_type.value}, количество дверей - {self.number_of_doors.value}.'

@dataclass
class Diameter:
    """
    Класс, представляющий диаметр колес авто.

    Attributes:
        value (int | float): Значение диаметра колеса авто, которое может быть целым или
        вещественным числом.
    """
    value: int | float
    def __post_init__(self):
        """
        Производит проверку значения (value) после его инициализации.
        Вызывает исключение ValueError, если значение < 33 или > 45.
        :raise: ValueError: Неверный диаметр колеса.
        :return: None

        >>> diameter = Diameter(38)
        >>> diameter.value
        38
        >>> Diameter(30)
        Traceback (most recent call last):
        ...
        ValueError: Неверный диаметр колеса.
        >>> Diameter(48)
        Traceback (most recent call last):
        ...
        ValueError: Неверный диаметр колеса.
        """
        if self.value < 33 or self.value > 45:
            raise ValueError('Неверный диаметр колеса.')

@dataclass
class RubberType:
    """
    Класс, представляющий тип резины колес автомобиля.

    Attributes:
        value (str): Значение, содержащее тип резины колес автомобиля.
        Должно соответствовать одному из значений из списка rubber_types_list.
    """
    value: str
    rubber_types_list = [
        'летняя', 'зимняя', 'всесезонная', 'спортивная', 'внедорожная', 'картинговая', 'премиум', 'эко', 'модулярная'
    ]
    def __post_init__(self):
        """
        Производит проверку значения (value) после его инициализации.
        Вызывает исключение ValueError, если значение не входит в rubber_types_list.
        :raise: ValueError: Неверный тип резины.
        :return: None

        >>> type_of_rubber = RubberType('картинговая')
        >>> type_of_rubber.value
        'картинговая'
        >>> RubberType('с высоким сцеплением')
        Traceback (most recent call last):
        ...
        ValueError: Неверный тип резины.
        """
        if self.value not in self.rubber_types_list:
            raise ValueError('Неверный тип резины.')

class Wheel:
    """
    Класс, представляющий колесо автомобиля.
    """
    def __init__(self, diameter: Diameter, type_of_rubber: RubberType):
        """
        Создание и подготовка к работе объекта класса Wheel(Колесо).
        :param diameter: Diameter: Длина диаметра колеса авто в см.
        :param type_of_rubber: RubberType: Тип резины колес.
        """
        self.diameter: Diameter = diameter
        self.type_of_rubber: RubberType = type_of_rubber
        
    def __str__(self) -> str:
        """
        Возвращает информацию о 4-х колесах авто. Предусмотрен вариант только с одинаковыми колесами.
        :return: Diameter, RubberType: Диаметр каждого колеса, тип резины.
        """
        return f'Диаметр колеса: {wheel.diameter.value}, резина - {wheel.type_of_rubber.value}\n' * 4

doctest.testmod()

engine = Engine(max_power=MaxPower(150), fuel_type=FuelType.DIESEL)
print(engine)
car_body = CarBody(body_type=BodyType('хетчбэк'), number_of_doors=Doors(4))
print(car_body)
wheel = Wheel(diameter=Diameter(45), type_of_rubber=RubberType('летняя'))
print(wheel)