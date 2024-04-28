#mohammadreza mohammadi
dic = {'a' :[]  , 'b' : []  ,  'c' :[] ,   'd':[] }

lie_counter=0

for key in dic.keys():
	
	for j in range(3):
		x = input(f' person {key} .... sentence number {j+1}.... is truth or lie:  ')
		if x == 'truth' :
			dic[key].append(True)
		
		elif x=='lie':
			dic[key].append(False)
			lie_counter +=1
		else:
			print('incorrect input.... and it concedered as a lie ')
			dic[key].append(False)
			lie_counter +=1
	
if lie_counter != 6 :
	print('the amount of lie is not 6 .... so you are wrong')
	exit
 

for key,value in dic.items():
	if any(value):
		print(f"{key} is not robber")
	else: 
	    print(f"{key} is the Robber")