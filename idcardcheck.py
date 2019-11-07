'''
身份证验证
得到一张火车票，生日会被隐藏，通过获得所有生日的可能性
再到对应的网站上去验证身份证是否和名字匹配，从而获得身份证信息
'''
import time

def isVaildDate(date):
    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False 

def trans_date(elem):
    if elem < 10:
        return '0'+ str(elem)
    return str(elem)

def generate_date(year):
    date=[]
    for m in range(1,13):
        month=trans_date(m)
        for d in range(1,32):
            day=trans_date(d)
            date.append(year +'-'+ month+'-' + day)
    return date

def isVaildID(id):
    #id 的类型为str
    sum = 0
    key_dict = (7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
    checkCodeTable={
        '1':'0',
        '2':'X',
        '3':'9',
        '4':'8',
        '5':'7',
        '6':'6',
        '7':'5',
        '8':'4',
        '9':'3',
        '10':'2'
        }
    for str_id_num,n in zip(id,key_dict):
        sum += int(str_id_num) * n
    check_code = str(sum % 11)

    endWord = checkCodeTable.get(check_code)
    if(id[-1] == endWord):
        return True
    return False

def check():
    #填写身份证的前六位 和 后四位
    first_ten_digits = ''
    end_four_digits = ''

    date = generate_date(first_ten_digits[-4:])
    for p in date:
        if isVaildDate(p):
            id_date = first_ten_digits+p.split('-')[1]+p.split('-')[2]+end_four_digits
            if isVaildID(id_date):
                print(id_date)

check()