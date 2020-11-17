import os
import shutil
from PIL import Image

root = os.environ['USERPROFILE'] + r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

# make images and mobile folders if they dont exist
if not os.path.exists('images'):
    os.makedirs('images')

if not os.path.exists('mobile'):
    os.makedirs('mobile')

for file in os.listdir(root):
    src = os.path.join(root, file)
    width, height = Image.open(src).size
    if width == 1920:
        dst = os.path.join('images', file+'.jpg')
        shutil.copyfile(src, dst)
    if height == 1920:
        dst = os.path.join('mobile', file+'.jpg')
        shutil.copyfile(src, dst)