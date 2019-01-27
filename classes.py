class Item:
    def __init__(self, name, category, price, count=1):
        self.name = name
        self.count = count
        self.category = category
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name:
            if isinstance(name, str):
                if name.isalpha():
                    self.__name = name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if category:
            if isinstance(category, str):
                if category.isalpha():
                    self.__category = category.upper()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price:
            if isinstance(price, int) or isinstance(price, float):
                self.__price = price * self.count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        pass

    def __str__(self):
        return str(
            "name = {}, category = {}, price = {} , count = {}"
        ).format(self.name, self.category, self.price, self.count)

    def __repr__(self):
        return str(
            "name = {}, category = {}, price = {} , count = {}"
        ).format(self.name, self.category, self.price, self.count)


class ContinuousItem(Item):

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count:
            if isinstance(count, float):
                self._count = count


class DiscreteItem(Item):

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        if count:
            if isinstance(count, int):
                self._count = count

class Items:

    def __init__(self):
        self.items = dict()

    def add_item(self, item):
        if item:
            if isinstance(item, Item):
                category = item.category
                items = list(self.items.get(category))
                items.append(items)
                self.items[self.items.get(item.category)] = items