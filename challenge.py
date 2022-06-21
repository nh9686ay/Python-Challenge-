######################################################
# Part 1: Most Clocks are Normal, But Some are Cuckoo

time = 8
# Complete the prompt here
td = int(time)
if td < 9:
    print('Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.')
elif td <= 16:
    print('Working hard or hardly working?')
elif td < 20 and td > 16:
    print('How did it get so late so soon?')
elif td < 22:
    print('A day without sunshine is like, you know, night.')
else:
    print('Burning the midnight oil!')

######################################################
# Part 2: I Came, I 'Saur, I Conquered

angry = True
bored = True
hungry = False
tired = False

# Complete the prompt here
# Example `if` statement:
if angry == True and hungry == True and bored == True:
    print("he will eat the Triceratops")
elif tired == True and hungry == True:
    print('he will eat the Iguanadon')
elif hungry == True and bored == True:
    print("he will eat the Stegasaurus.")
elif tired == True:
    print('he will take a nap')
elif angry == True and bored == True:
    print("he will fight the Velociraptor")
elif angry == True or bored == True:
    print("he roars")
else:
    print('T-Rex gives a toothy smile')

######################################################
# Part 3: IOU

disney_characters = ['simba', 'ariel', 'pumba',
                     'flounder', 'nala', 'ursula', 'scar', 'flotsam', 'timon']

# Complete the prompt here
for name in disney_characters:
    if ("u" in name):
        print(f"{name}, U are so Uniquely U!")
    elif ("i" in name):
        print(f"{name}, I bet you're Impressively Intelligent!")
    elif ("o" in name):
        print(f"{name}, O My! How Original!")
    else:
        print(f"{name} Ehh, a's and e's are so ordinary.")
        ######################################################
        # Part 4: If You're Cold, Sit in a Corner. It's 90 Degrees!

temperature = 90

# Complete the prompt here
while temperature > 75:
    print(f"Temperature is {temperature} — crank the AC!")
    temperature -= 3
print("75. Ahh, that's better.")
