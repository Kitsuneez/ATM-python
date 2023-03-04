from AdditionalException import AdditionalException
class Account:
	def __init__(self, accountType, owner):
		self._accountType = accountType
		self.__owner = owner
		self.balance = 0

	def check_balance(self):
		return self.balance

	def get_owner(self):
		 return self.__owner

	def get_accountType(self):
		return self._accountType

	def credit(self, amount):
		self.__validateAmount(amount)
		if(float(amount) > 0):
			self.balance += float(amount)

	def debit(self, amount):
		self.__validateAmount(amount)
		if(float(amount) <=  self.balance):
			self.balance -= float(amount)
			return True
		else:
			raise AdditionalException.InsufficientFunds()

	def __validateAmount(self, amount):
		try:
			if(float(amount) <= 0 or str(amount)[::-1].find('.') > 2):
				raise ValueError
			return True
		except ValueError:
			raise ValueError

class Savings_Account(Account):
	def __init__(self, accountNumber, owner):
		super(Savings_Account, self).__init__("Savings",owner)
		self.__accountNumber = accountNumber

	def get_accountNumber(self):
		return self.__accountNumber

class Current_Account(Account):
	def __init__(self, accountNumber, owner):
		super(Current_Account, self).__init__("Current",owner)
		self.__accountNumber = accountNumber

	def get_accountNumber(self):
		return self.__accountNumber
		
		