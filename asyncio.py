import logging
import os
from time import time
import asyncio

import aiohttp
from download import setup_download_dir, get_links


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# We will decorate this function to donwload asynchorously instead of synchorously
# Use the aysn decorator
@asyncio.coroutine
def async_download_link(directory, link):
	download_path = directory / os.path.basename(link)
	#using yield
	response = yield from aiohttp.request
	with download_path.open('wb') as f:
		while True:
			chunk = yield  from response.content.read(1000)
			if not chunk:
				break
			f.write(chunk)
	logger.info('Downloaded %s', link)

def main():
	st= time()
	client_id = 'ee43c9d73f7dcc9'
	if not client_id:
		raise Exception("Couldn't find IMGUR_CLIENT_ID enviroment variable")
	download_dir = setup_download_dir()
	loop = asyncio.get_event_loop()
	#Instead of asyncio.async you can use loop.create_task, but loop.create_task is only avaible
	# in python >=3.4.2
	tasks = [asyncio.async(async_download_link(download_dir, l)) for l in get_links(client_id)]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()
	logger.info('Took %s seconds to complete', time() -st)

if __name__ == '__main__':
	main()