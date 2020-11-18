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

initial_df = html.Img(src='assets/initial_df.png', className='img-fluid')

nulls_pricecalc = html.Img(src='assets/nulls_pricecalc.png', className='img-fluid')

clean_rocky_code = html.Img(src='assets/clean_rocky_code.png', className='img-fluid')
clean_rocky = html.Img(src='assets/clean_rocky.png', className='img-fluid')

index_code_1 = html.Img(src='assets/index_code_1.png', className='img-fluid')
index_code_2 = html.Img(src='assets/index_code_2.png', className='img-fluid')
index_clean = html.Img(src='assets/index_clean.png', className='img-fluid')

wind_power_initial = html.Img(src='assets/wind_power_initial.png', className='img-fluid')
wind_park_clean = html.Img(src='assets/wind_park_clean.png', className='img-fluid')

kulltorp = html.Img(src='assets/kulltorp.png', className='img-fluid')

wind_park_production = html.Img(src='assets/wind_park_production.png', className='img-fluid')
wind_park_decision_tree_feature_importances2 = html.Img(src='assets/wind_park_decision_tree_feature_importances2.png', className='img-fluid')
wind_park_anomalies2 = html.Img(src='assets/wind_park_anomalies2.png', className='img-fluid')


# header = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             ## Insights  
#             Prosjektet startet med SimpleLog.bak som ble lastet opp til en FTP server tilhørende Markedskraft. Med et Python SFTP library koblet jeg meg opp mot serveren og lastet ned SimpleLog filen. Dette var en ukjent filtype, og det var krevende å få lastet inn data med kjente teknikker. Hverken Microsoft Server Management Studio (SMSS), PostgreSQL, eller Python gjorde jobben.

#             Jeg valgte å sende en mail til børre, da jeg ikke selv greide å finne problemet. I denne perioden hadde jeg enda ikke fått tilgang til dataen, så jeg begynte arbeidet med å sette opp en Plotly Dash nettside med CI via Travis CI og CD gjennom Heroku. Jeg satt også opp min egen database med et Docker mssql image. Etter kontakt med Birger, fant Børre og jeg en løsning med Microsoft SMSS. 

#             Dataen var da analysert med SQL queries i SMSS, Etter å ha kikket på dataene, virket det på meg som at dbo.LogLevel og dbo.Applications kun var inkludert fordi dbo.Log benyttet en kolonne fra hver. Jeg konsentrerte derfor videre fokus rundt dbo.Log. Dette både reduserte kompleksitet og tid det tok meg å vaske datasettet. Uten å gå glipp av potensielt viktige data. 
#             """
#         ),
#     ],
#     width=12,
# )

# block4 = dbc.Col(
#     [ 
#         html.Div(
#             initial_df   
#         )  
#     ]
# )

# block5 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             Dataen ble i Python omgjort til datetime format, sortert, og analysert i kronologisk rekkefølge. Jeg gikk nøye gjennom hver applikasjon, og gjorde notater for å kartlegge deres funksjonalitet, data, kvalitet og sammenheng med resterende programmer. 

#             Når denne listen var komplett, satt jeg igjen med en tilstrekkelig forståelse av datasettet jeg hadde levert. Jeg gjorde meg en rekke betraktninger rundt datasettet: 

#             """
#         ),
#     ],
#     md=4,
# )

# block6 = dbc.Col(
#     [ 
#         html.Div(
#             nulls_pricecalc   
#         )  
#     ]
# )

# block7 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             Jeg valgte å videre analysere tre applikasjoner:
#             RockyII
#             Index_Mgmt
#             Wind_Power_Import
#             Da disse så ut til å holde mest relevant data. Disse applikasjonene hadde også mer variert data, som lett kunne benyttes uten mye skrubbing.
            
#             """
#         ),
#     ],
#     md=4,
# )

# block8 = dbc.Col(
#     [
#         html.Img(id='img4', src=url_img4, width="100%")      
#     ]
# )

# block9 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             Jeg skrev funksjoner for å sortere tekst-dataen og formatere den i håndterlige tabeller. Analysen fokuserte hovedsakelig på data fra svenske vindparker (Wind_Power_Import). Jeg kjørte en anomaly modell og lagde en decision tree modell som predikerte strømproduksjon basert på temperatur, dato, og vindpark. Jeg fant blant annet ut at
#             Kulltorp returnerer kun NULL verdier.
#             Bleikevare produserer betydelig mye mer strøm enn de andre parkene.
#             Dagene lekker data inn i modellen.
#             Dette er fordi datasettet ble splittet slik at noen av de samme dagene ble inkludert i trenings og test settet.
#             Dermed har modellen lært seg en korrelasjon som gjør at den legger høyere vekt på visse dager hvor det var høy vindhastighet og produksjon. Denne korrelasjonen er ikke reell, da det er kunstig mange variabler som er berørt av denne “dobbel-lagringen”. 
#             Modellen kan for eksempel forbedres med å kjøre en random forest modell på mer data. Jeg tror modellen forbedres betraktelig med data fra flere vindparker, barometrisk trykk og forbruksdata ol. fra SE3, SE4 og potensielt andre relevante prisområder.

