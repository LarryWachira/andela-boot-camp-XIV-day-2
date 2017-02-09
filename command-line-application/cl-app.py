import requests

response = requests.get("http://api.open-notify.org/astros.json")
info = response.json()

if response.status_code == 200:
    print("\nWant to play 'Guess how many people are in space'?\n\n")
    answer = input('Type Y or N:> ')

    if answer == 'Y' or answer == 'yes' or answer =='y' or answer == 'YES' or answer == 'Yes':
        print("\nWell, what are you waiting for? Guess how many humans are in space right now:")
        answer = input('\n> ')

        try:
            if int(answer) == info["number"]:
                print("\nOf course. Google, right? \n\n:( ")
            else:
                print("\nWrong! There are {} people in space right now.".format(info["number"]))
                print("\nThat'll be one billion dollars. I'll take cash.")
        except:
            print("\nWrong! There are {} people in space right now.".format(info["number"]))
            print("\nThat'll be one billion dollars. I'll take cash.")

    elif answer == 'N' or answer == 'NO' or answer == 'n' or answer == 'no' or answer == 'No':
        print("\nYou must be a lot of fun at parties. \n:(")

    else: print("\nSeriously? And the darwin award goes to...")

else: print("Error: {}\n\nPlease try again later.".format(response.status_code))