import aiohttp

async def buscar_eventos(server):
    url = f"https://files.kakele.io/events/{server}?cache=disable"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None
            return await resp.json()
