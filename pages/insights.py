# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            # Note that images are not responsive on IE 10.
            Text describing project and initial data state


            """
        ),

    ],
)

column2 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Currently: Explaining NULL values
            should be after initial df
            Talking about how PriceCalcWs either returns a NULL call with each log event, or no NULL values at all.

            """
        ),

    ],
)

column3 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Explaining how I cleaned the text fields into dataframes
            # Note: missing all analysis, which is in the notebook.

            """
        ),

    ],
)

initial_df = html.Img(src='assets/initial_df.png', className='img-fluid')

nulls_pricecalc = html.Img(src='assets/nulls_pricecalc.png', className='img-fluid')

clean_rocky_code = html.Img(src='assets/initial_df.png', className='img-fluid')
clean_rocky = html.Img(src='assets/initial_df.png', className='img-fluid')

index_code_1 = html.Img(src='assets/index_code_1.png', className='img-fluid')
index_code_2 = html.Img(src='assets/index_code_2.png', className='img-fluid')
index_clean = html.Img(src='assets/index_clean.png', className='img-fluid')

wind_power_initial = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_clean = html.Img(src='assets/initial_df.png', className='img-fluid')

kulltorp = html.Img(src='assets/initial_df.png', className='img-fluid')

wind_park_production = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_decision_tree_feature_importances2 = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_anomalies2 = html.Img(src='assets/initial_df.png', className='img-fluid')

layout = dbc.Row([column1, initial_df, column2, nulls_pricecalc, clean_rocky_code, clean_rocky, column3])

# row = html.Div(
#     [
#         dbc.Row(dbc.Col(html.Div("A single column"))),
#         dbc.Row(
#             [
#                 dbc.Col(index_code_1),
#                 dbc.Col(index_code_2),
#                 dbc.Col(index_clean),
#             ]
#         ),
#     ]
# )

# row2 = html.Div(
#     [
#         dbc.Row(dbc.Col(html.Div("A single column"))),
#         dbc.Row(
#             [
#                 dbc.Col(wind_park_production),
#                 dbc.Col(wind_park_decision_tree_feature_importances2),
#                 dbc.Col(wind_park_anomalies2),
#             ]
#         ),
#     ]
# )