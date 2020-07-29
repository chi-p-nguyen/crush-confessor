import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

opennings = ['Tu lau roi', 'May nam roi', 'Bao lau nay']
love_words = ['yeu', 'thich', 'crush', 'co cam giac manh liet hon tinh ban']
love_sentences = ['Lam nguoi yeu t nhe', 'Lam vo t nhe', 'Chut chut']

def confession():
    open = random.randint(0, len(opennings) - 1)
    word = random.randint(0, len(love_words) - 1)
    sentence = random.randint(0, len(love_sentences) - 1)
    confess = opennings[open] + ', to ' + love_words[word] + ' cau. ' +  love_sentences[sentence] + '. From Bot ver 01.'
    return confess

username = input("Enter you username: ")
password = input("Enter your password: ")
crusher = input("Enter your crush Facebook: ")

driver = webdriver.Chrome()
driver.get("https://www.messenger.com/")
time.sleep(2)
email_place = driver.find_element_by_css_selector("#email")
email_place.send_keys(username)
pass_place = driver.find_element_by_css_selector("#pass")
pass_place.send_keys(password)
log_button = driver.find_element_by_css_selector('#loginbutton')
log_button.click()


search = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input')

search.send_keys(crusher)
time.sleep(2)

try:
    person = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li[1]/a/div/div[2]/div/div')
except:
    person = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div')

person.click()

mess = driver.find_element_by_class_name('notranslate')
mess.send_keys(confession())
mess.send_keys(Keys.ENTER)

#driver.close()





