import glob
import os
import shutil
from PIL import Image

if os.path.exists("public/images/thumbnails"):
    shutil.rmtree("public/images/thumbnails")
os.mkdir("public/images/thumbnails")

# get all the jpg files from the current folder
for filepath in glob.glob("public/images/photos/*"):
  filename = filepath.split("/")[-1]
  if not os.path.isfile("public/images/thumbnails/" + filename):
       im = Image.open(filepath)
       root_ext = os.path.splitext(os.path.basename(filename))
       if root_ext[1] != ".jpg":
           old_filepath = filepath
           filename = root_ext[0] + ".jpg"
           filepath = "public/images/photos/" + filename

           if root_ext[1] in (".JPG", ".jpeg", ".JPEG"):
               os.rename(old_filepath, filepath)
           else:
               rgb_im = im.convert("RGB")
               rgb_im.save(filepath)
               im = rgb_im
               os.remove(old_filepath)

       im.thumbnail((256, 1024))
       im.save("public/images/thumbnails/" + filename, "JPEG")
