import sys
import requests
import shutil
import os 

m3u8 = str(sys.argv[1])
videoName = str(sys.argv[2])

with open(m3u8, 'r') as f:
    tslist = [line.rstrip() for line in f if line.rstrip().endswith('.ts')]
if len(tslist) > 0:
    print 'Total '+ str(len(tslist)) +' files'
else:
    print 'No ts file found.'
    exit()

index = 1
tsNames = []
for tsUrl in tslist:
    videoNameTmp = videoName[0:-3]+'_'+str(index)+videoName[-3:]
    if not os.path.isfile('./videos/tmp/'+videoNameTmp):
        res = requests.get(tsUrl, stream=True)
        if res.status_code == 200:
            with open('./videos/tmp/'+videoNameTmp, 'wb') as f:
                for chunk in res:
                    f.write(chunk)
            print videoNameTmp+' downloaded\r',
        else:
            print '\nConnection error'
            exit()
    tsNames.append(videoNameTmp)
    index += 1

if index == len(tslist)+1:
    with open('./videos/'+videoName, 'wb') as f:
        for ts in tsNames:
            with open('./videos/tmp/'+ts, 'rb') as mergefile:
                shutil.copyfileobj(mergefile, f)
            os.remove('./videos/tmp/'+ts)
        print videoName+' merged.'
else:
    print 'Merge failed, missing files.'