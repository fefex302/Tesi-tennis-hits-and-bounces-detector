#script dei modelli e delle varie prove effettuate con essi, il parametro <control> se impostato a 1 fornisce dei grafici del modello random forest ai fini di
#analisi visiva

import pandas as pd
import sklearn as sk
import sys
import csv
import joblib
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import neighbors
from sklearn import model_selection
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

if(len(sys.argv) < 3):
    print('run as: "python3 model.py <file.csv> <output.txt> <control>"')
    exit(1)

input = sys.argv[1]
output = sys.argv[2]
if(len(sys.argv) == 4):
    control = int(sys.argv[3])
else:
    control = 0

ball = pd.read_csv(input, sep=',', header=0)

#numero di colonne - 1 perchè parto da zero
columns = len(ball.columns) - 1

f = open('./Good_results/'+output,'w+')

ball.head()
X = ball.iloc[:,:columns]
Y = ball.iloc[:,columns]


###########################################################   25-75   #######################################################################
f.write('###########################################################   25-75   #######################################################################')
f.write('\n')

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y,
                                        test_size=0.75, random_state=0)

two = 0
one = 0
for tmp in Y :
    if tmp == 2:
        two +=1
    if tmp == 1:
        one +=1

print(two)
print(one)
print("%r, %r, %r" % (X.shape, X_train.shape, X_test.shape))

SVM = svm.SVC(decision_function_shape="ovo").fit(X_train, y_train)
predicted = SVM.predict(X_test)
expected = y_test
bug_test = SVM.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))

f.write('----------------------SVM--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted)))
f.write('\n')

#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

KN = neighbors.KNeighborsClassifier(n_neighbors=5).fit(X_train,y_train)
predicted_KN = KN.predict(X_test)
bug_test = KN.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('----------------------KN--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_KN)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_KN)))
f.write('\n')

#print(metrics.classification_report(expected, predicted_KN))
#print(metrics.confusion_matrix(expected, predicted_KN))

RF = RandomForestClassifier(n_estimators=1000,max_depth=10, random_state=0).fit(X_train,y_train)
predicted_RF = RF.predict(X_test)
bug_test = RF.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------RF--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

#print(metrics.classification_report(expected, predicted_RF))
#print(metrics.confusion_matrix(expected, predicted_RF))

#f.write('\n')
#f.write('\n')
#f.write('---------------------SECONDO VIDEO TEST--------------------')
#f.write('\n')

GNB = GaussianNB().fit(X_train,y_train)
predicted_RF = GNB.predict(X_test)
bug_test = GNB.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------GNB--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

MLP = MLPClassifier(hidden_layer_sizes = 2048,activation = "relu" ,random_state = 1, max_iter = 1000).fit(X_train,y_train)
predicted_MLP = MLP.predict(X_test)
bug_test = MLP.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------MLP--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_MLP)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_MLP)))
f.write('\n')


###########################################################   50-50   #######################################################################

f.write('###########################################################   50-50   #######################################################################')
f.write('\n')

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y,
                                        test_size=0.50, random_state=0)

print("%r, %r, %r" % (X.shape, X_train.shape, X_test.shape))


SVM = svm.SVC(decision_function_shape="ovo").fit(X_train, y_train)
predicted = SVM.predict(X_test)
expected = y_test
bug_test = SVM.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))


f.write('----------------------SVM--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted)))
f.write('\n')

#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

KN = neighbors.KNeighborsClassifier(n_neighbors=5).fit(X_train,y_train)
predicted_KN = KN.predict(X_test)
bug_test = KN.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('----------------------KN--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_KN)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_KN)))
f.write('\n')

#print(metrics.classification_report(expected, predicted_KN))
#print(metrics.confusion_matrix(expected, predicted_KN))

RF = RandomForestClassifier(n_estimators=1000,max_depth=10, random_state=0).fit(X_train,y_train)
predicted_RF = RF.predict(X_test)
bug_test = RF.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------RF--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

#print(metrics.classification_report(expected, predicted_RF))
#print(metrics.confusion_matrix(expected, predicted_RF))

#f.write('\n')
#f.write('\n')
#f.write('---------------------SECONDO VIDEO TEST--------------------')
#f.write('\n')

GNB = GaussianNB().fit(X_train,y_train)
predicted_RF = GNB.predict(X_test)
bug_test = GNB.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------GNB--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

MLP = MLPClassifier(hidden_layer_sizes = 2048,activation = "relu" ,random_state = 1, max_iter = 1000).fit(X_train,y_train)
predicted_MLP = MLP.predict(X_test)
bug_test = MLP.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------MLP--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_MLP)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_MLP)))
f.write('\n')

