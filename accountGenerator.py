# nike account generator
# need to pull email and password, numbers, and names/ birthdays, proxies, browser
#need to learn https://stackoverflow.com/questions/62260445/how-to-run-a-python-script-multiple-times-simultaneously-using-python-and-termin to define operation times
# need to use selenium commands in order to automate tasks
#need to enter proxies using extensions
#https://stackoverflow.com/questions/37642452/using-python-to-fill-in-text-boxes-on-websites-and-clicking-button-to-download/37642689
#https://www.youtube.com/watch?v=YbGAUEjTKg4
#https://www.youtube.com/watch?v=U6gbGk5WPws

#new ideas  
    #stop the function if there is an error
    #must have a proxy fail safety to start new broswer if proxy is bad
    #must return with a confirmation




from selenium import webdriver
import time 

web = webdriver.Chrome()
web.get("https://www.nike.com/register")

time.sleep(2)

myEmail = ("testemail@gmail.com")
email = web.find_element_by_xpath("/html/body/div[2]/div[3]/div[4]/form/div[1]/input")
email.send_keys(myEmail)

time.sleep(2)

myPassword = ("Password")
password = web.find_element_by_xpath("/html/body/div[2]/div[3]/div[4]/form/div[2]/input")
password.send_keys(myPassword)

time.sleep(2)

myFirstName = ("test")
first = web.find_element_by_xpath("/html/body/div[2]/div[3]/div[4]/form/div[3]/input")
first.send_keys(myFirstName)

time.sleep(2)

myLastName = ("last")
last = web.find_element_by_xpath("/html/body/div[2]/div[3]/div[4]/form/div[4]/input")
last.send_keys(myLastName)

time.sleep(2)

myDateOfBirth = ("12/21/2001")
birthday = web.find_element_by_xpath("/html/body/div[2]/div[3]/div[4]/form/div[5]/input")
birthday.send_keys(myDateOfBirth)

time.sleep(2)

gender = web.find_element_by_css_selector("d1686a1c-08d3-48c7-8946-aeadc1001e9b")
gender.click()

time.sleep(2)

joinUs = web.find_element_by_css_selector("d17adf28-c356-4054-8408-5b8e3516d019")
joinUs.click()



















with open("proxy.txt") as f:  # using the proxy text lists  #need to loop this operation i times in order to repeat and read the next lines in the files
    #lines_to_read = [0, x+ 1] if x>0
    #lines_to_read = [x, x+ 1] if x<0
    for line in f:
        print(line, end="0")
    f.close()
#https://www.youtube.com/watch?v=vJwcW2gCCE4

with open("accounts.txt") as f:  # using the account lists  #need to loop this operation i times in order to repeat and read the next lines in the files
    #lines_to_read = [0, x + 1] if x > 0
    #lines_to_read = [x, x + 1] if x < 0
    for line in f:
        print(line, end="0")
    f.close()


with open("information.txt") as f:    #contains the name, last name, birthday         #need to loop this operation i times in order to repeat and read the next lines in the files
    #lines_to_read = [0, x + 1] if x > 0
    #lines_to_read = [x, x + 1] if x < 0
    for line in f:
        print(line, end="0")
    f.close()


#select gender for the account



with open("location.txt") as f:
    for line in f:
        print(line, end="0")


#define number of times operation will run




