from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

dataset = pd.read_excel('E:\\Projetos\\previsor-de-apostas-futebol\\datasets\\all-euro-data-2021-2022.xlsx') # Gets first sheet of the dataset

print(len(dataset))
#print(dataset.head(10))

