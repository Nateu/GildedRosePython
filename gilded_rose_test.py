import unittest
from approvaltests import combination_approvals
from gilded_rose import ItemFactory, GildedRose

def doUpdateItem(name: str, sell_in: int, quality: int, days: int) -> str:
    item_factory = ItemFactory()
    item = item_factory.createItem(name=name, sell_in=sell_in, quality=quality)
    app = GildedRose([item])
    while days > 0:
        app.update_quality()
        days -= 1
    return str(app.items[0])

class GildedRoseTest(unittest.TestCase):
    def test_main(self):
        combination_approvals.verify_all_combinations(doUpdateItem, [[
            'foo', 'Aged Brie', 'Backstage passes to a TAFKAL80ETC concert',
            'Sulfuras, Hand of Ragnaros', 'Conjured butter'
        ], [-1, 0, 2, 6, 11], [0, 1, 49, 50, 60], [1, 2, 5, 6, 7, 10, 11, 12, 20, 30]])


if __name__ == "__main__":
    unittest.main()
