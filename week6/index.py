from flask import *
import mysql.connector
from mysql.connector import errorcode
import ssl
import os
from dotenv import load_dotenv

# 使用.env隱藏私密訊息
load_dotenv()
sql_user = os.getenv("sql_user")
sql_password = os.getenv("sql_password")

# 安全憑證
ssl._create_default_https_context = ssl._create_unverified_context

# 初始化Flask伺服器
# 建立Application物件，靜態檔案處理設定
app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
# 登入資mysql料庫
connection = mysql.connector.connect(
    host="localhost",          # 主機名稱
    database="week6",  # 資料庫名稱
    user=sql_user,        # 帳號
    password=sql_password)  # 密碼

# 設定Session的密鑰
app.secret_key = "any string but secret"


# 路由設定
@app.route("/")  # 首頁
def index():
    return render_template("index.html")  # 使用靜態模板首頁


@app.route("/member")  # 會員頁
def member():
    if "member_id" in session:  # 確認會員是否有在session裡
        name = session["name"]  # 找出名字將名字顯示在頁面上
        connection.reconnect()  # 重新連接資料庫
        # 從資料庫輸出所有姓名及留言回傳到html
        cursor = connection.cursor()  # 使用游標
        query = ("select name, content from message INNER JOIN members"
                 " on members.id=message.member_id order by time DESC;")
        cursor.execute(query)
        result = cursor.fetchall()  # 找出所有姓名：留言
        connection.close()
        # 回傳至html
        return render_template("member.html", name=name, result=result)
    else:
        return redirect("/")


@app.route("/message", methods=["POST"])
def message():
    member_id = session["member_id"]  # 找出member帳號
    content = request.form["message"]  # 接收表單數據
    connection.reconnect()
    cursor = connection.cursor()
    sql_member_id = (
        "SELECT id FROM members WHERE member_id =%s;")  # sql找出會員id
    cursor.execute(sql_member_id, (member_id,))
    result_id = cursor.fetchone()
    id = result_id[0]  # 將資料取出

    sql = ("INSERT INTO message(member_id,content) "  # 添加到資料庫
           "VALUES (%s, %s);")
    member_message = (id, content)
    cursor.execute(sql, member_message)
    connection.commit()
    connection.close()
    return redirect("/member")


@app.route("/signup", methods=["POST"])  # 註冊
def signup():
    member_name = request.form["name"]  # 取得表單name
    member_id = request.form["id"]  # 取得表單帳號
    password = request.form["password"]  # 取得表單密碼
    # 根據接受到的資料做驗證
    # 檢查是否有相同帳號的資料
    if member_name == "" or member_id == "" or password == "":  # 如果有任一輸入為空返回錯誤訊息
        return redirect("/error?msg=請重新輸入註冊姓名、帳號、密碼不可為空")
    # 重新連接資料庫
    connection.reconnect()
    cursor = connection.cursor()  # 使用游標
    query = ("SELECT member_id FROM members "  # 搜尋member帳號
             "WHERE member_id = %s")
    cursor.execute(query, (member_id,))
    data = cursor.fetchone()
    if data == None:  # 如果沒有找到帳號密碼新增會員資料至資料庫
        sql = ("INSERT INTO members(name, member_id, password) "
               "VALUES ( %s, %s, %s)")
        member = (member_name, member_id, password)
        cursor.execute(sql, member)
        connection.commit()
        connection.close()
        return redirect("/")  # 引導到首頁頁面
    else:
        return redirect("/error?msg=帳號已被註冊")  # 頁面顯示帳號已被註冊


@app.route("/error")  # 錯誤頁面
def error():
    message = request.args.get("msg", "發生錯誤，請聯繫客服")
    return render_template("erro.html", message=message)


@app.route("/signin", methods=["POST"])
def signin():
    sign_id = request.form["sign_id"]  # 取得表單name
    sign_password = request.form["sign_password"]  # 取得表單密碼
    # 檢查帳號密碼是否正確
    if sign_id == "" or sign_password == "":  # 如果帳號或密碼任一為空
        return redirect("/error?msg=請輸入帳號、密碼")
    connection.reconnect()
    # 找尋是否有此密碼及帳號
    cursor = connection.cursor()
    query = (
        "SELECT name,member_id, password from members WHERE member_id= %s and password= %s;")
    member = (sign_id, sign_password)
    cursor.execute(query, member)
    data = cursor.fetchone()
    # 找不到對應的資料，登入失敗，到錯誤頁面
    if data[1] == None or data[2] == None:
        return redirect("/error?msg=帳號、或密碼輸入錯誤")
    else:
        # 登入成功，在session紀錄會員資訊，導向會員頁面
        session["member_id"] = sign_id
        session["name"] = data[0]  # 將姓名加入至session以取得會員姓名
        connection.close()
        return redirect("/member")


@app.route("/signout")
def signout():
    # 移除session中的會員資訊
    del session["member_id"]
    del session["name"]
    return redirect("/")  # 返回首頁


if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
