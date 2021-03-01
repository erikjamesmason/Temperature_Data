import pandas as pd
import numpy as np
import plotly.graph_objs as go
import json
import plotly

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

    layout_test = go.Layout(
        xaxis=dict(tick0=0,
      dtick = 1), 
      yaxis=dict(tick0=2003,
      dtick = 1),
      title="128 TMR_SUB_18 Heatmap")

    annotations = []

    for n, row in enumerate(z):
        for m, val in enumerate(row):
            annotations.append(go.layout.Annotation(text=str(z[n][m]), 
                                                    x=x[m], 
                                                    y=y[n], 
                                                    xref='x1', 
                                                    yref='y1', 
                                                    showarrow=False, 
                                                    font=dict(
                                                        size=14,
                                                        color="#ffffff" )))

    layout_test.update(annotations=annotations,
    )

    # convert layout annotations to plotly JSON encoded form 
    layout_json = json.dumps(layout_test, cls=plotly.utils.PlotlyJSONEncoder)

    # Convert to dictionary otherwise json.dumps.cls.plotly will leave as string
    layout_two = json.loads(layout_json)

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
    colors = plotly.colors.sequential.Blugrn * 2
    color_counter = 0 
    for year in new_df_all.year.unique():
    # print(data_test_group.loc[data_test_group.year==year].groupby(['year', 'month'])['TMR_SUB_18'].mean())
        graph_three.append(go.Scatter(x=month_list, 
                             y=new_df_all.loc[new_df_all.year==year].groupby(['year',
                             'month'])['TMR_SUB_18'].mean(),
                    mode='lines+markers',
                             opacity=0.8,
                    name=str(year) + ' Monthly Averages',
                            connectgaps=False,
                            line_shape='spline',
                            line=dict(color=colors[color_counter])))
        color_counter += 1                    
    
        # fig.update_xaxes(nticks=12)
        # fig.update_xaxes(tick0=1, dtick=1)
    
    graph_three.append(go.Scatter(x=month_list, 
                         y=new_df_all.groupby(['month'])['TMR_SUB_18'].mean(), 
                         line = dict(color='darkturquoise', 
                                     width=4, 
                                     dash='dot'),
                        name='Average',
                            line_shape='spline'))
    
    layout_three = dict(title='128 TMR_SUB_18 Line Graph', hovermode='closest', xaxis=dict(tick0 = 1,
      dtick = 1))

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
