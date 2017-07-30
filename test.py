import asyncio
from goroutine import goroutine, yield_from, yield_from_or_block


@asyncio.coroutine
def main():
    print('[main] start')
    result = yield from myclet(3)
    print('[main] result =', result)


@goroutine
def except_goroutine():
    raise ValueError('[except_goroutine] exception thrown')


@asyncio.coroutine
def except_coroutine():
    raise ValueError('[except_coroutine] exception thrown')


@goroutine
def myclet(num):
    print('[myclet] start with num =', num)
    result = yield_from(subcoro(num))
    print('[myclet] result =', result)
    try:
        yield_from(except_goroutine())
    except ValueError as e:
        print(str(e))
    else:
        raise SystemError()

    try:
        yield_from(except_coroutine())
    except ValueError as e:
        print(str(e))
    else:
        raise SystemError()

    subfunc_sleep(.5)
    return result * 2


@asyncio.coroutine
def subcoro(num):
    print('[subcoro] start with num =', num)
    return num * 2


def subfunc_sleep(time):
    print('[subfunc_sleep] sleeping for', time)
    yield_from_or_block(asyncio.sleep(time))
    print('[subfunc_sleep] done sleeping')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

subfunc_sleep(.5)
