from selenium import webdriver

print('Input your Gmail adrress')
userEmail = raw_input()


browser = webdriver.Firefox()
browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys(userEmail)


loginElem = browser.find_element_by_id('next')
loginElem.click()

print('Input your Gmail password')
userPassword = raw_input()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys(userPassword)

signInElem = browser.find_element_by_id('signIn')
signInElem.click()

print('Email of recipient?')
sendTo = raw_input()

print('What should be the subject line?')
subjectLine = raw_input()

print('Type your message')
body = raw_input()

composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

toElem = browser.find_element_by_class_name('vO')
toElem.send_keys(sendTo)

subjectElem = browser.find_element_by_class_name('aoT')
subjectElem.send_keys(subjectLine)

bodyElem = browser.find_element_by_class_name('Am')
bodyElem.click()
bodyElem.send_keys(body)

sendElem = browser.find_element_by_class_name('aoO')
sendElem.click()





