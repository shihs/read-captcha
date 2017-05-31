# -*- coding: utf-8 -*-
# 破解國貿局進出口廠商管理系統驗證碼https://fbfh.trade.gov.tw/rich/text/indexfbOL.asp
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract


def ReadCaptcha():
	'''
	獲取國貿局進出口網站驗證碼值
	'''
	s = requests.Session()
	
	#驗證碼網址
	res = s.get("https://fbfh.trade.gov.tw/rich/text/common/code_98/CheckImageCode.aspx", stream = True, verify = False, timeout = 30)
	
	# save captcha pitcure
	with open('pic.png','wb') as f:
	    f.write(res.content)
	
	# read captcha
	image = Image.open('pic.png')

	# image.show()

	# 獲取顏色，共有256個像素點(0-256)，每個數字代表在圖片中含有對應位的顏色的像素的數量
	his = image.histogram()

	# 以像素點(0-256)為key，出現次數為value，形成對應的dictionary values
	values = {}
	for i in range(0, 256):
	    values[i] = his[i]

	temp = sorted(values.items(), key = lambda x:x[1], reverse = True)
	
	# 儲存顏色出現次數小於五次的顏色代碼(0-256)
	col = set()
	for j, k in temp:
	    if k < 5:
	        col.add(j)
	
	## 這裡主要的概念是，將數字以外的點在與原圖相同大小的黑色圖片點上白色，產生字母與數字為黑色的白底圖
	# 生成一張與圓圖大小相同的黑底圖(0是黑色)
	image_new = Image.new("P", image.size, 0)
	# 原始圖x坐標
	for x in range(image.size[1]):
	    # 原始圖y坐標
	    for y in range(image.size[0]):
	    	# 獲取該坐標位置的顏色數字
	        pix = image.getpixel((y,x))
	        # 將白色(255)、灰色(212)、深灰色(169)與只出現五次以下(set col)的顏色的點圖成白色
	        if pix == 255 or pix == 212 or pix == 169 or pix in col:
	            image_new.putpixel((y,x), 255)
	
	# 儲存新的黑白圖片
	image_new.save("pic2.png","PNG")
	image = Image.open("pic2.png")
	# 調整圖片大小，增加辨識度
	image.resize((120, 33),Image.ANTIALIAS).save("pic2.png")
	image = Image.open("pic2.png")
	image.show()
	# 解讀圖片字母與數字，並排除雜質
	captcha = pytesseract.image_to_string(image).replace(" ", "").replace("-", "").replace("$", "").replace("~", "").replace("'", "").replace(".", "").replace(";", "")[0:6]
	return captcha



captcha = ReadCaptcha()
print captcha


