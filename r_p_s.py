import random
import string
computer = random.choice(['剪刀', '石頭', '布']) #指定字串隨機
while True:
	gesture = input('請出拳！剪刀、石頭、布： ')
	if gesture == computer:
		print(computer)
		print('平手！再試一次！')
		continue

	elif gesture == '石頭':
		print('電腦出',computer)
		
		if computer == '布':
			print('你輸了！')
			break
		elif computer == '剪刀':
			print('你贏了！')
			break
	
	elif gesture == '布':
		print('電腦出',computer)

		if computer == '剪刀':
			print('你輸了！')
			break
		elif computer == '石頭':
			print('你贏了！')
			break

	elif gesture == '剪刀':
		print('電腦出',computer)

		if computer == '石頭':
			print('你輸了！')
			break
		elif computer == '布':
			print('你贏了！')
			break

