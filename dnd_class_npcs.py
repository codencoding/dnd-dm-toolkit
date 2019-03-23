"""This is a class contained version of dnd_webscrape_npcs_selenium.py

Using Selenium, get randomly generated NPCs from
http://donjon.bin.sh/5e/random/#type=npc 

To use this you'll need selenium and its geckodriver
for firefox, found here: https://github.com/mozilla/geckodriver/releases
Place the geckodriver in the same directory as this file.

To install Selenium through Python:
pip install selenium
"""
# pylint: disable=E0401
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import atexit

class npcs():
    # We set headless for FireFox so it doesn't open a window at every run
    # of this program.
    options = Options()
    options.headless = True
    url = "http://donjon.bin.sh/5e/random/#type=npc"

    def timeout_check(self):
        """Exception if program is unable to access the website's NPC summaries."""
        timeout = 30
        last_summ_xpath = "/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]/div/ol/li[10]"
        try:
            element_present = EC.presence_of_element_located((By.XPATH, last_summ_xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutError:
            print("Timed out waiting for page to load")

    def init_npcs(self):
        # Start program execution timer.
        start = time.time()
        
        # Replace "webdriver.____" below with .Firefox(), or with the browser of your choice.
        self.driver = webdriver.Firefox(options=npcs.options) 
        # Navigate to the page indicated by the url.
        self.driver.get(npcs.url)
        self.timeout_check()
        atexit.register(self.driver.quit)

        end = time.time()

    def refresh_npcs(self):
        """Refresh the current list of NPCS.

        ***IMCOMPLETE***
        """
        button_xpath = "//html/body/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/input"
        button = self.driver.find_elements_by_xpath(button_xpath)[0]
        button.click()
        self.timeout_check()
        return "NPC list refreshed."

    def list_npcs(self):
        """Return a list of the currently generated NPC summaries.

        -Start by using the xpath of the npc summaries
            (found by using inspect on the webpage, picking
            a summary from the page, then doing right-click>copy>XPath)
        -Create a list of npc_web_elems from the npc summary identifiers.
        -Format the web element objects into text and return
        a list of npc descriptions.
        """
        npc_summs_xpath = "/html/body/div[2]/div[2]/form/table/tbody/tr[13]/td[2]/div/ol/li"
        npc_web_elems = self.driver.find_elements_by_xpath(npc_summs_xpath)

        npc_summs = []
        for i in npc_web_elems:
            npc_summs.append(i.text)
        return npc_summs

    def dropboxes_lists(self):
        backend_options = []
        frontend_options = []
        for i in range(4):
            backend_options.append([])
            frontend_options.append([])

        # list format:
        # backend: [xpath, elements]
        # frontend: [extracted text options]
        for i in range(len(backend_options)):
            backend_options[i].append("/html/body/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/select[" + str(i + 1) + "]/option")
            backend_options[i].append(self.driver.find_elements_by_xpath(backend_options[i][0]))
            for j in backend_options[i][1]:
                if isinstance(j, list):
                    for k in j:
                        frontend_options[i].append(k.text)
                else:
                    frontend_options[i].append(j.text)

        return frontend_options