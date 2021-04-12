x = 0
score = x

print("COME ON! You can do it last level to go...ALL THE BEST!")
# Question One 
print("An oscillator for an AM transmitter has a 100μH coil and a 10nF capacitor. If a modulating frequency of 10 KHz modulates the oscillator, find the frequency range of the side bands.")
answer_1 = input("a)149 KHz to 169 KHz\nb)184 KHz to 296 KHz\nc)238 KHz to 296 KHz\nd)155 KHz to 166 KHz\n:")
if answer_1.lower() == "a" or answer_1.lower()== "149 KHz to 169 KHz":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is a) 149 KHz to 169 KHz")

# Question Two
print("Square law modulators")
answer_2 = input("a)Have non linear current-voltage characteristics\nb)Are used for Amplitude Modulation\nc)Are used for frequency modulation\nd) Both a and b are correct
\n:")
if answer_2.lower() == "d" or answer_2.lower() == "Both a and b are correct":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is d)  Both a and b are correct")

# Question Three
print("What is the effect on the transmitted power of AM signal when the modulation index changes from 0.8 to 1?")
answer_3 = input("a)0.1364\nb)0.3856\nc)1.088\nd)0.5\n:")
if answer_3.lower() == "a" or answer_3.lower() == "0.1364":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is a) 0.1364")  

# Question Four
print("TRF receiver and super heterodyne receiver are used for")
answer_4 = input("a)Detection of modulating signal\nb)Removal of unwanted signal\nc)Both a and b \nd)None of the above")
if answer_4.lower() == "c" or answer_4 == "Both a and b":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is c) Both a and b")

# Question Five 
print(" Advantage of using a high frequency carrier wave is")
answer_5 = input("a)Signal can be transmitted over very long distances \nb)Dissipates very small power\nc)Antenna height of the transmitter is reduced\nd)All of the above\n:")
if answer_5.lower() == "d" or answer_5.lower() == "All of the above":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is d) All of the above")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("Bravo! you're good to go...!")
    b=input("press y to continue")
    if b=="y":
        close();
    else:
        close();
else:
    print("NEVERMIND , start again!")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('x.py')
    close()
else:
    close()
