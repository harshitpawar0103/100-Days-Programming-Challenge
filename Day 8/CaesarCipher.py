

text = '''I am a Data Analyst with expertise in Power BI, Tableau, SQL, Python, and Excel. I have hands-on experience in analyzing and visualizing data to drive business insights. My background includes a B.Sc. in Computer Science and I am currently pursuing an MCA from UIT RGPV Bhopal.
I have worked on real-world projects like IPL Analysis, Promotion Analysis for Atliq Mart, Business 360 for Brick & Mortar & Ecommerce, and more. Additionally, I actively contribute to data analytics communities, assisting learners and solving analytical problems.
Currently, I am also expanding my knowledge in Machine Learning and working on a Predictive Maintenance API for the telecom industry using FastAPI and ML.
Apart from my analytical skills, I have a passion for music I play the flute, synthesizer, and guitar and enjoy singing.
I aim to leverage data analytics to enhance business profitability and eventually establish my own venture. '''


def convert_cipher(text):
    text_list = list(text)
    n = int(input("Enter no by you wanna displace the character : "))
    ord_list = []

    # Encode
    for i in range(len(text_list)):
        if ord(text_list[i])==32: # Exclude space from encrypting
            ord_list.append(" ")
        else :
            ord_list.append(chr(ord(text_list[i])+n))    

    cipher_text = "".join(ord_list)
    print(cipher_text)
    return cipher_text



def decode_cipher(text):
    # Decode
    n = int(input("Enter no by you wanna displace the character : "))
    decode_list = list(text)
    lsit = []
    for i in range(len(decode_list)):
        if ord(decode_list[i]) == 32: 
            lsit.append(" ")
        else : 
            lsit.append(chr(ord(decode_list[i])+n))

    decode_text = "".join(lsit)
    print(decode_text)
    return decode_text



c = convert_cipher(text)
d = decode_cipher(c)