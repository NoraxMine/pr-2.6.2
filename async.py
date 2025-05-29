import asyncio
import aiohttp
import time


urls = ["https://httpbin.org/get"] * 10  # 10 одинаковых запросов для примера

# Синхронные запросы
def sync_requests():
    import requests
    start = time.time()
    for url in urls:
        requests.get(url).status_code #отправляет запрос на указанный url, ожидает ответ от сервера и возвращает объект
    return time.time() - start

# Асинхронные запросы
async def async_requests():
    async with aiohttp.ClientSession() as session: #открывает асинхронную HTTP-сессию
        tasks = []
        start = time.time()
        for url in urls:
            tasks.append(session.get(url)) #одновременно отправляет все запросы, ждет их завершения
        responses = await asyncio.gather(*tasks)
        return time.time() - start

# Запуск
print(f"Синхронные запросы: {sync_requests():.2f} сек")
print(f"Асинхронные запросы: {asyncio.run(async_requests()):.2f} сек")


# requests.get(url) — работает синхронно (каждый запрос ждет ответа, перед тем как начать следующий).
# aiohttp.ClientSession().get(url) — работает асинхронно, позволяя выполнять несколько запросов одновременно.