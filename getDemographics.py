from selenium import webdriver

savePath = raw_input('Please enter download location\n')

options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : savePath,
"profile.content_settings.exceptions.automatic_downloads.*.setting":1}
options.add_experimental_option("prefs",prefs)

url = raw_input('Please enter url of webpage to get data from\n')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.get(url)

def downloadOne(i,j,k,l):
	driver.execute_script(' \
			let selectorMenu = document.getElementById(\'idc-nav-page-list\'); \
    		let selector = selectorMenu.children[arguments[0]]; \
		    let innerDiv = selector.getElementsByTagName(\'div\')[0]; \
		    let innerList = innerDiv.getElementsByTagName(\'ul\')[0]; \
	        let inner = innerList.children[arguments[1]]; \
	        inner.click(); \
	        \
	        let dataTypeSelector = document.getElementById(\'idc-controlpanel-buttongroup-datatype-dropdown-menu\'); \
			dataTypeSelector.children[arguments[2]].click(); \
			\
    		let genderSelector = document.getElementById(\'idc-controlpanel-buttongroup-SexKey-dropdown-menu\'); \
			genderSelector.children[arguments[3]].click(); \
			\
			document.getElementById(\'tblAgregate\').children[0].children[2].children[0].children[1].children[0].click() \
		', i, j, k, l)

try:
	raw_input('Select all SH1 areas to get data from, then press any key to continue\n')
	
	# Need to write script to download one after the previous is done. 
	# Check when a new file has appeared. Might as well rename them when checking
	# use this -> downloadOne(0,0,0,0);
				
finally:
	raw_input('press any key when all downloads have finished\n')
	driver.quit()
