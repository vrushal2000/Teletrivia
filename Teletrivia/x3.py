x = 0
score = x
# Question One
print("An unmodulated AM signal produces a current of 5.4 A. If the modulation is 100 percent, calculate:(a) the carrier power, (b) the total power, (c) the sideband power when it is transmitted through an antenna having an impedance of 50Ω.")   
answer_1 = input("a)1458 W, 2187.5 W, 729.25 W\nb)278 W, 2187.5 W, 1917.25 W\nc)1438 W, 2187.5 W, 759.25 W\nd)280 W, 2187.5 W, 750.25 W\n:")
if answer_1.lower() == "a" or answer_1.lower() =="1458 W, 2187.5 W, 729.25 W":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, The answer is a) 1458 W, 2187.5 W, 729.25 W")



# Question Two
print("The total power in an Amplitude Modulated signal if the carrier of an AM transmitter is 800 W and it is modulated 50 percent.")
answer_2 = input("a) 850 W\nb)1000.8 KW\nc)750 W\nd)900 W\n:")
if answer_2.lower() == "d" or answer_2.lower() == "900 W":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is d) 900 W")

# Question Three
print("Calculate the depth of modulation when a transmitter radiates a signal of 9.8KW after modulation and 8KW without modulation of the signal.")
answer_3 = input("a)80%\nb)67%\nc)50%\nd)100%\n:")
if answer_3.lower() == "b" or answer_3.lower() == "67%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is b) 67%")  

# Question Four
print("If an AM signal is represented by v = ( 15 + 3 Sin( 2Π * 5 * 103 t) ) * Sin( 2Π * 0.5 * 106 t) volts i) Calculate the values of the frequencies of carrier and modulating signals. ii) Calculate the value of modulation index. iii) Calculate the value of bandwidth of this signal.")
answer_4 = input("a) 1.6 MHz and 8 KHz, 0.6, 16 MHz\nb) 1.9 MHz and 18 KHz, 0.2, 16 KHz\nc) 2.4 MHz and 18 KHz, 0.2, 16 KHz\nd) 1.6 MHz and 8 KHz, 0.2, 16 KHz\n:")
if answer_4.lower() == "d" or answer_4 == "1.6 MHz and 8 KHz, 0.2, 16 KHz":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is d) 1.6 MHz and 8 KHz, 0.2, 16 KHz")

# Question Five 
print("Calculate the power saved in an Amplitude Modulated wave when it is transmitted with 45% modulation: \n– Without carrier \n– Without carrier and a sideband")
answer_5 = input("a)90%, 95% \nb)82%, 91%\nc)82%, 18%\nd)68%, 16%\n:")
if answer_5.lower() == "a" or answer_5.lower() == "90%, 95%":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The answer is a) 90%, 95%")


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
    os.startfile('y.py')
    close()
else:
    close()





