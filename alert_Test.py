from common import *
from selenium.webdriver.support.ui import WebDriverWait          #available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC #available since 2.26.0
import init
import time

"""Test alert box"""

##region prepare the html file
html='''
<!DOCTYPE html>
<html>
<script>
alert("Hello! I am an alert box!");
</script>
<body>
<p>An alert box must show on start-up</p>

</body>
</html>
'''

#generate temp file
import tempfile
htmlFile = tempfile.NamedTemporaryFile().name #ref. https://stackoverflow.com/a/13717435/248616

#write html to file ref. https://stackoverflow.com/a/27708256/248616
with open(htmlFile, 'w') as f:
  f.write(html)
##endregion prepare the html file

#open sample alert page
driver = init.init_chrome_driver("/home/ning/PycharmProjects/testBlueWhale/chromedriver")
driver.implicitly_wait(100)
url = 'file:///'+htmlFile
print('Testing at %s' % url)
driver.get(url)
time.sleep(2)
alertBox = driver.switch_to_alert()
alertBox.accept()

#import time ; time.sleep(10) #even wait, it's NOT working

# WebDriverWait(driver,10).until(EC.alert_is_present()) #TODO Why alert box not available? We got error here
