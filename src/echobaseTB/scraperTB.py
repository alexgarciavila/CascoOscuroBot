from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
allycode = "336544232"
tipobt = "SeparatistMight"
fasebt = "3"

condsadriver = webdriver.Chrome("..\webdriver\chromedriver.exe")
driver.get("https://echobase.app/login")

time.sleep(1)

# Entramos con nuestro código de aliado
eballycode = driver.find_element_by_id("allyCode")
eballycode.send_keys(allycode)
eballycode.send_keys(Keys.ENTER)
time.sleep(1)

# Navegamos hasta las asignaciones de pelotones
#driver.get("https://echobase.app/platoonAssigner")
driver.get("https://echobase.app/platoonAssigner?battle=" + tipobt + "&phase=" + fasebt)
time.sleep(2)
presubmit = driver.find_element_by_id("platoonSubmitButton")
presubmit.click()
time.sleep(1)
preview = driver.find_element_by_id("previewButton")
preview.click()
time.sleep(2)

total_platoons = 6
total_zones = 3
total_units = 15
countz = 1

while countz <= total_zones:
    if countz == 1:
        print("\n##########")
        print("Zona Naves")
        print("##########")
    elif countz == 2:
        print("\n##########")
        print("Zona medio")
        print("##########")
    else:
        print("\n##########")
        print("Zona inferior")
        print("##########")
    countpt = 1
    while countpt <= total_platoons:
        countztxt = str(countz)
        countpttxt = str(countpt)
        platoon = driver.find_element_by_xpath("//*[@id='platoonAssignerForm']/div/div/div/div[" + countztxt + "]/div/table/tbody/tr/td/div/div[" + countpttxt + "]/div/div[1]/div/button/small").text
        print("\n#########")
        print(platoon)
        print("#########\n")
        countunits = 1
        while countunits <= total_units:
            countpttxt = str(countpt - 1)
            countztxt = str(countz - 1)
            countunitstxt = str(countunits - 1)
            units = driver.find_element_by_xpath("//*[@id='requirementImage-" + countztxt + "-" + countpttxt + "-" + countunitstxt + "']").get_attribute('title')
            members = driver.find_element_by_xpath("//*[@id='requirementDonorDisplay-" + countztxt + "-" + countpttxt + "-" + countunitstxt + "']").get_attribute('title')
            print(units + " - " + members)
            countunits += 1
        countpt += 1
    countz += 1