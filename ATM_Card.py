from Customer import Customer
from Account import Account
class ATM_Card:
	def __init__(self, cardNumber, customer):
		self.__cardNumber = cardNumber
		self.__customer = customer

	def get_acct_types(self, customer):
		return Customer.get_accounts(customer)
	
	def access(self):
		return Account(self.__customer)	

	def get_Number(self):
		return self.__cardNumber

	def get_owner(self):
		return self.__customer.name
	
	def __str__(self):
		return f"Card Number: {self.get_Number()}\nName: {self.get_owner()}"