#             """
#         ),
#     ],
#     md=4,
# )

# block10 = dbc.Col(
#     [
#         html.Img(id='img3', src=url_img3, width="100%")      
#     ]
# )

# blankrow = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#             &nbsp;
#             """
#         ),
#     ],
#     md=4,
# )
# layout = dbc.Col([
#     dbc.Row(header),
#     dbc.Row([block4])
#     dbc.Row(blankrow),
#     dbc.Row([block5]),
#     dbc.Row(blankrow),
#     dbc.Row([block7]),
#     dbc.Row(blankrow),
#     dbc.Row([block9]),
# ])

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            Prosjektet startet med SimpleLog.bak som ble lastet opp til en FTP server tilhørende Markedskraft. Med et Python SFTP library koblet jeg meg opp mot serveren og lastet ned SimpleLog filen. Dette var en ukjent filtype, og det var krevende å få lastet inn data med kjente teknikker. Hverken Microsoft Server Management Studio (SMSS), PostgreSQL, eller Python gjorde jobben.

            Jeg valgte å sende en mail til børre, da jeg ikke selv greide å finne problemet. I denne perioden hadde jeg enda ikke fått tilgang til dataen, så jeg begynte arbeidet med å sette opp en Plotly Dash nettside med CI via Travis CI og CD gjennom Heroku. Jeg satt også opp min egen database med et Docker mssql image. Etter kontakt med Birger, fant Børre og jeg en løsning med Microsoft SMSS. 

            Dataen var da analysert med SQL queries i SMSS, Etter å ha kikket på dataene, virket det på meg som at dbo.LogLevel og dbo.Applications kun var inkludert fordi dbo.Log benyttet en kolonne fra hver. Jeg konsentrerte derfor videre fokus rundt dbo.Log. Dette både reduserte kompleksitet og tid det tok meg å vaske datasettet. Uten å gå glipp av potensielt viktige data. 

            Dataen ble i Python omgjort til datetime format, sortert, og analysert i kronologisk rekkefølge. Jeg gikk nøye gjennom hver applikasjon, og gjorde notater for å kartlegge deres funksjonalitet, data, kvalitet og sammenheng med resterende programmer. 

            Når denne listen var komplett, satt jeg igjen med en tilstrekkelig forståelse av datasettet jeg hadde levert. Jeg gjorde meg en rekke betraktninger rundt datasettet: 
            PriceCalcWs står for 77% av alle log events, hvorav en tredjedel av disse er log events som returnerer NULL verdier.
            Disse har en egen “characteristic”.
            0.1% av datasettet var feilmeldinger av type 0/1. 
            Alle utenom 4% av disse var i Transfer to Nimbus.
            4% av disse var critical errors i TradeFetcher

            Jeg valgte å videre analysere tre applikasjoner:
            RockyII
            Index_Mgmt
            Wind_Power_Import
            Da disse så ut til å holde mest relevant data. Disse applikasjonene hadde også mer variert data, som lett kunne benyttes uten mye skrubbing. 

            Jeg skrev funksjoner for å sortere tekst dataen og formatere den i håndterlige tabeller. Analysen fokuserte hovedsakelig på data fra svenske vindparker (Wind_Power_Import). Jeg kjørte en anomaly modell og lagde en decision tree modell som predikerte strømproduksjon basert på temperatur, dato, og vindpark. Jeg fant blant annet ut at
            Kulltorp returnerer kun NULL verdier.
            Bleikevare produserer betydelig mye mer strøm enn de andre parkene.
            Dagene lekker data inn i modellen.
            Dette er fordi datasettet ble splittet slik at noen av de samme dagene ble inkludert i trenings og test settet.
            Dermed har modellen lært seg en korrelasjon som gjør at den legger høyere vekt på visse dager hvor det var høy vindhastighet og produksjon. Denne korrelasjonen er ikke reell, da det er kunstig mange variabler som er berørt av denne “dobbel-lagringen”. 
            Modellen kan for eksempel forbedres med å kjøre en random forest modell på mer data. Jeg tror modellen forbedres betraktelig med data fra flere vindparker, barometrisk trykk og forbruksdata ol. fra SE3, SE4 og potensielt andre relevante prisområder. 


            Jeg valgte å fokusere på en decision-tree regresjonsmodell. I en slik modell kan man enkelt se hvordan forskjellige valg ble tatt og hvilke features modellen la vekt på. Datasettet virket å være godt egnet for en slik modell, grunnet begrensede variabler og treningsdata som er en fordel i mer kompliserte modeller. Eksempelvis en deep learning LSTM modell. En RNN modell kan også passe, gitt tilstrekkelig data på flere variabler.I slike modeller kan data fra vær-sonar også være aktuelt. 

            Jeg kjørte også en anomaly analyse på dataene i modellen. Denne analysen er imidlertid ikke tilstrekkelig. Analysen kan forbedres ved å kjøre lignende analyser på et lavere threshold, Trolig vil vi da se utslag fra modellen som går i tråd med forventninger om anomaliteter. Min modell har en altfor lav nøyaktighetsgrad. 



            """
        ),

    ],
)

layout = dbc.Row([column1])
