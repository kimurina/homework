#_*_coding:utf-8_*_
import os
os.environ['PYTHON_EGG_CACHE'] = '/home/hosting_users/naancoco/tmp'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="naancoco", passwd="ghghgh246", 
			db = "naancoco", charset = "utf8")

print("connection!")

curs = conn.cursor()

sql = "select * from USER"
curs.execute(sql)

data = curs.fetchall()
#print(data)

for i in data:
    user_email = i[1]
    user_calories_need = int(i[7])
    user_carbo_need_min = int(i[8])
    user_carbo_need_max = int(i[9])
    user_protein_need = int(i[10])
    user_sugar_need = int(i[11])
    user_fat_need_min = int(i[12])
    user_fat_need_max = int(i[13])
    user_natrium_need = int(i[14])
    user_cholesterol_need = int(i[15])
    user_saturated_fatty_need = int(i[16])
    user_unsaturated_fatty_need = int(i[17])
    
sql_food ="select * from FOOD"
curs.execute(sql_food)
row=curs.fetchall()
#food_category dictionary is empty
food_category={}
#food db에서 식품군의 이름을 food_category의 key로 사용.각각의 value는 0으로 초기화 시킴.
for i in row:
    val=i[0]
    #가장 처음에 값이 들어가는 상황.
    if len(food_category.items())==0:
            food_category[val]=0
    else:
    #그다음부터 값이 들어가는 상황.
        #if val in food_category:
        if food_category.has_key(val) ==False:
            food_category[val]=0
#for k,v in food_category.items():
#    print(k,v)
sql1 = "select * from MENU"
curs.execute(sql1)

data1 = curs.fetchall()
#print(data1)

for i in data1:
    bre_category=i[2]
    bre_calories= i[3]
    bre_carbo = i[5]
    bre_protein = i[6]
    bre_sugar = i[8]
    bre_fat = i[7]
    bre_natrium = i[9]
    bre_cholesterol = i[10]
    bre_saturated = i[11]
    bre_unsaturated = i[12]
#bre_category에 해당에하는 key를 가진 food_category의 value값을 증가시켜준다.     
    if bre_category in food_category.keys():
        food_category[bre_category]=food_category[bre_category]+1
#########################################추가######################################
#lambda는 sort를 해주는 역할.나중에 마지막 column을 선택해서 추천해주면 된다.

cat_list=[]
for k,v in sorted(food_category.items(),key=lambda food_category:food_category[1]):
    if v!=0:
        print(k,v)
        cat_list.append(k)
#그럼 cat_list의 마지막 순서에 있는 food_category가 가장 많은 횟수로 섭취한 상황#
use_cat=cat_list[len(cat_list)-1]
######print(use_cat)
#######################################################################################
calories = bre_calories
carbo = bre_carbo
protein = bre_protein
sugar = bre_sugar
fat = bre_fat
natrium = bre_natrium
cholesterol = bre_cholesterol
saturated = bre_saturated
unsaturated = bre_unsaturated


if calories < user_calories_need:
    calories_result = user_calories_need - calories
    calories_choice = "small"
else:
    calories_result = calories - user_calories_need
    calories_choice = "excessive"
    
if carbo < user_carbo_need_min:
    carbo_result = user_carbo_need_min - carbo
    carbo_choice = "small"
elif user_carbo_min < carbo < user_carbo_need_max:
    carbo_result = carbo
    carbo_choice = "appropriate"
elif carbo > user_carbo_need_max:
    carbo_result = carbo - user_carbo_need_max 
    carbo_result = "excessive"
    
if protein < user_protein_need:
    protein_result = user_protein_need - protein
    protein_choice = "small"
else:
    protein_result = protein - user_protein_need
    protein_choice = "excessive"

if sugar < user_sugar_need:
    sugar_result = user_sugar_need - sugar
    sugar_choice = "small"
else:
    sugar_result = sugar - user_sugar_need
    sugar_choice = "excessive"

if fat < user_fat_need_min:
    fat_result = user_fat_need_min - fat
    fat_choice = "small"
elif user_fat_need_min < fat < user_fat_need_max:
    fat_result = fat
    fat_choice = "appropriate"
elif fat > user_fat_need_max:
    fat_result = fat - user_fat_need_max
    fat_choice = "excessive"

if natrium < user_natrium_need:
    natrium_result = user_natrium_need - natrium
    natrium_choice = "appropriate"
else:
    natrium_result = natrium - user_natrium_need
    natrium_choice = "excessive"

if cholesterol < user_cholesterol_need:
    cholesterol_result = user_cholesterol_need - cholesterol
    cholesterol_choice = "appropriate"
