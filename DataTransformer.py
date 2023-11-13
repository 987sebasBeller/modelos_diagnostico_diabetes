import pandas as pd
from sklearn.preprocessing import OrdinalEncoder 
from sklearn.preprocessing import StandardScaler
class DataTransformer:
    def __init__(self):
        self.__ord_enc=OrdinalEncoder()
        self.__scaler=StandardScaler()
    def codificacionOrdinal(self,df):
        ord_enc=self.__ord_enc
        df_categoricas= df.select_dtypes(include=['object'])
        if hasattr(ord_enc, 'categories_'):
             df_lleno=ord_enc.transform(df_categoricas)
        else :
            df_lleno=ord_enc.fit_transform(df_categoricas)
        df_lleno=pd.DataFrame(data=df_lleno,columns=df_categoricas.columns,index=df_categoricas.index)
        df_diabetes_train=df.drop(df_lleno.columns,axis=1)
        df_diabetes_train=pd.concat([df_diabetes_train,df_lleno],axis=1)
        return df_diabetes_train
    def normalizar(self,df):
        scaler=self.__scaler
        X=df.iloc[:,:-1]
        X_cats=df.iloc[:,-1]
        if hasattr(scaler, 'feature_names_in_'):
            dat_stan=scaler.transform(X)
        else:
            dat_stan=scaler.fit_transform(X)
        X=pd.DataFrame(dat_stan,columns=X.columns,index=X.index)
        X=pd.concat([X,X_cats],axis=1)
        return X
    def get_category(self,indice):
        return self.get_categories[-1][int(indice)]
    @property
    def get_categories(self):
        return self.__ord_enc.categories_