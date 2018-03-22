from functools import partial
from multiprocessing.pool import Pool
from time import time
from download import *

def main():
	st = time()
	client_id = 'ee43c9d73f7dcc9'
	if not client_id:
		raise Exception("Couldn't find IMGUR_CLIENT_ID enviroment variable!")
	download_dir = setup_download_dir()
	links = [l for l in get_links(client_id) if l.endswith('jpg') or l.endswith('.png')]
	download = partial(download_link, download_dir)
	# Create a pool with 8 entries
	with Pool(16) as p:
		p.map(download,links)

	print ('Took {}s'.format(time()- st))
if __name__ == "__main__":
	# 2.9s
	main()