from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep,time

# Wait for an element
# Set up the driver
options = Options()
options.add_argument("--disable-notifications")

driver_path = "C:/Users/hp/Downloads/chromedriver_win32.zip/chromedriver" # replace with the path to your driver executable
driver = webdriver.Chrome(options= options)

# Open the website
url = "https://www.registrarofcompanies.gov.bm/bmroccapr/viewInstance/view.html?id=17ebe370d468cb92f798d1454402234bd328197b9e23412f&_timestamp=5403374449792320" # replace with the URL of the website you want to scrape
driver.get(url)

# Find all the article titles on the homepage
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button")))
driver.find_element(By.CSS_SELECTOR,"button").click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input#Name")))
search_bar = driver.find_element(By.CSS_SELECTOR,"input#Name")
search_bar.send_keys("force")
search_button = driver.find_element(By.CSS_SELECTOR,"button.appSubmitButton")
search_button.click()
sleep(5)
final_data = []
try:

    while True:
        table = driver.find_element(By.CLASS_NAME,"appRepeaterContent")
        all_rows = driver.find_elements(By.CSS_SELECTOR,".appRepeaterContent a")
        for index,row in enumerate(all_rows):
            if index != 0:
                table = driver.find_element(By.CLASS_NAME,"appRepeaterContent")
                all_rows = driver.find_elements(By.CSS_SELECTOR,".appRepeaterContent a")
                row = all_rows[index]
 
            row.click()
            company = {}
            sleep(5)
            displayed_data = driver.find_element(By.CSS_SELECTOR,".appBoxChildren").find_elements(By.CSS_SELECTOR,".appBoxChildren .appAttrValue")
            company['type'] = displayed_data[0].text
            company['name'] = displayed_data[1].text
            company['registration_date'] = displayed_data[2].text.split("\n")[0]
            final_data.append(company)
            driver.back()
            sleep(5)
            
        break
except Exception as e:
    print(e)
    
print(final_data)
sleep(5)
# Close the driver
driver.quit()
