import random
star = input('請設定隨機範圍開始值')
end = input('請設定隨機範圍結束值')
star = int(star)
end = int(end)
r = random.randint(star, end)#逗號後空白鍵
count = 0
while True:
	count = count + 1
	num = input('請輸入密碼: ')
	num = int(num)
	if num == r:
		print('終於猜對了!')
		break
	elif num > r:
		print('比答案大')
	elif num <r:
		print('比答案小')
	print('這是你猜的第', count, '次')
