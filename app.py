import streamlit as st
import random
import string 

st.title("🔐 PASSWORD GUARDIAN")
st.caption("Analyze password strength and generate secure passwords.")

st.write("Welcome to Password Guardian")
st.header("🔍 Password Analyzer")
password = st.text_input("Enter your Password:", type ="password")

if st.button("Analysed password"):
    
    
    length = len(password)
    st.write(f"length of password: {length}")
    
    score = 0
    
    if length >=8 :
        st.success("✅ password length is good")
        score+=1
    else:
        st.error("❌ password has some error")


    uppercase_found = False
    for char in password:
        if char.isupper():
            uppercase_found = True
            score+=1
            break
        
    if uppercase_found:
        st.success("🔐Password has a upper character ✅")
    else:
        st.error("🔐Your password doesn't have upper character❌")
    
    
    lowercase_found = False
    for char in password:
        if char.islower():
            lowercase_found = True
            score+=1
            break
    
    if lowercase_found:
        st.success("🔐Password has a lower character ✅")
    else:
        st.error("🔐Your password doesn't have lower character❌")
    
    
    digit_found = False
    for num in password:
        if num.isdigit():
            digit_found = True
            score+=1
            break
        
    if  digit_found:
        st.success("🔐Password has a digit  ✅")
    else:
        st.error("🔐Your password doesn't have digit❌")
        
    special_found = False
    for char in password:
        if not char.isupper() and not char.islower() and not char.isdigit():
                special_found = True
                score+=1
                break  
        
    if special_found:
        st.success("🔐Password has a special character ✅")
    else:
        st.error("🔐password does not have a special character ❌")
        
##password strength  
    st.write(f"###score:{score}/5")
    st.progress(score/5)
        
    if score == 5:
            st.success("🟢 The password is strong")
    elif score== 3 or score == 4:
            st.success("🟡 The password is medium")
    else:
            st.success("🔴 The password is too weak")  
    
##password imporvement tip
    if score < 5:
        st.subheader("💡 Tips to Make Your Password Stronger")

    if length < 8:
        st.write("• Make your password at least 8 characters long.")

    if not uppercase_found:
        st.write("• Add at least one uppercase letter (A-Z).")

    if not lowercase_found:
        st.write("• Add at least one lowercase letter (a-z).")

    if not digit_found:
        st.write("• Include at least one number (0-9).")

    if not special_found:
        st.write("• Add at least one special character (!@#$%^&*).")
        
st.divider()           
st.header("🔑 Password Generator")
generator_length = st.slider(
    "length of the password",
    min_value=8,
    max_value=32,
    value=12
)
include_uppercase = st.checkbox("Included upper case", value=False)
include_lowercase = st.checkbox("Included lower case" , value=True)
include_digit = st.checkbox("Included numbers",value=True)
include_special = st.checkbox("Included special character",value=True)
exclude_ambiguous= st.checkbox("exculded ambiguous",value=False)

char=""

if include_uppercase:
    char += string.ascii_uppercase
if include_lowercase:
    char += string.ascii_lowercase
if include_digit:
    char += string.digits
if include_special:
    char +=string.punctuation
if exclude_ambiguous:
    for ch in "0oIL1":
        char = char.replace(ch,"")
    
    
if st.button("Generate Password"):
    if char:
        generated_password=""
        for _ in range(generator_length):
            generated_password += random.choice(char)
            st.success("The Password is generated")
            st.code(generated_password)
    else:
        st.error("Please select atleast one character type")
        
        
st.divider()
st.caption("🔐 Password Guardian | Built with ❤️ using Python & Streamlit")
