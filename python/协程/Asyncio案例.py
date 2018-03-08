import asyncio
async def do_some_work(x):
    print('Waiting'+str(x))
    await asyncio.sleep(x)
    print('等待',x,'秒结束')
# coroutine	协程 iscoroutinefunction 是协程函数吗?
# print(asyncio.iscoroutinefunction(do_some_work))
# print(asyncio.iscoroutine(do_some_work(3))) # True
loop = asyncio.get_event_loop()
# loop.run_until_complete(do_some_work(3))
# loop.run_until_complete(asyncio.ensure_future(do_some_work(3)))

def done_callback(futu):
    print('Done')

# futu = asyncio.ensure_future(do_some_work(3))
# 顺序写法写回调函数,不要写js那么蛋疼的回调了
# 执行完 do_some_work,自动执行done_callback
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)


# loop.run_until_complete(asyncio.gather(do_some_work(1), do_some_work(3)))

# loop = asyncio.get_event_loop()

# asyncio.ensure_future(do_some_work(3))

# loop.run_forever()


# async def do_some_work(loop, x):
#     print('Waiting ' + str(x))
#     await asyncio.sleep(x)
#     print('Done')
#     loop.stop()

# loop = asyncio.get_event_loop()
# asyncio.ensure_future(do_some_work(loop, 1))
# asyncio.ensure_future(do_some_work(loop, 88))
# loop.run_forever()

# async def do_some_work(loop, x):
#     print('Waiting ' + str(x))
#     await asyncio.sleep(x)
#     print('Done')
#
#
# def done_callback(loop, futu):
#     loop.stop()
#
#
# loop = asyncio.get_event_loop()
# import functools
# futus = asyncio.gather(do_some_work(loop, 1), do_some_work(loop, 3))
# futus.add_done_callback(functools.partial(done_callback, loop))
# loop.run_forever()
# loop.run_until_complete(do_some_work(loop, 1))
# loop.run_until_complete(do_some_work(loop, 3))
# loop.close()

async def timer(x, cb):
    futu = asyncio.ensure_future(asyncio.sleep(x))
    futu.add_done_callback(cb)
    await futu

t = timer(3, lambda futu: print('Done'))
loop.run_until_complete(t)