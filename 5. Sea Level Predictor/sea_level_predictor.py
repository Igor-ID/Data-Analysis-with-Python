import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    years_extended = range(1880, 2051, 1) # np.arange(1880, 2051, 1)
    result = linregress(x, y)
    slope = result.slope
    intercept = result.intercept
    y_hat = [slope * xi + intercept for xi in years_extended]

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 7))
    plt.scatter(x, y, color='blue')

    # Create first line of best fit
    plt.plot(years_extended, y_hat, color='red')

    df_2000 = df.copy()
    df_2000 = df_2000.loc[df_2000['Year'] >= 2000]
    x_2000 = df_2000['Year']
    y_2000 = df_2000['CSIRO Adjusted Sea Level']
    years_extended_2000 = range(2000, 2051, 1) # np.arange(2000, 2051, 1)
    result_2000 = linregress(x_2000, y_2000)
    slope_2000 = result_2000.slope
    intercept_2000 = result_2000.intercept
    y_hat_2000 = [slope_2000 * xi + intercept_2000 for xi in years_extended_2000]

    # Create second line of best fit
    plt.plot(years_extended_2000, y_hat_2000, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()