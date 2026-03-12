from sklearn.feature_selection import RFE #recursive feature elimination
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def getTopFeatureNames(selector, x):
    features = selector.get_feature_names_out()
    # print(features)
    for i in range(len(features)):
        features[i] = int(features[i][1:])
    # print(features)
    feature_names = []
    for i in range(len(x.columns)):
        if i in features:
            feature_names.append(x.columns[i])
    return feature_names

def featureRank(mod):
    model = mod[0]
    x = mod[1]
    y = mod[2]
    mse = mod[3]
    r2 = mod[4]
    data = mod[5]
    print("MSE without feature ranking: ", mse)
    print("R^2 score without feature ranking: ", r2)
    print()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)

    selector = RFE(model, n_features_to_select=20)
    selector = selector.fit(x_train, y_train)

    print("Support of feature: ", selector.support_)
    print("Feature ranking: ", selector.ranking_)
    print("Feature names: ", x.columns.tolist())
    feature_names = getTopFeatureNames(selector, x)
    print(f"Top {len(feature_names)} features: ", feature_names)

    x_train2, x_test2, y_train2, y_test2 = train_test_split(x[feature_names], y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train2 = scaler.fit_transform(x_train2)
    x_test2 = scaler.transform(x_test2)

    modelTest = LinearRegression()
    modelTest.fit(x_train2, y_train2)
    y_pred2 = modelTest.predict(x_test2)
    mse2 = mean_squared_error(y_test2, y_pred2)
    r2_2 = r2_score(y_test, y_pred2)

    print("MSE with feature ranking: ", mse2)
    print("R^2 score with feature ranking: ", r2_2)
    print()

    dropped = x.drop(columns=feature_names)
    x_train3, x_test3, y_train3, y_test3 = train_test_split(dropped, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train3 = scaler.fit_transform(x_train3)
    x_test3 = scaler.transform(x_test3)

    modelTest2 = LinearRegression()
    modelTest2.fit(x_train3, y_train3)
    y_pred3 = modelTest2.predict(x_test3)
    mse3 = mean_squared_error(y_test3, y_pred3)
    r2_3 = r2_score(y_test3, y_pred3)

    print("MSE without top 20 features: ", mse3)
    print("R^2 score without top 20 features: ", r2_3)

    selector2 = RFE(model, n_features_to_select=5)
    selector2 = selector2.fit(x_train3, y_train3)

    print("Support of features (without top 20): ", selector2.support_)
    print("Feature ranking (without top 20): ", selector2.ranking_)
    print("Feature names (without top 20): ", dropped.columns.tolist())
    feature_names2 = getTopFeatureNames(selector2, dropped)
    print(f"Top {len(feature_names2)} features (without top 20): ", feature_names2)

    return mse, r2, mse2, r2_2, mse3, r2_3, data, x.columns.tolist(), selector.ranking_, feature_names

# Testing function
# featureRank()