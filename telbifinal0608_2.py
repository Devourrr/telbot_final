# telbi 큰 카테 고리 4가지
#음식 운동 날씨 뉴스
#6월 2일 할꺼 
#음성파일 저장 오류, 스케줄 짜기
#쓰레드 넣기 현재 오류 쓰레드안에 키보드 구현하는거
#음식에 driver.quit 넣기 부분 부분 마다
#6월 3일 

import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)
import telebot # pip install pyTelegramBotAPI
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import time
from PIL import Image
import schedule   #pip install schedule
import threading
import random
from gtts import gTTS #pip install gTTS
import pyautogui    #pip install pyautogui
from urllib3.packages.six import b
#pip install opencv-python
import pyautogui as pag
import pywinauto
import pygetwindow as gw

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
TOKEN = "1709776665:AAF-sEQXF2TAW67-aOno7o4zrDoiGSeeRrU"
bot = telebot.TeleBot(TOKEN)
now = time.localtime()
chat_id = 1598663873
result = ""

opts = webdriver.ChromeOptions()
opts.add_argument('window-size=960,750')

now = time.localtime(time.time())
hour = now.tm_hour

CATEGORY = range(1)

EXERCISE,MEAL,NEWS,WEATHER,CARDIOEXERCISE,WEIGHTTRAINING,KOREA,JAPAN,USA,CHINA,CORONA,HEADLINE,POLITICS,ECONOMY,SOCIAL = range(15)

