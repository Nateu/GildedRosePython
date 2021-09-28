# Goal

Teach / show people how to refactor legacy code, but before they even begin, how to take a snapshot of the current situation first using approval testing. The example used here is based on the well-known [Gilded Rose kata by Emily Bache](https://github.com/emilybache/GildedRose-Refactoring-Kata), but then in the updated version of [Gil Gonçalves](https://github.com/LuRsT/gilded_rose_kata).

## Approval tests and coverage reports

By default, approval tests are run, coverage reports are generated and served via an HTTP server, that is equipped with a hot reload. So no further manual actions are needed but a press on the run button.

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

## Refactoring vids by Emily Bache

[Part 1](https://www.youtube.com/watch?v=zyM2Ep28ED8)  
Preperation:
Create a code coverage of 100%, make sure you hit all branches!
Use mutation testing to see if you have a stringent enough test set.

[Part 2](https://www.youtube.com/watch?v=OJmg9aMxPDI)  
This kata! Refactoring the code: "Lift up coditional"

[Part 3](https://www.youtube.com/watch?v=NADVhSjeyJA)  
Possible in this kata if time allows, refactoring coditional behaviour with polymorphism

## References

- [Approval tests in Python](https://github.com/approvals/approvaltests.Python)
- [Emily Bache's version of the Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata)
- [The updated version to Python 3 of Emily's version](https://github.com/LuRsT/gilded_rose_kata)
- [Run webserver locally](https://gist.github.com/willurd/5720255)

### Books by Emily Bache
https://leanpub.com/b/codekatas
