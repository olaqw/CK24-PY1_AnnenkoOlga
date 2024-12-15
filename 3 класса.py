import doctest


class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param length: Длина прямоугольника в миллиметрах
        :param width: Ширина прямоугольника в миллиметрах

        Примеры:
        >>> rectangle = Rectangle(100, 100)  # инициализация экземпляра класса
        """
        if not isinstance(length, int):
            raise TypeError("Длина прямоугольника должна быть типа int")
        if length <= 0:
            raise ValueError("Длина прямоугольника должна быть положительным числом")
        self.length = length

        if not isinstance(width, int):
            raise TypeError("Ширина прямоугольника должна быть int")
        if width <= 0:
            raise ValueError("Ширина прямоугольника должна быть положительным числом")
        self.width = width

    def add_or_remove_length(self, length_change: int) -> None:
        """
        Добавление или убавление длины прямоугольника.

        :param length_change: Изменяемая длина в миллиметрах
        :raise ValueError: Если убавляемая длина больше имеющейся длины, то вызываем ошибку

        :return: Итоговая длина и ширина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(100, 100)
        >>> rectangle.add_or_remove_length(200)
        """
        if not isinstance(length_change, int):
            raise TypeError("Добавляемая длина должна быть типа int")
        if self.length + length_change <= 0:
            raise ValueError("Убавляемая длина должна должна быть не меньше имеющейся")
        ...

    def add_or_remove_width(self, width_change: int) -> None:
        """
        Добавление или убавление ширины прямоугольника.

        :param width_change: Изменяемая ширина в миллиметрах
        :raise ValueError: Если убавляемая ширина больше имеющейся ширины, то вызываем ошибку

        :return: Итоговая длина и ширина прямоугольника

        Примеры:
        >>> rectangle = Rectangle(100, 100)
        >>> rectangle.add_or_remove_width(-50)
        """
        if not isinstance(width_change, int):
            raise TypeError("Добавляемая ширина должна быть типа int")
        if self.width + width_change <= 0:
            raise ValueError("Убавляемая ширина должна должна быть не меньше имеющейся")
        ...


class Tree:
    def __init__(self, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param age: Возраст дерева (лет)
        :param height: Высота дерева в метрах

        Примеры:
        >>> birch = Tree(150, 34)  # инициализация экземпляра класса
        """
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типом int")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом")
        self.age = age

        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть типом int или float")
        if height <= 0:
            raise ValueError("Высота дерева не может быть отрицательным числом")
        self.height = height

    def is_oldest_tree(self, oldest_age_of_tree_type: int) -> bool:
        """
        Функция которая проверяет является ли дерево старейшим
        :param oldest_age_of_tree_type: Возраст дерева, при котором оно считается старейшим по типу дерева

        :return: Является ли дерево старейшим

        Примеры:
        >>> birch = Tree(150, 34)
        >>> birch.is_oldest_tree(120)
        """
        if not isinstance(oldest_age_of_tree_type, int):
            raise TypeError("Параметр должен быть типа int")
        if oldest_age_of_tree_type <= 0:
            raise ValueError("Параметр должен быть положительным числом")
        ...

    def update_tree_parameters(self, added_age: int, added_height: float) -> None:
        """
        Функция обновления параметров дерева.
        :param added_age: Добавление возраста дерева (лет)
        :param added_height: Добавление длины дерева в метрах

        :return: Итоговые возраст и длина дерева

        Примеры:
        >>> birch = Tree(150, 34)
        >>> birch.update_tree_parameters(2, 0.02)
        """
        if not isinstance(added_age, int):
            raise TypeError("Добавленный возраст должен быть типа int")
        if added_age <= 0:
            raise ValueError("Добавленный возраст должен быть положительным числом")
        ...

        if not isinstance(added_height, (int, float)):
            raise TypeError("Добавленная высота должна быть типа int или float")
        if added_height < 0:
            raise ValueError("Добавленная высота должна быть положительным числом или нулем")
        ...


class CourierResults:
    def __init__(self, work_hours: float, orders_count: int):
        """
        Создание и подготовка к работе объекта "Результаты курьера"

        :param work_hours: Количество проработанных часов за определенный период
        :param orders_count: Количество отработанных заказов за определенный период

        Пример (результаты за месяц):
        >>> courier = CourierResults(122.3, 493)  # инициализация экземпляра класса
        """
        if not isinstance(work_hours, (int, float)):
            raise TypeError("Количество проработанных часов должно быть типа int или float")
        if work_hours < 0:
            raise ValueError("Количество проработанных часов должно быть положительным числом")
        self.work_hours = work_hours

        if not isinstance(orders_count, int):
            raise TypeError("Количество отработанных заказов должно быть int")
        if orders_count < 0:
            raise ValueError("Количество отработанных заказов не может быть отрицательным числом")
        self.orders_count = orders_count

    def calculate_hours_efficiency(self, hours_plan: float) -> None:
        """
        Сравнение отработанных часов с плановым показателем, рассчет эффективности по часам работы.

        :param hours_plan: Плановый показатель отработанных часов

        :return: Процент выполнения плана по часам работы

        Примеры:
        >>> courier = CourierResults(122.3, 493)
        >>> courier.calculate_hours_efficiency(160)
        """
        if not isinstance(hours_plan, (int, float)):
            raise TypeError("Плановый показатель отработанных часов должен быть типа int или float")
        if hours_plan <= 0:
            raise ValueError("Плановый показатель отработанных часов должен быть положительным числом")
        ...

    def calculate_orders_efficiency(self, orders_plan: int) -> None:
        """
        Сравнение отработанных заказов с плановым показателем, рассчет эффективности по заказам.

        :param orders_plan: Плановый показатель отработанных заказов

        :return: Процент выполнения плана по заказам

        Примеры:
        >>> courier = CourierResults(122.3, 493)
        >>> courier.calculate_orders_efficiency(800)
        """
        if not isinstance(orders_plan, int):
            raise TypeError("Плановый показатель отработанных заказов должен быть типа int")
        if orders_plan <= 0:
            raise ValueError("Плановый показатель отработанных заказов должен быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
