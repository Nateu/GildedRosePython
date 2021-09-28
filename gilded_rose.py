class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class AgedBrieItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Aged Brie", sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1


class BackstagePassesItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)

    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = 0


class SulfurasItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def update_quality(self):
        pass


class ConjuredItem(Item):
    def __init__(self, sell_in: int, quality: int):
        super().__init__("Conjured butter", sell_in, quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 2
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 2


class GenericItem(Item):
    def __init__(self, name: str, sell_in: int, quality: int):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1


class ItemFactory:
    def createItem(self, name: str, sell_in: int, quality: int):
        if name == "Aged Brie":
            return AgedBrieItem(sell_in=sell_in, quality=quality)
        elif name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassesItem(sell_in=sell_in, quality=quality)
        elif name == "Sulfuras, Hand of Ragnaros":
            return SulfurasItem(sell_in=sell_in, quality=quality)
        elif name == "Conjured butter":
            return ConjuredItem(sell_in=sell_in, quality=quality)
        else:
            return GenericItem(name=name, sell_in=sell_in, quality=quality)


class GildedRose:
    def __init__(self, items: [Item]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
