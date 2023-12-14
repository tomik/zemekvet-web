import glob
import os
import shutil
from PIL import Image

if os.path.exists("public/images/thumbnails"):
    shutil.rmtree("public/images/thumbnails")
os.mkdir("public/images/thumbnails")

# get all the jpg files from the current folder
for filepath in glob.glob("public/images/photos/*"):
  filename= filepath.split("/")[-1]
  if not os.path.isfile("public/images/thumbnails/" + filename):
       im = Image.open(filepath)
       root_ext = os.path.splitext(os.path.basename(filename))
       if root_ext[1] != "jpg":
           rgb_im = im.convert("RGB")

           old_filepath = filepath
           filename = root_ext[0] + ".jpg"
           filepath = "public/images/photos/" + filename

           rgb_im.save("public/images/photos/" + root_ext[0]+".jpg")
           im = rgb_im
           os.remove(old_filepath)

       im.thumbnail((256, 1024))
       im.save("public/images/thumbnails/" + filename, "JPEG")