def start(update:Update, _: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s  started the conversation.", user.first_name)
    keyboard = [
        [
            InlineKeyboardButton("1.운동", callback_data=str(EXERCISE)),
            InlineKeyboardButton("2.식사", callback_data=str(MEAL)),
            InlineKeyboardButton("3.뉴스", callback_data=str(NEWS)),
            InlineKeyboardButton("4.날씨", callback_data=str(WEATHER)),
            
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "안녕하세요 텔비입니다." + "원하시는걸 선택해주세요!", reply_markup=reply_markup
        )
    return CATEGORY

def exercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("유산소 운동", callback_data=str(CARDIOEXERCISE)),
            InlineKeyboardButton("무산소 운동", callback_data=str(WEIGHTTRAINING)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="어떤 운동 하시겠어요?", reply_markup=reply_markup)
    return CATEGORY

def cardioexercise(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="유산소 운동을 안내해드립니다.")
    driver = webdriver.Chrome('chromedriver.exe')
    cardio= ['점핑잭', '버피 테스트', '계단 오르기','스트레칭','걷기', '조깅', '달리기', '자전거']
    health_result = random.choice(cardio)
    if health_result == cardio[0]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=510&cal_type=E')
        jump = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        jm_info = f'실내에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다.\n{jump}'
        tts = gTTS(jm_info, lang='ko')
        tts.save("jm_info.ogg")
        audio = open("jm_info.ogg", 'rb')
        bot.send_message(chat_id, jm_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == cardio[1]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=491&cal_type=E')
        buf = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bf_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{buf}'
        tts = gTTS(bf_info, lang='ko')
        tts.save("bf_info.ogg")
        audio = open("bf_info.ogg", 'rb')
        bot.send_message(chat_id, bf_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == cardio[2]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=21&cal_type=E')
        stair = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        str_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{stair}'
        tts = gTTS(str_info, lang='ko')
        tts.save("str_info.ogg")
        audio = open("str_info.ogg", 'rb')
        bot.send_message(chat_id, str_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == cardio[3]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=194&cal_type=E')
        strch =driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        sr_info = f'실내에서 할 수 있는 유산소 운동  {health_result}을 추천합니다.\n스트레칭은 {strch}'
        tts = gTTS(sr_info, lang='ko')
        tts.save("sr_info.ogg")
        audio = open("sr_info.ogg", 'rb')
        bot.send_message(chat_id, sr_info)
        bot.send_audio(chat_id, audio=audio)
        
    elif health_result == cardio[4]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=14&cal_type=E')
        walk = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        wk_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다. 걷기 운동 효과 {walk}'
        tts = gTTS(wk_info, lang='ko')
        tts.save("wk_info.ogg")
        audio = open("wk_info.ogg", 'rb')
        bot.send_message(chat_id, wk_info)
        bot.send_audio(chat_id, audio=audio)
        
    elif health_result == cardio[5]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=54&cal_type=E')
        jog = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        jg_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다.\n{jog}'
        tts = gTTS(jg_info, lang='ko')
        tts.save("jg_info.ogg")
        audio = open("jg_info.ogg", 'rb')
        bot.send_message(chat_id, jg_info)
        bot.send_audio(chat_id, audio=audio)
        
    elif health_result == cardio[6]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=77&cal_type=E')
        run = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        rn_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}를 추천합니다. 달리기는 {run}'
        tts = gTTS(rn_info, lang='ko')
        tts.save("rn_info.ogg")
        audio = open("rn_info.ogg", 'rb')
        bot.send_message(chat_id, rn_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == cardio[7]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=254&cal_type=E')
        bic = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bc_info = f' 야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다.\n{bic}'
        tts = gTTS(bc_info, lang='ko')
        tts.save("bc_info.ogg")
        audio = open("bc_info.ogg", 'rb')
        bot.send_message(chat_id, bc_info)
        bot.send_audio(chat_id, audio=audio)

    driver.quit()
    time.sleep(1)
    win = gw.getWindowsWithTitle('Telegram')[0] # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
    app =pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
    win.activate() #윈도우 활성화
    app.move_window(x=0, y=0, width=796, height=1000, repaint=True)
    pag.click(win.left + 64, win.top + 893) # 해당 윈도우의 633,936 위치 클릭
    # Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    # pyautogui.click(Click)
    return ConversationHandler.END

def weighttraining(update:Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    driver = webdriver.Chrome('chromedriver.exe')
    query.edit_message_text(text="무산소 운동을 안내해드립니다.")
    weight = ['팔굽혀펴기','윗몸일으키기','턱걸이','플랭크','벤치프레스','데드리프트','스쿼트','밀리터리프레스'] 
    
    health_result = random.choice(weight)
    if health_result == weight[0]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=451&cal_type=E')
        pus = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        pu_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{pus}' 
        tts = gTTS(pu_info, lang='ko')
        tts.save("pu_info.ogg")
        audio = open("pu_info.ogg", 'rb')
        bot.send_message(chat_id, pu_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[1]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=453&cal_type=E')
        stup = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        st_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{stup}'
        tts = gTTS(st_info, lang='ko')
        tts.save("st_info.ogg")
        audio = open("st_info.ogg", 'rb')
        bot.send_message(chat_id, st_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[2]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=316&cal_type=E')
        pul = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        pl_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{pul}'
        tts = gTTS(pl_info, lang='ko')
        tts.save("[pl_info.ogg")
        audio = open("pl_info.ogg", 'rb')
        bot.send_message(chat_id, pl_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[3]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=378&cal_type=E')
        plk = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        plk_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{plk}'
        tts = gTTS(plk_info, lang='ko')
        tts.save("plk_info.ogg")
        audio = open("plk_info.ogg", 'rb')
        bot.send_message(chat_id, plk_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[4]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=105&cal_type=E')
        bnp = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{bnp}'
        tts = gTTS(bp_info, lang='ko')
        tts.save("bp_info.ogg")
        audio = open("bp_info.ogg", 'rb')
        bot.send_message(chat_id, bp_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[5]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=59&cal_type=E')
        dlft = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        dl_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{dlft}'
        tts = gTTS(dl_info, lang='ko')
        tts.save("dl_info.ogg")
        audio = open("dl_info.ogg", 'rb')
        bot.send_message(chat_id, dl_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[6]:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=461&cal_type=E')
        squ =driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        sq_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 스쿼트 운동 효과, {squ}'
        tts = gTTS(sq_info, lang='ko')
        tts.save("sq_info.ogg")
        audio = open("sq_info.ogg", 'rb')
        bot.send_message(chat_id, sq_info)
        bot.send_audio(chat_id, audio=audio)

    else:
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=471&cal_type=E')
        mlp = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li/text()').text
        mp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n밀리터리 프레스는 {mlp}'
        tts = gTTS(mp_info, lang='ko')
        tts.save("mp_info.ogg")
        audio = open("mp_info.ogg", 'rb')
        bot.send_message(chat_id, mp_info)
        bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END


def meal(update:Update,_: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("한식", callback_data=str(KOREA)),
            InlineKeyboardButton("일식", callback_data=str(JAPAN)),
            InlineKeyboardButton("양식", callback_data=str(USA)),
            InlineKeyboardButton("중식", callback_data=str(CHINA)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="음식 메뉴를 선택해주세요!", reply_markup=reply_markup)
    return CATEGORY

def korea(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="한식을 선택하셨습니다!")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 선택 중입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    korean_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[2]')
    korean_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    kor_info = voice1 + voice3 + voice4
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    tts = gTTS(kor_info, lang='ko')
    tts.save("kor_info.ogg")
    audio = open("kor_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, kor_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def japan(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="일식을 선택하셨습니다!")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    japan_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[4]')
    japan_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n 입니다.'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    jap_info = voice1 + voice3 + voice4 
    tts = gTTS(jap_info, lang='ko')
    tts.save("jap_info.ogg")
    audio = open("jap_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, jap_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def usa(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="양식을 선택하셨습니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중 입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    usa_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[5]')
    usa_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    usa_info = voice1 +voice3 + voice4
    tts = gTTS(usa_info, lang='ko')
    tts.save("usa_info.ogg")
    audio = open("usa_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, usa_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END
    
def china(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="중식을 선택하셨습니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    query.edit_message_text(text= "메뉴 고민 중 입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    china_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[3]')
    china_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    query.edit_message_text(text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    chi_info = voice1 +voice3 + voice4
    tts = gTTS(chi_info, lang='ko')
    tts.save("chi_info.ogg")
    audio = open("chi_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, chi_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def news(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard =[
        [
            InlineKeyboardButton("코로나", callback_data=str(CORONA)),
            InlineKeyboardButton("헤드라인", callback_data=str(HEADLINE)),
            InlineKeyboardButton("정치", callback_data=str(POLITICS)),
            InlineKeyboardButton("경제", callback_data=str(ECONOMY)),
            InlineKeyboardButton("사회", callback_data=str(SOCIAL)),

            

        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="카테고리를 선택해주세요", reply_markup=reply_markup)
    return CATEGORY

def corona(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
    route = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/table/tbody').text
    time.sleep(1)
    driver.get('https://m.news.naver.com/covid19/index.nhn')
    add1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[1]').text
    add2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[2]').text
    add3 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[3]').text
    stt= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/dl').text
    covd = f'코로나 환자 신규 합계 {stt} \n 확진자 이동경로 \n{route}, \n실시간 추가 확진 현황{add1}+{add2}+{add3}'
    tts = gTTS(covd, lang='ko')
    tts.save("covd.ogg")
    audio = open("covd.ogg",'rb')
    bot.send_message(chat_id, covd)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def headline(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com') 
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    head = f'네이버 헤드라인 뉴스 탑 5 소개해드릴게요.\n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(head, lang='ko')
    tts.save("head.ogg")
    audio = open("head.ogg",'rb')
    bot.send_message(chat_id, head)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def politics(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    politi = f'네이버 정치뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(politi, lang='ko')
    tts.save("politi.ogg")
    audio = open("politi.ogg",'rb')
    bot.send_message(chat_id, politi)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def economy(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    eco = f'네이버 경제 뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(eco, lang='ko')
    tts.save("eco.ogg")
    audio = open("eco.ogg",'rb')
    bot.send_message(chat_id, eco)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def social(update: Update, _: CallbackContext) -> int:
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    soci = f'네이버 사회뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(soci, lang='ko')
    tts.save("soci.ogg")
    audio = open("soci.ogg",'rb')
    bot.send_message(chat_id, soci)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END
    
def weather(update: Update, _: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/search?q=오늘날씨')
    time.sleep(0.5)
    weather= driver.find_element(By.XPATH,'//*[@id="wob_dc"]')
    weather_info = weather.text
    svg = driver.find_element(By.XPATH,'//*[@id="wob_gsvg"]')
    tmp_list = svg.text.split('\n')
    map_list = list(map(float, tmp_list))
    tmp_max = max(map_list)
    tmp_min = min(map_list)
    tmp_gap = float(tmp_max) - float(tmp_min)
    tmp_avg = sum(map_list)/len(map_list)
    voice_tmp = f'오늘의 날씨정보는 {weather_info}, 최고기온 {tmp_max}도,최저기온 {tmp_min}도,평균기온 {tmp_avg}도, 일교차는{tmp_gap}도 입니다.\n'    
    v_w_info =""
    voice_tmp_gap= ""
    voice_cl = ""

    if weather_info == '광역성 소나기':
        v_w_info1 = f'{weather_info}가 예정되어 있습니다. 휴대용 우산을 챙겨주세요.\n'
        v_w_info = v_w_info1
    elif weather_info == '비':
        v_w_info2 = f'{weather_info}가 예정되어 있습니다. 우산을 챙겨주세요.\n'
        v_w_info = v_w_info2

    if tmp_gap > 7.5:
        voice_tmp_gap1 = f'오늘은 일교차가 큽니다. 얇은 옷을 겹쳐입거나 외투를 준비해주세요.\n'
        voice_tmp_gap = voice_tmp_gap1
    else:
        voice_tmp_gap2 = f'오늘은 일교차가 크지 않습니다.\n'
        voice_tmp_gap = voice_tmp_gap2

    if tmp_avg >= 10 and tmp_avg <=16:
        voice_cl1 = f'기온별 옷차림 추천, 평균 {tmp_avg}도에는 자켓, 셔츠, 가디건, 간절기 야상, 살구색 스타킹을 추천드릴게요!'
        voice_cl = voice_cl1
    elif tmp_avg > 16 and tmp_avg <= 19:
        voice_cl2 = f'기온별 옷차림 추천, {tmp_avg}도에는 니트, 가디건, 후드티, 맨투맨, 청바지, 면바지, 슬랙스, 원피스을 추천드릴게요!'
        voice_cl = voice_cl2
    elif tmp_avg >19 and tmp_avg <=  22:
        voice_cl3 = f'기온별 옷차림 추천, {tmp_avg}도에는 긴팔티, 가디건, 후드티, 면바지 ,슬랙스, 스키니을 추천드릴게요!'
        voice_cl = voice_cl3
    elif tmp_avg >22 and tmp_avg <= 26:
        voice_cl4 = f'기온별 옷차림 추천, {tmp_avg}도에는 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지을 추천드릴게요!'
        voice_cl = voice_cl4
    elif tmp_avg > 26:
        voice_cl5 = f'기온별 옷차림 추천, {tmp_avg}도에는 나시티, 반바지, 민소매, 원피스을 추천드릴게요!'
        voice_cl = voice_cl5
    elif tmp_avg < 10:
        voice_cl6 = f'기온별 옷차림 추천, {tmp_avg}도에는 패딩점퍼, 코트, 야상, 목도리, 장갑, 히트텍을 추천드릴게요!'
        voice_cl = voice_cl6

    weather_message = voice_tmp + v_w_info + voice_tmp_gap + voice_cl
    tts = gTTS(weather_message, lang='ko')
    tts.save("weather_message.ogg")
    audio = open("weather_message.ogg",'rb')
    bot.send_message(chat_id,weather_message)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    return ConversationHandler.END

def main() -> None:
    updater = Updater("1709776665:AAF-sEQXF2TAW67-aOno7o4zrDoiGSeeRrU")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start',start)],
        states={
            CATEGORY: [
                CallbackQueryHandler(exercise, pattern='^' + str(EXERCISE) + '$'),
                CallbackQueryHandler(cardioexercise, pattern='^' + str(CARDIOEXERCISE) + '$'),
                CallbackQueryHandler(weighttraining, pattern='^' + str(WEIGHTTRAINING) + '$'),
                CallbackQueryHandler(news, pattern='^' + str(NEWS) + '$'),
                CallbackQueryHandler(corona, pattern='^' + str(CORONA) + '$'),
                CallbackQueryHandler(headline, pattern='^' + str(HEADLINE) + '$'),
                CallbackQueryHandler(politics, pattern='^' + str(POLITICS) + '$'),
                CallbackQueryHandler(economy, pattern='^' + str(ECONOMY) + '$'),
                CallbackQueryHandler(social, pattern='^' + str(SOCIAL) + '$'),
                CallbackQueryHandler(weather, pattern='^' + str(WEATHER) + '$'),
                CallbackQueryHandler(meal, pattern='^' + str(MEAL) + '$'),
                CallbackQueryHandler(korea, pattern='^' + str(KOREA) + '$'),
                CallbackQueryHandler(japan, pattern='^' + str(JAPAN) + '$'),
                CallbackQueryHandler(usa, pattern='^' + str(USA) + '$'),
                CallbackQueryHandler(china, pattern='^' + str(CHINA) + '$'),
                
            ],
        },
        fallbacks= [CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()

def wakeup_time():
    bot.send_message(chat_id, "굿모닝 좋은 아침입니다! ")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://www.google.com/search?q=오늘날씨')
    time.sleep(0.5)
    weather= driver.find_element(By.XPATH,'//*[@id="wob_dc"]')
    weather_info = weather.text
    svg = driver.find_element(By.XPATH,'//*[@id="wob_gsvg"]')
    tmp_list = svg.text.split('\n')
    map_list = list(map(float, tmp_list))
    tmp_max = max(map_list)
    tmp_min = min(map_list)
    tmp_gap = float(tmp_max) - float(tmp_min)
    tmp_avg = sum(map_list)/len(map_list)
    voice_tmp = f'오늘의 날씨정보는 {weather_info}, 최고기온 {tmp_max}도,최저기온 {tmp_min}도,평균기온 {tmp_avg}도, 일교차는{tmp_gap}도 입니다.\n'    
    v_w_info =""
    voice_tmp_gap= ""
    voice_cl = ""

    if weather_info == '광역성 소나기':
        v_w_info1 = f'{weather_info}가 예정되어 있습니다. 휴대용 우산을 챙겨주세요.\n'
        v_w_info = v_w_info1
    elif weather_info == '비':
        v_w_info2 = f'{weather_info}가 예정되어 있습니다. 우산을 챙겨주세요.\n'
        v_w_info = v_w_info2

    if tmp_gap > 7.5:
        voice_tmp_gap1 = f'오늘은 일교차가 큽니다. 얇은 옷을 겹쳐입거나 외투를 준비해주세요.\n'
        voice_tmp_gap = voice_tmp_gap1
    else:
        voice_tmp_gap2 = f'오늘은 일교차가 크지 않습니다.\n'
        voice_tmp_gap = voice_tmp_gap2

    if tmp_avg >= 10 and tmp_avg <=16:
        voice_cl1 = f'기온별 옷차림 추천, 평균 {tmp_avg}도에는 자켓, 셔츠, 가디건, 간절기 야상, 살구색 스타킹을 추천드릴게요!'
        voice_cl = voice_cl1
    elif tmp_avg > 16 and tmp_avg <= 19:
        voice_cl2 = f'기온별 옷차림 추천, {tmp_avg}도에는 니트, 가디건, 후드티, 맨투맨, 청바지, 면바지, 슬랙스, 원피스을 추천드릴게요!'
        voice_cl = voice_cl2
    elif tmp_avg >19 and tmp_avg <=  22:
        voice_cl3 = f'기온별 옷차림 추천, {tmp_avg}도에는 긴팔티, 가디건, 후드티, 면바지 ,슬랙스, 스키니을 추천드릴게요!'
        voice_cl = voice_cl3
    elif tmp_avg >22 and tmp_avg <= 26:
        voice_cl4 = f'기온별 옷차림 추천, {tmp_avg}도에는 반팔, 얇은 셔츠, 얇은 긴팔, 반바지, 면바지을 추천드릴게요!'
        voice_cl = voice_cl4
    elif tmp_avg > 26:
        voice_cl5 = f'기온별 옷차림 추천, {tmp_avg}도에는 나시티, 반바지, 민소매, 원피스을 추천드릴게요!'
        voice_cl = voice_cl5
    elif tmp_avg < 10:
        voice_cl6 = f'기온별 옷차림 추천, {tmp_avg}도에는 패딩점퍼, 코트, 야상, 목도리, 장갑, 히트텍을 추천드릴게요!'
        voice_cl = voice_cl6

    weather_message = voice_tmp + v_w_info + voice_tmp_gap + voice_cl
    tts = gTTS(weather_message, lang='ko')
    tts.save("weather_message.ogg")
    audio = open("weather_message.ogg",'rb')
    bot.send_message(chat_id,weather_message)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)


def morning_news_corona():
    bot.send_message(chat_id, "코로나 현황에 대해 알려드릴게요.")
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
    route = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/table/tbody').text
    time.sleep(1)
    driver.get('https://m.news.naver.com/covid19/index.nhn')
    add1 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[1]').text
    add2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[2]').text
    add3 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[6]/div[3]/div/ul/li[3]').text
    stt= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[3]/div[2]/div[1]/dl').text
    covd = f'코로나 환자 신규 합계 {stt} \n 확진자 이동경로 \n{route}, \n실시간 추가 확진 현황{add1}+{add2}+{add3}'
    tts = gTTS(covd, lang='ko')
    tts.save("covd.ogg")
    audio = open("covd.ogg",'rb')
    bot.send_message(chat_id, covd)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click) 

def breakfast_time():
    bot.send_message(chat_id, "아침 메뉴 한식 추천드릴게용")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    bot.send_message(chat_id, "메뉴 선택 중입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    korean_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[2]')
    korean_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    bot.send_message(chat_id, text="오늘은 " + result + " 을(를) 추천드릴게요.")
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    kor_info = voice1 + voice3 + voice4
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    tts = gTTS(kor_info, lang='ko')
    tts.save("kor_info.ogg")
    audio = open("kor_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, kor_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)

def morning_headline():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com') 
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    head = f'네이버 헤드라인 뉴스 탑 5 소개해드릴게요.\n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(head, lang='ko')
    tts.save("head.ogg")
    audio = open("head.ogg",'rb')
    bot.send_message(chat_id, head)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click) 

def Break_time():
    if hour >= 9 and hour < 13:
        bot.send_message(chat_id, f"주인님 현재 {now.tm_hour}시{now.tm_min}분 입니다."
                +"\n쉬는시간입니다. 다음 시간을 위해 충분히 쉬어주세요.")
    elif hour >= 14 and hour < 18:
        bot.send_message(chat_id, f"주인님 현재 {now.tm_hour}시{now.tm_min}분 입니다."
                +"\n쉬는시간입니다. 다음 시간을 위해 충분히 쉬어주세요.")
    else:
        return  
    
def launch_time():
    bot.send_message(chat_id, "점심 메뉴 중식 추천드릴게요")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    bot.send_message(chat_id, "메뉴 고민 중 입니다 . . . ")
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    china_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[3]')
    china_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    bot.send_message(chat_id,text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 탐색하겠습니다.'
    bot.send_message(chat_id, voice1)
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    chi_info = voice3 + voice4
    tts = gTTS(chi_info, lang='ko')
    tts.save("chi_info.ogg")
    audio = open("chi_info.ogg", 'rb')
    time.sleep(0.5)
    driver.quit()
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, chi_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)

def gym_time():
    bot.send_message(chat_id, "오늘 운동 헬스운동 추천 드릴게요!")
    driver = webdriver.Chrome('chromedriver.exe')
    weight = ['팔굽혀펴기','윗몸일으키기','턱걸이','플랭크','벤치프레스','데드리프트','스쿼트','밀리터리프레스'] 
    
    health_result = random.choice(weight)
    if health_result == weight[0]:
        driver.get(f'https://www.google.com/search?q={anaerobic[0]} 효과')
        pus = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div[2]/ul').text
        pu_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 팔굽혀펴기 운동 효과, {pus}' 
        tts = gTTS(pu_info, lang='ko')
        tts.save("pu_info.ogg")
        audio = open("pu_info.ogg", 'rb')
        bot.send_message(chat_id, pu_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[1]:
        driver.get(f'https://www.google.com/search?q={weight[1]} 효과')
        stup = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        st_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 윗몸일으키기 운동 효과, {stup}'
        tts = gTTS(st_info, lang='ko')
        tts.save("st_info.ogg")
        audio = open("st_info.ogg", 'rb')
        bot.send_message(chat_id, st_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[2]:
        driver.get(f'https://www.google.com/search?q={weight[2]} 효과')
        pul = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        pl_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 턱걸이 운동 효과, {pul}'
        tts = gTTS(pl_info, lang='ko')
        tts.save("[pl_info.ogg")
        audio = open("pl_info.ogg", 'rb')
        bot.send_message(chat_id, pl_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[3]:
        driver.get(f'https://www.google.com/search?q={weight[3]} 효과')
        plk = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        plk_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다. 플랭크 운동 효과, {plk}'
        tts = gTTS(plk_info, lang='ko')
        tts.save("plk_info.ogg")
        audio = open("plk_info.ogg", 'rb')
        bot.send_message(chat_id, plk_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[4]:
        driver.get(f'https://www.google.com/search?q={weight[4]} 효과')
        bnp = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        bp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 벤치 프레스 운동 효과, {bnp}'
        tts = gTTS(bp_info, lang='ko')
        tts.save("bp_info.ogg")
        audio = open("bp_info.ogg", 'rb')
        bot.send_message(chat_id, bp_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[5]:
        driver.get(f'https://www.google.com/search?q={weight[5]} 효과')
        dlft = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        dl_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 데드리프트 운동 효과, {dlft}'
        tts = gTTS(dl_info, lang='ko')
        tts.save("dl_info.ogg")
        audio = open("dl_info.ogg", 'rb')
        bot.send_message(chat_id, dl_info)
        bot.send_audio(chat_id, audio=audio)

    elif health_result == weight[6]:
        driver.get(f'https://www.google.com/search?q={weight[6]} 효과')
        squ =driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        sq_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 스쿼트 운동 효과, {squ}'
        tts = gTTS(sq_info, lang='ko')
        tts.save("sq_info.ogg")
        audio = open("sq_info.ogg", 'rb')
        bot.send_message(chat_id, sq_info)
        bot.send_audio(chat_id, audio=audio)

    else:
        driver.get(f'https://www.google.com/search?q={weight[7]} 효과')
        mlp = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
        mp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 밀리터리 프레스 운동 효과, {mlp}'
        tts = gTTS(mp_info, lang='ko')
        tts.save("mp_info.ogg")
        audio = open("mp_info.ogg", 'rb')
        bot.send_message(chat_id, mp_info)
        bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)

def dinner_news():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    eco = f'네이버 경제 뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(eco, lang='ko')
    tts.save("eco.ogg")
    audio = open("eco.ogg",'rb')
    bot.send_message(chat_id, eco)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)
    
def dinner_time():
    bot.send_message(chat_id, "저녁 양식메뉴 추천드릴게요~")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.implicitly_wait(10)
    driver.get('http://dogumaster.com/select/menu')
    meal = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[1]/label[2]')
    usa_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[2]/label[5]')
    usa_food.click()
    Alone_food = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[3]/label[2]')
    Alone_food.click()
    randomMenu_click = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[5]')
    randomMenu_click.click()
    time.sleep(1.5)
    result = driver.find_element(By.XPATH, '//*[@id="section_search"]/form/div[4]/p').text
    bot.send_message(chat_id, text="오늘은 " + result + " 을(를) 추천드립니다.")
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    driver.get('https://www.google.com/')
    input_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    input_search.clear()
    input_search.send_keys(result, Keys.ENTER)
    food_image_search = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div//*[text()="이미지"]')
    food_image_search.click()
    food_image_choice = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    food_image = food_image_choice.get_attribute('src')
    img_folder = 'C:/Users/ds_a/Desktop/python/조별과제/foodPhoto'
    if not os.path.isdir(img_folder):
        os.mkdir(img_folder)
    urllib.request.urlretrieve(food_image, img_folder+'test.jpg')
    food_Photo = Image.open(img_folder+'test.jpg')
    bot.send_photo(chat_id, food_Photo.resize((120,120)))
    driver.quit()
    keyword = result
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f'https://www.diningcode.com/isearch.php?query={keyword}')
    location = driver.find_element(By.XPATH,'//*[@id="contents"]/div[1]/div/img')
    action_loc = webdriver.ActionChains(driver)
    action_loc.move_to_element(location)
    action_loc.click() # 내 위치 업데이트
    action_loc.perform() #action함수 실행
    time.sleep(0.3)
    shop = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[1]').text.split('.')
    score = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/p[3]')
    voice1 = f'내 주변 {keyword} 맛집검색결과:\n맛집 점수 {score.text}, 상위{shop[0]}순위 {shop[1]}입니다.\n이동경로를 안내해드릴게요.\n'
    destination = driver.find_element(By.XPATH,'//*[@id="div_normal_nearby"]/ul/li[1]/a/span[3]')
    dt = destination.text # 목적지, 맛집주소
    driver.get('https://map.kakao.com/') # 맛집 길찾기 시작
    time.sleep(1)
    direction = driver.find_element(By.XPATH,'//*[@id="search.tab2"]/a')
    box = driver.find_element(By.XPATH,'/html/body/div[10]/div/div/img')
    action_box = webdriver.ActionChains(driver)
    action_box.move_to_element(box)
    action_box.click()
    action_box.perform()
    direction.click()
    startpoint = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input0"]')
    ds = '서울특별시 강동구 천호동 432-11' # 대신it학원 주소
    action_start = webdriver.ActionChains(driver)
    action_start.move_to_element(startpoint)
    action_start.click()
    action_start.perform()
    startpoint.send_keys(ds, Keys.ENTER) # 출발지입력
    time.sleep(1.5)
    des = driver.find_element(By.XPATH,'//*[@id="info.route.waypointSuggest.input1"]')
    des.send_keys(dt, Keys.ENTER) # 목적지입력
    time.sleep(1.5)
    public_tr = driver.find_element(By.XPATH, '//*[@id="transittab"]')
    public_tr.click()
    time.sleep(1)
    no_pass = driver.find_elements(By.XPATH, '//*[@id="info.flagsearch"]/div[7]/div/div[1]/h3')
    if len(no_pass) == 0:
        pub_time = driver.find_element(By.XPATH, '//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[1]')
        pub_info = driver.find_element(By.XPATH,'//*[@id="info.flagsearch"]/div[5]/ul/li[1]/div[1]/span[2]')
        voice3 = f'대중교통 이용시 예상소요시간 {pub_time.text}, {pub_info.text}. 교통카드를 챙겨주세요.\n'
    else:
        voice3 = "대중교통 경로가 없습니다."
        pass
    work = driver.find_element(By.XPATH, '//*[@id="walktab"]')
    work.click()
    time.sleep(1)
    work_fast_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_fast_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    work_slow_time = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[1]')
    work_slow_dis = driver.find_element(By.XPATH,'//*[@id="info.walkRoute"]/div[1]/ul/li[2]/div[1]/div/p/span[2]')
    voice4 = f'도보 이용시 최단거리는 {work_fast_time.text}, {work_fast_dis.text}, 편안한 길은 {work_slow_time.text}, {work_slow_dis.text}\n'
    screen = driver.find_element_by_class_name("cont_map")
    element_png = screen.screenshot_as_png
    with open('test.png', 'wb') as file:
        file.write(element_png)
    usa_info = voice1 +voice3 + voice4
    tts = gTTS(usa_info, lang='ko')
    tts.save("usa_info.ogg")
    audio = open("usa_info.ogg", 'rb')
    bot.send_photo(chat_id, element_png)
    bot.send_message(chat_id, usa_info)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)

def night_news():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get('https://news.naver.com')
    tit = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[1]/div[1]/a').text
    tit2 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[2]/div[1]/a').text
    tit3 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[3]/div[1]/a').text
    tit4 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[4]/div[1]/a').text
    tit5 = driver.find_element_by_xpath('//*[@id="today_main_news"]/div[2]/ul/li[5]/div[1]/a').text
    soci = f'네이버 사회뉴스 탑 5 소개해드릴게요. \n 1.{tit},\n 2.{tit2},\n 3.{tit3}, \n 4.{tit4},\n 5.{tit5}'
    tts = gTTS(soci, lang='ko')
    tts.save("soci.ogg")
    audio = open("soci.ogg",'rb')
    bot.send_message(chat_id, soci)
    bot.send_audio(chat_id, audio=audio)
    driver.quit()
    time.sleep(0.5)
    Click = pyautogui.locateCenterOnScreen('playbutton125.PNG')
    pyautogui.click(Click)

def sleep_time():
    bot.send_message(chat_id, "주무실 시간입니다. 좋은 밤되세요!")


schedule.every().day.at("14:29").do(wakeup_time)
schedule.every().day.at("14:31").do(morning_news_corona)
schedule.every().day.at("14:33").do(breakfast_time)
schedule.every().day.at("14:35").do(morning_headline)
#schedule.every(10).minutes.do(Break_time)
schedule.every().day.at("14:37").do(launch_time)
schedule.every().day.at("14:39").do(gym_time)
schedule.every().day.at("14:41").do(dinner_news)
schedule.every().day.at("14:43").do(dinner_time)
schedule.every().day.at("14:45").do(night_news)
schedule.every().day.at("14:47").do(sleep_time)

def AutoThread1(name):
    while 1:
        schedule.run_pending()
        time.sleep(1)
        


t1 = threading.Thread(target=AutoThread1, args=('1'))
t1.start()


if __name__ == '__main__':
    main()