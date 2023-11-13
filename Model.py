import pandas as pd
class Model:
    def __init__(self, modelSlc,dataTransformer):
        self.__modeloSlc = modelSlc
        self.__dataTransformer=dataTransformer
    def predict(self,df):
        df=self.__dataTransformer.codificacionOrdinal(df)
        df=self.__dataTransformer.normalizar(df.iloc[:,:-1])
        indices=self.__modeloSlc.predict(df)
        prediccion=[]
        for indice in indices:
          prediccion.append(self.__dataTransformer.get_category(indice))
        return prediccion