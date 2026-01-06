import aiohttp, zlib, datetime, json, os

async def atualizar_ranking(server):
    hoje = datetime.date.today().strftime("%Y-%m-%d")
    url = f"https://files.kakele.io/rankings/{server}-{hoje}.zlib"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return False

            raw = await resp.read()
            text = zlib.decompress(raw).decode("utf-8")

            os.makedirs("data", exist_ok=True)
            with open("data/ranking.json", "w", encoding="utf-8") as f:
                json.dump(text.splitlines(), f)

            return True
