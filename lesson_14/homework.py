import asyncio
import aiohttp
import logging

# Create a list of URLs to scrape.
urls_to_scrape = ["https://example.com", "https://example.net"]

# Use asyncio's semaphore to limit the number of concurrent requests.
semaphore = asyncio.Semaphore(10)  

# Use asyncio queues to manage the URLs to be scraped and the retrieved data to be saved to a file.
url_queue = asyncio.Queue()
data_queue = asyncio.Queue()

# Add logging to the scraper to monitor its progress and handle errors.
logging.basicConfig(level=logging.INFO)

# Use the aiohttp library to make HTTP requests instead of the built-in urllib library.

async def scrape_url(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.text()
                        await data_queue.put(data)
                        logging.info(f"Successfully fetched {url}")
                    else:
                        logging.error(f"Failed to fetch {url}. Status code: {response.status}")
            except aiohttp.ClientError as e:
                logging.error(f"Error while fetching {url}: {str(e)}")

async def save_data_to_file():
    while True:
        data = await data_queue.get()

# Use asyncio tasks to execute the scraping and saving functions asynchronously.
async def main():

    save_task = asyncio.create_task(save_data_to_file())


    for url in urls_to_scrape:
        await url_queue.put(url)


    tasks = []
    for _ in range(len(urls_to_scrape)):
        task = asyncio.create_task(scrape_url(await url_queue.get()))
        tasks.append(task)


    await asyncio.gather(*tasks)


    await data_queue.put(None)
    await save_task

# Use asyncio's event loop to schedule tasks at specific intervals.
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())