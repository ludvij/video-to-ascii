# video-to-ascii
converts a video to ascii

# Image
to use image to ascii just call ascii_video.image_to_ascii

# Video
can be used either sync or async
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
call the script like py ascii_video.py path/to/video -l to create a looping image
call the script like py ascii_video.py path/to/video [fps] [width] [height] -l to create a looping image resized to width x height and try to run it at the fps provided, it's made in python not expect much
## In discord
Using youtube-dl in my discord bot, not recommended since recently is running super slow,
ydlp is much better,
```python
# stuff to download the video
# no audio, worst quality possible
vid_path = fr"rcs\video\ascii.mp4"
ydl_opts = {
    "format" : '160',
    "outtmpl" : vid_path,
}
# download the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])
# asynchronous generator, I have no idea what i'm doing
# but I think this will make the bot run better
agen = ascii_video.process(vid_path, 60, 33)
self.video_play = True
async for res in agen:
    await ctx.send(res, delete_after=10)
    if not self.video_play: break
# TODO find a way to fix this
agen = None
```
