import re

bigMessages = []
contacts = ""
for i in fh:
    arr = i.split(',')
    regex = re.compile('[^a-zA-Z]')
    firstName = regex.sub('', arr[0])
    lastName = regex.sub('', arr[1])
    email = arr[-1].replace('\r\n','').lower()
    bigMessages.append([firstName, email])
    contacts += firstName + " " + lastName + " " + email + "\n"

fh = open('final.txt', 'w+')
emailMessage = "With that subject heading and coming from me, I am certain you are thinking this is yet another program request!\n\nBut no, not this time!  It is with mixed emotions that I am retiring from the NYPL Business Center on December 31.\n\nI will miss working with you and miss all the interesting times we had working with the public.\n\nThe Business Center intends to continue with Financial Empowerment/ Planning Programs. They are in the process of hiring a new person to assume my programming responsibilities. Until the new person is in place, the Business Center's Director, Anne Lehmann (annelehmann@nypl.org), will be your contact.\n\nI am forever grateful for all the time you so willingly contributed to the cause.\n\nBest and thank you for all your support.\n\nKathleen"
finalEmail = '----------------------------------------------------------\n\n' 
for i in bigMessages: 
    message = i[1] + '\n\n-\n\nRetirement' + '\n\n-\n\n' + i[0] + ',\n\n' + emailMessage + '\n\n----------------------------------------------------------\n\n'
    print(message)
    finalEmail += message

fh.write(finalEmail)
fh.close()




    
   