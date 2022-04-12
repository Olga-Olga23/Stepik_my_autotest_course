from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector('#treasure')
x_element_attribute = x_element.get_attribute("valuex")
x = x_element_attribute
y = calc(x) 
print(x)

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