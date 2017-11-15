from bs4 import BeautifulSoup
import urllib
import pandas as pd 

pages = 140
i =1
rec_count =0
rank = []
game = []
platform =[]
year = []
genre = []
publisher = []
sales_na = []
sales_eu = []
sales_jp = []
sales_ot = []
sales_gl = []
def clear_data(self):
    rank.clear
    game.clear
    platform.clear
    year.clear
    genre.clear
    publisher.clear
    sales_na.clear
    sales_eu.clear
    sales_jp.clear
    sales_ot.clear
    sales_gl.clear
urlhead = 'http://www.vgchartz.com/gamedb/?page='
urltail = '&results=186344&name=&platform=&minSales=0&publisher=&genre=&sort=GL'
for x in range(1): 
    for page in range(x+1,pages):
        rank.clear()
        game.clear()
        platform.clear()
        year.clear()
        genre.clear()
        publisher.clear()
        sales_na.clear()
        sales_eu.clear()
        sales_jp.clear()
        sales_ot.clear()
        sales_gl.clear()
        real_url = urlhead + str(page) +urltail
        r = urllib.request.urlopen(real_url)
        soup = BeautifulSoup(r,"lxml")
        print("page:"+str(page))
        chart = soup.find("table", class_="chart")
        for row in chart.find_all('tr')[1:]:
                try:
                    col = row.find_all('td')

                    column1 = col[0].string.strip()
                    column2 = col[1].string.strip()
                    column3 = col[2].string.strip()
                    column4 = col[3].string.strip()
                    column5 = col[4].string.strip()
                    column6 = col[5].string.strip()
                    column7 = col[6].string.strip()
                    column8 = col[7].string.strip()
                    column9 = col[8].string.strip()
                    column10 = col[9].string.strip()
                    column11 = col[10].string.strip()

                    #清除数据
                    
                    #添加数据到list中

                    rank.append(column1)
                    game.append(column2)
                    platform.append(column3)
                    year.append(column4)
                    genre.append(column5)
                    publisher.append(column6)
                    sales_na.append(column7)
                    sales_eu.append(column8)
                    sales_jp.append(column9)
                    sales_ot.append(column10)
                    sales_gl.append(column11)

                    rec_count += 1
                    print(rec_count)
                except:
                    continue
        
        if page==page:
            columns = {'rank': rank, 'name': game, 'platform': platform, 'year': year, 'genre': genre, 'publisher': publisher, 'NA_Sales':sales_na, 'EU_Sales': sales_eu,'JP_Sales': sales_jp,'Other_Sales':sales_ot, 'Global_Sales':sales_gl }
            print("rec_count"+str(rec_count))
            df = pd.DataFrame(columns)
            # df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
            del df.index.name
            df.to_csv(str(page)+"vgsales.csv",sep=",",encoding='utf-8')
            print("save csv"+str(page))
            continue
            
        # elif page==2 :
        #     columns = {'rank': rank, 'name': game, 'platform': platform, 'year': year, 'genre': genre, 'publisher': publisher, 'NA_Sales':sales_na, 'EU_Sales': sales_eu,'JP_Sales': sales_jp,'Other_Sales':sales_ot, 'Global_Sales':sales_gl }
        #     print("rec_count"+str(rec_count))
        #     df = pd.DataFrame(columns)
        #     # df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
        #     del df.index.name
        #     df.to_csv("vgsales2.csv",sep=",",encoding='utf-8')
        #     print("save csv2")
        #     continue
        # elif page==3 :
        #     columns = {'rank': rank, 'name': game, 'platform': platform, 'year': year, 'genre': genre, 'publisher': publisher, 'NA_Sales':sales_na, 'EU_Sales': sales_eu,'JP_Sales': sales_jp,'Other_Sales':sales_ot, 'Global_Sales':sales_gl }
        #     print("rec_count"+str(rec_count))
        #     df = pd.DataFrame(columns)
        #     # df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
        #     del df.index.name
        #     df.to_csv("vgsales3.csv",sep=",",encoding='utf-8')
        #     print("save csv2")
        #     continue

        # elif page==4 :
        #     columns = {'rank': rank, 'name': game, 'platform': platform, 'year': year, 'genre': genre, 'publisher': publisher, 'NA_Sales':sales_na, 'EU_Sales': sales_eu,'JP_Sales': sales_jp,'Other_Sales':sales_ot, 'Global_Sales':sales_gl }
        #     print("rec_count"+str(rec_count))
        #     df = pd.DataFrame(columns)
        #     # df = df[['Rank','Name','Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']]
        #     del df.index.name
        #     df.to_csv("vgsales4.csv",sep=",",encoding='utf-8')
        #     print("save csv2")
        #     continue
        else:
            continue
        
            
           



