import pandas
import numpy
import sklearn
from sklearn import linear_model
import sklearn.model_selection
from sklearn.utils import shuffle

data = pandas.read_csv("student-mat.csv", sep=";")
data = data[["G1", "G2", "G3","studytime" , "absences", "failures"]]

#print(data.head())
predict = "G3"
x = numpy.array(data.drop([predict], axis=1))
y = numpy.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

#print("Coefficient: \n", linear.coef_)
#print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
