##### 테이블 형태의 자료도 가져와보기 #####
import requests
from model.company import CompanyModel
from bs4 import BeautifulSoup

url = 'https://www.corporateknights.com/reports/2020-global-100/2020-global-100-ranking-15795648/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# [table 찾기] table_1이라는 id는 딱 하나밖에 없으니까, select_one으로 불러오도록 한다!
#table = soup.select_one('#table_1')          #id를 검색할 때에는 앞에 '#' (cf/ class는 '.')
#print(table)

# [table 하위의 <tbody> 가져오기]
tbody = soup.select_one('#table_1 tbody')     #이렇게 띄어쓰기로 하위항목 표시할 수 있다
#print(tbody)

companyList = []

# [tbody 하위의 <tr>, <td> 가져오기] for문을 활용하자
for tr in tbody.select('tr'):     #<tbody> 하위에 <tr>은 여러개 있으니까 select를 이용한다
    #print(tr)
    
    #<tr> 하위에 6개의 <td>가 존재하므로(여러개) select 이용하여 <td>를 추출하자
    #.text로 < > 태그 다 없애고 문자만 남기기
    
    #첫번째 <td>는 2020년 순위, 정수(int)로 형변환
    rank2020 = int(tr.select('td')[0].text) 

    #두번재 <td>는 2019년 순위, 정수(int)로 형변환         
    rank2019 = tr.select('td')[1].text  
    #rank2019는 현재 순위와 변동이 없으면 '-'로 표기되므로 숫자 변환을 위해 if로 걸러주기           
    if rank2019.isdigit() == False:                   
        rank2019 = rank2020
    else:
        rank2019 = int(rank2019)

    #세번째 <td>는 기업명
    name = tr.select('td')[2].text    

    #네번째 <td>는 종목
    category = tr.select('td')[3].text 

    #다섯번째 <td>는 국가              
    country = tr.select('td')[4].text             

    #여섯번째 <td>는 점수, 텍스트로 받았기 때문에 %를 지우고 실수(float)로 형변환을 해주어야 한다.
    score = float(tr.select('td')[5].text.replace('%', ''))

    company = CompanyModel(name, category, country, score, rank2020, rank2019)
    companyList.append(company)

# [데이터로 저장하기]
f = open('C:/Users/671/Desktop/y/python/crawlingtest/company list/list.txt', 'w', encoding='utf-8')

for c in companyList:
    #data = '{0};{1};{2};{3};{4};{5}'.format(c.name, c.category, c.country, c.score, c.rank2020, c.rank2019)
    #나중에 불러오기 쉽게 ';'로 구분해주는 것이 좋다

    #위의 data를 CompanyModel 내의 메서드로 구현을 해보자
    data = c.SaveFormat()
    
    f.write(data + '\n')

    #데이터를 불러와서 처리할 때 한 줄 띄어지는 공백 현상이 생기면 따로 write를 해봐
    #f.write(data)
    #f.write('\n')

f.close()





