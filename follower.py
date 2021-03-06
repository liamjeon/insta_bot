from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import numpy as np
import pandas as pd


rand_tag = ['홈스타그램', '인테리어소품', '집꾸미기', '신혼', '신혼집', '공간',
            '이사', '집들이', '집들이선물', '홈스타일링', '신혼가구', '홈데코', '홈인테리어',
            '집꾸미기', '오늘의집', '홈스타일링', '집스타그램', '신혼집집들이']


def init():
    # 좋아요 개수 랜덤
    global insta_cnt, insta_tag

    insta_cnt = random.randrange(182, 297)
    print('좋아요 누를 개수는 {}개'.format(insta_cnt))

    # 해시 태그 선택
    insta_tag = random.choice(rand_tag)
    print('이번 태그는 {} 입니다.'.format(insta_tag))


def login():
    # ID = 'the.lazuli.official@gmail.com'
    # PW = 'lazulilove1!'
    ID = 'ikhyun709@gmail.com'
    PW = 'roejddl1'

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
    later_btn = driver.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/div/div/div/button')
    later_btn.click()

    # 잠시 대기
    time.sleep(2)
    # 알림설정 '나중에하기' 버튼 클릭
    later_btn = driver.find_element_by_css_selector(
        'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    later_btn.click()
    # 잠시 대기
    time.sleep(3)

def enterId(insta_id):
    #Login ID 속성 값 찾고 입력
    input_id = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.QY4Ed.P0xOK > input');
    input_id.send_keys(insta_id)
    input_id.send_keys(Keys.RETURN)
    time.sleep(1)
    input_id.send_keys(Keys.RETURN)
    time.sleep(1)
    input_id.send_keys(Keys.RETURN)
    time.sleep(3)
    
    #팔로워 수 가져오기
    global number_of_following
    following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span')
    number_of_following = following.get_attribute("innerHTML")
    print("number_of_following :- "+number_of_following)
    time.sleep(1)

    #프로필에서 팔로워 클릭
    click_follower = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > div')
    click_follower.click()
    time.sleep(6)


def scroll():
    # 스크롤 높이 가져옴
    scroll_box = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]')
    last_ht, ht = 0, 1
    num = 0;
    while last_ht != ht:
        print('스크롤')
        last_ht = ht
        time.sleep(5)
        ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """, scroll_box)
        num +=1
        if(num == 180): break

    time.sleep(2)
    #Follow List를 읽어옴
    print('팔로우를 읽어 옵니다.')
    print(number_of_following)
    follower_list = []
    for x in range(2, 1500):  
        username = driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/ul/div/li['+str(x)+']/div/div[1]/div[2]/div[1]/span/a/span')
        # print(username.get_attribute("innerHTML")) 
        follower_list.append(username.get_attribute("innerHTML"))

    print('리스트 파일 출력')
    arr = np.array(follower_list)
    df = pd.DataFrame(arr)
    df.to_csv('follower_list.csv', index=False)

init()
login()
enterId('maumio_store')
scroll()
