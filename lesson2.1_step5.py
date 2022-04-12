from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x) 

try: 
   
    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))
    
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()

    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()