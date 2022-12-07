# video-to-ascii
converts a video to ascii

# Usage
Call the script like py ascii_video.py path/to/video [fps] [width] [height] path/to/video to create the video resized to width x height and try to run it at the fps provided, it's made in python not expect much
## In other apps
the usage in other apps will no have a locked frame rate, you should add your own if you so desire
- **image:** call image_to_ascii
- **Video:** call eiher process or async_process
## Sync
```python
agen = ascii_video.process(vid_path, 60, 33)
[print(x) for x in agen]
```
## Async
to use video call ascii_video.async_process, since it works in a generator it has to be used like
```python
agen = ascii_video.async_process(vid_path, 60, 33)
async for res in agen:
    await # your usage here
```

# ⚠ Important ⚠ 
## Terminal
You need an ascii compliant terminal, in linux/mac I think they already are, in windows powershell and windows terminal are, but cmd is not, to make it compliant you have to [modify the registry](https://superuser.com/questions/413073/windows-console-with-ansi-colors-handling)
## Python packages
I could Freeze the thing, but I'm lazy, so you have to install opencv2-python.
```sh
python -m pip insall opencv2-python
```
