from queue import Queue
from threading import Thread
from download import *
from time import time
class DownloadWorker(Thread):
	def __init__(self,queue, index):
		Thread.__init__(self)
		self.queue = queue
		self.index = index

	def run(self):
		while True:
			# Get the work from the queue and expand the tuple
			directory, link = self.queue.get()
			download_link(directory, link)
			print('thread index {} downloaded {}'.format(self.index, link))
			self.queue.task_done()

def main():
	st = time()
	client_id = 'ee43c9d73f7dcc9'
	download_dir = setup_download_dir()
	links = [l for l in get_links(client_id) if l.endswith('.jpg')]
	#Create a queue to communicate with worker threads
	queue = Queue()

	#Create 4 worker threads
	for x in range(8):
		worker = DownloadWorker(queue,x)
		worker.daemon = True
		worker.start()

	for link in links:
		print('Queueing {}'.format(link))
		queue.put((download_dir, link))

	# Cause the main thread to wait for the queue to finish the processing all the tasks
	queue.join()
	print('Took {}'.format(time() - st))
#because we have 7 pictures so 7 threads will be the best
main()