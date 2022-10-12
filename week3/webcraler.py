import urllib.request as req
import ssl
import bs4
ssl._create_default_https_context = ssl._create_unverified_context  # 驗證
good = []
normal = []
bad = []


def getData(url):
    # 建立一個Request物件 附加Request header的資訊
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
    })  # 要讓系統得我們是正常人

    with req.urlopen(request) as response:  # 抓取電影版網頁原始碼
        data = response.read().decode("utf-8")    # 解析原始碼

    root = bs4.BeautifulSoup(data, "html.parser")  # 讓bs4協助我們解析HTML，parser解析器
    titles = root.find_all("div", class_="title")  # 尋找class="title"的div標籤
    # print(titles.a.string)  # 找到class=title裡的a的string
    for title in titles:
        if title.a != None:  # 如果標題包含a標籤(沒有被刪除) 印出來
            if title.a.string[1:3] == "好雷":
                good.append(title.a.string)
            elif title.a.string[1:3] == "普雷":
                normal.append(title.a.string)
            elif title.a.string[1:3] == "負雷":
                bad.append(title.a.string)
    # 抓取上一頁的連結
    nextlink = root.find("a", string="‹ 上頁")  # 找到內文是‹ 上頁的a標籤
    return nextlink["href"]  # 找到上一頁網址


pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 10:
    pageurl = "https://www.ptt.cc"+getData(pageurl)  # 找出上一頁網址
    count += 1

# print(good, normal, bad)

with open("move.txt", "w") as data:
    for i in good:
        data.write(i+"\n")
    for j in normal:
        data.write(j+"\n")
    for k in bad:
        data.write(k+"\n")
