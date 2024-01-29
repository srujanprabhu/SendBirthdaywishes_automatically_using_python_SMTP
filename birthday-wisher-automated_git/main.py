
import pandas as pd
import pyarrow
import datetime
import random
import smtplib
MY_EMAIL = "" #your mail id
password = "" #your password
df = pd.read_csv("birthdays.csv")
today_date = datetime.datetime.now().date()
# Get the day and month
day_month = today_date.strftime("%d-%m")
# Print day and month
#print("Day and Month:", day_month)
year_col = "year"
mon_col = "month"
day_col = "day"
df["combined_column"] = df[day_col].astype(str).str.zfill(2) + '-' +df[mon_col].astype(str).str.zfill(2)
#print(df)
lett = ["letter_1.txt","letter_2.txt","letter_3.txt"]
randletter = random.choice(lett)
for i in df["combined_column"]:
    if i == str(day_month):
        with open(file=f"letter_templates/{randletter}" ,mode="r") as file:
            names_change = file.readlines()
            old_name = "[NAME]"
            row = df.loc[df["combined_column"] == i]
            new_name = row['name'].values[0]
            #print(new_name)
            modified_list = [item.replace(old_name,new_name) for item in names_change]
            #print(modified_list)
            email_body = ''.join(modified_list)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_EMAIL,password)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="srujanprabhu18@gmail.com",
                    msg=f"Subject: Happy Birthday\n\n{email_body}"
                )

                print(f"it's birthdy of {new_name}")
                print("Emailsent")
    else:
        pass
        #print("No birthday today")
