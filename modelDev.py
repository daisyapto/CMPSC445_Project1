from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

def modelDevelopment(data):
    # Debug statements
    # print(data)
    # print(data.columns)
    x = data[['Year',
              'Annual CH4 Mean',
              'Annual CH4 Uncertainty',
              'Annual CO2 Mean',
              'Annual CO2 Uncertainty',
              'Annual N2O Mean',
              'Annual N2O Uncertainty',
              'Jan (Land-Ocean Global Means)',
              'Feb (Land-Ocean Global Means)',
              'Mar (Land-Ocean Global Means)',
              'Apr (Land-Ocean Global Means)',
              'May (Land-Ocean Global Means)',
              'Jun (Land-Ocean Global Means)',
              'Jul (Land-Ocean Global Means)',
              'Aug (Land-Ocean Global Means)',
              'Sep (Land-Ocean Global Means)',
              'Oct (Land-Ocean Global Means)',
              'Nov (Land-Ocean Global Means)',
              'Dec (Land-Ocean Global Means)',
              'D-N (Land-Ocean Global Means)',
              'DJF (Land-Ocean Global Means)',
              'MAM (Land-Ocean Global Means)',
              'JJA (Land-Ocean Global Means)',
              'SON (Land-Ocean Global Means)',
              'TSI',
              'TSI_UNC',
              'Annual CO2 Concentration Mean',
              'Annual CO2 Mean / Annual CH4 Mean', # Engineered feature
              'Annual N2O Mean / Annual CO2 Mean', # Engineered feature
              'Annual N2O Mean / Annual CH4 Mean', # Engineered feature
              'Annual CO2 Concentration Mean / Annual CO2 Mean', # Engineered feature
              'TSI * TSI_UNC']] # Engineered feature
    y = data['Land-Ocean Global Mean (Jan - Dec)']
    # Debug statements
    # print(y)
    # print(x.shape, y.shape)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Debug statement
    # print(x_train.shape, y_train.shape)
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    # Debug statements
    # print(mean_squared_error(y_test, y_pred))
    # print(r2_score(y_test, y_pred))

    return model, x, y, mse, r2, data

# Testing function
# modelDevelopment()