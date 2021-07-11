driving = input('請問你有沒有開過車(請回答有或沒有):')
if driving != '有' and driving != '沒有':
	print('不好意思，本問卷只能輸入「有」或「沒有」！')
	raise SystemExit
	
age = input('那請問您的年齡是？：')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過測驗了！')
	else:
		print('奇怪了，你怎麼會開過車？本局將3分鐘後抵達您的家門口！')
elif driving == '沒有':
	if age >= 18:
		print('你怎麼不想考駕照勒？')
	else:
		print('沒關係，長大後再開知道嗎～？')
