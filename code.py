class ATM:
    def __init__(self,name,balance,pin):
        self.name=name
        self.balance=balance
        self.pin=pin
    def checkbalance(self):
        p=int(input('Enter Your Pin: '))
        if(p==self.pin):
            print('The Balance In Your Account Is ',str(self.balance))
        else:
            print('Inncorrect Pin')
    def withdrawmoney(self):
        p=int(input('Enter Your Pin: '))
        if(p==self.pin):
            a=int(input('Enter The Amount You Want To Withdraw: '))
            if(a>self.balance):
                print('Insufficient Balance')
            else:
                self.balance=self.balance-a
                print('The Balance In Your Account Is ',str(self.balance))
        else:
            print('Inncorrect Pin')
    def depositmoney(self):
        p=int(input('Enter Your Pin: '))
        if(p==self.pin):
            a=int(input('Enter Ho Much You Want To Deposit: '))
            self.balance=self.balance+a
            print('The Balance In Your Account Is ',str(self.balance))
        else:
            print('Inncorrect Pin')

coustmer1=ATM('bill',5000,1980)
coustmer1.withdrawmoney()
coustmer1.depositmoney()
coustmer1.checkbalance()



        