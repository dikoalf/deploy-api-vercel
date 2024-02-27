# import package
from fastapi import FastAPI
import pandas as pd

# membuat object FastAPI /  Instance
app = FastAPI()

# membuat alamat/endpoint
# contoh get / surveys

# membbuat alamat utama / home endpoint

df = pd.DataFrame({
    "Name": ['Budi', 'John', 'Cena'],
    "Location": ['Cianjur', 'LA', 'Florida']
})

@app.get('/')
def getHome():

    return {
            "message":"Hello"
        }

@app.get('/show-data')
def getShowData():
    result = df.to_dict(orient='records')

    return result

@app.get('/search-data/{keyword}/{location}')
def getSearchData(keyword, location):
    # filter
    filterDf = df[(df['Name'] == keyword) & (df['Location'] == location)]

    return filterDf.to_dict(orient='records')

@app.post('/create-data')
def createData(data:dict):
    df.loc[len(df.index)] = [data['Name'], data['Location']]
    # df = df.reset_index(drop=True)
    return df.to_dict(orient='records')