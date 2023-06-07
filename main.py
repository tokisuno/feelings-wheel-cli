# feeling wheel app
# lucas cordero 2023
import os 
from datetime import datetime, timedelta

"""
Going to hopefully use the dates to generate a markdown file that it adds to.
    - to be synced in dropbox/syncthing folder
"""

today = datetime.now()
yest = datetime.now() - timedelta(1)

"""
TODO:
* maybe find a way to not hard-code this dictionary in? using class?
    - issue being every feeling has their own amount of args/sub-feelings
    - i think i am overthinking it
""" 
feelings = {
        'happy':
            {
                'playful':
                    {'aroused', 'cheeky'},
                'content':
                    {'free', 'joyful'},
                'interested':
                    {'curious', 'inquisitive'},
                'proud':
                    {'successful', 'confident'},
                'accepted':
                    {'respected', 'valued'},
                'powerful':
                    {'courageous', 'creative'},
                'peaceful':
                    {'loving', 'thankful'},
                'trusting':
                    {'sensitive', 'intimate'},
                'optimistic':
                    {'hopeful', 'optimistic'},
             },
        'sad':
            {
                'lonely':
                    {'isolated', 'abandoned'},
                'vulnerable':
                    {'victimized', 'fragile'},
                'despair':
                    {'grief', 'powerless'},
                'guilty':
                    {'ashamed', 'remorseful'},
                'depressed':
                    {'empty', 'inferior'},
                'hurt':
                    {'disappointed', 'embarrassed'},
                },
        'disgusted':
            {
                'repelled':
                    {'hesitant', 'horrified'},
                'awful':
                    {'detestable', 'hauseated'},
                'disappointed':
                    {'revolted', 'appalled'},
                'disapproving':
                    {'embarrassed', 'judgemental'},
            },
        'angry':
            {
                'critical':
                    {'dismissive', 'skeptical'},
                'distant':
                    {'numb', 'withdrawn'},
                'frustrated':
                    {'annoyed', 'infuriated'},
                'aggressive':
                    {'hostile', 'provoked'},
                'mad':
                    {'jealous', 'furious'},
                'bitter':
                    {'violated', 'indignant'},
                'humiliated':
                    {'ridiculed', 'disrespected'},
                'let down':
                    {'resentful', 'betrayed'},
                },
        'fearful':
            {
                'threatened':
                    {'exposed', 'nervous'},
                'rejected':
                    {'persecuted', 'excluded'},
                'weak':
                    {'insignificant', 'worthless'},
                'insecure':
                    {'inferior', 'inadequate'},
                'anxious':
                    {'worried', 'overwhelmed'},
                'scared':
                    {'frightened', 'helpless'},
                },
        'bad':
            {
                'bored':
                    {'indifferent', 'apathetic'},
                'busy':
                    {'pressured', 'rushed'},
                'stressed':
                    {'overwhelmed', 'out of control'},
                'tired':
                    {'sleepy', 'unfocussed'},
                },
        'surprised':
            {
                'startled':
                    {'shocked', 'dismayed'},
                'confused':
                    {'disillusoined', 'perplexed'},
                'amazed':
                    {'astonished', 'awe'},
                'excited':
                    {'eager', 'energetic'},
                },
        }

def run():
    base_feelings = ["happy", "sad", "disgusted", "angry", "fearful", "bad", "surprised"] 
    print(base_feelings)
    user_input = input("""
    Which of these best describe you right now?: 
    """)
    # for x, y in feelings.items():
    #     print(x)
    #     print(y)

def exit_application():
    print("exit_application")
    sys.exit(0)



def main():
    user_input = input("""
    Feelings Wheel CLI Application
    Press Y to Continue
    Press Q to Quit
    """)
    try:
        if not (user_input.lower() == "y" or user_input.lower() == "q"):
            raise ValueError("Input input")
    except ValueError as error:
        print(error)
    else:
            switcher = {
                    "y": run,
                    "q": exit_application
            }
    return switcher.get(user_input)()

if __name__ == "__main__":
    main()


