import os
import glob
from PIL import Image
import subprocess

base_dir = 'C:\\Users\\singhs\\Videos\\Virtual Tour\\Video\\Natural Area Teaching Lab'
thumb_dir = base_dir + '\\thumbnails'

# get all the jpg files from the current folder
for infile in glob.glob(base_dir+"\\*.jpg"):
	im = Image.open(infile)
	# convert to thumbnail image
	im.thumbnail((512, 512), Image.ANTIALIAS)
	# don't save if thumbnail already exists
	fileName = os.path.basename(infile)
	if fileName[0:2] != "T_":
		# prefix thumbnail file with T_
		print(fileName)
		if not os.path.exists(thumb_dir):
			os.makedirs(thumb_dir)
		exists = os.path.isfile(thumb_dir + "\\T_" + fileName)
		if not exists:
			im.save(thumb_dir + "\\T_" + fileName, "JPEG")


for infile in glob.glob(base_dir+"\\*.mp4"):
	# im = VideoStream(infile).get_frame_at_sec(5).image()
	# prefix thumbnail file with T_
	fileName = os.path.basename(infile)
	print(fileName[0:-4])
	exists = os.path.isfile(thumb_dir + "\\T_" + fileName[0:-4] + ".jpg")
	img_output_path = thumb_dir + "\\T_" + fileName[0:-4] + ".jpg"
	if not exists:
		subprocess.call(['ffmpeg', '-i', infile, '-ss', '00:00:00.000', '-vframes', '1', '-vf', 'scale=iw*0.1:ih*0.1', img_output_path])
	