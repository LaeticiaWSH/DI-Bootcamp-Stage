import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'letmein'
DATABASE = 'bank'
class BankAccount():
    def __init__(self,account_number, first_name,last_name,amount):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount
    def __str__(self):
        return 'This is the bank account (%d) of %s %s who has Rs %d' % (self.account_number,self.first_name,self.last_name,self.amount)
    @staticmethod
    def transfer(bankaccount1,bankaccount2,amount):
        ba1 = BankAccount.getBankAccountByNumber(bankaccount1)
        ba2 = BankAccount.getBankAccountByNumber(bankaccount2)
        if(amount <= ba1.amount):
            BankAccount.update_account(ba1.account_number,-amount)
            BankAccount.update_account(ba2.account_number,amount)
            print('transfer complete')
        else:
            print('insufficient funds')
    @staticmethod
    def getAllBankAccounts():
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM accounts LIMIT 20;")
        results = cursor.fetchall()
        for i in range(len(results)):
            results[i] = BankAccount(results[i][0],results[i][1],results[i][2],results[i][3])
        connection.close()
        return results
    @staticmethod
    def getBankAccountByNumber(number):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = "SELECT * FROM accounts WHERE account_number = %d LIMIT 1;" % number
        print(query)
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        row = results[0]
        result = BankAccount(row[0],row[1],row[2],row[3])
        connection.close()
        return result
    @staticmethod
    def createBankAccount(first_name,last_name,amount):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute("INSERT INTO accounts (first_name,last_name,amount) VALUES ('%s','%s',%d);" % (first_name,last_name,amount))
        connection.commit() # important when writing
        connection.close()
        return True
    @staticmethod
    def delete_account(account_number):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute("DELETE FROM accounts where account_number = %d" % (account_number))
        connection.commit() # important when writing
        connection.close()
        return True
    @staticmethod
    def update_account(account_number,amount):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        cursor.execute("UPDATE accounts SET amount = amount + %d WHERE account_number = %d" % (amount,account_number))
        connection.commit() # important when writing
        connection.close()
        return True
    @staticmethod
    def printAllbankAccounts():
        print('---------------')
        results = BankAccount.getAllBankAccounts()
        for result in results:
            print(result)
        print('---------------')
# BankAccount.printAllbankAccounts()
# # BankAccount.createBankAccount('Oneyka','Stanley',50000)
# # BankAccount.delete_account(2)
# # BankAccount.update_account(1,-10000)
# BankAccount.createBankAccount('Laeticia','Wong',40000)
# BankAccount.createBankAccount('Anas','Rasmally',50000)
# BankAccount.printAllbankAccounts()
ba = BankAccount.getBankAccountByNumber(3)
print(ba)
# BankAccount.printAllbankAccounts()
# BankAccount.transfer(4,1,10000)
# BankAccount.printAllbankAccounts()

