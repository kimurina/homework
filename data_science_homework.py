import numpy as np
from sklearn import tree
from sklearn import svm
from sklearn import linear_model
from sklearn import neighbors
from sklearn.model_selection import train_test_split

while True:
	print('[ Student ID: 1315872 ]\n[ Name: 김유리나 ]\n')
	print('1. Predict wine quality\n2. Quit\n')
	menu = int(input('> '))
	if menu == 1:
		print('\nInput the values of a wine:')
		fixed_acidity = float(input('1. fixed acidity: '))
		volaile_acidity = float(input('2. volatile acidity: '))
		citric_acid = float(input('3. citric acid: '))
		residual_sugar = float(input('4. residual sugar: '))
		chlorides = float(input('5. chlorides: '))
		free_sulfur_dioxide = float(input('6. free sulfur dioxide: '))
		total_sulfur_dioxide = float(input('7. total sulfur dioxide: '))
		density = float(input('8. density: '))
		pH = float(input('9. pH: '))
		sulphates = float(input('10. sulphates: '))
		alcohol = float(input('11. alcohol: '))
		print()
		
		data = np.genfromtxt('winequality-red.csv',dtype = np.float32,delimiter = ";",skip_header = 1)
					  
		x = data[:, 0:11]
		y = data[:, 11]

		test_sample = [[fixed_acidity, volaile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]

		def predict(classifier):
			predicted_class = classifier.predict(test_sample)
			return predicted_class
	
		classifier_1 = (tree.DecisionTreeClassifier(random_state = 0)).fit(x, y)
		predicted_class_1 = predict(classifier_1)
		classifier_2 = (svm.SVC(random_state = 0)).fit(x, y)
		predicted_class_2 = predict(classifier_2)
		classifier_3 = (linear_model.LogisticRegression(random_state = 0)).fit(x, y)
		predicted_class_3 = predict(classifier_3)
		classifier_4 = (neighbors.KNeighborsClassifier(n_neighbors = 5)).fit(x, y)
		predicted_class_4 = predict(classifier_4)

		print('Predicted wine quality:')
		print('1. Decision tree: %d' %predicted_class_1)
		print('2. Support vector machine: %d' %predicted_class_2) 
		print('3. Logistic regression: %d' %predicted_class_3) 
		print('4. k-NN classifier: %d\n' %predicted_class_4)
	
	elif menu == 2:
		break
		
	


