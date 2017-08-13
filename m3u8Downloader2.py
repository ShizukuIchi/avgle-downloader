import sys
import requests
import shutil

m3u8 = str(sys.argv[1])
videoName = str(sys.argv[2])

with open('./video/m3u8/'+m3u8, 'r') as f:
    tslist = [line.rstrip() for line in f if line.rstrip().endswith('.ts')]
print 'Total '+ str(len(tslist)) +' files'
print ' '

index = 1
tsNames = []
for tsUrl in tslist:
    res = requests.get(tsUrl, stream=True)
    if res.status_code == 200:
        with open('./videos/tmp/'+videoName[0:-3]+str(index)+'.ts', 'wb') as f:
            for chunk in res:
                f.write(chunk)
        print videoName[0:-3]+str(index)+'.ts downloaded\r',
        tsNames.append(videoName[0:-3]+str(index)+'.ts')
        index += 1

with open('./videos/'+videoName, 'wb') as f:
    for ts in tsNames:
        with open('./videos/tmp/'+ts, 'rb') as mergefile:
            shutil.copyfileobj(mergefile, f)
        print videoName+' merged in videos folder'