class GildedRose:

    def __init__(self, items):
        self.items = items

    def increase_item_quality_by_1_if_below_50(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrease_item_quality_by_1_if_above_0(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def decrease_sell_in_by_1(self, item):
        item.sell_in = item.sell_in - 1
    
    def update_item(self, item):
        if item.name == "Aged Brie":
            self.increase_item_quality_by_1_if_below_50(item)
            self.decrease_sell_in_by_1(item)
            if item.sell_in < 0:
                self.increase_item_quality_by_1_if_below_50(item)

        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.quality < 50:
                self.increase_item_quality_by_1_if_below_50(item)
                if item.sell_in < 11:
                    self.increase_item_quality_by_1_if_below_50(item)
                if item.sell_in < 6:
                    self.increase_item_quality_by_1_if_below_50(item)
            self.decrease_sell_in_by_1(item)
            if item.sell_in < 0:
                item.quality = 0

        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass

        else:
            self.decrease_item_quality_by_1_if_above_0(item)
            self.decrease_sell_in_by_1(item)
            if item.sell_in < 0:
                self.decrease_item_quality_by_1_if_above_0(item)

    def update_quality(self):
        for item in self.items:
            self.update_item(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
