from selenium import webdriver

driver = webdriver.Chrome('C://Users//user//Desktop//Python Study//chromedriver.exe')
driver.implicitly_wait(3)
#login
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('hsk6540')
driver.find_element_by_name('pw').send_keys('hansk66412!')
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# Naverpay
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())