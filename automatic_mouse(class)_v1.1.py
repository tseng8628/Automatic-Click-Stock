import time
import pyautogui
import os
import datetime

class AutomaticClickStock():
	def __init__(self):
		today_date = ''.join(str(datetime.date.today()).split('-'))
		self.filename = today_date + '_stocklist.txt'
		self.monitor = ['250 360', '888 360', '1500 360', '2100 360', '2800 360', '3500 360', '3500 777', '2800 777', '2100 777', '1500 777', '888 777', '250 777']

	def readFile(self):
		file = open(self.filename)
		lines = file.readlines()
		updated_data = lines[0]

		return updated_data

	def automaticControl(self, nowindex, updated_data):
		pos = self.monitor[nowindex].split()
		pyautogui.moveTo(int(pos[0]), int(pos[1]), duration=0.5)
		pyautogui.click()
		pyautogui.typewrite(updated_data)
		pyautogui.press('enter')

	def main(self):
		now_index = 0
		last_data_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(self.filename).st_ctime))
		temp = ['0' for n in range(12)]

		while True:
			now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(self.filename).st_ctime))
			if now_index > 11:
				now_index = 0
			if last_data_time != now:
				updated_data = self.readFile()
				if updated_data in temp:
					continue
				else:
					self.automaticControl(now_index, updated_data)
					temp[now_index] = updated_data
					now_index += 1

				last_data_time = now

			pyautogui.FAILSAFE = True

if __name__ == '__main__':
	today_date = ''.join(str(datetime.date.today()).split('-'))
	file = today_date + '_stocklist.txt'

	if file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
		pass
	else:
		output = open(file, 'w')
		output.write('2330')
		output.close()

	a = AutomaticClickStock()
	a.main()