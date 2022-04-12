from selenium import webdriver
import math

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)


try: 
   
    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(calc(x))
    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
