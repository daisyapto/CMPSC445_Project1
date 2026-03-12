import matplotlib.pyplot as plt

def dataVisualization(fr):
    mse = fr[0]
    r2 = fr[1]
    mse2 = fr[2]
    r2_2 = fr[3]
    mse3 = fr[4]
    r2_3 = fr[5]
    data = fr[6]
    all_features = fr[7]
    feature_ranking = fr[8]
    feature_names = fr[9]

    plotData1 = data[data['Annual CH4 Mean'] != 1783.2539024390244] # all data that was not filled in the mean (the blanks)
    plt.plot(plotData1['Year'], plotData1['Annual CH4 Mean'])
    plt.title("Year vs Annual CH4 Mean")
    plt.xlabel("Year")
    plt.ylabel("Annual CH4 Mean")
    plt.show()

    plotData2 = data[data['Annual CO2 Mean'] != 361.2510447761194] # all data that was not filled in the mean (the blanks)
    plt.plot(plotData2['Year'], plotData2['Annual CO2 Mean'])
    plt.title("Year vs Annual CO2 Mean")
    plt.xlabel("Year")
    plt.ylabel("Annual CO2 Mean")
    plt.show()

    plotData3 = data[data['Annual N2O Mean'] != 326.02125] # all data that was not filled in the mean (the blanks)
    plt.plot(plotData3['Year'], plotData3['Annual N2O Mean'])
    plt.title("Year vs Annual N2O Mean")
    plt.xlabel("Year")
    plt.ylabel("Annual N2O Mean")
    plt.show()

    plotData4 = data[data['Annual CO2 Concentration Mean'] != 235.70139502936468] # all data that was not filled in the mean (the blanks)
    plt.plot(plotData4['Year'], plotData4['Annual CO2 Concentration Mean'])
    plt.title("Year vs Annual CO2 Mean")
    plt.xlabel("Year")
    plt.ylabel("Annual CO2 Mean")
    plt.show()

    plt.plot([r2, r2_2, r2_3], [mse, mse2, mse3])
    plt.title("No feature ranking, feature ranking, and removal of top 15 features")
    plt.xlabel("R^2 score")
    plt.ylabel("MSE")
    plt.show()

    plt.bar(all_features, feature_ranking)
    # GeeksforGeeks - label each bar with a for loop
    for i in range(len(feature_ranking)):
        plt.text(i, feature_ranking[i], feature_ranking[i])
    plt.title("Feature ranking")
    plt.xlabel("Feature")
    plt.xticks(rotation=90, fontsize=6)
    plt.ylabel("Feature rank")
    # Google search AI Overview - how to fit all labels onto plot
    plt.tight_layout()
    plt.show()

    # Generates 80 line plots - all 20 top features mapped against the 4 gases
    gases = ['Annual CH4 Mean', 'Annual CO2 Mean', 'Annual N2O Mean', 'Annual CO2 Concentration Mean']
    # Plot data filters out the blanks that were filled in with the mean; filled in mean is useful for training the model but not for plotting
    plotData = [plotData1, plotData2, plotData3, plotData4]
    for g in range(len(gases)):
        for i in range(len(feature_names)):
            data = plotData[g].sort_values(by=feature_names[i])
            plt.plot(data[feature_names[i]], data[gases[g]])
            plt.title(f"{feature_names[i]} vs {gases[g]}")
            plt.xlabel(f"{feature_names[i]}")
            plt.ylabel(f"{gases[g]}")
            plt.show()

    # Generates 80 scatter plots - all 20 top features mapped against the 4 gases
    for g in range(len(gases)):
        for i in range(len(feature_names)):
            data = plotData[g].sort_values(by=feature_names[i])
            plt.scatter(data[feature_names[i]], data[gases[g]])
            plt.title(f"{feature_names[i]} vs {gases[g]}")
            plt.xlabel(f"{feature_names[i]}")
            plt.ylabel(f"{gases[g]}")
            plt.show()

# Testing function
# dataVisualization()