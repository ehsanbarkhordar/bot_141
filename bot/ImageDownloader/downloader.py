import asyncio

import aiohttp

from bot.Utils.utils import my_logger


async def async_request(callback, state):
    url = "https://images.141.ir/Province/{state}.jpg".format(state=state)
    future = asyncio.Future()
    my_logger.info("Url = {}".format(url))
    future.add_done_callback(callback)
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            data = await response.content.read()
            # try:
            #     data = await response.text()
            # except Exception as e:
            #     pass
            response_dict = {
                "status": response.status,
                "content": data
            }
            future.set_result(response_dict)