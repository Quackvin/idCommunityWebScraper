from selenium import webdriver

url = 'https://atlas.id.com.au/wanneroo#'

options = webdriver.ChromeOptions() 

prefs = {"download.default_directory" : "/Users/KeviN/Documents/Uni/2018/CEED/data/scraper/files",
"profile.content_settings.exceptions.automatic_downloads.*.setting":1}
options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get(url)

raw_input()

driver.execute_script('document.getElementById(\'tblAgregate\').children[0].children[2].children[0].children[1].children[0].click()')

driver.quit()