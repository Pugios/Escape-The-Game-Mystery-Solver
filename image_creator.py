from PIL import Image, ImageColor
import os
from ast import literal_eval

def main():
	path = './sus_files/'
	for file in os.listdir(path):
		if file.endswith('.txt') or file == '6':
			createImage(path, file)

def createImage(path, file):
	print('Creating Image: ', file)
	file_content = read_file(path + file)
	
	image_size = file_content['image_size']
	image_contents = file_content['image_contents']
	anomalies = file_content['anomalies']

	print('Anomalies:', anomalies)
	print('================')

	largest_pixel_value = get_largest_value(image_contents)

	im = draw_image(image_size, image_contents, largest_pixel_value)
	if file == '6':
		file = '6.png'
	im.save('./decoded_files/' + file[:-3] + 'png')

def read_file(path):
	first = True
	image_size = 0
	image_contents = []
	anomalies = []

	with open(path, 'r') as file:
		for line in file.readlines():
			if first:
				image_size_list = literal_eval(line.encode("ascii", errors="ignore").decode())
				image_size = (image_size_list[0], image_size_list[1])
				first = False
			else:
				try:
					content = literal_eval(line)
					if type(content) == int: # Int Lines are just the number of Anomalies
						print('Number of Anomalies:', content)
					else:
						image_contents.append(content)
				except Exception as e:
					anomalies.append(str(line))
	return {'image_size': image_size, 'image_contents': image_contents, 'anomalies': anomalies}

def get_largest_value(image_contents):
	largest_pixel_value = 1

	for row in image_contents:
		for value in row:
			if(value > largest_pixel_value):
				largest_pixel_value = value
	return largest_pixel_value

def draw_image(image_size, image_contents, largest_pixel_value):
	im = Image.new('RGB', (image_size[0],image_size[1])) # create the Image of size 1 pixel 
	current_color = 0
	row_number = 0
	for row in image_contents:
		if type(row) != str:
			for j, pixel in enumerate(row):
				color = ImageColor.getrgb("hsl(" + str(current_color) + ", 0%, " + str(round(pixel/largest_pixel_value*100)) + "%)")
				im.putpixel((j, row_number), color)
			row_number += 1
		else:
			pass
	return im

if __name__ == "__main__":
	main()