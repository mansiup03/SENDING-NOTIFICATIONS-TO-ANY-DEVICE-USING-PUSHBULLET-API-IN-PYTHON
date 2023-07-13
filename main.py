print("---------INTERNSHIP PROJECT----------\n"
      "------SENDING NOTIFICATIONS TO A DEVICE USING PUSHBULLETS IN PYTHON------\n"
      "------By Mansi Upadhyay ")

import requests, json

def push_notification(title, msg, email):
     endpoint = "https://api.pushbullet.com/v2/pushes"

     headers = {"Content-Type" : "application/json",
                "Access-Token" : "o.IbO9dQguEkY5CPIbHT3qPBuGN5wF3g1e"}

     data = { "type" : "note" ,
              "title" : title ,
              "body" : msg ,
              "email" : email}

     res = requests.post(url = endpoint, data = json.dumps(data), headers = headers)
     print(res.content)

push_notification(email = "purnimafag2010@gmail.com", title= "Hello there!", msg= "How are you'?")
