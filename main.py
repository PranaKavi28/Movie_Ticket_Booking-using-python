import datetime
import mysql.connector
import smtplib

def main():
    print("Welcome to THEATRE")
    print("Morning show - Sachin\n Afternoon show - Ghilli\n Night show - Ghost\n")

sachin_movie = 100
ghilli_movie = 130
ghost_movie = 200

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="movie_ticket_db"
)
print(mydb)

mycursor = mydb.cursor()

id = int(input("Enter your id:"))
first_name = input("Enter your name to book:")
movie_name = input("Which movie would you like to watch? (sachin/ghilli/ghost): ")
movie_ticket = "1"  
how_many = ""     

if movie_name == "sachin":
    how_many = int(input("How many tickets do you want? "))
    movie_ticket= how_many
    total = sachin_movie * how_many
    if total <= 1000:
        gst_rate = 4
        gst_price = total * 4 / 100
        net_price = total + gst_price
        print(f"GST: {gst_price}, GST Rate: {gst_rate}%")
        print(f"Total after GST: {net_price}")
        print(f" no of tickets {how_many}  one ticket cost {sachin_movie}  Total: {net_price}")
        with open("bill.txt", "w") as f:
            today = datetime.datetime.now()
            f.write(f"Your total bill as of {today}: {net_price}\n")
            print("Bill generated successfully")
            print("Sachin movie booked successfully")
            movie_time = "5 PM"
    
if movie_name == "ghilli":
    how_many = int(input("How many tickets do you want? "))
    movie_ticket= how_many
    total = ghilli_movie * how_many
    if total <= 1000:
        gst_rate = 4
        gst_price = total * 4 / 100
        net_price = total + gst_price
        print(f"GST: {gst_price}, GST Rate: {gst_rate}%")
        print(f"Total after GST: {net_price}")
        print(f" no of tickets {how_many} one ticket cost {ghilli_movie}  Total: {net_price}")
        with open("bill.txt", "w") as f:
            today = datetime.datetime.now()
            f.write(f"Your total bill as of {today}: {net_price}\n")
            print("Bill generated successfully")
            print("Ghilli movie booked successfully")
            movie_time = "2 PM"
    
if movie_name == "ghost":
    how_many = int(input("How many tickets do you want? "))
    movie_ticket= how_many
    total = ghost_movie * how_many
    if total <= 1000:
        gst_rate = 4
        gst_price = total * 4 / 100
        net_price = total + gst_price
        print(f"GST: {gst_price}, GST Rate: {gst_rate}%")
        print(f"Total after GST: {net_price}")
        print(f" no of tickets {how_many}  one ticket cost {ghost_movie} Total: {net_price}")
        with open("bill.txt", "w") as f:
            today = datetime.datetime.now()
            f.write(f"Your total bill as of {today}: {net_price}\n")
            print("Bill generated successfully")
            print("Ghost movie booked successfully")
            movie_time = "11 AM"
    
sql = "insert into  movie_ticket_db (id, first_name, movie_name, movie_ticket) values (%s, %s, %s, %s)"
val = (id, first_name, movie_name, movie_ticket)

mycursor.execute(sql, val)
mydb.commit()
print("You have booked a movie successfully")

mail_id = input("Enter your mail id: ")

try:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("hello@gmail.com", "password")
    message = (f" ur total bill is  for movie ticket {net_price}")
    s.sendmail("hello@gmail.com", mail_id, message)
    print(f"Mail sent successfully to {mail_id}")
    s.quit()

except :
    print( "mail not sent")


