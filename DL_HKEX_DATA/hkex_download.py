import os
import requests
import time
import sys, getopt

print('len: ',len(sys.argv))
print('list',str(sys.argv))

file_dir = os.path.dirname(os.path.abspath(__file__))
print(file_dir)
## Open file
if len(sys.argv)>1:
  lines = ['https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsio'+sys.argv[1]+'.zip','https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhio'+sys.argv[1]+'.zip','https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsif'+sys.argv[1]+'.zip','https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhif'+sys.argv[1]+'.zip']
else:
  fp = open(file_dir+'\\download.list.txt',"r")
  lines = fp.readlines()
  fp.close()

for i in range(len(lines)):
  url =lines[i].rstrip('\n')
  myfile  = requests.get(url)
  filename = url.rsplit('/',1)[1]
  print(url)
  open('C:\\Users\\Mathus\\Documents\\Google Drive\\download_data\\hkex.data\\'+filename,'wb').write(myfile.content)
  time.sleep(1)


