
def typee(type):
	rasm = """png webp cr2 tif bmp jxr psd ico heic"""
	video = """mp4 m4v mkv webm mov avi wmv mpg flv"""
	audio = """mid mp3 m4a ogg flac wav amr"""
	doc = """doc docx xls html html xml js apk epub Zip zip tarl rar gz bz2 7z xz pdf exe swf rtf eot ps sqlite nes crx cab deb ar Z lz woff woff2 ttf otf"""
	if type in rasm:
		return "r"
	elif type in video:
		return "v"
	elif type in video:
		return "a"
	elif type in doc:
		return "d"
	else:
		pass