# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random  

def display_instruct():
	print(
	"""
	Witaj w grze 'Jaka to liczba'!
	
	Mam na myśli pewną liczbę z zakresu od 1 do 100.
	Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n
	""")

def ask_number(question, number, step = 1):
	response = None
	while response != number and step != 5:
		response = int(input(question))
		if response > number:
			print("Za duża...")
		else:
			print("Za mała...")
		
		step += 1
	return response, step

def check(guess, tries):
	if guess == the_number:
		print("Odgadłeś! Ta liczba to", the_number)
		print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
	elif tries == 5:
		print("Wykorzystałeś limit prób")
		print("\nTo była liczba", the_number)


the_number = random.randint(1, 100)

def main():
	
	display_instruct()
	guess, tries = ask_number("Ta liczba to: ", the_number)
	check(guess, tries)
	
main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")