# video-to-ascii
converts a video to ascii

# Usage in other applications
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

# Usage
You need to have opencv2-python imported
```sh
python -m pip insall opencv2-python
```
call the script like py ascii_video.py path/to/video [fps] [width] [height] path/to/video to create a looping image resized to width x height and try to run it at the fps provided, it's made in python not expect much

