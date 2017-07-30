# goroutine

Use [greenlets](http://greenlet.readthedocs.org/) as coroutines in [asyncio](https://docs.python.org/3/library/asyncio.html).

A **goroutine** (a green coroutine) is a coroutine compatible with `asyncio.coroutine`s. However, instead of using the
`yield from` or `await` keywords to delegate to another coroutine, goroutines use a function `goroutine.yield_from`,
allowing subfunctions of a coroutine to schedule other coroutines.

The idea for goroutine was inspired by [greenio](https://github.com/1st1/greenio).

## Usage

Create goroutines using `goroutine.goroutine` decorator. Instead of the `yield from` keyword, use `goroutine.yield_from`
to get a result from an `asyncio.Future`.

```py3
import asyncio
from goroutine import goroutine, yield_from


@goroutine
def my_goroutine():
    print('in a goroutine')

    # Corolets are particularly useful when calling subfunctions.
    return subfunction()


def subfunction():
    print('in a subfunction')

    # Non-goroutine subfunctions can still call yield_from to delegate to
    # another coroutine (or goroutine).
    result = yield_from(subcoro())

    return result


@asyncio.coroutine
def subcoro():
    return 3


@asyncio.coroutine
def main():
    # Corolets are still coroutines and can be called from normal asyncio code.
    result = yield from my_goroutine()

    print(result)     # => 3

if __name__ == '__main__':
    # Goroutines run in the normal event loop.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
