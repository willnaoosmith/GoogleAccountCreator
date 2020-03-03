# coding: utf-8

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time
import random

male = ["André","Antônio","Arthur","Bernardo","Breno","Bruno","Caio","Carlos","Cauã","Daniel","Danilo","Davi","Diego","Douglas","Eduardo","Enzo","Erick","Felipe","Filipe","Franciso","Gabriel","Guilherme","Gustavo","Heitor","Henrique","Igor","Iuri","Joari","José","João","Joaquim","Juarez","Júlio","Juraci","Juvenal","Kaio","Kauan","Kauã","Kauê","Leonardo","Luan","Lucas","Luiz","Luís","Marcos","Mateus","Matheus","Miguel","Murilo","Nicolas","Otávio","Paulo","Pedro","Rafael","Renan","Ryan","Samuel","Thiago","Tiago","Victor","Vinícius","Vicente","Victor","Vitór"]
female = ["Adriana","Alice","Aline","Amanda","Ana","Anna","Antonia","Beatriz","Bianca","Brenda","Bruna","Camila","Carolina","Caroline","Clara","Daniela","Eduarda","Emilly","Emily","Evelyn","Fernanda","Francisca","Gabriela","Gabrielle","Gabrielly","Giovana","Giovanna","Helena","Isabela","Isabella","Isabelle","Janaina","Joseane","Júlia","Juliana","Juraci","Lara","Larissa","Laura","Lavinia","Letícia","Livia","Luana","Luisa","Luiza","Manuela","Marcia","Maria","Mariana","Marina","Melissa","Nicole","Patricia","Rafaela","Raissa","Rebeca","Sarah","Sofia","Sophia","Thaís","Vitória","Yasmin","Ágatha"]
surnames = ["Almeida","Alvaréz","Alves","Araújo","Azevedo","Barbosa","Barboza","Cardoso","Carvalho","Cavalcante","Cavalcanti","Correa","Correia","Costa","Cruz","Dias","Díaz","Fernandes","Fernandez","Ferreira","German","Gomes","Gomez","Gonzáles","Gonçalves","Gónzalez","Lima","Martins","Mello","Melo","Montes","Moraes","Morais","Oliveira","Pereira","Pinto","Ribeiro","Rocha","Rodrigues","Santiago","Santos","Schmidt","Schmitz","Silva","Sousa","Souza","Teixeira"]

coin = random.randint(0, 1)

if (coin == 0):
	namePosition = random.randint(0, len(male))
	Name = unicode(male[namePosition], errors='replace')
else:
	namePosition = random.randint(0, len(female))
	Name = unicode(female[namePosition], errors='replace')

surnamePosition = random.randint(0, len(surnames))

MiddleName =  surnames[surnamePosition]
User =  Name + MiddleName + str(random.randint(9999, 999999))
Pass = Name + str(random.randint(0, 9999)) + MiddleName
phone = '4185817014499'
BirthDay = '6'
BirthYear = '1969'

options = Options()
options.headless = False
browser = webdriver.Firefox(options=options, executable_path=r'/home/vmax-william/desktop/Bot5/geckodriver')
browser.set_page_load_timeout(10)

browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
browser.maximize_window()
time.sleep(2)

FirstName = browser.find_element_by_id('firstName')
LastName = browser.find_element_by_id('lastName')
UserName = browser.find_element_by_id('username')
Password = browser.find_element_by_name('Passwd')
PasswordConfirm = browser.find_element_by_name('ConfirmPasswd')

FirstName.send_keys(Name)
LastName.send_keys(MiddleName)
UserName.send_keys(User)
Password.send_keys(Pass)
PasswordConfirm.send_keys(Pass)
time.sleep(1)

LoginButton = browser.find_element_by_id('accountDetailsNext').click()
time.sleep(2)

PhoneNumber = browser.find_element_by_id('phoneNumberId')
PhoneNumber.send_keys(phone)
time.sleep(1)

NumberButton = browser.find_element_by_id('gradsIdvPhoneNext').click()
time.sleep(2)

CodeBox = browser.find_element_by_id('code')

ConfirmCode = input("Digite aqui o seu codigo: ")
CodeBox.send_keys(ConfirmCode)
time.sleep(1)

CodeButton = browser.find_element_by_id('gradsIdvVerifyNext').click()
time.sleep(2)

DayInput = browser.find_element_by_id('day')
MonthSelect = Select(browser.find_element_by_id('month'))
YearInput = browser.find_element_by_id('year')
GenderSelect = Select(browser.find_element_by_id('gender'))

DayInput.send_keys(BirthDay)
GenderSelect.select_by_value('1')
MonthSelect.select_by_value('1')
YearInput.send_keys(BirthYear)
time.sleep(1)

LoginButton = browser.find_element_by_id('accountDetailsNext').click()

PersonalDetailsButton = browser.find_element_by_id('personalDetailsNext').click()
PersonalDetailsButton.click()

#browser.close()