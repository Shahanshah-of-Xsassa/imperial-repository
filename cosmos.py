import json
import matplotlib.pyplot as plot
import numpy as np

TURN_ANNOUNCEMENT = "Comrade, which turn is it?"

def Open():
	try:
		name = str(input("Name of the file: ")) + ".txt"
	except:
		main()
		
	with open(name, "r") as the_file:
		line = json.load(the_file)
	the_file.close()
	return line
	
def Arrange(line):
	eco_invest = line["Economy"]
	tech_invest = line["Technology"]
	mil_invest = line["Military"]
	eco_invest, tech_invest, mil_invest = Additions(eco_invest, tech_invest, mil_invest)
	return eco_invest, tech_invest, mil_invest
	
def Additions(eco_invest, tech_invest, mil_invest):
	eco_invest.append(int(input("Insert new economical investments: ")))
	tech_invest.append(int(input("Insert new technological investments: ")))
	mil_invest.append(int(input("Insert new military investments: ")))
	return eco_invest, tech_invest, mil_invest
	
def Save(eco_invest, tech_invest, mil_invest):
	name = str(input("Name of the file: ")) + ".txt"
	
	line = {
		"Economy": eco_invest,
		"Technology": tech_invest,
		"Military": mil_invest,
	}
	with open(name, "w") as the_file:
		line = json.dump(line, the_file)
	the_file.close()
	
def Income(eco_invest, tech_invest, mil_invest):
	tura = int(input(TURN_ANNOUNCEMENT))
	return (eco_invest[tura-1]/3)+(tech_invest[tura-1]/4)+(mil_invest[tura-1]/5)+(eco_invest[tura-2]/3)+(tech_invest[tura-2]/4)+(mil_invest[tura-2]/5)
	
def Show(something):
	print(something)
	
def main():
	x = str(input("Create new file? Type Yes or No "))
	if (x == "No"):
		line = Open()
	if (x == "Yes"):
		eco_invest = []
		tech_invest = []
		mil_invest = []
		eco_invest, tech_invest, mil_invest = Additions(eco_invest, tech_invest, mil_invest)
		Save(eco_invest, tech_invest, mil_invest)
		line = Open()
	eco_invest, tech_invest, mil_invest = Arrange(line)
	Save(eco_invest, tech_invest, mil_invest)
	income = Income(eco_invest, tech_invest, mil_invest)
	Show("Income: ")
	Show(income)
	
main()
