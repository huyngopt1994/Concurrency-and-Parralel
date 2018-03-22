import json
import logging
import os
from pathlib import Path
from urllib.request import urlopen, Request

logger = logging.getLogger(__name__)

def get_links(client_id):
	"""Generate the links and send it to get link."""
	headers ={'Authorization': 'Client-ID {}'.format(client_id)}
	# generate http request
	request = Request(' https://api.imgur.com/3/album/PKRo4/images', headers=headers, method='GET')
	with urlopen(request) as resp:
		data = json.loads(resp.read().decode('utf-8'))
	return map(lambda item: item['link'], data['data'])

def download_link(directory, link):
	print (link)
	logger.info('Downloading %s', link)
	#generate a download path = directory + base name of link
	download_path = directory / os.path.basename(link)
	# send a request and open file
	with urlopen(link) as image, download_path.open('wb') as f:
		f.write(image.read())

def setup_download_dir():
	"""Create download destination directory if its doesn't already exists."""
	download_dir = Path('images')
	if not download_dir.exists():
		download_dir.mkdir()

	return download_dir