import asyncio
import time
import aiohttp


devices = ['192.168.2.60', '192.168.2.61', '192.168.2.62',
           '192.168.2.50', '192.168.2.51', '192.168.2.52',
           '192.168.2.60', '192.168.2.61', '192.168.2.62',
           '192.168.2.50', '192.168.2.51', '192.168.2.52'
           ]


async def worker(i, ip, session):
    time.sleep(1)
    print(f"I am session: {i}")
    url = f"http://127.0.0.1:8000/ip/{ip}/version"
    response = await session.request(method='GET', url=url)
    return {"response:": response}


async def main():
    async with aiohttp.ClientSession() as session:
        # asyncio.gather creates tasks in one shot
        combined_results = await asyncio.gather(*(worker(f'{i}', ip, session) for i, ip in enumerate(devices)))
        for result in combined_results:
            print(f'***** {result} *****')


if __name__ == "__main__":
    start = time.perf_counter()
    # introduced in 3.7, handles event loop
    # Pre-3.7 asyncio.get_event_loop().run_until_complete()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"executed in {elapsed} seconds.")


