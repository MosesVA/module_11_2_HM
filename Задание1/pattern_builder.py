from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add('Часть A')

    def produce_part_b(self) -> None:
        self._product.add('Часть B')

    def produce_part_c(self) -> None:
        self._product.add('Часть C')


class Product1:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f'Части продуктов {', '.join(self.parts)}')


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print('Базовый продукт: ')
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print()

    print('Продукт со всеми фичами: ')
    director.build_full_featured_product()
    builder.product.list_parts()

    print()

    print('Индивидуальная комплектация: ')
    builder.produce_part_a()
    builder.produce_part_c()
    builder.product.list_parts()

