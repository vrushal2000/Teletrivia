x = 0
score = x
# Question One
print("If an AM signal is represented by v = ( 15 + 3 Sin( 2Π * 5 * 103 t) ) * Sin( 2Π * 0.5 * 106 t) volts Calculate the values of the frequencies of carrier and modulating signals. \n ii) Calculate the value of modulation index. \n iii) Calculate the value of bandwidth of this signal.")   
answer_1 = input("a)1.6 MHz and 8 KHz, 0.6, 16 MHz\nb)1.9 MHz and 18 KHz, 0.2, 16 KHz\nc)2.4 MHz and 18 KHz, 0.2, 16 KHz\nd)1.6 MHz and 8 KHz, 0.2, 16 KHz\n:")
if answer_1.lower() == "d" or answer_2.lower() == "1.6 MHz and 8 KHz, 0.2, 16 KHz":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, ANSWER: (d) 1.6 MHz and 8 KHz, 0.2, 16 KHz")



# Question Two
print(" An AM signal has a total power of 48 Watts with 45% modulation. Calculate the power in the carrier and the sidebands.")
answer_2 = input("a)39.59 W, 4.505 W\nb)40.59 W, 4.205 W\nc)43.59 W, 2.205 W\nd)31.59 W, 8.205 W\n:")
if answer_2.lower() == "c" or answer_2.lower() == "43.59 W, 2.205 W":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, ANSWER: (c) 43.59 W, 2.205 W ")

# Question Three
print("Calculate the power saved in an Amplitude Modulated wave when it is transmitted with 45% modulation \n– Without carrier\n– Without carrier and a sideband")
answer_3 = input("a)90%, 95%\nb)82%, 91%\nc)82%, 18%\nd)68%, 16%\n:")
if answer_3.lower() == "a" or answer_3.lower() == "90%, 95%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect,ANSWER: (a) 90%, 95% ")  

# Question Four
print("The antenna current of the transmitter is 10A. Find the percentage of modulation when the antenna current increases to 10.4A.")
answer_4 = input("a)32%\nb)28.5%\nc)64%\nd)40%\n:")
if answer_4.lower() == "b" or answer_4 == "28.5%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, ANSWER:(b) 28.5%")

# Question Five 
print("What is the carrier frequency in an AM wave when its highest frequency component is 850Hz and the bandwidth of the signal is 50Hz?")
answer_5 = input("a)80 Hz\nb)695Hz\nc)625Hz\nd)825Hz\n:")
if answer_5.lower() == "d" or answer_5.lower() == "825Hz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the answer is 825Hz")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('y3.py')
        close()
    else:
        close()
    
    
else:
    print("That's poor knowledge, try again!/n")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('z.py')
    close()
else:
    close()
