import asyncio
import aiohttp
import requests
import time


urls = ["https://example.com"] * 100

async def fetch_url(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f"{url}: {response.status}")
        delta =time.time()-start
    print("Время",delta)

def simplefetch_url( url):
    start = time.time()
    for url in urls:
        requests.get(url).status_code
        delta =time.time()-start
    print("Время",delta)

def main():
    asyncio.run(fetch_url())
    simplefetch_url()

