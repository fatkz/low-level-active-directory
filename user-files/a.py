import time






timezone = time.time()
rtime = time.localtime(timezone)

print("{0}:{1}/{2}/{3}/{4}".format(rtime.tm_hour,rtime.tm_min,rtime.tm_mday,rtime.tm_mon,rtime.tm_year))