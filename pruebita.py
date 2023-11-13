import pickle
import pandas as pd
with open("./modelo.pkl", "rb") as file:
    modelo = pickle.load(file)
    print(modelo)
datos_prediccion = {
    'AGE': [39,45],
    'HbA1c': [10.1,2.1],
    'Chol': [10.6752,1.3],
    'TG': [9.174,2.8],
    'VLDL': [1.8348,1.02],
    'BMI': [32,15],
    'Gender': ['M','F'],
    'CLASS':['N','N']
}
#print(type(ord_enc))
datos_prediccion = pd.DataFrame(datos_prediccion)
# datos_prediccion=pr.codificacionOrdinal(datos_prediccion,ord_enc)
# datos_prediccion=pr.normalizar(datos_prediccion.iloc[:,:-1],scaler)
print(datos_prediccion)
print(modelo.predict(datos_prediccion))


