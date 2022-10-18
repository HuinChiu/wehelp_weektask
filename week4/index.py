from flask import *
import pymongo
import ssl
import certifi
ssl._create_default_https_context = ssl._create_unverified_context

# 初始化資料庫連線
# 連線到ＭongoDB雲端資料庫
client = pymongo.MongoClient(
    "mongodb+srv://root:root123@mycluster.nfytqra.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
# 選擇操作week4資料庫
db = client.week4
print("連線成功")

# 初始化Flask伺服器
# 建立Application物件，靜態檔案處理設定
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
# 設定Session的密鑰
app.secret_key = "any string but secret"

# 處理路由


@app.route("/")  # 首頁
def index():
    return render_template("index.html")  # 使用靜態模板


@app.route("/menber")  # 會員頁
def menber():
    if "menber_name" in session:  # 確認會員是否有在session裡
        return render_template("menber.html")
    else:
        return redirect("/")


@app.route("/signup", methods=["POST"])  # 註冊
def signup():
    # 從前端接收資料
    menber_name = request.form["name"]  # 取得表單name
    password = request.form["password"]  # 取得表單密碼
    # 根據接受到的資料做驗證
    collection = db.users
    # 檢查是否有相同帳號的資料
    result = collection.find_one({
        "menber_name": menber_name
    })
    if result != None:
        return redirect("/error?msg=帳號已被註冊")  # 頁面顯示帳號已被註冊
    # 把資料放進資料庫完成註冊
    collection.insert_one({
        "menber_name": menber_name,
        "password": password
    })
    return redirect("/menber")  # 引導到會員頁面

# /erro?msg=錯誤訊息


@app.route("/signin", methods=["POST"])
def signin():
    menber_name = request.form["name"]  # 取得表單name
    password = request.form["password"]  # 取得表單密碼
    collection = db.users
    # 檢查帳號密碼是否正確
    result = collection.find_one({
        "$and": [
            {"menber_name": menber_name},
            {"password": password}
        ]
    })
    # 找不到對應的資料，登入失敗，倒到錯誤頁面
    if menber_name == "" or password == "":  # 如果帳號或密碼任一為空
        return redirect("/error?msg=請輸入帳號、密碼")
    elif result == None:  # 如果找不到會員資訊
        return redirect("/error?msg=帳號、或密碼輸入錯誤")
    else:
        # 登入成功，在session紀錄會員資訊，導向會員頁面
        session["menber_name"] = result["menber_name"]
        return redirect("/menber")


@app.route("/error")  # 錯誤頁面
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("erro.html", message=message)


@app.route("/signout")
def signout():
    # 移除session中的會員資訊
    del session["menber_name"]
    return redirect("/")  # 返回首頁


@app.route("/square/<int:num>")
def square(num):
    final_num = num*num  # 將數字相乘
    return render_template("square.html", final_num=final_num)  # 將結果回傳至html


@app.route("/count", methods=["POST"])
def count():
    num = int(request.form["num"])  # 取得表單num數字
    return redirect(url_for("square", num=num))  # 回傳給square函式


app.run(port=3000)
