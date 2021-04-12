x = 0
score = x
# Question One
print("A modulating signal m(t)=10cos(2π×103t) is amplitude modulated with a carrier signal c(t)=50cos(2π×105t). Find the modulation index, the carrier power, and the power required for transmitting AM wave")   
answer_1 = input("a)1.5\nb)0.2\nc)1.8\nd)1\n:")
if answer_1.lower() == "b" or answer_2.lower() == "200W":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is 0.2")



# Question Two
print("The equation of amplitude wave is given by s(t)=20[1+0.8cos(2π×103t)]cos(4π×105t). Find the carrier power")
answer_2 = input("a)200W\nb)150W\nc)300W\nd)250W\n:")
if answer_2.lower() == "a" or answer_2.lower() == "200W":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Frequency spectrum is the representation of a signal in frequency domain")

# Question Three
print("What is frequency band for audio applications?")
answer_3 = input("a)30kHz-300kHz\nb)3kHz-30kHz\nc)300Hz-3kHz\nd)30Hz-300Hz\n:")
if answer_3.lower() == "c" or answer_3.lower() == "300Hz-3kHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Bandwidth is the difference of upper and lower frequency")  

# Question Four
print("What is the change in the value of transmitted power when the modulation index changes from 0 to 1")
answer_4 = input("a)100%\nb)Remains unchanged\nc) 50%\nd)80%\n:")
if answer_4.lower() == "c" or answer_4 == "50%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is 50%")

# Question Five 
print("Calculate the frequencies available in the frequency spectrum when a 2MHz carrier is modulated by two sinusoidal signals of 350Hz and 600Hz.")
answer_5 = input("a)2000.35, 1999.65 and 2000.6, 1999.4 \nb)1999.35, 1999.65 and 2000.6, 2000.4\nc)2000.35, 2000.65 and 2000.6, 2000.4\nd)1999.35, 1999.65 and 1999.6, 1999.4\n:")
if answer_5.lower() == "a" or answer_5.lower() == "2000.35, 1999.65 and 2000.6":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the answer is 2000.35, 1999.65 and 2000.6")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('x3.py')
        close()
    else:
        close()
    
    
else:
    print("That's poor knowledge, try again!/n")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('y.py')
    close()
else:
    close()






