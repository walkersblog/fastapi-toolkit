import httpx


async def get_joke_async():
    url = f'https://official-joke-api.appspot.com/random_joke'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()
