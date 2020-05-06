import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_availability(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket"))>0, "Button not find"
    #time.sleep(10) #uncomment for checking
