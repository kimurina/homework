import os
os.environ['PYTHON_EGG_CACHE'] = '/home/hosting_users/naancoco/tmp'
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="naancoco", passwd="ghghgh246", 
			db = "naancoco",charset ="utf8")

print("connection!")

curs = conn.cursor()

sql = "select * from USER"
curs.execute(sql)

data = curs.fetchall()
print(data)

for row in data:
	
    height = row[4]
    weight = row[5]
    sex = row[2]
    
    bmi = int(weight)/((float(height)/100)*(float(height)/100))
	
    if bmi < 18.5:
        case = 0
    elif 18.5 <= bmi <22.9:
        case = 1
    elif 23 <= bmi <24.9:
        case = 2
    elif 25 <= bmi:
        case = 3

    if sex == 'man':
        std_weight = ((float(height)/100)**2)*22
        print('standard_weight: %.2f' %std_weight)
    elif sex == 'woman':
        std_weight = ((float(height)/100)**2)*21
        print('standard_weight: %.2f' %std_weight)

    if case == 0:
        calories_need = std_weight*40
        print('calories_per_day: %.2f' %calories_need)
    elif case == 1:
        calories_need = std_weight*35
        print('calories_per_day: %.2f' %calories_need)
    elif case == 2:
        calories_need = std_weight*32.5
        print('calories_per_day: %.2f' %calories_need)
    elif case == 3:
        calories_need = std_weight*30
        print('calories_per_day: %.2f' %calories_need)
		
    carbo_need_min = calories_need * 0.55
    carbo_need_max = calories_need * 0.65
    print('carbohydrate: %2.f ~ %2.f' %(carbo_need_min,carbo_need_max))
	
    if sex == 'man':
	if 6 <= int(row[3]) <= 8:
	    protein_need = 30
        elif 9 <= int(row[3]) <= 11:
            protein_need = 40
        elif 12 <= int(row[3]) <= 14:
            protein_need = 55
        elif 15 <= int(row[3]) <= 29:
            protein_need = 65
        elif 30 <= int(row[3]) <= 64:
            protein_need = 60
        elif int(row[3]) >= 65:
            protein_need = 55
    elif sex == 'woman':
        if 6 <= int(row[3]) <= 8:
            protein_need = 25
        elif 9 <= int(row[3]) <= 11:
            protein_need = 40
        elif 12 <= int(row[3]) <= 18:
            protein_need = 50
        elif 19 <= int(row[3]) <= 29:
            protein_need = 55
        elif 30 <= int(row[3]) <= 64:
            protein_need = 50
        elif int(row[3]) >= 65:
            protein_need = 45
   
    print('protein: %d(g)' %protein_need)
	
    sugar_need = calories_need * 0.1
    print('sugar < %2.f' %sugar_need)
    
    fat_need_min = calories_need * 0.15
    fat_need_max = calories_need *0.3
    print('fat: %2.f ~ %2.f' %(fat_need_min, fat_need_max))
    
    natrium_need = 2000
    print('natrium: 2000mg')
	
    cholesterol_need = 300
    print('cholesterol_need: 300mg')
	
    saturated_fatty_need = calories_need * 0.07
    print('saturated_fatty_acid < %2.f' %saturated_fatty_need)
	
    unsaturated_fatty_need = calories_need * 0.01
    print('unsaturated_fatty_acid < %2.f' %unsaturated_fatty_need)
 	
    sql1 = "update USER set calories_need = %2.f, carbo_need_min = %2.f, carbo_need_max = %2.f, protein_need = %2.f, sugar_need = %2.f, fat_need_min = %2.f, fat_need_max = %2.f, natrium_need = %2.f, cholesterol_need = %2.f, saturated_fatty_need = %2.f, unsaturated_fatty_need = %2.f where USER_EMAIL = '%s'" %(calories_need, carbo_need_min, carbo_need_max, protein_need, sugar_need, fat_need_min, fat_need_max, natrium_need, cholesterol_need, saturated_fatty_need, unsaturated_fatty_need, row[1])
    curs.execute(sql1)

conn.commit()
