import os
import shutil
import send2trash

pwd = os.getcwd()
dest = '/Users/simar/AllPictures'
dest_pdf = '/Users/simar/Documents/sort_pdf'
dest_mp3 = '/Users/simar/soundtracks'
files = os.listdir(pwd)

for f in files:
	if (f.endswith("jpg") or f.endswith(".jpeg") or f.endswith("png")):
		shutil.move(f,dest)
		print("moving file "+f)
	elif (f.endswith("pdf")):
		shutil.move(f,dest_pdf)
		print("moving file " + f)
	elif (f.endswith("mp3")):
                shutil.move(f,dest_mp3)
                print("moving file " + f)
	elif (f.endswith('zip') or f.endswith("dmg")):
        	send2trash.send2trash(f)
		print("Go To Trash " + f)
