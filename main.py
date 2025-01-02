# Step 1 : importing important lib or modules
from twilio.rest import Client
from datetime import datetime,timedelta
import time
from secure import account_sid,auth_token

# Step 2 : setting up twilio client help us to send message

client = Client(account_sid,auth_token)


# Step 3 : designing a function which will send message

def send_message(recieverNumber,messageBody):
    try:
        message = client.messages.create(
        from_= 'whatsapp:+14155238886',
        body = messageBody , 
        to = f'whatsapp:{recieverNumber}'

        )
        print("Message send succesfully . ")
    except Exception as e:
        print(f"An error occurs {e}")


#Step 4 : Taking user inputs
name = input('Enter recievers name : ')
recieverNumber = input("Enter reciver's whatsapp number with country code : ")
message = input(f'Enter the message you want to send to {name} : ')

#Step 5 : Inputing time and scheduling it to send message on that date and time 

date_str = input('Enter date you want tp send message in format(YYYY-MM-DD) :')
time_str = input('Enter time you want to send message in format(HH-MM  24 hours) : ')


#datetime module usage
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_time = datetime.now()

#calculate delay
time_diff = schedule_datetime - current_time
delaySeconds = time_diff.total_seconds()

#logic of sending message  : 
if delaySeconds<=0 :
    print("Message can't be send please enter future date time .")
else :
    print(f'Message scheduled for {name} at {schedule_datetime} ...')

    #time sleep for delayed seconds
    time.sleep(delaySeconds)

    #sending message after dealyed time 
    send_message(recieverNumber,message)
