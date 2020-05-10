import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import chromedriver_binary


def scrapingLogin():
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
    username = '16B11094'
    # あなたのパスワード
    password = 'Kamihate3510'

    # ユーザー名の入力ボックスを探す F12を押してhtmlを出力し、xpathをここに入力する
    username_box = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/input")
    # パスワードの入力ボックスを探す
    password_box = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[3]/td/div/div/input")

    # ユーザ名とパスワードをインプットする
    username_box.send_keys(username)
    password_box.send_keys(password)

    # ログインボタンを探す
    login_button = driver.find_element_by_xpath(
        "/html/body/center[3]/form/table/tbody/tr/td/table/tbody/tr[5]/td/input[1]")
    # ログインボタンをクリック
    login_button.click()

    # time.sleep(1)

    Dictionary = {
        "[A,1]": 'H', "[A,2]": 'H', "[A,3]": 'I', "[A,4]": 'K', "[A,5]": 'E', "[A,6]": 'M', "[A,7]": 'B',
        "[B,1]": 'I', "[B,2]": 'T', "[B,3]": 'Q', "[B,4]": 'O', "[B,5]": 'E', "[B,6]": 'E', "[B,7]": 'E',
        "[C,1]": 'A', "[C,2]": 'A', "[C,3]": 'Q', "[C,4]": 'D', "[C,5]": 'K', "[C,6]": 'J', "[C,7]": 'E',
        "[D,1]": 'X', "[D,2]": 'H', "[D,3]": 'S', "[D,4]": 'V', "[D,5]": 'A', "[D,6]": 'V', "[D,7]": 'F',
        "[E,1]": 'P', "[E,2]": 'R', "[E,3]": 'D', "[E,4]": 'U', "[E,5]": 'S', "[E,6]": 'T', "[E,7]": 'Q',
        "[F,1]": 'R', "[F,2]": 'P', "[F,3]": 'H', "[F,4]": 'G', "[F,5]": 'Y', "[F,6]": 'T', "[F,7]": 'U',
        "[G,1]": 'B', "[G,2]": 'K', "[G,3]": 'M', "[G,4]": 'D', "[G,5]": 'M', "[G,6]": 'Y', "[G,7]": 'W',
        "[H,1]": 'E', "[H,2]": 'K', "[H,3]": 'E', "[H,4]": 'X', "[H,5]": 'S', "[H,6]": 'K', "[H,7]": 'T',
        "[I,1]": 'L', "[I,2]": 'I', "[I,3]": 'J', "[I,4]": 'L', "[I,5]": 'C', "[I,6]": 'Z', "[I,7]": 'N',
        "[J,1]": 'K', "[J,2]": 'C', "[J,3]": 'W', "[J,4]": 'V', "[J,5]": 'R', "[J,6]": 'C', "[J,7]": 'M',
    }

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


def main():
    # scrapingLogin関数を実行
    output = scrapingLogin()
    print(output)


# プログラム実行のおまじない
if __name__ == '__main__':
    main()
