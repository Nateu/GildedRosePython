import unittest
from approvaltests import combination_approvals
from gilded_rose import Item, GildedRose


def doUpdateItem(name: str, sell_in: int, quality: int):
    item = Item(name, sell_in, quality)
    app = GildedRose([item])
    app.update_quality()
    return str(app.items[0])


class GildedRoseTest(unittest.TestCase):
    def test_main(self):
        combination_approvals.verify_all_combinations(doUpdateItem, [
            [
                'foo',
                'Aged Brie',
                'Backstage passes to a TAFKAL80ETC concert',
                'Sulfuras, Hand of Ragnaros'
            ], [
                -1,
                2,
                0,
                6,
                11
            ], [
                0,
                1,
                49,
                50
            ]
        ])

    def test_new_conjured_item_quality_degrades_twice_as_fast_as_normal_items(self):
        conjured_item = Item(name = "Magic desk of cards", sell_in = 5, quality = 20)
        shop = GildedRose([conjured_item])
        shop.update_quality()
        assert shop.items[0].quality == 18


if __name__ == "__main__":
    unittest.main()
