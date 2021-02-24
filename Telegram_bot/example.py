# import asyncio
# import aiohttp

# async def fetch(session: aiohttp.ClientSession) -> None:
#     params = [('key', 'value1'), ('key', 'value2')]
#     async with session.get("http://0.0.0.0:8080/get_all_confs", params=params) as resp:
#         print('http://httpbin.org/get?key=value2&key=value1')
#         print(resp.status)
#         data = await resp.json()
#         print(data)

# async def go() -> None:
#     async with aiohttp.ClientSession() as session:
#         await fetch(session)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(go())
# loop.close()

# -----

# import asyncio
# import aiohttp

# async def fetch(session: aiohttp.ClientSession) -> None:
#     params = [('conf_id', 'hello')]
#     async with session.get("http://0.0.0.0:8080/get_conf_themes", params=params) as resp:
#         # print('http://httpbin.org/get?key=value2&key=value1')
#         print(resp.status)
#         data = await resp.json()
#         print(data)


# async def go() -> None:
#     async with aiohttp.ClientSession() as session:
#         await fetch(session)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(go())
# loop.close()

# ----------

# import asyncio
# import aiohttp

# async def fetch(session: aiohttp.ClientSession) -> None:
#     params = {'event_id': '01art10', 'conf_options': '100', 'user_id':['hello', 'world']}
#     # params = [('conf_id', 'hello'), ('user_id', ['asdf','a12'])]
#     async with session.post("http://0.0.0.0:8080/set_user_remind_for_event", params=params) as resp:
#         # print('http://httpbin.org/get?key=value2&key=value1')
#         print(resp.status)
#         data = await resp.json()
#         print(data)


# async def go() -> None:
#     async with aiohttp.ClientSession() as session:
#         await fetch(session)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(go())
# loop.close()

# ---

import asyncio
import aiohttp

async def fetch(session: aiohttp.ClientSession) -> None:
    params = {'event_id': '01art10', 'conf_options': '100', 'user_id':['hello', 'world']}
    # params = [('conf_id', 'hello'), ('user_id', ['asdf','a12'])]
    async with session.delete("http://0.0.0.0:8080/del_user_remind_for_event", params=params) as resp:
        # print('http://httpbin.org/get?key=value2&key=value1')
        print(resp.status)
        data = await resp.json()
        print(data)


async def go() -> None:
    async with aiohttp.ClientSession() as session:
        await fetch(session)

loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()