for i in '0123456789abcde':
    if (int('131'+i+'1',15)+int('13'+i+'3',17))%11==0:
        print((int('131'+i+'1',15)+int('13'+i+'3',17)),i)
