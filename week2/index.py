# 要求一
def calculate(min, max, step):
    sum = 0
    for i in range(min, max+1, step):  # range(1,4,1)--->1,2,3
        sum = sum+i  # 0+1=1 1+2=3 3+3=6
    print(sum)

    # 請用你的程式補完這個函式的區塊
calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0
# -------------------------------要求2完成------------------------------
# 要求二


def avg(data):
    total = data["employees"]  # shown所有dic裡的資料(共4筆)
    allsalary = 0  # 記錄累加結果
    count = 0  # 紀錄false有幾人
    for i in total:  # 2 第一筆{name:...}
        if i["manager"] == False:  # 如果第一筆{"manager":false}
            salary = i["salary"]  # salary={salary:30000}
            allsalary = allsalary+salary  # allsalary = 0+30000
            count += 1  # 目前有1人
    avgsalary = allsalary/count  # 40000=120000/3
    print(avgsalary)

    # 請用你的程式補完這個函式的區塊
avg({"employees": [{
    "name": "John", "salary": 30000, "manager": False
}, {"name": "Bob", "salary": 60000, "manager": True
    }, {"name": "Jenny", "salary": 50000, "manager": False
        }, {"name": "Tony", "salary": 40000, "manager": False
            }]
})
# 呼叫 avg 函式
# -------------------------------要求3完成------------------------------


# 要求三


def func(a):  # 這裡第一個函數調用返回另一個函數
    def sum(num1, num2):  # 然後用它自己的參數調用它
        print(a+num1*num2)  # 它也可以使用第一個函數的參數和局部變量。
    return sum

    # 請用你的程式補完這個函式的區塊
func(2)(3, 4)  # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5)  # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9)  # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# -------------------------------要求4完成------------------------------
# 要求四


def maxProduct(nums):
    if len(nums) >= 2:  # 觀察列表有無只有2個
        maxnum = nums[0]*nums[1]  # 如果是 maxnum = -1*2=-2 #結果為-2結束
        for i in range(len(nums)-1):  # 會有重複相乘情況故-1
            for j in range(i+1, len(nums)):  # 會有重複相乘情況故＋1
                num = nums[i]*nums[j]  # num=5*20
                if num > maxnum:  # 如果最大數字大於maxnum
                    maxnum = num
    print(maxnum)


# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


# -----------------------------完成要求5------------------------------
# 要求五


def twoSum(nums, target):
    for i in range(len(nums)):  # for i in 4:
        for j in range(i+1, len(nums)):  # for j in(1,4)
            sum = nums[i]+nums[j]  # sum = 2+11
            if sum == target:  # 如果sum = target
                result = [i, j]  # return列表
    print(result)


twoSum([2, 11, 7, 15], 9)  # show [0, 2] because nums[0]+nums[2] is 9
# ---------------------------完成要求6----------------------------------
# 要求六


def maxZeros(nums):
    count = 0   # 記錄目前底幾次出現记录当前元素是第几次连续出现
    maxcount = 0  # 記錄目前出現最大次數
    for i in nums:
        if i == 0:   # 如果i=0
            count = count+1  # 紀錄＋1
        else:  # 如果不等於0
            if count > maxcount:   # 如果目前次數大於最大次數
                maxcount = count  # 最大次數等於目前次數
            count = 0  # 不等於0 count歸零
    if count > maxcount:  # 如果目前次數大於最大次數
        maxcount = count  # 最大次數等於目前次數

    print(maxcount)


    # 請用你的程式補完這個函式的區塊
maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
