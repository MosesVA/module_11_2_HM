class Spaghetti:
    def type(self):
        return "Спагетти"

    def sauce(self):
        return "Томатный соус"

    def topping(self):
        return "Фрикадельки"

    def extras(self):
        return "Сыр пармезан"


class Penne:
    def type(self):
        return "Пенне"

    def sauce(self):
        return "Сливочный соус"

    def topping(self):
        return "Курица"

    def extras(self):
        return "Брокколи"


class Fusilli:
    def type(self):
        return "Фузилли"

    def sauce(self):
        return "Соус песто"

    def topping(self):
        return "Креветки"

    def extras(self):
        return "Вяленые помидоры"


class PastaFactory:
    def create_pasta(self, pasta_type):
        if pasta_type == "спагетти":
            return Spaghetti()
        elif pasta_type == "пенне":
            return Penne()
        elif pasta_type == "фузилли":
            return Fusilli()
        else:
            return "Не знаю пасту такого типа!"


if __name__ == "__main__":
    factory = PastaFactory()

    pasta1 = factory.create_pasta("спагетти")
    print(f"Тип: {pasta1.type()}")
    print(f"Соус: {pasta1.sauce()}")
    print(f"Начинка: {pasta1.topping()}")
    print(f"Добавка: {pasta1.extras()}")
    print()

    pasta2 = factory.create_pasta("пенне")
    print(f"Тип: {pasta2.type()}")
    print(f"Соус: {pasta2.sauce()}")
    print(f"Начинка: {pasta2.topping()}")
    print(f"Добавка: {pasta2.extras()}")
    print()

    pasta3 = factory.create_pasta("фузилли")
    print(f"Тип: {pasta3.type()}")
    print(f"Соус: {pasta3.sauce()}")
    print(f"Начинка: {pasta3.topping()}")
    print(f"Добавка: {pasta3.extras()}")
