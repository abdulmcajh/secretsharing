import subprocess
import time

i=0
while (i<4):
	time.sleep(5)
	subprocess.Popen("python Client.py",shell=True)
	i+=1
