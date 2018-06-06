import csv
import os

def degreeEnglish(p):
	if p == "M 碩士班":
		return "Master"
	elif p == "B 四技":
		return "4 Bachelor"	
	elif p =="C 二技":
		return "2 Bachelor"	
	elif p =="D 博士班":
		return "Doctor"	
	elif p =="C 二技":
		return "2 Bachelor"	
	elif p == "B 學士班": 
		return "Bachelor"
	elif p == "2 二專":
		return "2 Associate"
	elif p == "5 五專":
		return "5 Associate"
	else:
		return "others"

path = './data/'
save_path = './handle_data/'

fileName = input("請輸入檔名:")
fileName_read = os.path.join(path,fileName)
reader = open(fileName_read,"r",encoding='utf-8')
fileName_write = os.path.join(save_path,fileName)
write = open(fileName_write,'w',newline='',encoding='utf-8')

reader.readline()

header = ['學校類別','設立別','學校名稱','日間/進修','學制別','新生註冊率']

rows = csv.reader(reader)
writer = csv.writer(write)
writer.writerow(header)
write_data = []

for row in rows:
	deal_data = []

	deal_data.append(row[1])
	deal_data.append(row[2])
	deal_data.append(row[3][5:])
	deal_data.append(row[4])
	deal_data.append(degreeEnglish(row[5]))
	deal_data.append(row[6])

	write_data.append(deal_data)

for i in write_data:
	writer.writerow(i)

reader.close()
write.close()