from Bank import Bank
from ATM import ATM
from Account import Savings_Account, Current_Account
from ATM_Card import ATM_Card
from Customer import Customer
from AdditionalException import AdditionalException

def atm_app(atm):
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
						menu2(atm)
			except Exception as e:
				print(e)
		case "2":
			quit(0)


def menu1():
	print("1. Insert ATM card\n2. Quit Simulation")

def menu2(atm):
	print("""Available options:
1. Check Balance
2. Withdraw Funds
3. Transfer Funds
4. Return Card
""")
	authorized(atm)

def authorized(atm):
	option = input("Enter a transaction option: ")
	match option:
		case "1":
			Menu3()
			option = input("Enter an account option: ")
			match option:
				case "1":
					print(f"${atm.show_balance('Current'):.2f}")
				case "2":
					print(f"${atm.show_balance('Savings'):.2f}")
		case "2":
			Menu3()
			option = input("Enter an account option: ")
			amount = input("Enter an amount to withdraw: ")
			match option: 
				case "1":
					atm.transactions("Withdrawal", amount, "Current", None)
					print(f"Card Returned\nYour current account has a balance of ${atm.show_balance('Current'):.2f}")
				case "2":
					atm.transactions("Withdrawal", amount, "Savings", None)
					print(f"Card Returned\nYour savings account has a balance of ${atm.show_balance('Savings'):.2f}")
		case "3":
			pass
		case "4":
			pass

def Menu3():
	print("""Choose Account:
1. Current Account
2. Savings Account
""")


