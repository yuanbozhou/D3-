import requests, csv,re
from lxml import etree
import mysql.connector




#设置浏览器代理,它是一个字典
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 创建文件夹并打开
fp = open("./drama.csv", 'a', newline='', encoding = 'utf-8-sig')
writer = csv.writer(fp) #我要写入
# 写入内容
writer.writerow(('id', '主题', '时间', '地点', '费用'))
id=0
for page in range(0, 2): #226
    print ("正在获取第%s页"%page)
    pageweb=page*10
    # url = 'https://movie.douban.com/top250?start=%s&filter='%page
    url =   'https://douban.com/location/hangzhou/events/future-drama?start=%s'%pageweb
    
    print(pageweb)

    #请求源代码，向服务器发出请求,200代表成功，回退对其，Ctrl+]
    reponse = requests.get(url = url, headers = headers).text
    # 快捷键运行，Ctrl+Enter
    
    html_etree = etree.HTML(reponse) # 看成一个筛子，树状
    # 过滤
    # li = html_etree.xpath('//*[@id="content"]/div/div[1]/ol/li')
    li = html_etree.xpath('//*[@id="db-events-list"]/ul/li')
    
    for item in li:        
        #名称
        name = item.xpath('./div[2]/div/a/span/text()')[0]
        #时间     
        time =item.xpath('./div[2]/ul/li[1]/text()')[1]
        #地点 //*[@id="db-events-list"]/ul/li[1]/div[2]/ul/li[2]
        
        location =item.xpath('./div[2]/ul/li[2]/text()')[1]
        # print("location="+location)
        #费用 
        rmb =item.xpath('./div[2]/ul/li[3]/strong/text()')[0]
        print (name,time,location,rmb)
        # print(1234)
        print(type(str(time)))
        name1=str(name).strip()
        time1=str(time).strip()
        location1=str(location).strip()
        rmb1=str(rmb).strip()
        # print(time1.strip())
        # print(len(time1))

        
        # connect = mysql.connector.connect(
        #     host="127.0.0.1",       # 数据库主机地址
        #     user="root",            # 数据库用户名
        #     passwd="",          # 数据库密码
        #     database="yuanbo_keshituili"         # 要连接的数据库
        # )
        # # 数据库插入指令,待定字符无论是数值还是文字，都需要用%s
        # sql = "INSERT INTO `drama`(`id`, `name`, `time`, `location`, `rmb`) VALUES (%s,%s,%s,%s,%s)"
       
        # id=id+1
        # var = (id,name1,time1,location1,rmb1)
      
        
        # # 获取数据库操作游标
        # myCursor = connect.cursor()
        # try:
        #     # 执行sql语句
        #     myCursor.execute(sql, var)
        #     # 提交给数据库执行命令
        #     connect.commit()
        # except :
        #     #回滚，以防出现错误
        #     connect.rollback()

        # connect.close()
        # 写入内容
        id=id+1
        writer.writerow((id,name1,time1,location1,rmb1))
fp.close()

