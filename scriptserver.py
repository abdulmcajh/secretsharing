import subprocess
import time
i=0
while (i<10):
	time.sleep(2)
	subprocess.call(["nc", "127.0.0.1", "9999","&"])
	print("launched" + i)
	i=i+1
