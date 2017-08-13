import sys
import requests
import shutil
import os 

m3u8 = str(sys.argv[1])
videoName = str(sys.argv[2])

with open('./videos/m3u8/'+m3u8, 'r') as f:
    tslist = [line.rstrip() for line in f if line.rstrip().endswith('.ts')]
print 'Total '+ str(len(tslist)) +' ts files'

index = 1
tsNames = []
for tsUrl in tslist[0:3]:
    res = requests.get(tsUrl, stream=True)
    if res.status_code == 200:
        with open('./videos/tmp/'+videoName[0:-3]+'_'+str(index)+'.ts', 'wb') as f:
            for chunk in res:
                f.write(chunk)
        print videoName[0:-3]+'_'+str(index)+' downloaded\r',
        tsNames.append(videoName[0:-3]+'_'+str(index)+'.ts')
        index += 1

with open('./videos/'+videoName, 'wb') as f:
    for ts in tsNames:
        with open('./videos/tmp/'+ts, 'rb') as mergefile:
            shutil.copyfileobj(mergefile, f)
        os.remove('./videos/tmp/'+ts)
    print videoName+' merged'