import glob
import os
import shutil
from PIL import Image

shutil.rmtree("public/images/thumbnails")
os.mkdir("public/images/thumbnails")

# get all the jpg files from the current folder
for filepath in glob.glob("public/images/*.jpg"):
  filename= filepath.split("/")[-1]
  if not os.path.isfile("public/images/thumbnails/" + filename):
       im = Image.open(filepath)
       im.thumbnail((256, 1024))
       im.save("public/images/thumbnails/" + filename, "JPEG")
