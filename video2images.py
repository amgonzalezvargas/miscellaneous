import os
from datetime import timedelta
import cv2
import numpy as np


"""
The basis for this code is found at:
https://www.thepythoncode.com/article/extract-frames-from-videos-in-python
"""

def format_timedelta(td):
    """Utility function to format timedelta objects in a cool way (e.g 00:00:20.05) 
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


my_path="/media/sf_vboxshare/videos/vids/"
my_files=os.listdir(my_path)

print("\nList of files in my path: ")
print(my_files)

#Every how many seconds do you want to save the frame?
frame_every_n_seconds=10
SAVING_FRAMES_PER_SECOND=1/frame_every_n_seconds

for video_file in my_files:

	#video_file=my_files[0]
	frames_folder=my_path+video_file+"-opencv"
	print(frames_folder)
	print("\n\n\n")

	# make a folder by the name of the video file
	if not os.path.isdir(frames_folder):
		os.mkdir(frames_folder)

	# read the video file 
	cap=cv2.VideoCapture(my_path+video_file)

	# get the FPS of the video
	fps = cap.get(cv2.CAP_PROP_FPS)
	print(f"Original fps is {fps}, extracting one frame every {frame_every_n_seconds} seconds")

	# if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
	saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)

	# get the list of duration spots to save
	saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)

	count = 0
	n_frames_saved=0

	print(f"\nExtracting frames from: {video_file}.jpg")

	while True:
		is_read, frame = cap.read()
		if not is_read:
			# break out of the loop if there are no frames to read
			break
		# get the duration by dividing the frame count by the FPS
		frame_duration = count / fps
		try:
			# get the earliest duration to save
			closest_duration = saving_frames_durations[0]
		except IndexError:
			# the list is empty, all duration frames were saved
			break
		if frame_duration >= closest_duration:
			# if closest duration is less than or equals the frame duration, 
			# then save the frame
			frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
			cv2.imwrite(os.path.join(frames_folder, f" {frame_duration_formatted}.jpg"), frame) 

			#keeping track of progress:
			n_frames_saved+=1
			print(f"Saving frame: {frame_duration_formatted}.jpg")

			# drop the duration spot from the list, since this duration spot is already saved
			try:
				saving_frames_durations.pop(0)
			except IndexError:
				pass
		# increment the frame count
		count += 1

	print(f'succesfully extracted {n_frames_saved} frames from {video_file} \n\n\n')

