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
            text text text

            """
        ),

    ],
)

initial_df = html.Img(src='assets/initial_df.png', className='img-fluid')
nulls_pricecalc = html.Img(src='assets/nulls_pricecalc.png', className='img-fluid')
clean_rocky_code = html.Img(src='assets/initial_df.png', className='img-fluid')
clean_rocky = html.Img(src='assets/initial_df.png', className='img-fluid')
index_code_1 = html.Img(src='assets/initial_df.png', className='img-fluid')
index_code_2 = html.Img(src='assets/initial_df.png', className='img-fluid')
index_clean = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_power_initial = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_clean = html.Img(src='assets/initial_df.png', className='img-fluid')
kulltorp = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_production = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_decision_tree_feature_importances2 = html.Img(src='assets/initial_df.png', className='img-fluid')
wind_park_anomalies2 = html.Img(src='assets/initial_df.png', className='img-fluid')

layout = dbc.Row([column1, initial_df, nulls_pricecalc])