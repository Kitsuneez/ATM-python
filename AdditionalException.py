class AdditionalException(Exception):

    
    def InvalidAccount():
        raise AdditionalException("Invalid Account")
    def AccountNotFound():
        raise AdditionalException("Account Not Found")
    def InsufficientFunds():
        raise AdditionalException("Insufficient Funds")
    def InvalidATMCard():
        raise AdditionalException("Invalid ATM Card")
    def InvalidPinNumber():
        raise AdditionalException("Invalid PIN Number")