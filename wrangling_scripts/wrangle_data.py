import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`


def read_data(dataset):

    """
    simple function to read in data to Pandas Dataframe
    """
    
    df = pd.read_pickle(dataset)
    
    return df

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    graph_one = []
    graph_two = []
    graph_three = []

    df = read_data('data/df_all_rules.pkl')

    df_all_rules_group = df.groupby(['SITE_NUMBER',
                                     'year',
                                     'month']).mean().reset_index()

    df_all_rules_group_pivot = df_all_rules_group.pivot(index='year',
                                                  columns='month',
                                                  values='TMR_SUB_18')
    

    # Graph One - Table

    ########################################################################################

    headerColor = 'grey'
    rowEvenColor = 'lightgrey'
    rowOddColor = 'white'
    
    fig_table = go.Table(
            columnwidth=180,
            header=dict(values=list(['year'])
                               + list(df_all_rules_group_pivot.columns),
                        fill_color=headerColor,
                        line_color='darkslategray',
                        align=['left', 'center'],
                        font=dict(color='white', size=12),
            height=40),
            cells=dict(values=[
                df_all_rules_group_pivot.index,
                np.around(df_all_rules_group_pivot.iloc[:, :1].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 1:2].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 2:3].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 3:4].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 4:5].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 5:6].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 6:7].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 7:8].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 8:9].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 9:10].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 10:11].values,2),
                np.around(df_all_rules_group_pivot.iloc[:, 11:12].values,2) ],
                line_color='darkslategray',
                # 2-D list of colors for alternating rows
                fill_color = [[rowOddColor,
                rowEvenColor,
                rowOddColor, 
                rowEvenColor,
                rowOddColor]*5],
                align = ['left'],
                font = dict(color = 'darkslategray', size = 11)
            ))

    graph_one.append(
        fig_table
    )
    
    layout_one = dict(title='128 TMR_SUB_18',
                      xaxis=dict(title='Months'),
                      yaxis=dict(title='Years')
                      )

    
    ########## graph heatmap

    ########################################################################################
    # best result in Jupyter #
    import plotly.figure_factory as ff

    z=np.round(df_all_rules_group_pivot.values[::-1],2)
    x=list(df_all_rules_group_pivot.columns)
    y=list(df_all_rules_group_pivot.index[::-1])

    # fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z, colorscale='Viridis')

    """layout_two = {}
    layout_two = dict(title='128 TMR_SUB_18 Heatmap',
                      xaxis=dict(title='Months'),
                      yaxis=dict(title='Years')
                      )

    fig_heatmap = ff.create_annotated_heatmap(z, 
    x=x, 
    y=y, 
    font_colors=['antiquewhite'], 
    hoverinfo='y+x+z')
        
    graph_two.append(fig_heatmap)"""
    
    # Other attempt with go.Heatmap instead of ff.create_annotated_heatmap # 

    """fig_heatmap_2 = go.Figure(data=go.Heatmap(
                   z=df_all_rules_group_pivot.values[::-1],
                   x=df_all_rules_group_pivot.columns,
                   y=df_all_rules_group_pivot.index[::-1],
                   hoverongaps = False))

    layout = go.Layout(title="Temperature test", showlegend=True)
    graph_two.append(fig_heatmap_2)"""
    

    # working attempt *
    annotations = []

    for n, row in enumerate(z):
        for m, val in enumerate(row):
            annotations.append(go.layout.Annotation(text=str(z[n][m]), 
            x=x[m], 
            y=y[n], 
            xref='x1', 
            yref='y1', 
            showarrow=False, 
            font=dict( size=14,
            color="#ffffff")))

    trace_heatmap = go.Heatmap(
                   z=np.round(df_all_rules_group_pivot.values[::-1], 2),
                   x=df_all_rules_group_pivot.columns,
                   y=df_all_rules_group_pivot.index[::-1],
                   hoverongaps = False,
                   text=annotations,
                   colorscale="Viridis")

    # data = [trace_heatmap]
    # trace_layout = go.Layout(title="Test", showlegend=True)
    # figure_heatmap = go.Figure(data=data, layout=trace_layout)              


    """heatmap_figure = go.Figure(data=trace_heatmap)

    heatmap_figure.layout.update(annotations=annotations)

    heatmap_figure.update_xaxes(nticks=12)
    heatmap_figure.update_xaxes(tick0=1, dtick=1)

    heatmap_figure.update_yaxes(nticks=len(x))
    heatmap_figure.update_yaxes(tick0=1, dtick=1)"""
    graph_two.append(trace_heatmap)

    layout_two = {"annotations": [{"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "17.05", "x": 1, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "21.66", "x": 2, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "18.02", "x": 3, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "34.86", "x": 4, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "45.04", "x": 5, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.78", "x": 6, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.28", "x": 7, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.69", "x": 8, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "50.96", "x": 9, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "41.1", "x": 10, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "29.15", "x": 11, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.33", "x": 12, "xref": "x", "y": 2017, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 1, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "30.68", "x": 2, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "31.45", "x": 3, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "41.5", "x": 4, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "52.16", "x": 5, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "62.71", "x": 6, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "65.09", "x": 7, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.92", "x": 8, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.8", "x": 9, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "39.83", "x": 10, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "33.91", "x": 11, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "23.23", "x": 12, "xref": "x", "y": 2016, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.94", "x": 1, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "22.49", "x": 2, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.5", "x": 3, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "36.77", "x": 4, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.12", "x": 5, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "64.46", "x": 6, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 7, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "61.69", "x": 8, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "53.77", "x": 9, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "38.56", "x": 10, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 11, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 12, "xref": "x", "y": 2015, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "29.13", "x": 1, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "22.49", "x": 2, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.5", "x": 3, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "36.8", "x": 4, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.12", "x": 5, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.6", "x": 6, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "65.75", "x": 7, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "61.69", "x": 8, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "53.77", "x": 9, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "38.56", "x": 10, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "33.04", "x": 11, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "31.94", "x": 12, "xref": "x", "y": 2014, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "10.94", "x": 1, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "25.14", "x": 2, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "27.25", "x": 3, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "33.74", "x": 4, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "49.56", "x": 5, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "67.26", "x": 6, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "67.75", "x": 7, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "63.76", "x": 8, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "52.93", "x": 9, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "42.51", "x": 10, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "32.92", "x": 11, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "19.53", "x": 12, "xref": "x", "y": 2013, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 1, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 2, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "23.62", "x": 3, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "39.28", "x": 4, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "49.56", "x": 5, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.31", "x": 6, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.6", "x": 7, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.59", "x": 8, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "50.8", "x": 9, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "37.56", "x": 10, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "22.45", "x": 11, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "10.81", "x": 12, "xref": "x", "y": 2012, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "13.68", "x": 1, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.24", "x": 2, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "29.3", "x": 3, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "36.57", "x": 4, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.18", "x": 5, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "61.32", "x": 6, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.55", "x": 7, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 8, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 9, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "39.65", "x": 10, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "32.89", "x": 11, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 12, "xref": "x", "y": 2010, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "13.86", "x": 1, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "19.07", "x": 2, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "24.56", "x": 3, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "35.86", "x": 4, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "53.83", "x": 5, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "61.45", "x": 6, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "68.19", "x": 7, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "61.56", "x": 8, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "53.8", "x": 9, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "43.05", "x": 10, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 11, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 12, "xref": "x", "y": 2009, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "18.27", "x": 1, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "23.94", "x": 2, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "14.12", "x": 3, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "35.66", "x": 4, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "50.17", "x": 5, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.29", "x": 6, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "65.16", "x": 7, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "62.12", "x": 8, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.73", "x": 9, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "39.34", "x": 10, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "34.12", "x": 11, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "27.82", "x": 12, "xref": "x", "y": 2007, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 1, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "21.62", "x": 2, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "23.78", "x": 3, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "37.45", "x": 4, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "51.72", "x": 5, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "62.1", "x": 6, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "65.82", "x": 7, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "59.18", "x": 8, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "52.73", "x": 9, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "41.33", "x": 10, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "17.65", "x": 11, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "23.72", "x": 12, "xref": "x", "y": 2006, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "21.65", "x": 1, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "21.25", "x": 2, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "30.54", "x": 3, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 4, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 5, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "64.03", "x": 6, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "67.71", "x": 7, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "65.49", "x": 8, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "55.13", "x": 9, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "41.76", "x": 10, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "27.21", "x": 11, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 12, "xref": "x", "y": 2005, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "15.23", "x": 1, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 2, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "29.66", "x": 3, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "36.53", "x": 4, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "56.25", "x": 5, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 6, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "70.96", "x": 7, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "70.35", "x": 8, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "55.6", "x": 9, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "42.1", "x": 10, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "32.97", "x": 11, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "30.12", "x": 12, "xref": "x", "y": 2004, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "nan", "x": 1, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "31.47", "x": 2, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "28.14", "x": 3, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "37.17", "x": 4, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.59", "x": 5, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "60.53", "x": 6, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "69.49", "x": 7, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "64.19", "x": 8, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "54.7", "x": 9, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "43.32", "x": 10, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "32.5", "x": 11, "xref": "x", "y": 2003, "yref": "y"}, {"font": {"color": "#ffffff", "size": 14}, "showarrow": False, "text": "24.65", "x": 12, "xref": "x", "y": 2003, "yref": "y"}], "xaxis": {"nticks": 12, "tick0": 1, "dtick": 1}, "yaxis": {"nticks": 12, "tick0": 1, "dtick": 1}}
    # line graphs

    ########################################################################################

    month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    new_df_all = pd.DataFrame()

    for year in df_all_rules_group.year.unique():
        months_list_loop = list(df_all_rules_group.loc[df_all_rules_group.year==year].month.unique())
        # print(f'count of months: {len(months_list_loop)} \nlist of months: {months_list_loop} \n')
        new_df_group = df_all_rules_group.loc[df_all_rules_group.year==year].groupby(['year',
                                                                            'month'])['TMR_SUB_18'].mean().reset_index()
        # print(f'new_df_group: \n{new_df_group.head()}')
        # print()
        for month in month_list:
            if month not in list(new_df_group.month.unique()):
                # print(f'missing month: {month}') 
                null_month = {'year':year, 'month':month, 'TMR_SUB_18':np.nan}
                # print(f'null_month: {null_month}')
                # print(f'null month list size: {len(null_month)}')
                new_df_group = new_df_group.append(null_month, ignore_index=True)
            
                # print(f'new_df_group shape: \n{new_df_group.shape}')
                # print()
    
        # print(f'new_df unique months: {new_df_group.month.unique()}')
    
        new_df_all = new_df_all.append(new_df_group)
        new_df_all = new_df_all.astype({"year": int, "month": int, 'TMR_SUB_18': float})
        new_df_all['TMR_SUB_18'] = new_df_all['TMR_SUB_18'].round(2)
        new_df_all = new_df_all.sort_values(['year', 'month'])

    # 
    for year in new_df_all.year.unique():
    # print(data_test_group.loc[data_test_group.year==year].groupby(['year', 'month'])['TMR_SUB_18'].mean())
        graph_three.append(go.Scatter(x=month_list, 
                             y=new_df_all.loc[new_df_all.year==year].groupby(['year',
                             'month'])['TMR_SUB_18'].mean(),
                    mode='lines+markers',
                    name=str(year) + ' Monthly Averages',
                            connectgaps=False,
                            line_shape='spline'))
    
        # fig.update_xaxes(nticks=12)
        # fig.update_xaxes(tick0=1, dtick=1)
    
    graph_three.append(go.Scatter(x=month_list, 
                         y=new_df_all.groupby(['month'])['TMR_SUB_18'].mean(), 
                         line = dict(color='darkturquoise', 
                                     width=4, 
                                     dash='dot'),
                        name='Average',
                            line_shape='spline'))
    
    layout_three = dict(title='128 TMR_SUB_18 Line Graph', hovermode='closest')

    ########################################################################################

    """
# third chart plots percent of population that is rural from 1990 to 2015
    
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = df.Functional_Class,
      y = df.AADT_2019.tolist(),
      mode = 'markers',
          text=df['Traffic_Link_ID'],
          marker=dict(color=df.AADT_2019.tolist(),
                      colorscale='Viridis')
      )
    )
    
    layout_three = dict(title = '2019 AADT by Functional Class',
                xaxis = dict(title = 'Functional Class'),
                yaxis = dict(title = '2019 AADT'),
                        hovermode= "closest",
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    df_fc = df.groupby('Functional_Class')['Traffic_Link_ID'].nunique()
    graph_four.append(
      go.Bar(
      x = df_fc,
      y = df.Functional_Class.unique(),
          orientation='h',
      )
    )

    layout_four = dict(title = 'Count of Traffic Links by Functional Class',
                xaxis = dict(title = 'Traffic Link Count'),
                yaxis = dict(title = 'Functional Class'),
                )"""
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    """figures.append(dict(data=graph_four, layout=layout_four))"""

    return figures
