import requests  #얘는 url(http)에서 html 불러올 때 쓰는 메서드
from bs4 import BeautifulSoup


### file open 시 path 앞 'r'의 의미? 경로를 쓰겠다는 의미! /와 \ 구분을 없애준다고 생각하면 됨~
f = open(r"C:/Users/671/Desktop/y/python/webtest/my/info.html", encoding='utf-8')
soup = BeautifulSoup(f)
#print(soup)


### (tbody 뽑아내기) <==> tbody = soup.select_one('#table1 tbody') 한줄로도 가능
#table = soup.select_one('#table1')
#print(table)

#tbody = table.select_one('tbody')
#print(tbody)


### (th 뽑아내기) for문을 활용하자
thead = soup.select_one('#table1 thead')

# for th in thead.select('th'):
#     print(th.text)


### (tr 뽑아내기) for문을 활용하자
#soup에서 한 번에 'tr' 찾아내기도 가능 (내 html에는 table이 한 개니까, 만약 테이블이 여러개이면 명확하지 않으니 사용 지양)
#<==> trs = tbody.select('tr')
trs = soup.select('tr')

#만약 가져오려는 tr에 class('tr1')가 부여되어있다면 class명 앞에 '.'을 찍어 찾아내자
# tr1 = soup.select('.tr1')
# print(tr1)

# for tr in trs:
#     print(tr)


### (th의 각각 값에 맞게 tr 값 찾아내기)
# release = thead.select('th')[0].text
# print(release)

# for tr in trs:
#     tds = tr.select('td')
#     text = tds[0].text
    
#     date = text.split('.')
#     year = int(date[0])
#     month = int(date[1])
#     day = int(date[2])

#     print('{0}년 {1:>2}월 {2:>2}일'.format(year, month, day))


### (한 줄 씩 전부 뽑아내기)
for tr in trs:
    date = tr.select('td')[0].text
    album = tr.select('td')[1].text
    title = tr.select('td')[2].text
    nation = tr.select('td')[3].text

    print('발매일: {0}, 앨범명: {1}, 타이틀곡: {2}, 발매국가: {3}'.format(date, album, title, nation))


