from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

rand_tag = ['홈스타그램', '인테리어소품', '집꾸미기','신혼','신혼집', '공간', 
            '이사','집들이','집들이선물','홈스타일링','신혼가구','홈데코','홈인테리어',
            '집꾸미기','오늘의집', '홈스타일링', '집스타그램', '신혼집집들이']

def init():
    # 좋아요 개수 랜덤
    global insta_cnt, insta_tag

    insta_cnt = random.randrange(182, 297)
    print('좋아요 누를 개수는 {}개'.format(insta_cnt))

    # 해시 태그 선택
    insta_tag = random.choice(rand_tag)
    print('이번 태그는 {} 입니다.'.format(insta_tag))


def login():
    ID = 'the.lazuli.official@gmail.com'
    PW = 'lazulilove1!'

    # 화면 띄우기
    global driver
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://instagram.com')
    driver.maximize_window()

    # 로딩 시간 대기
    time.sleep(3)
    print('3초 대기 끝')

    # Login ID 속성 값 찾고 입력
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(ID)

    # Login PW 속성값 찾고 입력
    login_pw = driver.find_element_by_name('password')
    login_pw.send_keys(PW)
    # 엔터키
    time.sleep(1)
    login_pw.send_keys(Keys.RETURN)
    print("로그인 완료")

    time.sleep(3)
    # 로그인정보 '나중에 하기' 버튼 클릭 
    later_btn = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button') 
    later_btn.click() 
    
    #잠시 대기 
    time.sleep(2)
    #알림설정 '나중에하기' 버튼 클릭
    later_btn = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm');
    later_btn.click()     
    #잠시 대기 
    time.sleep(2)
    
def firstFeed():
    #최신게시글 첫번쨰 피드 클릭
    print('최신게시글 첫번째 피드 클릭')
    first_feed = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]')
    first_feed.click()
    time.sleep(2)
    
    
    #좋아요 버튼을 이미 눌렀을까?
    btn = driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    svg_txt = btn.get_attribute('aria-label')
    #좋아요 버튼을 안눌렀으면 버튼 클릭!
    if svg_txt == '좋아요':
         #좋아요 버튼 클릭
        print('좋아요 버튼 클릭!')
        like_btn = driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
        like_btn.click()
        time.sleep(random.randrange(2,4))
    else :
        print('이미 좋아요 눌렀음')
        changeTag()
        firstFeed()
        

def nextFeed():
    #다음 피드 이동 버튼 클릭
    print('다음 피드 이동')
    next_btn = driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button')
    next_btn.click()
    time.sleep(3)
    
    #좋아요 버튼을 이미 눌렀을까?
    btn = driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    svg_txt = btn.get_attribute('aria-label')
    #좋아요 버튼을 안눌렀으면 버튼 클릭!
    if svg_txt == '좋아요':
        #좋아요 버튼 클릭
        print('좋아요 버튼 클릭!')
        like_btn = driver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
        like_btn.click()
        time.sleep(random.randrange(2,4))
    else :
        print('이미 좋아요 눌렀음')
        changeTag()
        firstFeed()
        
def changeTag():
    # 해시 태그 선택
    insta_tag = random.choice(rand_tag)
    print('이번 태그는 {} 입니다.'.format(insta_tag))
    
    #작업할 해시태그 검색 결과 페이지로 이동
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag)) 
    time.sleep(8)


def bot():
    for idx in range(100):
        if idx%3 == 0:
            changeTag()
            firstFeed()
        nextFeed()
        print(idx)

#피드 취소 버튼
#body > div.RnEpo._Yhr4 > div.NOTWr > button

init()
login()
bot()