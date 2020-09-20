import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


def extractQR(obj):
    Dictionary = {
        "gakuseki": obj.gakuseki, "PW": obj.PW,
        "[A,1]": obj.A1, "[A,2]": obj.A2, "[A,3]": obj.A3, "[A,4]": obj.A4, "[A,5]": obj.A5, "[A,6]": obj.A6, "[A,7]": obj.A7,
        "[B,1]": obj.B1, "[B,2]": obj.B2, "[B,3]": obj.B3, "[B,4]": obj.B4, "[B,5]": obj.B5, "[B,6]": obj.B6, "[B,7]": obj.B7,
        "[C,1]": obj.C1, "[C,2]": obj.C2, "[C,3]": obj.C3, "[C,4]": obj.C4, "[C,5]": obj.C5, "[C,6]": obj.C6, "[C,7]": obj.C7,
        "[D,1]": obj.D1, "[D,2]": obj.D2, "[D,3]": obj.D3, "[D,4]": obj.D4, "[D,5]": obj.D5, "[D,6]": obj.D6, "[D,7]": obj.D7,
        "[E,1]": obj.E1, "[E,2]": obj.E2, "[E,3]": obj.E3, "[E,4]": obj.E4, "[E,5]": obj.E5, "[E,6]": obj.E6, "[E,7]": obj.E7,
        "[F,1]": obj.F1, "[F,2]": obj.F2, "[F,3]": obj.F3, "[F,4]": obj.F4, "[F,5]": obj.F5, "[F,6]": obj.F6, "[F,7]": obj.F7,
        "[G,1]": obj.G1, "[G,2]": obj.G2, "[G,3]": obj.G3, "[G,4]": obj.G4, "[G,5]": obj.G5, "[G,6]": obj.G6, "[G,7]": obj.G7,
        "[H,1]": obj.H1, "[H,2]": obj.H2, "[H,3]": obj.H3, "[H,4]": obj.H4, "[H,5]": obj.H5, "[H,6]": obj.H6, "[H,7]": obj.H7,
        "[I,1]": obj.I1, "[I,2]": obj.I2, "[I,3]": obj.I3, "[I,4]": obj.I4, "[I,5]": obj.I5, "[I,6]": obj.I6, "[I,7]": obj.I7,
        "[J,1]": obj.J1, "[J,2]": obj.J2, "[J,3]": obj.J3, "[J,4]": obj.J4, "[J,5]": obj.J5, "[J,6]": obj.J6, "[J,7]": obj.J7,
    }
    return(Dictionary)


def QRLogin(Dictionary):
    options = Options()

    # ヘッドレスブラウザ指定
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # ChromeDriverのパスとオプションをつけてwebdriverを作成
    # this path is for keigo's windows PC
    # driver = webdriver.Chrome(
    #    'C:\\Users\\keigo\\chromedriver', options=options)

    # this path is passed by installing selenium and chromedriver_binary
    # detail will be in this URl
    # https://qiita.com/memakura/items/20a02161fa7e18d8a693
    # take care of the version of chromedriver_binary, should be same or near to your chrome
    driver = webdriver.Chrome(options=options)

    driver.get(
        'https://portal.nap.gsic.titech.ac.jp/GetAccess/Login?Template=userpass_key&AUTHMETHOD=UserPassword')

    # time.sleep(1)

    # あなたのユーザー名/メールアドレス
    gakuseki = Dictionary['gakuseki']
    # あなたのパスワード
    password = Dictionary['PW']

    # ユーザー名の入力ボックスを探す F12を押してhtmlを出力し、xpathをここに入力する
    username_box = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/input")
    # パスワードの入力ボックスを探す
    password_box = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[3]/td/div/div/input")

    # ユーザ名とパスワードをインプットする
    username_box.send_keys(gakuseki)
    password_box.send_keys(password)

    # ログインボタンを探す
    login_button = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]")
    # ログインボタンをクリック
    login_button.click()

    # time.sleep(1)

    m1 = youso(driver, "//*[@id=\"authentication\"]/tbody/tr[4]/th[1]")
    m2 = youso(driver, "//*[@id=\"authentication\"]/tbody/tr[5]/th[1]")
    m3 = youso(driver, "//*[@id=\"authentication\"]/tbody/tr[6]/th[1]")
    matrix1_box = driver.find_element_by_xpath(
        "//*[@id=\"authentication\"]/tbody/tr[4]/td/div/div/input")
    matrix1_box.send_keys(Dictionary[m1])
    matrix2_box = driver.find_element_by_xpath(
        "//*[@id=\"authentication\"]/tbody/tr[5]/td/div/div/input")
    matrix2_box.send_keys(Dictionary[m2])
    matrix3_box = driver.find_element_by_xpath(
        "//*[@id=\"authentication\"]/tbody/tr[6]/td/div/div/input")
    matrix3_box.send_keys(Dictionary[m3])

    # ログインボタンを探す
    OK = driver.find_element_by_xpath(
        "//*[@id=\"authentication\"]/tbody/tr[8]/td/input[1]")
    # ログインボタンをクリック
    OK.click()

    time.sleep(1)

    # スクショ用
    # driver.save_screenshot('screenshot.png')

    # ブラウザを終了
    # driver.quit()

    return "Worked it"


def youso(window, xpath):
    element = window.find_element_by_xpath(xpath)
    return element.text
