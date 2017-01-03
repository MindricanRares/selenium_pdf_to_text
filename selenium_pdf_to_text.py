

import win32com.client
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import subprocess
import shutil
import ctypes
import win32api
import win32con

temp_path='D:\\download_test'
if not os.path.isdir(temp_path):
    os.mkdir(temp_path)

# ctypes.windll.kernel32.SetFileAttributesW(temp_path, 2)
win32api.SetFileAttributes(temp_path,win32con.FILE_ATTRIBUTE_HIDDEN)
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", temp_path)

firefox_driver = webdriver.Firefox(firefox_profile=profile)


firefox_driver.get('http://www.pratocatering.ro/img/meniu/meniu.pdf')
time.sleep(0.5)
firefox_driver.find_element_by_id('download').click()
time.sleep(0.5)
shell=win32com.client.Dispatch("WScript.Shell")

time.sleep(1.5)
shell.Sendkeys("~")
# firefox_driver.close()
time.sleep(0.5)
# chrome_driver = webdriver.Chrome('chromedriver.exe')
# chrome_driver = webdriver.Firefox()
firefox_driver.get("http://pdftotext.com/")
time.sleep(0.5)
upload_files_buttons_button = firefox_driver.find_element_by_id('pick-files')
time.sleep(0.5)
upload_files_buttons_button.click()

time.sleep(0.5)
pdf_path=temp_path+"\\meniu.pdf"
print pdf_path
time.sleep(0.5)
shell.Sendkeys(pdf_path)
time.sleep(0.5)
shell.Sendkeys("~")
time.sleep(5)
download_all_button= firefox_driver.find_element_by_id('download-all')
time.sleep(0.5)
download_all_button.click()


time.sleep(1.5)
shell.Sendkeys("{DOWN}")
time.sleep(0.5)
shell.Sendkeys("~")

time.sleep(2)
firefox_driver.close()

zip_path=temp_path+'\\pdftotext.zip'
command_string = '7z x -y  {0} -{1}'.format(zip_path,'o'+temp_path)
subprocess.call(command_string)
time.sleep(5)

text_path=temp_path+'\\meniu.txt'
with open (text_path,'r') as file_reader:
    for line in file_reader.readlines():
        print line


shutil.rmtree(temp_path)


