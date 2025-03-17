def convert_cipher(text,shift):
    cipher_text = "".join(
        char if char == " " else chr(ord(char)+shift) for char in text
    )
    return cipher_text


def decode_cipher(text,shift):
    decoded_text = "".join(
        char if char == " " else chr(ord(char)-shift) for char in text
    )
    return decoded_text




text = '''I am a Data Analyst with expertise in Power BI, Tableau, SQL, Python, and Excel. I have hands-on experience in analyzing and visualizing data to drive business insights. My background includes a B.Sc. in Computer Science and I am currently pursuing an MCA from UIT RGPV Bhopal.
I have worked on real-world projects like IPL Analysis, Promotion Analysis for Atliq Mart, Business 360 for Brick & Mortar & Ecommerce, and more. Additionally, I actively contribute to data analytics communities, assisting learners and solving analytical problems.
Currently, I am also expanding my knowledge in Machine Learning and working on a Predictive Maintenance API for the telecom industry using FastAPI and ML.
Apart from my analytical skills, I have a passion for music I play the flute, synthesizer, and guitar and enjoy singing.
I aim to leverage data analytics to enhance business profitability and eventually establish my own venture. '''

cipher = convert_cipher(text,5)
print(cipher)
print("\n\n")
decoded = decode_cipher(cipher,5)
print(decoded)