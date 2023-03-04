from Customer import Customer
import random
from AdditionalException import AdditionalException
class Bank:
	def __init__(self, code, address):
		self.__code = code
		self.__address = address
		self.ATMs = []
		self.customers = []
		self.cards = []

	def add_customer(self, Customer, pin):
		customer = {
			"customer_id" : Customer.get_name() + str(random.randint(1000,9999)),
			"details" : Customer,
			"atm_pin" : pin
		}
		self.customers.append(customer)

	def manages(self, card):
		self.cards.append(card)

	def maintains(self, ATM):
		self.ATMs.append(ATM)

	def authorize_pin(self, pinInput, cust):
		for i in (self.customers):
			if(i["customer_id"][:-4] == cust["details"].get_name() and pinInput == i["atm_pin"]):
				return True
		raise AdditionalException.InvalidPinNumber()

	def get_acct(self, accountNo):
		check = filter(lambda x: x.details.Account.get_accountNumber() == accountNo, self.customers)
		if(check):
			return true
		else:
			raise AdditionalException.AccountNotFound()

			