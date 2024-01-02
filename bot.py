# coding: utf-8

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import random, os

male = ["André","Antônio","Arthur","Bernardo","Breno","Bruno","Caio","Carlos","Cauã","Daniel","Danilo","Davi","Diego","Douglas","Eduardo","Enzo","Erick","Felipe","Filipe","Franciso","Gabriel","Guilherme","Gustavo","Heitor","Henrique","Igor","Iuri","Joari","José","João","Joaquim","Juarez","Júlio","Juraci","Juvenal","Kaio","Kauan","Kauã","Kauê","Leonardo","Luan","Lucas","Luiz","Luís","Marcos","Mateus","Matheus","Miguel","Murilo","Nicolas","Otávio","Paulo","Pedro","Rafael","Renan","Ryan","Samuel","Thiago","Tiago","Victor","Vinícius","Vicente","Victor","Vitór"]
female = ["Adriana","Alice","Aline","Amanda","Ana","Anna","Antonia","Beatriz","Bianca","Brenda","Bruna","Camila","Carolina","Caroline","Clara","Daniela","Eduarda","Emilly","Emily","Evelyn","Fernanda","Francisca","Gabriela","Gabrielle","Gabrielly","Giovana","Giovanna","Helena","Isabela","Isabella","Isabelle","Janaina","Joseane","Júlia","Juliana","Juraci","Lara","Larissa","Laura","Lavinia","Letícia","Livia","Luana","Luisa","Luiza","Manuela","Marcia","Maria","Mariana","Marina","Melissa","Nicole","Patricia","Rafaela","Raissa","Rebeca","Sarah","Sofia","Sophia","Thaís","Vitória","Yasmin","Ágatha"]
surnames = ["Almeida","Alvaréz","Alves","Araújo","Azevedo","Barbosa","Barboza","Cardoso","Carvalho","Cavalcante","Cavalcanti","Correa","Correia","Costa","Cruz","Dias","Díaz","Fernandes","Fernandez","Ferreira","German","Gomes","Gomez","Gonzáles","Gonçalves","Gónzalez","Lima","Martins","Mello","Melo","Montes","Moraes","Morais","Oliveira","Pereira","Pinto","Ribeiro","Rocha","Rodrigues","Santiago","Santos","Schmidt","Schmitz","Silva","Sousa","Souza","Teixeira"]

try:

	if random.randint(0, 1) == 0:
		namePosition = random.randint(0, len(male))
		Name = str(male[namePosition])

	else:
		namePosition = random.randint(0, len(female))
		Name = str(female[namePosition])

	surnamePosition = random.randint(0, len(surnames))

	MiddleName =  surnames[surnamePosition]
	User =  Name + MiddleName + str(random.randint(9999, 999999))
	Pass = Name + str(random.randint(0, 9999)) + MiddleName
	phone = '4185817014499'
	BirthDay = '6'
	BirthYear = '1969'

	options = Options()
	options.add_argument("--headless")
	service = Service(log_path=os.devnull)
	browser = webdriver.Firefox(options=options, service=service)
	browser.set_page_load_timeout(10)

	browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
	browser.maximize_window()
	sleep(3)

	FirstName = browser.find_element(By.ID, 'firstName')
	LastName = browser.find_element(By.ID, 'lastName')
	UserName = browser.find_element(By.ID, 'username')
	Password = browser.find_element(By.NAME, 'Passwd')
	PasswordConfirm = browser.find_element(By.NAME, 'ConfirmPasswd')

	FirstName.send_keys(Name)
	LastName.send_keys(MiddleName)
	UserName.send_keys(User)
	Password.send_keys(Pass)
	PasswordConfirm.send_keys(Pass)
	sleep(1)

	LoginButton = browser.find_element(By.ID, 'accountDetailsNext').click()
	sleep(2)

	PhoneNumber = browser.find_element(By.ID, 'phoneNumberId')
	PhoneNumber.send_keys(phone)
	sleep(1)

	NumberButton = browser.find_element(By.ID, 'gradsIdvPhoneNext').click()
	sleep(2)

	CodeBox = browser.find_element(By.ID, 'code')

	ConfirmCode = input("Digite aqui o seu codigo: ")
	CodeBox.send_keys(ConfirmCode)
	sleep(1)

	CodeButton = browser.find_element(By.ID, 'gradsIdvVerifyNext').click()
	sleep(2)

	DayInput = browser.find_element(By.ID, 'day')
	MonthSelect = Select(browser.find_element(By.ID, 'month'))
	YearInput = browser.find_element(By.ID, 'year')
	GenderSelect = Select(browser.find_element(By.ID, 'gender'))

	DayInput.send_keys(BirthDay)
	GenderSelect.select_by_value('1')
	MonthSelect.select_by_value('1')
	YearInput.send_keys(BirthYear)
	sleep(1)

	LoginButton = browser.find_element(By.ID, 'accountDetailsNext').click()

	PersonalDetailsButton = browser.find_element(By.ID, 'personalDetailsNext').click()
	PersonalDetailsButton.click()

except Exception as error:
	print(error)

finally:	
	sleep(3)

	try:
		browser.close()
		browser.quit()
	
	except:
		pass