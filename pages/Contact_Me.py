import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="form"):
    email_address = st.text_input("Please enter your email address: "
                                  "That does not automatically send you any confirmation "
                                  "email but sends your email address to me as part of your message. "
                                  "As soon as I know I received the message, I'll respond to you!")
    raw_message = st.text_area("Your message:")
    message = f"""\
    Subject: New email from {email_address}
    
    From: {email_address}
    {raw_message}
    """
    submit_button = st.form_submit_button("Submit")
    print(submit_button)

    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully.")

