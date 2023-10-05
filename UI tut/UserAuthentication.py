import smtplib, random
from email.message import EmailMessage
def pass_gen()-> int:
    password = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return password
verification_Code = pass_gen()
def Send_Email(reciver:str , verification_Code:int):
    email_sender = "sup.Plonom@gmail.com"
    email_password = ""
    email_reciver = reciver
    subject = "Your verification code in Plonom"
    body = f"""
Hello dear , Your verification code in Plonom is 

{verification_Code}


As a rule, if this request is not from you, you can easily ignore it



Plonom Messanger 2023
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_reciver
    em["Subject"] = subject
    em.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())

#Send_Email("Anbarloo@protonmail.com", verification_Code=verification_Code)
