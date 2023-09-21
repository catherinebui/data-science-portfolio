
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

	try:
		assert((N > minimum_deposit)), 'Minimum deposit of ${0} is required to open account'.format(minimum_deposit)
	except:
		return 0
	return retrieve_combinedJ_balance(T, N, P)

### method 3: oop code -------------------------------------------------------------------------

class BankUser:
	def __init__(self, name):
		self.name = name
		self.N = 0
		self.bank_accounts = {}
		self.payment_schedule = {}


	def add_bank_account(self, account):
		## assign BankUser name to account
		account.owners.append(self)
		self.bank_accounts[account.name_account] = account
	def create_payment_schedule(self, account_name, N, T, P, increase_by):
		self.P = P
		self.N = N
		schedule = PaymentSchedule(self, account_name, self.N, T, self.P, increase_by)
		self.payment_schedule[account_name] = schedule
		if self.payment_schedule[account_name] and self.N >= 25:
			self.bank_accounts.get(account_name).add_payment_schedule(self.payment_schedule[account_name])
	def deposit_into_bank(self, account_name, amt):
		self.N = amt
		self.bank_accounts.get(account_name).add_deposit(amt)

class BankAccount:
	bank = 'Edwards Bank'
	minimum_deposit = 25
	def __init__(self, name_account):
		self.name_account = name_account
		self.balance = 0
		self.owners = []
		self.payment_schedule = {}
	def add_deposit(self, amt):
		self.balance += amt
	def retrieve_balance(self):
		return self.balance
	def add_payment_schedule(self, Schedule):
		self.payment_schedule[Schedule.user] = Schedule

class PaymentSchedule:
	def __init__(self, User, account_name, N, T, P, increase_by):
		self.user = User
		self.user_name = User.name
		self.account_name = account_name
		self.deposit = N
		self.months = T
		self.P = P
		self.increase_by = increase_by
	def calculate_amt_atgivenmonth(self, month):
		new_percentage = self.calculate_newP_atgivenmonth(month)
		new_amount = new_percentage*self.deposit
		return new_amount
	def calculate_newP_atgivenmonth(self, month):
		new_percentage = self.P + self.increase_by*(month-1)
		new_percentage = new_percentage if new_percentage <= 1 else 1
		return new_percentage
	def calculate_balance_aftermonths(self, months):
		return sum([self.calculate_amt_atgivenmonth(month) for month in range(1,months+1,1)])


def run_method3(N,T,P):
	### write code here:
	john = BankUser('John')
	martha = BankUser('Martha')
	j_account = BankAccount('J')
	m_account = BankAccount('M')

	john.add_bank_account(j_account)
	martha.add_bank_account(j_account)
	martha.add_bank_account(m_account)

	martha.create_payment_schedule('M', 100, T, 1, 0)
	martha.create_payment_schedule('J', N, T, P, 0.01)
	john.create_payment_schedule('J', N, T, 1, 0)

	## method 3a - adding in deposit into the bank accounts each month.
	for t in range(1, T+1, 1):
		john.deposit_into_bank('J', N)
		print(j_account.balance)
		martha.deposit_into_bank('J', j_account.payment_schedule.get(martha).calculate_amt_atgivenmonth(t))
		# martha.deposit_into_bank('M', 100)
		print(t, j_account.balance)
		
	## method 3b - predicting the final balance based on payment schedule
	## this method doesn't add to the BankAccount balance so j_account.balance would be equal to 0.
	## Therefore, ideally, method 3a is better for mutating objects
	# final_balance = j_account.payment_schedule.get(martha).calculate_balance_aftermonths(T) + j_account.payment_schedule.get(john).calculate_balance_aftermonths(T)
	# print(final_balance)
	return j_account.balance



### test run
if __name__ == '__main__':
	minimum_deposit = 25

	N = 40

	T = 5

	P = 0.5

	'''
	The outputs of all methods should be equal.
	Build function run_method3 using OOP to solve the question in the story above.
	'''

	print('METHOD 1', run_method1(N,T,P))
	print('METHOD 2', run_method2(N,T,P))
	print('METHOD 3', run_method3(N,T,P))
