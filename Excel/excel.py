import csv

results_list = []  # this is the running list of all results


def compound_interest(x):
	data = []  # temp list that keeps track of your results

	# assigning variable to list
	p = x[0]
	i = x[1]
	n = x[2]

	# runs compound interest formula
	ci = round(((p * (1 + i) ** n) - p),2)

	# Data tracking for output to excel
	data.append(p)
	data.append(i)
	data.append(n)
	data.append(ci)

	results_list.append(data)

	return print(ci)


def enter_numbers():
	# gets user input on their investments
	print('how much money did you invest?')
	principle = float(input("Enter your investment: "))

	print('How many years will you leave it invested?')
	years = int(input("enter years as a whole number: "))

	print('what is your expected annual return?')
	interest = float(input('if 5% enter .o5: '))

	return [principle, interest, years]


def grid_view(x):
	# Outputs grid view so you can compare your investments

	print('\n')
	print("Princ.  APR  Years   Interest")

	for i in x:
		print(i)

def ror(x):
	# calculates rate of return
	ror_list = []

	for i in x:
		calc_ror = (i[3] / i[0]) * 100
		ror_list.append(calc_ror)

	return print(max(ror_list))

def export_csv(x):
	investment_data = x

	investment_data.insert(0,["Principle","Interest","Years","Interest"])

	with open('investmentdata.csv','w', newline = '') as file:
		writer = csv.writer(file)
		writer.writerows(investment_data)

def run_calc():
	# runs a loop for core fucntions
	run_count = 0

	print("would you like to calculate the compound interest of your investment")
	answer = input('yes or no: ')
	while answer == 'yes':
		compound_interest(enter_numbers())
		run_count += 1
		print('would you like to run another investment?')
		answer = input('yes or no: ')
		if answer == 'no':
			if run_count == 1:
				print(f'this program ran {run_count} time')
				grid_view(results_list)
				ror(results_list)
				break
			else:
				print(f'this program ran {run_count} times')
				grid_view(results_list)
				ror(results_list)
				export_csv(results_list)
				break

	else:
		print('The best time to invest was yesterday! The next best time is today!')

run_calc()