# -*- coding: utf-8 -*-
import requests
from PIL import Image
import pytesseract


#get captcha of gcis(經濟部商業司商業資料頁面)
def ReadCaptcha():

	# address of gcis captcha
	res = requests.get("http://gcis.nat.gov.tw/gps/kaptcha.jpg", stream = True, verify = False, timeout = 30)
	
	# save captcha pitcure
	with open('pic.jpg','wb') as f:
		f.write(res.content)
		
	# read captcha
	image = Image.open('pic.jpg')

	# adjust pitcure size, it would read more correctly
	image.resize((150, 50),Image.ANTIALIAS).save("pic.jpg")
	image = Image.open("pic.jpg")
	captcha = pytesseract.image_to_string(image).replace(" ", "").replace("-", "").replace("$", "")
	return captcha



print ReadCaptcha()
