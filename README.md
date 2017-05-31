# How to read captcha

1. install pytesseract and PIL
2. download captcha picture
3. read captcha impage
4. read the text of image

*Resize picture could make it more correctly 

    

    
    


# GCIS
破解經濟部商業司公司登記資料查詢系統驗證碼  
http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do

![alt text](https://github.com/shihs/read-captcha/blob/master/GCIS/pic.jpg)    

這個驗證碼只有數字，沒有扭曲，而且底色單一，算是非常基本的驗證碼，
所以只要下載圖片後稍微調整圖片大小再利用pytesseract package解讀內容，
準確率就非常的高了。         

   
   
   
   
# BUREAU OF FOREIGN TRADE
破解國貿局進出口廠商基本資料查詢驗證碼 
https://fbfh.trade.gov.tw/rich/text/indexfbOL.asp  

![alt text](https://github.com/shihs/read-captcha/blob/master/BUREAU%20OF%20FOREIGN%20TRADE/pic.png)        

這個驗證碼就比較複雜，
包含數字與字母，被扭曲，且底色還有其他干擾。

這裡我使用的方式是，下載圖片後利用histogram()解讀圖片中包含的顏色，
再將數字以外的點在與原圖相同大小的黑色圖片點上白色，產生字母與數字為黑色的白底圖。

最後產生像這樣的圖片，      
![alt text](https://github.com/shihs/read-captcha/blob/master/BUREAU%20OF%20FOREIGN%20TRADE/pic2.png)       
少了一些干擾，比較容易辨認，但這個方式並無法每次都正確。

*參考   
https://www.urlteam.org/2017/02/%E4%BA%9A%E9%A9%AC%E9%80%8A%E9%AA%8C%E8%AF%81%E7%A0%81%E7%A0%B4%E8%A7%A3%E5%80%BE%E6%96%9C%E5%AD%97%E4%BD%93%E8%AF%86%E5%88%AB%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/






