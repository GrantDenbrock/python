#job search
jobs = {
'Boeing':{'applied':'no','rating':'8'},
'Honeywell':{'applied':'yes','rating':'7'},
'Prestige Worldwide':{'applied':'no','rating':'10'}
} #creates dictionary of jobs
print(jobs)

#now say I want to sort by applied

for job in jobs:
	while jobs[job['applied']] == 'yes':
		print(job)
