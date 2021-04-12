x = 0
score = x
# Question One
print("The modulation techniques used to convert analog signal into digital signal are")   
answer_1 = input("a)Pulse code modulation\nb)Delta modulation\nc)Adaptive delta modulation\nd)All of the above\n:")
if answer_1.lower() == "d" or answer_2.lower() == "All of the above":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, ANSWER: (d) All of the above")



# Question Two
print(" It is a term used to describe the amount of amplitude change present in an AM waveform.")
answer_2 = input("a)coefficient of modulation\nb)modulation index\nc)depth of modulation\nd)any of these\n:")
if answer_2.lower() == "d" or answer_2.lower() == "any of these":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, ANSWER: (d) any of these ")

# Question Three
print("An un modulated AM signal produces a current of 5.4 A. If the modulation is 100 percent, \ncalculate (a) the carrier power,\n(b) the total power, \n(c) the sideband power when it is transmitted through an antenna having an impedance of 50Ω.")
answer_3 = input("a)1458 W, 2187.5 W, 729.25 W\nb)278 W, 2187.5 W, 1917.25 W\nc)1438 W, 2187.5 W, 759.25 W\nd)280 W, 2187.5 W, 750.25 W\n:")
if answer_3.lower() == "a" or answer_3.lower() == "1458 W, 2187.5 W, 729.25":
    print("Correct")
    x = x + 1
else:
    print("Incorrect,ANSWER: 1458 W, 2187.5 W, 729.25 W")  

# Question Four
print("If an AM signal is represented by v = ( 15 + 3 Sin( 2Π * 5 * 103 t) ) * Sin( 2Π * 0.5 * 106 t) volts\n i) Calculate the values of the frequencies of carrier and modulating signals.\n ii) Calculate the value of modulation index. \n iii) Calculate the value of bandwidth of this signal.")
answer_4 = input("a)1.6 MHz and 8 KHz, 0.6, 16 MHz\nb)1.9 MHz and 18 KHz, 0.2, 16 KHz\nc)2.4 MHz and 18 KHz, 0.2, 16 KHz\nd)1.6 MHz and 8 KHz, 0.2, 16 KHz\n:")
if answer_4.lower() == "d" or answer_4 == "1.6 MHz and 8 KHz, 0.2, 16 KHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, ANSWER:(d) 1.6 MHz and 8 KHz, 0.2, 16 KHz")

# Question Five 
print("The antenna current of the transmitter is 10A. Find the percentage of modulation when the antenna current increases to 10.4A.")
answer_5 = input("a)32%\nb)28.5%\nc) 64%\nd)40%\n:")
if answer_5.lower() == "b" or answer_5.lower() == "28.5":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, the answer is (b) 28.5")


#Total Score
score = float(x / 5) * 100
print(x,"out of 5, that is",score, "%")
if x>2:
    print("THAT'S BRILLIANT! you're promoted to the next level...ALL THE BEST!")
    b=input("press y to continue")
    if b=="y":
        import os
        os.startfile('z3.py')
        close()
    else:
        close()
    
    
else:
    print("That's poor knowledge, try again!/n")
a=input("press y to continue")
if a=="y":
    import os
    os.startfile('x.py')
    close()
else:
    close()
