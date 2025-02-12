if __name__ == "__main__":
    class Tree:
        """ Базовый класс дерева. """
        def __init__(self, height: float, age: int) -> None:
            """
            Инициализация базового класса Tree.

            Все атрибуты класса защищены инкапсуляцией с целью спрятать их от прямого доступа пользователя
            :param height: Высота дерева в метрах.
            :param age: Возраст дерева в годах.
            """
            self._height = None  # Защищенный атрибут для высоты
            self._age = None  # Защищенный атрибут для возраста
            self.height = height  # Устанавливаем высоту через setter
            self.age = age  # Устанавливаем возраст через setter

        @property
        def height(self) -> float:
            """Возвращает высоту дерева."""
            return self._height

        @height.setter
        def height(self, height: float) -> None:
            """Устанавливает высоту дерева."""
            if not isinstance(height, (int, float)):
                raise TypeError("Высота должна быть числом (int или float)")
            if height <= 0:
                raise ValueError("Высота должна быть положительным числом")
            self._height = height  # Устанавливаем значение защищенному атрибуту

        @property
        def age(self) -> int:
            """Возвращает возраст дерева."""
            return self._age

        @age.setter
        def age(self, age: int) -> None:
            """Устанавливает возраст дерева."""
            if not isinstance(age, int):
                raise TypeError("Возраст должен быть типа int")
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным числом")
            self._age = age  # Устанавливаем значение защищенному атрибуту

        def grow(self, increase: float) -> None:
            """
            Метод увеличивает высоту дерева на заданную высоту.

            :param increase: Увеличение высоты в метрах.
            """
            self._height += increase

        def increment_age(self, years: int) -> None:
            """
            Метод увеличивает возраст дерева на заданное количество лет.

            :param years: Количество лет для добавления к возрасту.
            """
            self._age += years

        def __str__(self) -> str:
            return f"Дерево высотой {self._height} метров, {self._age} лет"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(height={self._height!r}, age={self._age!r})"


    class Conifer(Tree):
        """
        Дочерний класс для Tree.
        Методы __str__ и increment_age унаследованы
        """
        def __init__(self, height: float, age: int, tree_type: str) -> None:
            """
            Инициализация класса Conifer (хвойное дерево).

            :param height: Высота дерева в метрах.
            :param age: Возраст дерева в годах.
            :param tree_type: Вид хвойного дерева.
            """
            super().__init__(height, age)
            self.tree_type = tree_type  # Атрибут для вида хвойного дерева

        def grow(self, increase: float) -> None:
            """
            Увеличивает высоту дерева. Метод перегружен, т.к. в отличие от базового класса,
            средний рост хвойного дерева обычно превышает рост среднего дерева на 20%.

            :param increase: Увеличение высоты в метрах.
            """
            super().grow(increase * 1.2)  # Хвойные деревья растут быстрее на 20%

        def __repr__(self) -> str:
            """
            Метод перегружен для добавления доп. атрибута в строку
            """
            return f"{self.__class__.__name__}(type={self.tree_type!r}, height={self._height!r}, age={self._age!r})"
    pass
