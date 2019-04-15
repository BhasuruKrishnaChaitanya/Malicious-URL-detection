import pickle
import webscrapping as ws
import input_ls as il

def prediction(url):
    x = il.features(url,ws.webcontent(url))
    filename = 'finalized_model.sav' 
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(x)
    if(not result):
      return 'Happy browsing!!!! It is a benign website'
    else:
      return 'Be carefull!!!! It is a malicious website'
#print(prediction('thcvaporizer.com'))
