from sys import argv
import cv2
from time import perf_counter_ns, sleep

# Extracts frames from videos
# made a generator to not clutter dirs in images
# a frame is extracted a image is processed
def video_to_ascii(path:str, pwidth:int=0, pheight:int=0, reverse:bool=False, discord:bool=False) -> str:
	# path to the video
	vid = cv2.VideoCapture(path)
	# checks wheter frames where extracted
	has_frame, frame = vid.read()
	while has_frame:
		# converts the frame in ascii
		res = image_to_ascii(frame, pwidth, pheight, reverse, discord)
		# extracts the frames
		has_frame, frame = vid.read()
		yield res

# if only the width is provided
# it will be resized to pwidth x pwidth / ratio
# if only the height is provided
# it will be resized to pheight * ratio * pheight 
def resize(img, pwidth:int=0, pheight:int=0):
	if pheight != 0 or pwidth != 0:
		width = pwidth
		height = pheight
		ratio = img.shape[0] / img.shape[1]

		if width != 0 and height == 0:
			height = int(width * ratio)
		elif pheight != 0:
			width = int(height / ratio)
	else:
		height = img.shape[0]
		width = img.shape[1]
		
	return cv2.resize(img, (width, int(height / 2)), interpolation=cv2.INTER_LINEAR)
	
# converts an image or fram to ascii
# src is the image or path to image
# pwidth is the width of the image, don't use if you don't want to resize
# pheight is the height of the image, don't use if you don't want to resize
# reverse inverts the whitescale
# discord uses a different charset in order to make it look better in discord
def image_to_ascii(src, pwidth:int=0, pheight:int=0, reverse:bool=False, discord:bool=False):
	if (type(src) == str):
		src = cv2.imread(src)
	# convert image to gray scale
	gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

	# resize image to something more manageable or not, depending of cl args
	img = resize(gray, pwidth, pheight)
	# opencv puts height first
	height = img.shape[0]
	width = img.shape[1]

	# since pixels in gray scale go from 0 to 255 we have to divide
	# in ranges to get the best char
	# so we have to darkness * len(chars) - 1 / 255  to get the best index
	# so if we have 10 chars and we have to convert a pixel of value 67 we
	# divide 9 / 255 to get 0.035 and the we mult 67 * 0.035 and we get 2.36
	# so we truncate it to 2, so the char would be ":"
	# since this operation is length dependant we can add whatever char we like 
	# and it will be added to its range, a char hue if you like
	chars = ' .,_-~=+*:;!?#%@'
	# since discord can't send empty messages ans some characters do weird stuff we don't send them
	# also we use monospace characters
	if discord: chars = '⠄⠆⠖⠶⡶⣩⣪⣫⣾⣿'
	# to reverse the spectrum we reverse the string
	if reverse: chars = chars[::-1]
	# store to ease computations
	divisor = (len(chars) - 1) / 255
	# pixel array
	arr = [[(y,x) for x in range(width)] for y in range(height)]

	# iterate through each pixel and assign each char
	for i in range(width):
		for j in range(height):
			px = img[j, i]
			index = int(px * divisor)
			#print(px, index)
			arr[j][i] = chars[index]	

	# np char arrays are encoded by default, so if you want a nice printable output you
	# have to do this
	printable_arr = "\n".join([''.join(row) for row in arr])

	return printable_arr

# generator for the bot
async def async_process(vid_path:str, pwidth:int, pheight:int):
	for res in video_to_ascii(vid_path, pwidth=pwidth, pheight=pheight, discord=True, reverse=True):
		yield res

def process(vid_path:str, pwidth:int, pheight:int):
	arr = []
	for res in video_to_ascii(vid_path, pwidth=pwidth, pheight=pheight, discord=True, reverse=True):
		arr.append(res)
	return arr

def lock_framerate(frame_rate, frame, op):
	rate = 10e9/frame_rate
	start = perf_counter_ns()
	op(frame)
	end = perf_counter_ns()
	if end - start < rate:
		sleep(rate - (end - start))

def main():
	# check if we are looping 
	width = int(argv[2]) if len(argv) > 3 else 0
	height = int(argv[3]) if len(argv) > 4 else 0
	fps = int(argv[4]) if len(argv) > 2 else 24

	if'-l' in argv and len(argv) > 5:
		while True:
			[lock_framerate(fps, frame, print) for frame in video_to_ascii(argv[1], pwidth=width, pheight=height)]
	else:
		[lock_framerate(fps, frame, print) for frame in video_to_ascii(argv[1], pwidth=width, pheight=height)]







if __name__=='__main__':
	main()