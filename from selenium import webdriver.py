import os
from selenium import webdriver
from time import sleep
tumKullaniciler = ["ayserogglu","irmakinizkahraman"]
for kullanici in tumKullaniciler:
    driver = webdriver.Chrome(executable_path=r'C:\Users\Egemen\Downloads\chromedriver.exe')
    driver.get('https://www.instagram.com') #Go to instagram login page.
    sleep(2) #Wait for loading page.

    username = driver.find_element_by_name('username').send_keys(kullanici) 
    password = driver.find_element_by_name('password').send_keys('egemen13.')
    girisbutton = driver.find_element_by_xpath('//button[@type="submit"]').click() #Log-in button
    sleep(3) 

    simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]').click() #Answer to 'save your password?'
    sleep(1.5)
    simdidegil = driver.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]').click() #Answer to 'open notification?'
    sleep(0.5)

    aramakutusu = driver.find_element_by_xpath('//input[@type="text"]').send_keys('egemensenerr') #The search bar that we type target username
    sleep(3) #Wait for loading suggestions
    profile = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click() #Click on the first suggestion
    sleep(3) #Wait for loading target profile
    
    def scrollAllWayDown():
        #This function scroll down to see the footer element and wait for a couple second. If page scroll length has changed then scroll again because that mean there is other pictures.
        global driver
        footer = driver.find_element_by_tag_name('footer') #The footer element
        last_height = driver.execute_script('return document.body.scrollHeight') #Before scroll down note scroll length
        while True:
            footer.location_once_scrolled_into_view #Scroll down to see footer
            sleep(2) #Wait for internet
            new_height = driver.execute_script('return document.body.scrollHeight') #Run javascript code again to check scroll length.
            if new_height == last_height: #If scroll height hasnt changed then there is no more pictures.
                print('sayfa bitti!!!')
                break
            else: #If it changed set the last height equal new height and repeat function.
                last_height = new_height

    scrollAllWayDown()

    tumKutular = driver.find_elements_by_class_name('v1Nh3') #Every photo attribute has a parent div so first find divs
    tumLinkler = []
    for i in tumKutular:
        tumLinkler.append(i.find_element_by_tag_name('a')) #And find attribute in divs

    for i in tumLinkler:
        i.click() #Click link and open photo
        sleep(2)
        begenbuton = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button') 
        begenbuton.click() #Click heart button
        sleep(1)
        break
        #cikis = driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click() #Click exit button
    os.system("taskkill /im chrome.exe /f")     
