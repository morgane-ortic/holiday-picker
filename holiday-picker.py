import time
import random
from playsound import playsound

destinations = ["The Basque Country", "Barcelona", "Marseille", "Nice", "Toulouse"]

def main():
    while True:
        result = random.choice(destinations)
        destinations.remove(result)
        
        print("Picking your destination, please wait...")
        playsound('dice-roll.wav')

        print("Your dream holiday destination is...\n")
        time.sleep(1.5)
        print(f"                {result.upper()}")
        time.sleep(1.5)

        if destinations:
            input("\nChoose another destination? Press Enter\n")
            time.sleep(0.5)
        else:
            input("""
That was all the possible destinations.
Press Enter to exit the program.
""")
            time.sleep(0.5)
            break


if __name__ == "__main__":
    main()