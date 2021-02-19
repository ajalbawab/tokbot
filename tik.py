import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import threading
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

username = 'prince_alibabua'
locationofwebdriver = '//dellserver/BOND-GROUP/B - Michael/SQL/005 - Support Files/chromedriver.exe'
videoid = 6926249803596762374
videolistid = []
threads = []
def initializeproxy():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(chrome_options=options, executable_path=locationofwebdriver)
    driver.get("http://www.freeproxylists.net/?u=80&s=rs")
    driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='DataGrid']//td[contains(., 'IP Address')]"))))
    ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='DataGrid']//tbody//tr/td[1]/a")))][1:]
    ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='DataGrid']//tbody//tr/td[2]")))][1:]
    driver.quit()
    proxies = []
    for i in range(0, len(ips)):
        proxies.append(ips[i]+':'+ports[i])
    return proxies



def randomtime(start, end):
    return random.random() * (end - start) + start



def looper():
    print('starting looper')

    t = threading.Thread(target=runbot)
    threads.append(t)
    t.start()
    time.sleep(120)
    # print('starting new thread')
    # looper()


def runbot():
    randproxy = random.choice(proxylist)
    proxylist.remove(randproxy)
    condition2 = 0
    while True:
        condition2 +=1
        print("""
        
        
        SHOULD BE {} /3""".format(condition2))
        chrome_options = webdriver.ChromeOptions() 
        
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument('--proxy-server={}'.format(randproxy))
        
        driver = webdriver.Chrome(executable_path=locationofwebdriver,options=chrome_options)
        driver.set_page_load_timeout(45)
        try:
            driver.get('https://www.tiktok.com/@' + str(username) + '?lang=en')
            print("URL successfully Accessed")
            try:
                
                time.sleep(randomtime(1,3))

                condition = 1
                while True:
                    
                    try:
                        randvideoidstring = 'a[href="https://www.tiktok.com/@{}/video/{}"]'.format(str(username), str(videoid))

                        element = driver.find_element_by_css_selector(randvideoidstring)
                        hover = ActionChains(driver).move_to_element(element)
                        hover.perform()

                        try:

                            heheh = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[2]/div[1]/div[1]/div/div/div/a/span/div/div/div')
                            heheh.click()
                        except:
                            try:
                                heheh1 = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/main/div[2]/div[1]/span[1]/div/div/div[5]/div[1]/a/div/div/span[2]')
                                heheh1.click()
                            except:
                                pass
                            
                        more_buttons3 = driver.find_element_by_css_selector("p[class$='word-link']")

                        c=0
                        while c < 3:
                            time.sleep(randomtime(2,4))
                            more_buttons3.click()
                            c+=1
                            
                        time.sleep(randomtime(30,60))
                        # more_buttons3.click()
                        driver.close()
                        condition = 30
                        # condition2 += 1
                    except Exception as e: 
                        print(e)
                        condition += 1
                        pass
                    if condition == 30:
                        break
                driver.close()
            except Exception as e: 
                print('error 1')
                print(e)
                try:
                    driver.close()
                except:
                    pass
                pass
        except Exception as e: 
            print('error 2')
            print(e)
            condition2 = 3
        if condition2 == 3:
            break
    try:
        driver.close()
    except:
        pass    
    runbot()

    

if __name__ == "__main__":
    global proxylist
    proxylist = initializeproxy()
    looper()