else:
    cholesterol_result = cholesterol - user_cholesterol_need
    cholesterol_choice = "excessive"

if saturated < user_saturated_fatty_need:
    saturated_result = user_saturated_fatty_need - saturated
    saturated_choice = "appropriate"
else:
    saturated_result = saturated - user_saturated_fatty_need
    saturated_choice = "excessive"


sql4 = "update user_result set carbo = %d, carbo_result = '%s', protein = %d, protein_result = '%s', sugar = %d, sugar_result = '%s', fat = %d, fat_result = '%s', natrium = %d, natrium_result = '%s', cholesterol = %d, cholesterol_result = '%s', saturated = %d, saturated_result = '%s', calories = %d, calories_result = '%s' where user_email = '%s'" %(carbo_result, carbo_choice, protein_result, protein_choice, sugar_result, sugar_choice, fat_result, fat_choice, natrium_result, natrium_choice, cholesterol_result, cholesterol_choice, saturated_result, saturated_choice, calories_result, calories_choice, user_email) 
curs.execute(sql4)

sql_u = "select * from user_result"
curs.execute(sql_u)

data_u = curs.fetchall()
#print(data3)

for i in data_u:
    user_choice=i[15]
    food_choice=i[18]

##############################추가:영양소들의 부족################################################


sql_food ="select * from FOOD"
curs.execute(sql_food)
row=curs.fetchall()
for i in row:
#val:식품군이름
    ################# val=i[0]
    #최다 식품군과 일치시
    if (i[0]==use_cat):
        if user_choice=='carbo':
            #부족할 경우
            if carbo_choice=='small':
                #반찬일 경우,
                if food_choice=='side':
                    if i[4]*4>user_carbo_need_min/10 + carbo_result/10:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='e'                        
                                              
                #한끼음식일 경우
                elif food_choice=='meal':
                    print("executing")
                    if i[4]*4>user_carbo_need_min/3+ carbo_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break                        
                    else:
                        reco=i[1]
                        reco_amount='e'
                        break
                        
            #과다할 경우
            elif carbo_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[4]*4<user_carbo_need_max/10 - carbo_result/10:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                       
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[4]*4<user_carbo_need_max/3 - carbo_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                
        elif user_choice=='protein':
            #부족할 경우
            if protein_choice=='small':
                #반찬일 경우,
                if food_choice=='side':
                    if i[5]>user_protein_need/10 + protein_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='e'
                        break
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[5]>user_protein_need/3+ protein_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='e'
                        break                                                
            #과다할 경우
            elif protein_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[5]<user_protein_need/10 - protein_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[5]<user_protein_need/3- protein_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                                                
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                    
        elif user_choice=='fat':
             #부족할 경우
            if fat_choice=='small':
                #반찬일 경우,
                if food_choice=='side':
                    if i[6]*9>user_fat_need_min/10 + fat_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='e'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[6]*9>user_fat_need_min/3+ fat_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='e'
                        break                                               
            #과다할 경우
            if fat_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[6]*9<user_fat_need_max/10 + fat_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[6]*9<user_fat_need_max/3+ fat_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                                                
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break
                    
        elif user_choice=='sugar':
            #과다할 경우
            if sugar_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[7]*4<user_sugar_need/10 - sugar_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[7]*4<user_sugar_need/3 - sugar_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break
                
        elif user_choice=='natrium':
            #과다할 경우
            if natrium_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[8]<user_natrium_need/10 - natrium_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[8]<user_natrium_need/3- natrium_result/3:                        
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                        
                
        elif user_choice=='cholesterol':
            #과다할 경우
            if cholesterol_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[9]<user_cholesterol_need/10 - cholesterol_result/10 :
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[9]<user_cholesterol_need/3- cholesterol_result/3:
                        reco=i[1]
                        reco_amount='a'
                        break
                                                
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                
        elif user_choice=='saturated':
            #과다할 경우
            if saturated_choice=='excessive':
                #반찬일 경우,
                if food_choice=='side':
                    if i[10]*9<user_fat_need_max/10 + fat_result/10:
                        reco=i[1]
                        reco_amount='a'
                        break
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break                                                
                #한끼음식일 경우
                elif food_choice=='meal':
                    if i[10]*9<user_fat_need_max/3+ fat_result/10:
                        reco=i[1]
                        reco_amount='a'
                        break
                             
                    else:
                        reco=i[1]
                        reco_amount='s'
                        break
sqlr = "update set user_result recommended_food = %s where user_email = '%s'" %(reco, user_email)
curs.execute(sqlr)

sqlra = "update set user_result reco_amount = '%s' where user_email = '%s'" %(reco_amount, user_email)
curs.execute(sqlra)


















