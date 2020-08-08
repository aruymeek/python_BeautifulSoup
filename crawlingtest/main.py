############### URL 가져오기 ###############
#import requests

#url = 'https://naver.com'

#headers = {'Content-Type': 'application/json; charset=utf-8'}
#response = requests.get(url, headers=headers)

#print(response.status_code)
#print(response.text)





############### BeautifulSoup ###############
### 1) find
#import requests
#from bs4 import BeautifulSoup

#url = 'https://naver.com'
#response = requests.get(url)

#soup = BeautifulSoup(response.text, 'html.parser')

#find(태그): 해당 태그가 들어간 부분을 찾아냄
#result = soup.find('title')

#print(result)
#print(result.text)         #.text는 태그를 다 제외하고 텍스트만 반환


### 2) select
#import requests
#from bs4 import BeautifulSoup

#url = 'https://sports.news.naver.com/index.nhn'
#response = requests.get(url)

#soup = BeautifulSoup(response.text, 'html.parser')

#select: 해당 class가 들어간 부분을 전부 가져옴 (리스트 형태로)
#class 이름으로 찾고 싶을 때에는 앞에 '.'을 찍어주어야 한다.
#result = soup.select('.today_item')     
                                        
#print(type(result))
#print(result)

#for r in result:
    #select_one(tag)[attribute]: tag 요소 속 attribute에 해당하는 내용을 찾아낼 수 있음 (select보다 더 깊이 들어가기~)
    #print(r.select_one('a')['title'])        # 제목만 나왔다 !!!

    #print(r.select_one('a')['class'])        # class 이름만 나왔다 !!!
    #print(r.select_one('a')['href'])         # 링크만 나왔다 !!!


### 만약에 class가 연속된 게 아닐 경우에는? --> 아래처럼 select를 계속 해나아가면 됨~!
import requests
from model.sports import SportsModel
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/index.nhn'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
#result = soup.select('.today_item')     #얘는 연속성이 있는 데이터(<li>부분)을 가져온 것, select: 여러개
result2 = soup.select_one('.today_list') #만약에 연속성이 없다면 먼저 상위부분(<ul>) 가져오기, select_one: 한개

sportsList = []

for r in result2.select('li'):    #<ul>로 가져온 부분을 <li>를 select 해서 <li> 부분 다 가져오기, <li>는 여러개니까 select
    #print(r)                     #r: 가져온 <li> 부분
    #print(r.select_one('a'))     #r.select_one('a'): <li> 부분에서 또 <a> 태그 추출하기
    
    title = r.select_one('a')['title']     #<a> 태그 부분에서 title 속성 값 보기
    class1 = r.select_one('a')['class']    #<a> 태그 부분에서 class 속성 값 보기
    href = r.select_one('a')['href']       #<a> 태그 부분에서 href 속성 값 보기

    ### 이미지 주소도 가져와보고
    atag = r.select_one('a')
    div1 = atag.select_one('div')
        #html 소스를 보면 <a> 밑에 <div>가 2개 있음.
        #오류 나지 않게 찾아내기 위해서는 div1 = atag.select_one('.image_area')처럼
        #찾고자 하는 div의 class를 적어주면 더 정확하게 오류없이 찾을 수 있음!
    imgsrc = div1.select_one('img')['src']
    #imgsrc = r.select_one('a div img')['src'] 로 한 줄에 쓸 수도 있음!!!!!

    ### 기사 내용도 가져와보고
    content = atag.select_one('.news').text
        #지금 코드는 어차피 <a> 안에 news라는 class가 하나밖에 없어서 오류가 없지만
        #혹시라도 '.news'라는 클래스 이름은 여러군데에서 쓰일 수 있기때문에
        #최대한 <a>에서 하위 > 하위 > 하위 > 하위로 가면서 찾아내는 것이 정확함!
    
    spm = SportsModel(title, class1, href, imgsrc, content)
    sportsList.append(spm)

for sport1 in sportsList:
    print('{0} {1} {2} {3} {4}'.format(sport1.title, sport1.class1, sport1.href, sport1.imgsrc, sport1.content))


#★★★ [속성이름]은 해당 속성의 값을 가지고 올 때,
#select('속성값')은 해당 속성값이 들어있는 구문을 찾을 때라고 생각하자


