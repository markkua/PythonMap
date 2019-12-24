# -*- coding: utf-8 -*-
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# To read GPS position from JPEG images.


class ImgPositionReader:

	def get_exif_dict(self, filename: str):
		image = self._open_img(filename)
		if not image:
			print("can not open image: %s", filename)
			return None
		
		exif_row_dict = self._get_raw_exfi_dict(image)
		exif_decoded_dict = {}
		
		if exif_row_dict:
			for tag_code, value in exif_row_dict.items():
				tag_name = TAGS.get(tag_code, tag_code)
				if tag_name == "GPSInfo":
					gps_data = self._decode_GPS_exif(value)
					exif_decoded_dict[tag_name] = gps_data
				else:
					exif_decoded_dict[tag_name] = value
		return exif_decoded_dict
	
	def _open_img(self, full_filename) -> Image:
		# TODO 验证文件是否存在，是否能打开
		if True:
			img = Image.open(full_filename)
			return img
		else:
			return None
	
	@staticmethod
	def _get_raw_exfi_dict(image: Image):
		if image:
			exif_raw_dict: dict = image._getexif()
			return exif_raw_dict
		else:
			return None
	
	@staticmethod
	def _decode_GPS_exif(exif_GPS_value: dict):
		gps_data = {}
		for sub_tag_code, sub_value in exif_GPS_value.items():
			sub_tag_name = GPSTAGS.get(sub_tag_code, sub_tag_code)
			gps_data[sub_tag_name] = sub_value
		return gps_data
	
	@staticmethod
	def get_if_exist(key, dict_data):
		if key in dict_data:
			return dict_data[key]
		else:
			return None


def test_info(fileneme):
	img = Image.open(fileneme)
	info = img.info
	exif_row_dict: dict = img._getexif()
	
	print(exif_row_dict)  # TODO

	exif_decoded_dict = {}
	if exif_row_dict:
		for tag_code, value in exif_row_dict.items():
			tag_name = TAGS.get(tag_code, tag_code)
			# decode GPS info
			if tag_name == "GPSInfo":
				gps_data = {}
				for sub_tag_code, sub_value in value.items():
					sub_tag_name = GPSTAGS.get(sub_tag_code, sub_tag_code)
					gps_data[sub_tag_name] = sub_value
					
				exif_decoded_dict[tag_name] = gps_data
			else:
				exif_decoded_dict[tag_name] = value
		
		print(exif_decoded_dict['GPSInfo'])
		

def test(filename):
	IPR = ImgPositionReader()
	exif = IPR.get_exif_dict(filename)
	print(exif)


if __name__ == '__main__':
	test_img = '../test_img/test_img.jpg'
	# test_info(test_img)
	test(test_img)
	