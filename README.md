# ArticalCrawler
 WIkiArticalCrawler

 目標:
	1) 下載一個wikipedia頁面，例如川普的英文頁面，建議找英文因為病歷會是英文
	2) 用程式對下載下來的頁面做一些簡單的處理，包括
		i. 清除非文字資料，如圖片、連結，只留下純文字。
		ii. 清除特殊碼 (即句子中的參考文獻的部分)
	3) 利用工具進行詞性標記(pos tagging)，建議使用NLTK套件
	4) 做一個簡單的統計表，
		i. 前五個最常出現的詞性
		ii. 去除大小寫後最常見的詞
		iii. 同上，最常見的bi-gram, tri-gram (不要跨句子計算，應該先斷句後再計算)
		(例如在一個句子中"this is a pen"，這句的bi-gram有 "this is", "is a", "a pen"共四個，tri-gram則就是三個詞為一個單位)