""" Using Selenium, get randomly generated NPCs from
http://donjon.bin.sh/5e/random/#type=npc 

To use this you'll need selenium and its geckodriver
for firefox, found here: https://github.com/mozilla/geckodriver/releases
Place the geckodriver in the same directory as this file.

To install Selenium through Python:
pip install selenium
"""
# The below pylint comment disables notifications that the Selenium
# package is missing, even though it should be present.
# pylint: disable=E0401
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import atexit


# Start a timer to measure runtime of application.
start = time.time()

options = Options()
# We set headless for FireFox so it doesn't open a window at every run
# of this program.
options.headless = True
# Replace "webdriver.____" below with .Firefox(), or with the browser of your choice.
driver = webdriver.Firefox(options=options) 
url = "http://donjon.bin.sh/5e/random/#type=npc"
# Navigate to the page indicated by the url.
driver.get(url) 

def timeout_check():
    """Exception if program is unable to access the website's NPC summaries."""
    timeout = 30
    last_summ_xpath = "/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]/div/ol/li[10]"
    try:
        element_present = EC.presence_of_element_located((By.XPATH, last_summ_xpath))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutError:
        print("Timed out waiting for page to load")

timeout_check()

def refresh_npcs():
    """Refresh the current list of NPCS.

    ***IMCOMPLETE***
    """
    button_xpath = "//html/body/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input"
    button = driver.find_elements_by_xpath(button_xpath)[0]
    button.click()
    timeout_check()
    return "NPC list refreshed."

def list_npcs():
    """Return a list of the currently generated NPC summaries.

    -Start by using the xpath of the npc summaries
        (found by using inspect on the webpage, picking
        a summary from the page, then doing right-click>copy>XPath)
    -Create a list of npc_web_elems from the npc summary identifiers.
    -Format the web element objects into text and return
    a list of npc descriptions.
    """
    npc_summs_xpath = "/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]/div/ol/li"
    npc_web_elems = driver.find_elements_by_xpath(npc_summs_xpath)

    npc_summs = []
    for i in npc_web_elems:
        npc_summs.append(i.text)
    return npc_summs

print(list_npcs())
end = time.time()
print("Finished loading in {:.4f}s".format(end - start))

# Atexit makes sure the headless firefox sessions used for this
# program are closed when the program intentionally halts.
# Note: Won't work for unintentional program halts.
atexit.register(driver.quit)