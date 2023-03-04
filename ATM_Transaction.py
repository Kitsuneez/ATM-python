import datetime
from abc import abstractmethod
from Account import Account
import itertools

class ATM_Transaction:
	id_iter = itertools.count()
	def __init__(self, transactionType, amount):
		self.Id = next(self.id_iter)
		self.Date = datetime.datetime.now()
		self._type = transactionType
		self._Amount = amount
	
	@abstractmethod
	def update(self, Account, amount, transferAcc):
		pass

class Withdrawal(ATM_Transaction):
	def __init__(self, amount):
		self.Date = datetime.datetime.now()
		self._type = "Withdrawal"
		self._Amount = amount

	def withdraw(self, Account, amount):
		self.update(Account, amount, None)
	
	def update(self, Account, amount, transferAcc):
		return Account.debit(self._Amount)

class Transfer(ATM_Transaction):
	def __init__(self, amount):
		self.Date = datetime.datetime.now()
		self._type = "Transfer"
		self._Amount = amount
	
	def update(self, Account, amount, transferAcc):
		Account.debit(self._Amount)
		transferAcc.credit(self._Amount)


		