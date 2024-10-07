from bass_notes import notes_dict
import random, time

def main():
    while True:
        notes_list = [i for i in notes_dict]
        current_note = random.choice(notes_list)
        print(current_note)
        time.sleep(15)
        print(notes_dict.get(current_note))
        print(
            "| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |"
        )

if __name__ == '__main__':
    main()