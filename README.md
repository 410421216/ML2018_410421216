# machine-learning
machine learning assignment
  
機器學習導論 assignment1  
運用機器學習將加密圖片解鎖  
  
A.  
使用在PILLOW中的PIL讀取圖片資訊  
  
B.  
MaxlterLimit  訓練次數上限，我設定為100  
α  learning rate , 我設定為pdf建議的0.00001  
the vigilance level for checking the convergence of weight vectors (符號無法顯示)  權重調整必須大於此值，否則視為調整過小，調整效益不好，停止調整，我設定為0.00000001  
  
C.  
w1 = 0.249143307097  
w2 = 0.661381901042  
w3 = 0.0892395257167  
使用training algorithm通過兩個epoch後得到  
  
D.  
[image](https://github.com/410421216/ML2018_410421216/blob/master/data%26image/answer.png)  
  
E.  
第一個遇到的問題是github的上傳與同步，這次花了幾個小時終於弄懂了github的同步用法。  
第二是python的package，我安裝PIL時發現與現行package衝突，找了資訊才發現原來PIL已經被併到PILLOW裡了。在此又白浪費了幾個小時。  
第三個是解密出來的圖片效果很差，這個在同步敘述也有提到，是因為我在training algorithm中調整權重的部分被調整的參數打錯了，花了十幾分鐘找到問題所在。  

F.  
之前只有看過python程式碼，這是第一次從頭開始用python完成一次作業。  
學會機器學習的基礎與實作，和將陣列轉成圖片的函數。  
