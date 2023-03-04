class Customer:

	def __init__(self, name, address, DOB):
		self.name = name
		self.address = address
		self.DOB = DOB
		self._Accounts = []

	def owns(self, account):
		self._Accounts.append(account)

	def get_name(self):
		return self.name

	def get_accounts(self):
		return self._Accounts

	def __str__(self):
		return f"Name: {self.name}\nAddress: {self.address}\nDate Of Birth: {self.DOB}"
