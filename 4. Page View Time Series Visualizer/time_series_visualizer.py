import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
                  color='red', figsize=(18, 7), rot=0, legend=False).get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month

    # Get the months from the full year 2018
    year2018 = df_bar.loc[df_bar['Years'] == 2018]
    months = year2018['Months'].apply(lambda x: calendar.month_name[x])
    months_list = list(months.unique())

    # Draw bar plot
    df_bar = df_bar.groupby(['Years', 'Months'])['value'].mean().unstack()
    fig = df_bar.plot(kind='bar', figsize=(11, 6), xlabel='Years', ylabel='Average Page Views')
    fig.legend(labels=months_list, loc='upper left')
    fig = fig.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    year2018 = df_box.loc[df_box['year'] == 2018]
    months = list(year2018['month'].unique())

    fig = plt.figure(figsize=(14, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.title('Year-wise Box Plot (Trend)')
    ax2 = fig.add_subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, order=months, ax=ax2)
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig