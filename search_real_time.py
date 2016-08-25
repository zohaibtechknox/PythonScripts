import time, os

#Set the filename and open the file
filename = 'path/to/file/abc.log'
file = open(filename,'r')

#Find the size of the file and move to the end
st_results = os.stat(filename)
st_size = st_results[6]
file.seek(st_size)

while 1:
    where = file.tell()
    line = file.readline()
    if "search string" in line:
        time.sleep(1)
        file.seek(where)
        print line
        break
