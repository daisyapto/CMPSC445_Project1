import numpy as np
import pandas as pd

# Debugging
# Show all rows
pd.set_option('display.max_rows', None)

# Debugging
# Show all columns
pd.set_option('display.max_columns', None)

def dataPreprocessing(dataFrames):
    # Join all frames made in dataCollection
    data = pd.concat(dataFrames, ignore_index=True)
    data = data.drop(columns=['Entity (Long-term CO2 Concentration)',
                              'Code (Long-term CO2 Concentration)'])

    data['year'] = data['year'].astype(float)
    data = data.sort_values(by=['year'], ascending=True)
    data = data.rename(columns={'year': 'Year',
                                'mean (CH4)' : 'Annual CH4 Mean',
                                'unc (CH4)' : 'Annual CH4 Uncertainty',
                                'mean (CO2)' : 'Annual CO2 Mean',
                                'unc (CO2)' : 'Annual CO2 Uncertainty',
                                'mean (N2O)' : 'Annual N2O Mean',
                                'unc (N2O)' : 'Annual N2O Uncertainty',
                                'J-D (Land-Ocean Global Means)' : 'Land-Ocean Global Mean (Jan - Dec)',
                                'Annual average (Long-term CO2 Concentration)' : 'Annual CO2 Concentration Mean'})
    data.replace("NaN", np.nan, inplace=True)
    data.replace("***", np.nan, inplace=True)
    # Testing statements
    # data = data[data['Year'] != 2026 and data['Year'] != 1880]
    # data = data.astype(float)
    # data.replace(0, data.mean(), inplace=True)
    # Debug statement
    # print(data.shape)
    # Gemini suggestion for line 57
    # Use groupby function after replace function to group repeated instances of the same year with multiple values distributed across the instances
    # For Example: in the year column there were multiple instances of year x where the first instance lines up with col1 having a value but the second instance lines up with col2
    data = data.groupby('Year').first().reset_index()
    data = data.astype(float)
    data.replace(np.nan, data.mean(), inplace=True)
    # Debug statements
    # print(data.shape)
    # print(data.head())
    data.to_csv('data.csv', index=False)
    # print(data)

    return data

# Testing the function
# dataPreprocessing()