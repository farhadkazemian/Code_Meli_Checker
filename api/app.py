import json
from unittest import result
from flask import Flask
app = Flask(__name__)

doc_string='''
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
@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/api/',methods=['GET'])
def help():
  return doc_string

@app.route('/api/id/<id>',methods=['POST'])
def verify_id(id):
    if len(id)!=10 :
        verified='ID Length Incorrect'
    else:
        multipliers=[10,9,8,7,6,5,4,3,2]
        verify_digit=int(id[-1])
        sum_value=0
        for codemeli_digit,multiplier_digit in zip(id,multipliers):
            sum_value+=int(codemeli_digit)*multiplier_digit

        remainder=sum_value%11
        if remainder in [0,1]:
            verified= remainder==verify_digit
        else:
            verified= 11-remainder == verify_digit
    result={
        'id' : id,
        'valid':verified
    }
    return json.dumps(result)
if __name__ == '__main__':
    app.run(debug=False)