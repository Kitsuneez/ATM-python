import ATM_Transaction
from ATM_Card import ATM_Card
from Bank import Bank
from AdditionalException import AdditionalException

class ATM:
	def __init__(self, location, managed_by):
		self.location = location
		self.managed_by = managed_by
		self.__current = None

	def get_attribute(self):
		return self.__current

	def transactions(self, transactionType, amount, accountType, transferAccNo):
		match transactionType:
			case "Withdrawal":
				for i in self.managed_by.customers:
					if (i["details"].get_name() == self.__current.get_owner()):
						for x in i["details"].get_accounts():
							if(len(i["details"].get_accounts()) == 1):
								transaction = ATM_Transaction.Withdrawal(amount)
								transaction.withdraw(x, amount)
							if(x.get_accountType() == accountType):
								transaction = ATM_Transaction.Withdrawal(amount)
								transaction.withdraw(x, amount)
			case "Transfer":
				transferAcc = self.managed_by.get_acct(transferAccNo)
				for i in self.managed_by.customers:
					if (i["details"].get_name() == self.__current.get_owner()):
						for x in i["details"].get_accounts():
							if(len(i["details"].get_accounts()) == 1):
								transaction = ATM_Transaction.Transfer(amount)
								transaction.update(x, amount, transferAcc)
							if(x.get_accountType() == accountType):
								transaction = ATM_Transaction.Transfer(amount)
								transaction.update(x, amount, transferAcc)
		

	def check_accts(self):
		for i in self.managed_by.customers:
			if (i["details"].get_name() == self.__current.get_owner()):
				if(int(len(i["details"].get_accounts())>1)):
					 return True
		return False
				
	def check_pins(self, pin):
		for i in self.managed_by.customers:
			if (i["details"].get_name() == self.__current.get_owner()):
				return self.managed_by.authorize_pin(pin, i)

	def check_card(self, cardNumber):
		for i in (self.managed_by.cards):
			if(i.get_Number() == cardNumber):
				self.__current = i
				return True
		return False
	def show_balance(self, Accounttype):
		for i in self.managed_by.customers:
			if (i["details"].get_name() == self.__current.get_owner()):
				for x in i["details"].get_accounts():
					if(len(i["details"].get_accounts()) == 1):
						return x
					if(x.get_accountType() == Accounttype):
						return x.check_balance()