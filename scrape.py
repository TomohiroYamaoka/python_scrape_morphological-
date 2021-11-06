from time import sleep
from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup
import textwrap
import csv


def get_amazon_page_info(url):
    text = ""
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    text = driver.page_source
    driver.quit()

    return text


def get_all_reviews(url):
    review_list = []
    i = 1
    while True:
        print(i, 'page_search')
        i += 1
        text = get_amazon_page_info(url)
        amazon_bs = BeautifulSoup(text, features='lxml')
        reviews = amazon_bs.select('.review-text')

        for review in reviews:
            review_list.append(review)

        next_page = amazon_bs.select('li.a-last a')

        if next_page != []:
            next_url = 'https://www.amazon.co.jp/' + next_page[0].attrs['href']
            url = next_url

            sleep(1)
        else:
            break

    return review_list


if __name__ == '__main__':

    #　Amzon商品ページ
    url = 'https://www.amazon.co.jp/%E3%80%90%E5%8C%BB%E8%96%AC%E9%83%A8%E5%A4%96%E5%93%81%E3%80%91%E3%83%A1%E3%83%87%E3%82%A3%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AFH-%E3%81%B5%E3%81%91%E3%83%BB%E3%81%8B%E3%82%86%E3%81%BF%E3%82%92%E9%98%B2%E3%81%90-%E9%A0%AD%E7%9A%AE%E3%81%AE%E7%92%B0%E5%A2%83%E6%94%B9%E5%96%84-%E3%83%A1%E3%83%87%E3%82%A3%E3%82%AB%E3%83%AB%E3%82%B7%E3%83%A3%E3%83%B3%E3%83%97%E3%83%BC-200ml/dp/B00NPQIAOO/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%80%90%E5%8C%BB%E8%96%AC%E9%83%A8%E5%A4%96%E5%93%81%E3%80%91%E3%83%A1%E3%83%87%E3%82%A3%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AFH+%E3%81%B5%E3%81%91%E3%83%BB%E3%81%8B%E3%82%86%E3%81%BF%E3%82%92%E9%98%B2%E3%81%90+%E9%A0%AD%E7%9A%AE%E3%81%AE%E7%92%B0%E5%A2%83%E6%94%B9%E5%96%84+%E3%83%A1%E3%83%87%E3%82%A3%E3%82%AB%E3%83%AB%E3%82%B7%E3%83%A3%E3%83%B3%E3%83%97%E3%83%BC+200ml&qid=1635211123&s=beauty&sr=1-1'

    review_url = url.replace('dp', 'product-reviews')
    review_list = get_all_reviews(review_url)

    # CSVにレビュー情報の書き出し
    with open('result/4.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')

        # 全データを表示
        for i in range(len(review_list)):
            csvlist = []
            review_text = textwrap.fill(review_list[i].text)
            # データ作成
            csvlist.append('No.{} : '.format(i+1))
            csvlist.append(review_text.strip())
            # 出力
            writer.writerow(csvlist)
        # ファイルクローズ
        f.close()
