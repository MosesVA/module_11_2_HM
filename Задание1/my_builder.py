class Tiler:
    """Класс плиточник"""

    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def floor_preparation(self):
        self._product.add('Подготовка пола')

    def tile_laying(self):
        self._product.add('Укладка плитки')


class Finisher:
    """Класс отделочник"""

    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def putty(self):
        self._product.add('Нанести шпаклевку')

    def plaster(self):
        self._product.add('Оштукатурить стены')


class Painter:
    """Класс маляр"""

    def __init__(self):
        self._product = None
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def primer(self):
        self._product.add('Загрунтовать стену')

    def paint_the_wall(self):
        self._product.add('Покрасить стену')


class Foreman:
    """Класс прораб"""

    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder: object):
        self._builder = builder

    def make_floor(self):
        self.builder.floor_preparation()
        self.builder.tile_laying()

    def level_the_walls(self):
        self.builder.putty()
        self.builder.plaster()

    def paint_walls(self):
        self.builder.primer()
        self.builder.paint_the_wall()


class Product:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Части продуктов: {", ".join(self.parts)}')


if __name__ == '__main__':
    foreman = Foreman()
    builder1 = Tiler()
    builder2 = Finisher()
    builder3 = Painter()

    print('Сделать полы.')
    foreman.builder = builder1
    foreman.make_floor()
    builder1.product.list_parts()

    print()

    print('Выровнять стены.')
    foreman.builder = builder2
    foreman.level_the_walls()
    builder2.product.list_parts()

    print()

    print('Покрасить стены.')
    foreman.builder = builder3
    foreman.paint_walls()
    builder3.product.list_parts()

    print()

    print('Сделать все под ключ.')
    foreman.builder = builder1
    foreman.make_floor()
    builder1.product.list_parts()

    foreman.builder = builder2
    foreman.level_the_walls()
    builder2.product.list_parts()

    foreman.builder = builder3
    foreman.paint_walls()
    builder3.product.list_parts()
