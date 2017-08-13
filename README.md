m3u8Downloader
===
## Usage
> *Using python 2.7.13 with requests and bs4*
### m3u8Downloader.py  
Open `cmd.exe` for `Windows` or `Terminal` for `Linux`.  
Prepare your m3u8 file into `./vedio/m3u8` folder.
```
# .m3u8 -> .ts

$ python m3u8Downloader.py m3u8_name video_name 
```
Lots of ts files will be downloaded into `./video/tmp` folder named `vedio_nameX.ts` *(X is index)*.  
Once all ts files are downloaded, they will be merged to a file `video_name` into `./video` folder.  

**※ Don't foget** filename extension:  
`m3u8_name` is like `wait_for_download.m3u8`   
`video_name` is like `cannot_wait_to_watch.ts` 
### getM3u8.py
> No use in most situations

Open `cmd.exe` for `Windows` or `Terminal` for `Linux`.  
Download m3u8 file from an url.
```
$ python getM3u8.py url m3u8_name
```
