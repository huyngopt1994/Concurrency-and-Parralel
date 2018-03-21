import logging
import os
from time import time

from download import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL) #ignore it
logger = logging.getLogger(__name__)

def main():
	st = time()
	client_id = 'ee43c9d73f7dcc9'
	if not client_id:
		raise Exception("Couldn't find IMGUR_CLIENT environment variable")
	download_dir = setup_download_dir()
	links = [l for l in get_links(client_id) if l.endswith('.jpg')]
	for link in links:
		download_link(download_dir, link)
	print('Took {}s'.format(time() - st))

if __name__ == '__main__':
	#10.18704867362976s
	main()