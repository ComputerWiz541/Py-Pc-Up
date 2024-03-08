from twilio.rest import Client
import datetime

current_time = datetime.datetime.now()

account_sid = 'AC4b5d83151fb727c05ba004bc80aa5079'
auth_token = '70bbe6c530f21591f1df0c68f5d12236'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18773725530',
    body=f'PC Has Been Turned On at   Time: {current_time.hour}:{current_time.minute}:{current_time.second}   Date: {current_time.day}/{current_time.month}/{current_time.year}',
    to='+14707725225'
)

print(f"{message.sid} at   Time: {current_time.hour}:{current_time.minute}:{current_time.second}   Date: {current_time.day}/{current_time.month}/{current_time.year}")
with open('logs.txt', 'a') as file:
    file.write(f"{message.sid} at   Time: {current_time.hour}:{current_time.minute}:{current_time.second}   Date: {current_time.day}/{current_time.month}/{current_time.year}\n")

try:
    with open(r'\\10.0.0.42\Dataset_1\Pc Up Logs\logs.txt', 'a') as file:
        file.write(f"{message.sid} at   Time: {current_time.hour}:{current_time.minute}:{current_time.second}   Date: {current_time.day}/{current_time.month}/{current_time.year}\n")
except Exception as e:
    with open('logs.txt', 'a') as log_file:
        log_file.write(f"NAS LOGGING FAILED: {e}\n")

