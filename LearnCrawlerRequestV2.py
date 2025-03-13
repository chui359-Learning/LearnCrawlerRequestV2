import requests
from bs4 import BeautifulSoup

def extract_h2_with_bs4(url):
    # 發送HTTP請求以獲取網頁內容
    response = requests.get(url)
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML內容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到所有<div class="ProductCardNormalGrid__viewBox__1JSHC">標籤
        view_boxes = soup.find_all('div', class_='ProductCardNormalGrid__viewBox__1JSHC')
        # 提取每個view_box中的<h2>標籤中的文本內容
        h2_contents = [view_box.find('h2').text.strip() for view_box in view_boxes if view_box.find('h2')]
        return h2_contents
    else:
        return None

url = "https://www.asus.com/tw/laptops/for-gaming/rog-republic-of-gamers/filter?SubSeries=ROG-Zephyrus"
h2_contents_bs4 = extract_h2_with_bs4(url)
print(h2_contents_bs4)
