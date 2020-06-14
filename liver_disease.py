import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("indian_liver_patient.csv")

data = data.drop_duplicates()

data=data.dropna(how='any') 


X = data.iloc[:, :10]

def convert_to_int(word):

    word_dict = {'Male':0 ,'Female':1}
    return word_dict[word]

X['Gender'] = X['Gender'].apply(lambda x : convert_to_int(x))


y = data.iloc[:, -1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

regressor = LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#Fitting model with trainig data
regressor.fit(x_train, y_train)
dis = regressor.predict(x_test)
# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[64,1,0.9,0.3,310,61,58,7,3.4,0.9]]))
print(round(dis[0],2))








