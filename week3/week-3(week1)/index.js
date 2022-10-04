url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
let stitleList = [];//景點列表
let imgList = [];//圖片列表
fetch(url)
    .then(function (response) {
        return response.json() //將資料轉成json格式
    }).then(function (response) {

        let results = response["result"]["results"];
        for (let i = 0; i < results.length; i++) {
            let stitle = results[i]["stitle"]; //得到景點名稱
            stitleList.push(stitle)
            let file = results[i]["file"].toLowerCase(); //得到所有圖檔
            let file1 = file.split(".jpg");//圖檔網址分開
            let file2 = file1[0] + ".jpg";//取第1個圖檔位置
            imgList.push(file2)
        }
        // 設置productionitem
        let proDiv = document.querySelector(".production"); //找到id =prodiction div
        for (let i = 0; i < 2; i++) {
            let productionDiv = document.createElement("div"); //設置div
            productionDiv.className = "production-item";//設置div class

            let productionImg = document.createElement("img");//設置img
            productionImg.className = "production-img";//設置img class
            productionImg.src = imgList[i];//設置img scr = imgList[i]

            let productionP = document.createElement("p");//設置p
            productionP.className = "production-text";//設置 p class
            productionP.textContent = stitleList[i];//內容加入景點地名

            proDiv.appendChild(productionDiv); //在div裏加入div
            productionDiv.appendChild(productionImg);//在div加入ｉｍｇ
            productionDiv.appendChild(productionP);//在div裏加入 p
        };

        // 設置item
        let itemDiv = document.querySelector(".item-title-group"); //找到id =prodiction div
        for (let j = 2; j < 10; j++) {
            let itemTitleDiv = document.createElement("div"); //設置div
            itemTitleDiv.className = "item-title";//設置div class

            let itemImg = document.createElement("img");//設置img
            itemImg.className = "item-img";//設置img class
            itemImg.src = imgList[j];//設置img scr = imgList[i]

            let itemText = document.createElement("p");//設置p
            itemText.className = "item-text";//設置 p class
            itemText.textContent = stitleList[j];//內容加入景點地名

            itemDiv.appendChild(itemTitleDiv); //在div裏加入div
            itemTitleDiv.appendChild(itemImg);//在div加入ｉｍｇ
            itemTitleDiv.appendChild(itemText);//在div裏加入 p
        };

    })
    .catch(function (erro) {
        console.log(`錯誤代碼為${erro}`)
    });
