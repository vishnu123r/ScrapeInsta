import re
from validate_email import validate_email

def get_email(text):
    """
    
    Extracts email from text

    """
    if not text:
        return
    text = remove_emoji(text) #remove emoji
    email_gen = re.finditer(r"[\w\.-]+@[\w-]+\.[\w\.-]+", text) 
    if email_gen:
        email_array = [email.group(0) for email in email_gen if validate_email(email.group(0))]
        return email_array
    return


def remove_emoji(input_string):
    """
    
    Removes all emoji  from text
    
    """
    try:
        # Wide UCS-4 build
        myre = re.compile(u'['
                          u'\U0001F300-\U0001F64F'
                          u'\U0001F680-\U0001F6FF'
                          u'\u2600-\u26FF\u2700-\u27BF]+',
                          re.UNICODE)
    except re.error:
        # Narrow UCS-2 build
        myre = re.compile(u'('
                          u'\ud83c[\udf00-\udfff]|'
                          u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
                          u'[\u2600-\u26FF\u2700-\u27BF])+',
                          re.UNICODE)
    # replacing with empty space here due to emojis often being connected to next character
    return(myre.sub(r' ', input_string))



def get_phone (text):
    """
    Extracts Phone number from text

    """
    if not text:
        return
    text = remove_emoji(text)
    phone_gen = re.finditer("\(?\d{3}[-.)\s]{0,2}(\d{4}\s|\d{3}[\s\-.]?\d{4}\s)", text)
    if phone_gen:
        phone_array = [phone.group(0).strip() for phone in phone_gen]
        return phone_array
    return
