# Goal

Teach / show people how to refactor legacy code, but before they even begin, how to take a snapshot of the current situation first using approval testing. The example used here is based on the well-known [Gilded Rose kata by Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata), but then in the updated version of [Gil Gonçalves](https://github.com/LuRsT/gilded_rose_kata).

## Todo:

### Step 1
 Refactoring the code: "Lift up coditional"

### Step 2  
Continue to refacture until your satisfied, then add a new item 'Conjured' as described in Original specs of Gilded Rose (below). Use things like exctracting method.

### Step 3  
The goblin died!! Now add a item type for all situations:
* Chees that ages
* Tickets that lose their value once the sell_in is <= 0
* Normal items
* Conjured items
* Legendary items


## Approval tests and coverage reports

By default, approval tests are run, coverage reports are generated and served via an HTTP server, that is equipped with a hot reload. So no further manual actions are needed but a press on the run button.


## Refactoring vids by Emily Bache

### [Part 1](https://www.youtube.com/watch?v=zyM2Ep28ED8)  
Preperation:
Create a code coverage of 100%, make sure you hit all branches!
Use mutation testing to see if you have a stringent enough test set.

### [Part 2](https://www.youtube.com/watch?v=OJmg9aMxPDI)  
 Refactoring the code: "Lift up coditional"

### [Part 3](https://www.youtube.com/watch?v=NADVhSjeyJA)  
Possible in this kata if time allows, refactoring coditional behaviour with polymorphism

## References

- [Approval tests in Python](https://github.com/approvals/approvaltests.Python)
- [Emily Bache's version of the Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata)
- [The updated version to Python 3 of Emily's version](https://github.com/LuRsT/gilded_rose_kata)
- [Run webserver locally](https://gist.github.com/willurd/5720255)

### Books by Emily Bache
https://leanpub.com/b/codekatas


## Running manually

To run tests and update code coverage report:
```bash
$ make
```

To have a server that will display code coverage:
```bash
$ make serv
```

After each run, the HTML reports and view are live updated (hot reload)!


## Original specs of Gilded Rose:

> Gilded Rose Requirements Specification
> 
> Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We
have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
we can begin selling a new category of items. First an introduction to our system:
>
>	- All items have a SellIn value which denotes the number of days we have to sell the item
>	- All items have a Quality value which denotes how valuable the item is
>	- At the end of each day our system lowers both values for every item
>
> Pretty simple, right? Well this is where it gets interesting:
>
>	- Once the sell by date has passed, Quality degrades twice as fast
>	- The Quality of an item is never negative
>	- "Aged Brie" actually increases in Quality the older it gets
>	- The Quality of an item is never more than 50
>	- "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
>	- "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
>     - Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
>	  - Quality drops to 0 after the concert
>
> We have recently signed a supplier of conjured items. This requires an update to our system:
>
>	- "Conjured" items degrade in Quality twice as fast as normal items
>
> Feel free to make any changes to the UpdateQuality method and add any new code as long as everything
still works correctly. However, do not alter the Item class or Items property as those belong to the
goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover
for you).
>
> Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.