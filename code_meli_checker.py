'''
Validate Iran Resident ID number:

Formula:
-Multiply each ID digit in its Position

For Ex:id_number = 0044569981

(*Verify digit is the last number of your ID number|here its 1)

ID number        0   0   4   4   5   6   9   9   8   VerifyDigit (*Length of id is 10-digits)
            *
Positions        10  9   8   7   6   5   4   3   2
                ____________________________________
                 =            sum_value

-Calculate remainder of sum_value to 11 | sum_value%11

    if remainder is lower than 2 | remainder<2 AND remainder equals to verify_digit --> True
    if remainder is bigger or equals 2| remainder >=2 then calculate 11-remainder if 11-remainder equals to verify_digit -->True
    else situations return False
        
'''

code_meli=input("Enter Your 10-digits ID Number:\n")
assert len(code_meli)==10 , "ID Number should be in full 10-digits format" 
multipliers=[10,9,8,7,6,5,4,3,2]
verify_digit=int(code_meli[-1])
sum_value=0
for codemeli_digit,multiplier_digit in zip(code_meli,multipliers):
    sum_value+=int(codemeli_digit)*multiplier_digit

def test(sum_value):
    '''Test the sum_value against the verify_num'''
    remainder=sum_value%11
    if remainder in [0,1]:
        return remainder==verify_digit
    else:
        return 11-remainder == verify_digit

if test(sum_value):
    print("It's Validated as a True ID number")
else:
    print("It's Not a Valid ID number!")
