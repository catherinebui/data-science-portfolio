
### Python Exercise - Creating Bank Account System
### Written and Presented by Catherine Bui
'''
I'm going to compare three methods of coding styles and show why OOP may be necessary in some cases.

For my examples, I'm going to use the banking system to illustrate relationships and variable changes.

We will work to solve the problem with different methods.

Objective:
	- Learn how to use Classes
	- Learn about the effects of global variables
	- Learn about scalability on applications and system design
	- Learn about relationships between objects and future usability
	- Compare different methods of coding

Story:
        John went to the bank to create a debit account J where a minimum deposit of $25 is needed to open.
        He plans to deposit N monthly deposit into the account J
 
        His wife Martha is a co-owner of that same debit account J, and 
        she has her own account M where she has opened 2 months prior when the J account was first opened.
        She deposits $100 into account M each month. 
 
        She plans to deposit allocated percent P (30%) of John's monthly deposit amount N into account J 
        and gradually increase the allocated percent P by additional 1% each next month, up to 100%. 
 
        Assumptions: 
            - They deposited at the beginning of the month and total balance is counted at the end of the month.
            - 1 <= T
            - 25 <= N 
            - T(M) + 2 = T(J)
			- 0 <= P <= 1

        What is the account balance of account J in T months?

		Extra credit question: At what month T, will account J's total balance be $500,000?

'''
### global variables
# minimum_deposit = 25
#
# N = 500
#
# T = 3
#
# P = 0.3

'''

For the purpose of this exercise, assume that each run_method{int} is a new terminal environment.
'''

### method 1: (Imperative) ----------------------------------------------------------------------

def run_method1(N, T, P):

	j_bank_account_balance = 0
	m_bank_account_balance = 100*2
	for t in range(1, T+1):
		j_bank_account_balance = j_bank_account_balance + N
		percentage = (P + 0.01*(t-1))
		percentage = percentage if percentage <= 1 else 1
		j_bank_account_balance = j_bank_account_balance + (percentage*N)
		m_bank_account_balance += 100

	return j_bank_account_balance



### method 2: (Functional) ------------------------------------------------------------------------

### functions
def retrieve_amt_atgivenmonth(month, allocated_amount, percentage, increase_by):
	'''
	Args:
		*percentage (in decimal) such as 30% will be inputed as 0.3
	'''
	new_percentage = percentage + increase_by*(month-1)
	new_percentage = new_percentage if new_percentage <= 1 else 1
	new_amount = new_percentage*allocated_amount
	return new_amount
def retrieve_finalamt_aftermonths(months, allocated_amount, percentage, increase_by):
	return sum([retrieve_amt_atgivenmonth(month, allocated_amount, percentage, increase_by) for month in range(1,months+1,1)])

def retrieve_combinedJ_balance(months, N = 25 , P = 1):
	return retrieve_finalamt_aftermonths(months,N,P,0.01) + retrieve_finalamt_aftermonths(months, N, 1, 0)

def run_method2(N, T, P):

	assert((N > minimum_deposit)), 'Minimum deposit of ${0} is required to open account'.format(minimum_deposit)

	return retrieve_combinedJ_balance(T, N, P)

### method 3: oop code -------------------------------------------------------------------------

class BankUser:
	def __init__(self, name, N):
		self.name = name
		self.N = N
		self.bank_accounts = {}
		self.P = 1
		self.deposit = 0


	def add_bank_account(self, account):
		## assign BankUser name to account
		account.owners.append(self)
		self.bank_accounts[account.name_account] = account
	def assign_automatic_amount(self, amt, P= 1, increase_by = 0):
		self.change_PofN(P)


	def deposit_into_bank(self, account_name, amt):
		## amt must be greater than or equal to minimum deposit 25
		if amt >= 25:
			self.bank_accounts.get(account_name).add_deposit(amt)
	def change_PofN(self, p):
		self.P = p
	def add_user_address(self, address):
		self.address = address
		



class BankAccount:
	bank = 'Edwards Bank'
	def __init__(self, name_account):
		self.name_account = name_account
		self.balance = 0
		self.owners = []
	def add_deposit(self, amt):
		self.balance += amt
	def retrieve_balance(self):
		return self.balance


class BankTransaction:
	def __init__(self, amt, account, month):
		self.amt = amt
		self.account = account
		self.month_of_deposit = month


def run_method3(N,T,P):
	### write code here:
	john = BankUser('John', N)
	martha = BankUser('Martha', N)
	j_account = BankAccount('J')
	m_account = BankAccount('M')

	john.add_bank_account(j_account)
	martha.add_bank_account(j_account)
	martha.add_bank_account(m_account)

	return




### test run
if __name__ == '__main__':
	minimum_deposit = 25

	N = 500

	T = 3

	P = 0.3

	'''
	The outputs of all methods should be equal.
	Build function run_method3 using OOP to solve the question in the story above.
	'''

	print('METHOD 1', run_method1(N,T,P))
	print('METHOD 2', run_method2(N,T,P))
	print('METHOD 3', run_method3(N,T,P))
