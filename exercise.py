## <u>**Exercise**</u>
# **Task: Create your own App**
# Build a Contact Info Collector using `st.form`.
# Specifications:
# - Use `st.form(key = "my_form")` as a context manager (visit https://docs.streamlit.io/ to see how to use `st.form()`).
# - Inside the form, collect:
#     - First Name (`st.text_input`)
#     - Last Name (`st.text_input`)
#     - Favourite Number (`st.number_input`)
# - Use `st.form_submit_button("Register")`.
# - Validation: When clicked, check if First Name and Last Name are not empty strings.
# - Output: If valid, write the data to a file called `contacts.csv` (append mode). Display `st.success`.
# - Display: Show the `contacts.csv` contents as a table below the form.

import streamlit as st
import csv
import pandas as pd

contact_data = [
  ["First Name", "Last Name", "Favourite Number"]
]

st.title("Contact Info Collector")

contact_info = st.form(key="my_form")

contact_info.header("Insert your contact information below")
first_name = contact_info.text_input("Enter your first name: ")
last_name = contact_info.text_input("Enter your last name: ")
fav_num = contact_info.number_input("Enter your favourite number: ")

contact_info.form_submit_button("Register")

if len(first_name.strip()) == 0:
  st.error("First name cannot be empty")
elif len(last_name.strip()) == 0:
  st.error("Last name cannot be empty")
elif len(first_name.strip()) > 0 and len(last_name.strip()) > 0:
  contact_data.append([first_name, last_name, fav_num])

  contact_info.success("Your contact information is saved! Please review your information is correct below")
  contact_info.info(f"First Name: {first_name}, Last Name: {last_name}, Favourite Number: {fav_num}")

  with open("contacts.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(contact_data)

  df = pd.read_csv("contacts.csv")
  st.dataframe(df)
  