###########################################################   75-25   #######################################################################
f.write('###########################################################   75-25   #######################################################################')
f.write('\n')

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y,
                                        test_size=0.25, random_state=0)

print("%r, %r, %r" % (X.shape, X_train.shape, X_test.shape))


SVM = svm.SVC(decision_function_shape="ovo").fit(X_train, y_train)
predicted = SVM.predict(X_test)
expected = y_test
bug_test = SVM.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))


f.write('----------------------SVM--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted)))
f.write('\n')

#print(metrics.classification_report(expected, predicted))
#print(metrics.confusion_matrix(expected, predicted))

KN = neighbors.KNeighborsClassifier(n_neighbors=5).fit(X_train,y_train)
predicted_KN = KN.predict(X_test)
bug_test = KN.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('----------------------KN--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_KN)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_KN)))
f.write('\n')

#print(metrics.classification_report(expected, predicted_KN))
#print(metrics.confusion_matrix(expected, predicted_KN))

RF = RandomForestClassifier(max_depth=10,n_estimators=200, random_state=0).fit(X_train,y_train)
predicted_RF = RF.predict(X_test)
bug_test = RF.predict(X_train)
print(predicted_RF - y_test.to_numpy())
print(y_test.iloc[2])
print(str(metrics.confusion_matrix(y_train, bug_test)))
joblib.dump(RF,'./final_scripts/RF.joblib')
if(control == 1):
    for i in range(len(predicted_RF)):
        if(predicted_RF[i] != y_test.iloc[i]):
            x1, y1, x2, y2, x3, y3, mx, my = map(float, X_test.iloc[i])
            p1 = (0, 0)
            p2 = (x1, y1)
            p3 = (x1 + x2, y1 + y2)
            p4 = (x1 + x2 + x3, y1 + y2 + y3)
            plt.plot([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
            plt.scatter([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
            ann = 'was ' + str(y_test.iloc[i]) + ' labeled as ' + str(predicted_RF[i])
            plt.annotate(ann,(0,0),color='red')
            plt.show()
f.write('---------------------RF--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

#df = pd.DataFrame(X_test)
#df['BOUNCES'] = y_test
#df['PREDICTED'] = predicted_RF
#df.to_csv('./differences.csv')


#print(metrics.classification_report(expected, predicted_RF))
#print(metrics.confusion_matrix(expected, predicted_RF))

#f.write('\n')
#f.write('\n')
#f.write('---------------------SECONDO VIDEO TEST--------------------')
##f.write('\n')
GNB = GaussianNB().fit(X_train,y_train)
predicted_RF = GNB.predict(X_test)
bug_test = GNB.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------GNB--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_RF)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_RF)))
f.write('\n')

MLP = MLPClassifier(hidden_layer_sizes = 2048,activation = "relu" ,random_state = 1, max_iter = 1000).fit(X_train,y_train)
predicted_MLP = MLP.predict(X_test)
bug_test = MLP.predict(X_train)
print(str(metrics.confusion_matrix(y_train, bug_test)))
f.write('---------------------MLP--------------------')
f.write('\n')
f.write(str(metrics.classification_report(expected, predicted_MLP)))
f.write('----------Matrice di confusione---------')
f.write('\n')
f.write(str(metrics.confusion_matrix(expected, predicted_MLP)))
f.write('\n')

#X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y,
#                                        test_size=0.20, random_state=0)
#
#clf = RandomForestClassifier(n_estimators=1000,max_depth=10, random_state=0)
#print(cross_val_score(clf, X, Y, cv=5))

#f.close