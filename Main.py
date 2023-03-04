from Bank import Bank
from ATM import ATM
from Account import Savings_Account, Current_Account
from ATM_Card import ATM_Card
from Customer import Customer
from AdditionalException import AdditionalException

def atm_app(atm):
	while True:
		menu1()
		option = input("Enter an option: ")
		match option:
			case "1":
				cardNumber = input("Enter a ATM card number: ")
				try:
					if(not atm.check_card(cardNumber)):
						raise AdditionalException.InvalidATMCard()
					else:
						pin = input("Enter a Pin Number: ")
						if(atm.check_pins(pin)):
							authorized(atm)
				except Exception as e:
					print(e)
			case "2":
				quit(0)


def menu1():
	print("1. Insert ATM card\n2. Quit Simulation")

def authorized(atm):
	while True:
		print("""Available options:
1. Check Balance
2. Withdraw Funds
3. Transfer Funds
4. Return Card""")
		option = input("Enter a transaction option: ")
		match option:
			case "1":
				if(atm.check_accts()):
					Menu3()
					option = input("Enter an account option: ")
					match option:
						case "1":
							print(f"Your current account has a balance of ${atm.show_balance('Current'):.2f}\n")
						case "2":
							print(f"Your savings account has a balance of ${atm.show_balance('Savings'):.2f}\n")
				else:
					print(f"Your {atm.show_balance(None).get_accountType().lower()} account has a balance of ${atm.show_balance(None).check_balance():.2f}\n")
			case "2":
				if(atm.check_accts()):
					Menu3()
					option = input("Enter an account option: ")
					amount = input("Enter an amount to withdraw: ")
					match option: 
						case "1":
							atm.transactions("Withdrawal", amount, "Current", None)
							print(f"Card Returned\nYour current account has a balance of ${atm.show_balance('Current'):.2f}\n")
						case "2":
							atm.transactions("Withdrawal", amount, "Savings", None)
							print(f"Card Returned\nYour savings account has a balance of ${atm.show_balance('Savings'):.2f}\n")
				else:
					amount = input("Enter an amount to withdraw: ")
					atm.transactions("Withdrawal", amount, "Current", None)
					print(f"Card Returned\nYour {atm.show_balance(None).get_accountType().lower()} account has a balance of ${atm.show_balance(None).check_balance():.2f}\n")
				break
			case "3":
				if(atm.check_accts()):
					Menu3()
					option = input("Enter an account option: ")
					transferAccNo = input("Enter the account number to transfer funds to: ")
					amount = input("Enter an amount to transfer: ")
					match option: 
						case "1":
							atm.transactions("Transfer", amount, "Current", transferAccNo)
							print(f"Card Returned\nYour current account has a balance of ${atm.show_balance('Current'):.2f}\n")
						case "2":
							atm.transactions("Transfer", amount, "Savings", transferAccNo)
							print(f"Card Returned\nYour savings account has a balance of ${atm.show_balance('Savings'):.2f}\n")
				else:
					transferAccNo = input("Enter the account number to transfer funds to: ")
					amount = input("Enter an amount to transfer: ")
					atm.transactions("Transfer", amount, "Current", transferAccNo)
					print(f"Card Returned\nYour {atm.show_balance(None).get_accountType().lower()} account has a balance of ${atm.show_balance(None).check_balance():.2f}\n")
				break
			case "4":
				print("Card Returned\n")
				break

def Menu3():
	print("""Choose Account:
1. Current Account
2. Savings Account""")


