from selenium import webdriver

url = 'https://google.com'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

driver.execute_script('alert(arguments[0]); \
	alert(arguments[1]);\
	alert(arguments[2]);\
	alert(arguments[3]);'
	, 'hello world', 'foobar', 'wewr', 123)

raw_input()

driver.quit()