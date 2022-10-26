##要求二
1. 建立一個新的資料庫，取名字為 website。
2. 在資料庫中，建立會員資料表，取名字為 member。資料表必須包含以下欄位設定:
```sql
CREATE TABLE member (
  id bigint NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '獨立編號',
  name varchar(255) NOT NULL COMMENT '姓名',
  username varchar(255) NOT NULL COMMENT '帳戶姓名',
  password varchar(255) NOT NULL COMMENT '帳戶密碼',
  follower_count int unsigned NOT NULL DEFAULT '0' COMMENT '追蹤者數量',
  time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '註冊時間'
) 
```
![要求2](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%822.png "要求2")

##要求三
* 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
```sql
INSERT INTO member(name, username, password, follower_count) 
VALUES ('Marry' 'test' 'test' 10,
        'paul' 'fast' 'fast' 25,
        'Lucy' 'funny' 'funny_life' 100,
        'Nancy' 'hello' 'hello_world' 150 ,
        'Meggie' 'sweet' 'sweat candy' 350);
```
![要求3-1](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-1.png "要求3-1")
* 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![要求3-2](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-2.png "要求3-2")
* 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。
![要求3-3](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-3.png "要求3-3")
* 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![要求3-4](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-4.png "要求3-4")
* 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![要求3-5](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-5.png "要求3-5")
* 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![要求3-6](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-6.png "要求3-6")
* 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改
成 test2。
![要求3-7](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%823-7.png "要求3-7")
##要求四
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。  
![要求4-1](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%824-1.png "要求4-1")
* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![要求4-2](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%824-2.png "要求4-2")
* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![要求4-3](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%824-3.png "要求4-3")

##要求五

* 在資料庫中，建立新資料表紀錄留言資訊，取名字為 message。資料表中必須包含以下欄位設定:
```sql
CREATE TABLE message (
  id bigint NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '獨立編號',
  member_id bigint NOT NULL COMMENT '留言者會員編號',
  content varchar(255) NOT NULL COMMENT '留言內容',
  like_count int unsigned NOT NULL DEFAULT '0' COMMENT '按讚的數量',
  time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言時間',
  FOREIGN KEY (member_id) REFERENCES member (id)
) 
```
![要求5-1](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%825-1.png "要求5-1")
* 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![要求5-2](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%825-2.png "要求5-2")
* 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![要求5-3](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%825-3.png "要求5-3")
* 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中
欄位 username 是 test 的所有留言平均按讚數。
![要求5-4](https://github.com/HuinChiu/wehelp_weektask/blob/main/week5/%E5%9F%B7%E8%A1%8C%E9%A0%81%E9%9D%A2%E6%88%AA%E5%9C%96/%E8%A6%81%E6%B1%825-4.png "要求5-4")
