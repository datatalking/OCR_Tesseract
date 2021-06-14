# SOURCE https://stackoverflow.com/questions/54395735/how-to-work-with-heic-image-file-types-in-python

import whatimage
# brew install libffi libheif # subdependancy of pyheif # then install pip install git+https://github.com/carsales/pyheif.git
import pyheif
from PIL import Image
from pathlib import Path
import os
import shutil


def main():
	rename_heic_to_jpeg()

def decodeImage(bytesIo):
	fmt = whatimage.identify_image(bytesIo)
	if fmt in ['heic', 'avif']:
		i = pyheif.read_heif(bytesIo)
		
		# Extract metadata etc
		for metadata in i.metadata or []:
			if metadata['type'] == 'Exif':
		# do whatever
		
		# Convert to other file format like jpeg
		s = io.BytesIO()
		pi = Image.frombytes(
			mode=i.mode, size=i.size, data=i.data)
		
		pi.save(s, format="jpeg")


def rename_heic_to_jpeg():
"""convert heic to jpeg"""
from PIL import Image
import pyheif
# TOFIX pyheif creates wheel error
# tried sudo -H pip install wheel then pyheif
	# os.rename(dst_file, new_dst_file_name)#rename
	heif_file = Path('/owner/sbox/data/test_data/IMG_1647.HEIC')
	# heif_file = pyheif.read("IMG_7424.HEIC")
	image = Image.frombytes(
	    heif_file.mode,
	    heif_file.size,
	    heif_file.data,
	    "raw",
	    heif_file.mode,
	    heif_file.stride,
	    )
		image.save("IMG_1647.jpg", "JPEG")


iphoto_path = ['/{}/owner/owner/Pictures/Photos Library.photoslibrary/'].format(Users)
sbox_path = '/{}/owner/sbox/'
sbox_test_photo_path = '/{}/owner/sbox/data/test_data/'
empty_path = ''
# TODO incorporate https://pypi.org/project/osxphotos/ into photos
photo_files = ['.png', '.jpg', '.gif', '.tiff']
doc_files = ['.doc', '.pdf']
data_files = ['.txt', '.csv', '.tsv', '.xls', '.xlsx']
user_to_sort_files = ['/{}/owner/Library/'].format(Users)
clean_file_path = ['/{}/owner/Library/'].format(Users)
data_base_path = ''