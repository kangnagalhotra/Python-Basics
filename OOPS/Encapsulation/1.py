'''
getter and setter
'''

class bankAcc:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        #self.balance = balance #public var
        self.__balance = balance #private var
    def deposite(self,amount):
        self.__balance+=amount
        print(f'Deposited{amount}.New_Balance{self.__balance}')
    def total_balance(self):
        return self.__balance #control access
account = bankAcc('123452',7000)
account.deposite(6000)
print(account.total_balance())

        