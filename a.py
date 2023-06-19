# ASK ALI OR IMANUEL
# I DON'T KNOW HOW TF TO PROGRAM LMAO


import os
from datetime import datetime, timedelta

today = datetime.now()
yest = datetime.now() - timedelta(1)

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

base_feelings=('happy', 'sad', 'disgusted', 'angry', 'fearful', 'bad',' surprised')
happy_feelings=('playful', 'content', 'interested', 'proud', 'accepted', 'powerful', 'peaceful', 'trusting', 'optimistic')
sad_feelings=('lonely', 'vulnerable', 'despair', 'guilty' 'depressed', 'hurt')
disgusted_feelings=('repelled', 'awful', 'disappointed', 'disapproving') 
angry_feelings=('critical', 'distant', 'frustrated', 'aggressive', 'mad', 'bitter', 'humiliated', 'let down')
fearful_feelings=('threatened', 'rejected', 'weak', 'insecure', 'anxious', 'scared') 
bad_feelings=('bored', 'busy', 'stressed', 'tired')
surprised_feelings=('startled', 'confused', 'amazed', 'excited')

def run():
    for index, val in enumerate(base_feelings):
        print(index+1, val)
    user_input=str(input('Pick a feeling!: '))
    if user_input in base_feelings:
        print(True)
    else:
        print(False)

def exit_app():
    print("exit_app")
    sys.exit(0)

def main():
    user_input = str(input(
        """
        Feelings Wheel CLI Application
        Press Y to Continue
        Press Q to Quit
        """
        ))
    try:
        if not (user_input.lower() == "y" or user_input.lower() == "q"):
            raise ValueError("Input input")
    except ValueError as error:
        print(error)
    else:
            switcher = {
                    "y": run,
                    "q": exit_app
                    }
    return switcher.get(user_input)()

if __name__ == "__main__":
    main()
        

