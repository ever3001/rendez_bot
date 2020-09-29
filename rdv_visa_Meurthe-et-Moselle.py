# MIT License

# Copyright (c) 2020 Ever ATILANO (ever.developer3001@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time # for sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

while True:
    # New instance for Chrome
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # Open the webpage
    try:
        browser.get('http://www.meurthe-et-moselle.gouv.fr/booking/create/22259')
        # Save the window opener (current window, do not mistaken with tab... not the same)
        main_window = browser.current_window_handle
        # Accepter les cookies
        browser.find_element_by_xpath("//a[@onclick='javascript:accepter()']").click()
        ################################################## Fill all the first form
        # Click in checkbox "Veuillez cocher la case pour..."
        browser.find_element_by_xpath("//input[@name='condition']").click()
        # Click in the submit button
        browser.find_element_by_xpath("//input[@name='nextButton']").click()
        ##################################################

        ################################################## Fill all the second form
        # Click in the radio button "Prendre un rendez-vous pour un renouvellement de titre..."
        browser.find_element_by_xpath("//input[@id='planning22263']").click()
        # Click in the submit button
        browser.find_element_by_xpath("//input[@type='submit']").click()
        ##################################################

        # Text to find when there is an error
        text = "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous."

        if ((text in browser.page_source) or ("502" in browser.page_source) or ("503" in browser.page_source) or ("504" in browser.page_source)):
            # Print in console that we didn't have the rd
            print("Pas de chance pour trouver un rendez-vous ='(")
            # Close the browser
            browser.quit()
            # Retry in some seconds
            time.sleep(300)
        else:
            # Open tab and trigger the alarm
            browser.execute_script("window.open('http://soundbible.com/mp3/analog-watch-alarm_daniel-simion.mp3', '_blank')")
            break
    except:
        browser.quit()
        time.sleep(300)