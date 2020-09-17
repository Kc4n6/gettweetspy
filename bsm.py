from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
opt = Options()
opt.headless = True
driver = webdriver.Firefox(options=opt,executable_path="/home/key/Desktop/geckodriver")
driver.get("https://www.twitter.com/huseyinbayram__")
time.sleep(10)

tweets = []


while True:
    
    for i in range(1,20):
        text = "/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div["+str(i)+"]/div/div/article/div/div/div/div[2]/div[2]"
                
        try:
            string = ""
            for j in driver.find_element_by_xpath(text+"/div[2]/div[1]").find_elements_by_tag_name("span"):
                string = string+str(j.text)
                
            timee = driver.find_element_by_xpath(text+"/div[1]/div/div/div[1]/a").find_element_by_tag_name("time").get_attribute("datetime")
            elem = timee.split("T")
            time1 = elem[1].split(".")
            datetimee = "\ndate="+elem[0]+"\ntime="+time1[0]
            
            
            string= string+datetimee
            tweets.append(str(string))
                
        except Exception as ex:
            
            continue
    
    try:
        lenofpage = driver.execute_script("var lenOfPage= window.scrollY;return lenOfPage")
       
        bitti = False
        if(bitti== False):
            last = lenofpage
            time.sleep(0.5)
            lenofpage = driver.execute_script("window.scrollTo(window.scrollY,window.scrollY+1000);var lenOfPage=window.scrollY;return lenOfPage;")
            
            if(last == lenofpage):
                break
            else:
                pass
               # driver.execute_script("window.scrollTO(window.scrollY,window.scrollY-1000")
    except Exception as exe:
        
        pass        
driver.quit()
tweets = list(dict.fromkeys(tweets))


for i in tweets:
    print(i)



"""
/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[4]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time
/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[5]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time
/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[7]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time
/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[7]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span
"""
