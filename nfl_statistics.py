#nfl_statistics
cardinals = {"Name":"Cardinals","City":"Phoenix","Wins":9,"Losses":4,"Ranking":2}
lions = {"Name":"Lions","City":"Detroit","Wins":10,"Losses":3,"Ranking":2}
raiders = {"Name":"Raiders","City":"Oakland","Wins":11,"Losses":2,"Ranking":1}

nfl_teams = [cardinals, lions, raiders]

if cardinals in nfl_teams:
	print(cardinals.items())#will print all I know about the cardinals
	
if lions in nfl_teams:
	print(raiders["Wins"]) #returns the number of games the raiders have won
