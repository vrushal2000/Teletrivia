x = 0
score = x

print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
# Question One 
print("An oscillator for an AM transmitter has a 100μH coil and a 10nF capacitor. If a modulating frequency of 10 KHz modulates the oscillator, find the frequency range of the side bands.")
answer_1 = input("a)149 KHz to 169 KHz\nb)184 KHz to 296 KHz\nc)238 KHz to 296 KHz\nd)155 KHz to 166 KHz\n:")
if answer_1.lower() == "a" or answer_1.lower()== "149 KHz to 169 KHz":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is a) 149 KHz to 169 KHz")

# Question Two
print("Calculate the total modulation Index when a carrier wave is being modulated by two modulating signals with modulation indices 0.8 and 0.3.")
answer_2 = input("a)0.8544\nb)0.6788\nc)0.9999\nd)0.5545\n:")
if answer_2.lower() == "a" or answer_2.lower() == "0.8544":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answe is a) 0.8544")

# Question Three
print("Calculate the bandwidth occupied by a DSB signal when the modulating frequency lies in the range from 100 Hz to 10KHz.")
answer_3 = input("a)28 KHz\nb)24.5 KHz\nc)38.6 KHz\nd)19.8 KHz\n:")
if answer_3.lower() == "d" or answer_3.lower() == "19.8 KHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answe is d) 19.8 KHz")  

# Question Four
print("An AM broadcast station transmits modulating frequencies up to 6 kHz. If the AM station is transmitting on a frequency of 894 kHz, the values for maximum and minimum upper and lower sidebands and the total bandwidth occupied by the AM station are:")
answer_4 = input("a)900 KHz, 888 KHz, 12 KHz\nb) 894 KHz, 884 KHz, 12 KHz\nc)894 KHz, 888 KHz, 6 KHz\nd)900 KHz, 888 KHz, 6 KHz\n:")
if answer_4.lower() == "a" or answer_4 == "900 KHz, 888 KHz, 12 KHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is a) 900 KHz, 888 KHz, 12 KHz")

# Question Five 
print("Frequency components of an AM wave (m = modulation index) are")
answer_5 = input("a)Carrier frequency (ωc ) with amplitude A \nb)Upper side band (ωc + ωm) having amplitude mA/2\nc)Lower side band (ωc - ωm) having amplitude mA/2\nd)All of the above\n:")
if answer_5.lower() == "d" or answer_5.lower() == "All of the above":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is d) All of the above")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("You're einsteinious! you're promoted to the next level...LAST LEVEL TO GO!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('z3.py')
        close()
    else:
        close()
else:
    print("NEVERMIND , start again!")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('z.py')
    close()
else:
    close()

