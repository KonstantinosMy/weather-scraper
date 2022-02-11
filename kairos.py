from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier
import numpy

#ΑΡΧΙΚΟΠΟΙΗΣΗ ΜΕΤΑΒΛΗΤΩΝ
notifier = ToastNotifier()

highestTemp = 100
degreeA = 0
degreeU = 0
degreeP = 0
degreeI = 0
degreeH = 0

#ΑΠΟΘΗΚΕΥΣΗ ΑΠΑΝΤΗΣΕΩΝ ΑΠΟ ΤΑ REQUEST ΣΤΟ WEATHER.COM
responseA = requests.get('https://weather.com/el-GR/weather/tenday/l/5892dfe2c539df7d42cdbd8f9cfda434f21f6c2a63cec329fa598d4e5aa3d584')
responseU = requests.get('https://weather.com/el-GR/weather/tenday/l/4f7940e96197643c80e3c64a7d0ccb4fb6eff7bced4158152da995da08f40053')
responseP = requests.get('https://weather.com/el-GR/weather/tenday/l/a8c1d5fa8f854f3e5c626109483f1542b6eb8f29924330ccc44ffc07e3050bd7')
responseI = requests.get('https://weather.com/el-GR/weather/tenday/l/7a5351e10b7d52f667e9f0a0b71140bd176ef6cd09edf748f7e28a607baeb3e8')
responseH = requests.get('https://weather.com/el-GR/weather/tenday/l/4f3800462bc69d7213931d2a3ed41b2ea6f1e8ce1925bfdce551292d2d6fdb44')

#ΔΗΜΙΟΥΡΓΙΑ SOUPS
soupA = BeautifulSoup(responseA.content, 'lxml')
soupU = BeautifulSoup(responseU.content, 'lxml')
soupP = BeautifulSoup(responseP.content, 'lxml')
soupI = BeautifulSoup(responseI.content, 'lxml')
soupH = BeautifulSoup(responseH.content, 'lxml')

#ΑΡΧΙΚΟΠΟΙΗΣΗ ΛΙΣΤΩΝ ΠΟΥ ΘΑ ΧΡΗΣΙΜΟΠΟΙΗΣΟΥΜΕ
soupsList = [soupA, soupU, soupP, soupI, soupH]
degreeList = [degreeA, degreeU, degreeP, degreeI, degreeH]
cityList = ["ΑΘΗΝΑ", "ΘΕΣΣΑΛΟΝΙΚΗ", " ΠΑΤΡΑ", "ΙΩΑΝΝΙΝΑ", "ΗΡΑΚΛΕΙΟ"]

#ΛΗΨΗ ΕΠΙΛΟΓΩΝ ΑΠΟ ΤΟΝ ΧΡΗΣΤΗ ΚΑΙ ΔΗΜΙΟΥΡΓΙΑ ΛΙΣΤΑΣ ΜΕ ΑΥΤΕΣ
print("Παρακαλώ ορίστε για ποιές απο τις παρακάτω πόλεις θα θέλατε να λαμβάνετε ενημερώσεις:")
aRes = input("ΑΘΗΝΑ(Y/N):\n")
uRes = input("ΘΕΣΣΑΛΟΝΙΚΗ(Y/N):\n")
pRes = input("ΠΑΤΡΑ(Y/N):\n")
iRes = input("ΙΩΑΝΝΙΝΑ(Y/N):\n")
hRes = input("ΗΡΑΚΛΕΙΟ(Y/N):\n")
resList = [aRes, uRes, pRes, iRes, hRes]

#ΑΦΑΙΡΟΥΜΕ ΤΟ ΣΥΜΟΒΟΛΟ ΤΩΝ ΒΑΘΜΩΝ ΚΑΙ ΕΙΣΑΓΟΥΜΕ ΤΙΣ ΘΕΡΜΟΚΡΑΣΙΕΣ ΣΕ ΜΙΑ ΛΙΣΤΑ ΘΕΡΜΟΚΡΑΣΙΩΝ INT
for i in range (0,5):
   degreeList[i] = int(soupsList[i].select('.DailyContent--temp--3d4dn') [0].get_text().replace("°", ""))

#ΧΡΗΣΙΜΟΠΟΙΟΝΤΑΣ ΤΗΝ ΜΑΧ ΒΡΙΣΚΟΥΜΕ ΤΗΝ ΜΕΓΑΛΥΤΕΡΗ ΘΕΡΜΟΚΡΑΣΙΑ
highestTemp = max(degreeList)
#ΚΑΙ ΜΕ ΤΗΝ INDEX ΒΡΙΣΚΟΥΜΕ ΤΗΝ ΘΕΣΗ ΤΗΣ ΜΕΓΑΛΥΤΕΡΣ ΘΕΡΜΟΚΡΑΣΙΑΣ
highestTempIndex = degreeList.index(highestTemp)

print ("Η ΜΕΓΑΛΥΤΕΡΗ ΘΕΡΜΟΚΡΑΣΙΑ ΕΙΝΑΙ: ", highestTemp, '°', "ΣΤΗΝ ΠΟΛΗ: ", cityList[highestTempIndex], "\n")


#ΔΙΑΔΙΚΑΣΙΑ ΓΙΑ ΕΚΔΟΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ ΒΑΣΗ ΕΠΙΛΟΓΗΣ ΧΡΗΣΤΗY
for i in range (0,5):
    if resList[i] == "Y":
        print ("Η ΘΕΡΜΟΚΡΑΣΙΑ ΣΕ ",cityList[i]," EINAI: ",soupsList[i].select('.DailyContent--temp--3d4dn') [0].get_text())
        print ("Η ΠΙΘΑΝΟΤΗΤΑ ΒΡΟΧΗΣ ΣΕ ",cityList[i]," EINAI: ",soupsList[i].select('.DailyContent--value--37sk2') [0].get_text(),"\n")
        
        #ΔΗΜΙΟΥΡΓΙΑ WINDOWS TOAST
        notifier.show_toast(cityList[i], "ΘΕΡΜΟΚΡΑΣΙΑ: " + soupsList[i].select('.DailyContent--temp--3d4dn') [0].get_text()+ " ΠΙΘ. ΒΡΟΧΗΣ " + soupsList[i].select('.DailyContent--value--37sk2') [0].get_text())

print ("Τα δεδομένα παρέχονται απο το www.weather.com")