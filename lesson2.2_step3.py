from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)


a = browser.find_element_by_css_selector("#num1").text
b = browser.find_element_by_css_selector("#num2").text


c = str(int(a)+int(b))




try: 
   
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(value=str(c)) # ищем элемент с текстом "Python"

    # Ваш код, который заполняет обязательные поля
   
    
    
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
   