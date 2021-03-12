from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise



User = secrets["User"]
Pass = secrets["Pass"]

web = Browser(showWindow=False)
web.go_to(secrets["Router_IP"])
# web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
if(web.exists(id="form-login")):
	print("ta no login")
	user = web.type(User, id='login-username')
	web.press(web.Key.TAB)
	time.sleep(0.2)
	passw = web.type(Pass)
	time.sleep(0.3)
	web.click(id="login-btn")
time.sleep(0.3)
web.click(id='menu-top-management-li')
time.sleep(0.3)
web.click(classname="ledctl")

time.sleep(0.3)
web.click(text="Enable")
if(web.exists(classname="checked")):
	print("HABILITANDO LED")
else:
	print("DESABILITANDO LED")
time.sleep(0.3)
web.click(text="Save")
# web.press(web.Key.ENTER)
