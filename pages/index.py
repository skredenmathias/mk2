# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## MK Log Analyse

            Jeg benyttet data fra RockII, Index_Mgmt, og Wind_Power_Import, som oppga produksjonsdata fra svenske vindparker. Disse applikasjonene ble ansett som å holde mest relevant data.
            Disse dataene ble vurdert tilstrekkelige for en regresjonsmodell. Modellen er skrevet i python, og undersøker forhold mellom værforhold og produksjon i vindparkene. I modellen ser vi en klar korrelasjon mellom temperatur, enkelte vindparker, og strømproduksjon.

            For å forbedre modellen anbefales et bredere datasett, gjerne med mer sensordata fra værradar eller trykkdata med produksjon fra flere vindparker. I et slikt tilfelle vil en LSTM eller RNN modell kunne gi langt bedre innsikt i vindparkenes påvirkning på pris i det europeiske kraftmarkedet. 

            Jeg utførte også en avviksanalyse, men den er imidlertid ikke tilstrekkelig.

            """
        ),
        dcc.Link(dbc.Button('Oppsummering av analyse', color='primary'), href='/insights')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [ 
        html.Div(
            html.Img(src='assets/wind_park_production3.png', className='img-fluid', width="100%"),
        )  
    ]
)


layout = dbc.Row([column1, column2])