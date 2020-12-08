"""Write a program in which you declare three boolean variables (is_morning, is_mother, is_asleep) that you also give a value.
Then write the code to decide if you need to answer your mobile phone, according to these rules:
 You normally answer your phone except in the morning, then you only answer if it's your mother.
When you're asleep, you never answer the call.
Test your program by changing the three variables a number of times!"""
is_morning = False
is_mother = False
is_asleep = False

if is_morning:
    if is_asleep:
        print("I'm not answering my phone.")

    elif not is_asleep and is_mother:
        print("I'm answering my phone.")

    else:
        print("I'm not answering my phone.")

elif not is_morning and not is_asleep:
    print("I'm answering my phone.")

else:
    print("I'm not answering my phone.")