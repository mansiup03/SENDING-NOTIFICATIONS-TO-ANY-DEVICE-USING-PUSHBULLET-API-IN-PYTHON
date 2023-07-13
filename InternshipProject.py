print("---------INTERNSHIP PROJECT----------\n"
      "------SENDING NOTIFICATIONS/TEXT TO A DEVICE USING PUSHBULLETS IN PYTHON------\n"
      "------By Mansi Upadhyay ")
import requests
import pushbullet

class Pushbullet:
    URL =  "https://api.pushbullet.com/v2/pushes"

#Sending a text message in Pushbullet:

    def push_note(self, title, msg, email):
            data = {"type" : "note", "title" : title, "body" : msg, "email" : email}
            headers = {"Content-Type" : "application/json",
                       "Access-Token" : "o.jKqqNz59aQCjQ3UtviKsRMXSNL7T6oO6"}
            res = requests.post(url = self.URL, json=data, headers = headers)
            return res.json()

#Sending a link in Pushbulllet:

    def push_link(self, title, msg, link, email):

           data = {"type" : "link", "title" : title, "body" : msg, "url" : link, "email" : email}
           headers = {"Content-Type" : "application/json",
                      "Access-Token" : "o.jKqqNz59aQCjQ3UtviKsRMXSNL7T6oO6"}

           res = requests.post(url = self.URL, json=data, headers=headers)
           return res.json()

 #Pushing a file in Pushbullet:

    file = pushbullet.Pushbullet("o.jKqqNz59aQCjQ3UtviKsRMXSNL7T6oO6")
    f = open("C:/Users/MansiUpadhyay/OneDrive/Desktop/Space.png", "rb")
    params = file.upload_file(f, "Picture.png")
    print(params)
    file.push_file(**params, email = "purnimafag2010@gmail.com")

p1 = Pushbullet()

res1 = p1.push_note("Pushbullet using Python", "Hello!", email = "purnimafag2010@gmail.com")
print(res1)

res2 = p1.push_link("Pushbullet using Python", "Hello!", link = "https://www.google.com", email = "purnimafag2010@gmail.com")
print(res2)

#-------------------------End of the Project--------------------------------------------#




