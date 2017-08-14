m3u8Downloader
===
> *Using python 2.7.13 with requests and bs4*
## Usage

### m3u8Downloader.py  
Open `cmd.exe` for `Windows` or `Terminal` for `Linux`.  
Download video from a m3u8 file via:  
```
$ python m3u8Downloader.py m3u8_path video_name 
```
Lots of ts files will be downloaded into `./video/tmp` folder named `video_name_X.ts` *(X is index)*.  
Once all ts files are downloaded, they will be merged to a file `video_name` into `./video` folder.  

**※ Don't forget** filename extension:  
`m3u8_path` is like `your_path/wait_for_download.m3u8`   
`video_name` is like `cannot_wait_to_watch.ts`  

+ After merged, fragments will be deleted.
+ Duplicate video names **will not** be overwritten.
+ If you have downloaded some parts of a video, you can just use same video name to download remaining parts. 

### getM3u8.py
> No use in most situations.

Open `cmd.exe` for `Windows` or `Terminal` for `Linux`.  
Download m3u8 file from an url.  
Better surround urls with **""**
```
$ python getM3u8.py "url" XXX.m3u8
```
m3u8 file will be downloaded into `./video/m3u8` folder.

## License
MIT