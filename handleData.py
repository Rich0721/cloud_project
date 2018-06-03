import csv
import os

def StudentNumber(p):
	sum = 0
	for i in range(4,20):
		sum += int(p[i])
	return sum

def degreeEnglish(p):
	if p == "M 碩士":
		return "Master"
	elif p == "B 四技":
		return "4 Bachelor"	
	elif p =="C 二技":
		return "2 Bachelor"	
	elif p =="D 博士":
		return "Doctor"	
	elif p =="C 二技":
		return "2 Bachelor"	
	elif p == "B 學士": 
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

csv_header = ['學校代碼','學校名稱','日間∕進修別','等級別','學生數']

rows = csv.reader(reader)
writer = csv.writer(write)
writer.writerow(csv_header)
write_data = []

for row in rows:
	data =[]
	for i in range(0,3):
		data.append(row[i])
	data.append(degreeEnglish(row[3]))
	data.append(StudentNumber(row))
	write_data.append(data)

for i in write_data:
	writer.writerow(i)

reader.close()
write.close()