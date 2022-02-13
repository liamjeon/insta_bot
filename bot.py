from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import pandas as pd
import time
import random
import csv
import schedule 
import time 
import datetime

rand_tag = ['홈스타그램', '인테리어소품', '집꾸미기', '신혼', '신혼집', '공간',
            '이사', '집들이', '집들이선물', '홈스타일링', '신혼가구', '홈데코', '홈인테리어',
            '집꾸미기', '오늘의집', '홈스타일링', '집스타그램', '신혼집집들이']


def init():
    global driver
    driver = webdriver.Chrome('./chromedriver')

    global count_like, count_follow, max_follow, max_like
    count_like = 0
    count_follow = 0
    max_follow = 10
    # 좋아요 개수 랜덤
    max_like = random.randrange(150, 200)
    print('좋아요 누를 개수는 {}개'.format(max_like))
    # 해시 태그 선택
    insta_tag = random.choice(rand_tag)
    print('이번 태그는 {} 입니다.'.format(insta_tag))


def login():
    ID = 'ikhyun709@gmail.com'
    PW = 'roejddl1'

    # ID = 'the.lazuli.official@gmail.com'
    # PW = 'lazulilove1!'

    # 화면 띄우기
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
    print("로그인 버튼 클릭")

    time.sleep(4)
    # 로그인정보 '나중에 하기' 버튼 클릭
    try:
        later_btn = driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div/div/div/button')
        later_btn.click()
    except:
        print('Element 를 찾을 수 없어요')
        print('페이지 종료 후 다시 열기')
        login()

        

    # 잠시 대기
    time.sleep(2)
    # 알림설정 '나중에하기' 버튼 클릭
    later_btn = driver.find_element_by_css_selector(
        'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    later_btn.click()
    # 잠시 대기
    time.sleep(2)


def firstFeed():
    # 최신게시글 첫번쨰 피드 클릭
    print('최신게시글 첫번째 피드 클릭')
    first_feed = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]')
    first_feed.click()
    time.sleep(2)

    # 좋아요 버튼을 이미 눌렀을까?
    btn = driver.find_element_by_css_selector(
        'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    svg_txt = btn.get_attribute('aria-label')
    # 좋아요 버튼을 안눌렀으면 버튼 클릭!
    if svg_txt == '좋아요':
        # 좋아요 버튼 클릭
        print('좋아요 버튼 클릭!')
        like_btn = driver.find_element_by_css_selector(
            'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
        like_btn.click()
        time.sleep(random.randrange(2, 4))
    else:
        print('이미 좋아요 눌렀음')
        changeTag()
        firstFeed()


def nextFeed():
    # 다음 피드 이동 버튼 클릭
    print('다음 피드 이동')
    next_btn = driver.find_element_by_css_selector(
        'body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button')
    next_btn.click()
    time.sleep(3)

    # 좋아요!!
    clickLike()


def clickLike():
    # 좋아요 버튼을 이미 눌렀을까?
    btn = driver.find_element_by_css_selector(
        'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    svg_txt = btn.get_attribute('aria-label')
    # 좋아요 버튼을 안눌렀으면 버튼 클릭!
    if svg_txt == '좋아요':
        # 좋아요 버튼 클릭
        print('좋아요 버튼 클릭!')
        like_btn = driver.find_element_by_css_selector(
            'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
        like_btn.click()
        time.sleep(random.randrange(2, 4))
    else:
        print('이미 좋아요 눌렀음')
        changeTag()
        firstFeed()


def changeTag():
    # 해시 태그 선택
    insta_tag = random.choice(rand_tag)
    print('이번 태그는 {} 입니다.'.format(insta_tag))

    # 작업할 해시태그 검색 결과 페이지로 이동
    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))


def enterId(insta_id):
    # Login ID 속성 값 찾고 입력
    input_id = driver.find_element_by_css_selector(
        '#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > input')
    # input_id.clear()
    input_id.send_keys(insta_id)
    input_id.send_keys(Keys.RETURN)
    time.sleep(1)
    input_id.send_keys(Keys.RETURN)
    time.sleep(1)
    input_id.send_keys(Keys.RETURN)
    time.sleep(6)


def first_feed():
    feed = driver.find_element_by_css_selector(
        '#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0')
    return feed


def next_feed():
    # 다음 피드 이동 버튼 클릭
    print('다음 피드 이동')
    next_btn = driver.find_element_by_css_selector(
        'body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button')
    next_btn.click()
    time.sleep(3)


def click_like():
    # 좋아요 버튼을 이미 눌렀을까?
    btn = driver.find_element_by_css_selector(
        'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')
    svg_txt = btn.get_attribute('aria-label')

    # 좋아요 버튼을 안눌렀으면 버튼 클릭!
    print(svg_txt)
    if svg_txt == '좋아요':
        # 좋아요 버튼 클릭
        print('좋아요 버튼 클릭!')
        like_btn = driver.find_element_by_css_selector(
            'body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
        like_btn.click()
        time.sleep(random.randrange(2, 4))
    else:
        print('이미 좋아요 눌렀음')


def click_follow():
    # 팔로우 버튼을 이미 눌렀을까?
    try:
        btn = driver.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > div.XBGH5 > div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm.bPdm3 > div > div > div > span > span.vBF20._1OSdk > button > div')
        txt = btn.get_attribute('innerHTML')
        
        # 팔로우 버튼을 안눌렀으면 버튼 클릭!
        if txt == '팔로우':
            # 팔로우 버튼 클릭
            print('팔로우 버튼 클릭!')
            follow_btn = driver.find_element_by_css_selector(
                '#react-root > section > main > div > header > section > div.XBGH5 > div.qF0y9.Igw0E.IwRSH.eGOV_.ybXk5._4EzTm.bPdm3 > div > div > div > span > span.vBF20._1OSdk > button')
            follow_btn.click()
            time.sleep(random.randrange(2, 4))
        else:
            print('이미 팔로우 눌렀음')

        return 1

    except:
        print('비공개 계정입니다')
        return 0



def click_escape():
    escape_btn = driver.find_element_by_css_selector(
        ' body > div.RnEpo._Yhr4 > div.NOTWr > button')
    escape_btn.click()


def read_insta_id():
    global list_id
    with open('follower_list.csv', 'r') as f:
        data = list(csv.reader(f, delimiter=";"))
    list_id = np.array(data)


def bot():
    count_follow = 0
    count_like = 0
    count_bot = 0
    # 인스타 아이디 파일 리스트 읽어오기
    read_insta_id()

    for id in list_id:
        if(count_follow < max_follow and count_like < max_like):
            n = random.randrange(0, 16)
        # 팔로워 수 채웠을때 팔로워는 더이상 수행 안함
        elif(count_follow >= max_follow and count_like < max_like):
            n = random.randrange(1, 16)
        # 좋아요 수 채웠을때 좋아요는 더이상 수행 안함
        elif(count_follow < max_follow and count_like >= max_like):
            n = random.randrange(0, 1)
        # 좋아요, 팔로우 모두 채웠을 때 멈춤
        elif(count_follow >= max_follow and count_like >= max_like):
            break

        print('랜덤 값 : {}'.format(n))

        if(n == 0):
            print('아이디 검색', id)
            enterId(id)
            print('팔로우로 정했다')
            if(click_follow()):
                time.sleep(random.randrange(2,4))
                count_follow += 1
                print('지금까지 {}번 팔로우 했습니다.'.format(count_follow))
                print('남은 팔로우 수 : {}'.format(max_follow-count_follow))

        elif(n == 1 or n == 2):
            print('훼이크 다!')
            changeTag()
            time.sleep(8)

        else:
            print('아이디 검색', id)
            enterId(id)
            print('좋아요로 정했다')
            print('첫번째 피드 선택')
            try:
                feed = first_feed()
                feed.click()
                time.sleep(random.randrange(2,4))
                click_like()
                time.sleep(random.randrange(3,5))
                click_escape()
                time.sleep(random.randrange(2,4))
                count_like += 1
                print('지금까지 {}번 좋아요 눌렀습니다.'.format(count_like))
                print('남은 좋아요 수 : {}'.format(max_like-count_like))
            except:
                print('피드가 없습니다')

        print('잠시대기')
        time.sleep(random.randrange(4,8))
        print('-------------------------------------')
        count_bot +=1
        print('{}번째 시도입니다.'.format(count_bot))

    print('인스타 봇 종료')
    driver.close()

def tag():
    # 태그 바꿔가며 좋아요 누르기
    for idx in range(100):
        if idx % 3 == 0:
            changeTag()
            firstFeed()
        nextFeed()
        print(idx)


def loop():
    init()
    login()
    bot()

loop()

# def schedule_bot():
#     schedule.every().day.at("21:52").do(loop)
#     schedule.every().day.at("21:53").do(loop)
#     # schedule.every().day.at("21:32").do(loop)

# schedule_bot()
# while True:
#     schedule.run_pending()
#     time.sleep(1)