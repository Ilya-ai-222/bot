import random
emo = ["😊","😍","😘","😞","😲","😴","😠","🥹","🤯","😯"]
def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789abcdefghijklmnopqrstuvWxyz"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def em():
    emodsi = random.choice[emo]
    return emodsi
