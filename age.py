driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有/沒有')
	raise SystemExit 

age = input('請問你今年幾歲?')
age = int(age)
if driving == '有':
	if int(age)>= 18:
		print('你通過測驗了')
	else:
		print('偷開車, 抓')
elif driving == '沒有':
	if age >= 18:
		print('可以去考駕照拉')
	else:
		print('再等一下就可以考駕照了!')
else:
	print('只能輸入有或沒有')
