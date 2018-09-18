import aiohttp
import asyncio

import settings


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.DATA_URL) as resp:
            print(resp.status)
            print(await resp.text())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
