# return process memory usage in MB
import psutil
import threading
def print_memory():
	process = psutil.Process(1673)
	mem = process.memory_info_ex()[0] / float(2 ** 20)
	threading.Timer(0.7, print_memory).start()
	print(mem)
print_memory()
