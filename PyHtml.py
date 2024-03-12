import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import module.GET as GET
import time

str_server = GET.INNERIP()
dns_server = "182.213.254.158"

time_check = []

def backend_recall():
    if len(time_check) != 0:
        average = sum(time_check) / len(time_check)
        print(f"백엔드 프래임워크 평균 응답 속도 -> {average}")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], update_title=False, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.Div(id='output-div'), 
    html.Div(id='output-div2'), 
])

index_page = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Form([
                    dbc.Input(type="text", id="register-username-input", placeholder="Uid", style={'width': '80%'}),
                    dbc.Label(className="form-label"),
                    dbc.Input(type="password", id="register-password-input", placeholder="Password", style={'width': '80%'}),
                    dbc.Button("Login", id="register-button", color="primary", className="mt-3", style={"margin-right": "10px"}),
                ], style={'width': '100%', 'maxWidth': '500px', 'padding': '20px'}),
            ], style={'width': '100%', 'maxWidth': '600px', 'padding': '10px', 'borderRadius': '15px'})
        ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'height': '100vh'})
    ])
], fluid=True)


register_page = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.Form([
                    dbc.Input(type="text", id="register-username-input", placeholder="Uid", style={'width': '80%'}),
                    dbc.Label(className="form-label"),
                    dbc.Input(type="password", id="register-password-input", placeholder="Password", style={'width': '80%'}),
                    dbc.Button("Register", id="register-button", color="primary", className="mt-3", style={"margin-right": "10px"}),
                ], style={'width': '100%', 'maxWidth': '500px', 'padding': '20px'}),
            ], style={'width': '100%', 'maxWidth': '600px', 'padding': '10px', 'borderRadius': '15px'})
        ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'height': '100vh'})
    ])
], fluid=True)

@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/register':
        return register_page
    else:
        return index_page

@app.callback(
    Output('username-input', 'value'),
    Output('password-input', 'value'),
    Input('login-button', 'n_clicks'),  # 'login-button'으로 수정하였습니다.
    State('username-input', 'value'),
    State('password-input', 'value')
)
def update_login_output(n_clicks, username, password):
    if n_clicks is not None:
        print('로그인 시도: 아이디는 "{}", 비밀번호는 "{}"'.format(username, password))
        set_time = time.time()
        GET.GET(str_server, dns_server, 2193, 8000, {'UID': [username], 'Password': [password]})
        destination_time = time.time()
        time_check.append(destination_time - set_time)
        backend_recall()
        return '', ''
    return username, password

@app.callback(
    Output('register-username-input', 'value'),
    Output('register-password-input', 'value'),
    Input('register-button', 'n_clicks'),  # 'register-button'으로 수정하였습니다.
    State('register-username-input', 'value'),
    State('register-password-input', 'value')
)
def update_register_output(n_clicks, username, password):
    if n_clicks is not None:
        print('등록 시도: 아이디는 "{}", 비밀번호는 "{}"'.format(username, password))
        set_time = time.time()
        GET.GET(str_server, dns_server, 2193, 8000, {'UID': [username], 'Password': [password]})
        destination_time = time.time()
        time_check.append(destination_time - set_time)
        backend_recall()
        return '', ''
    return username, password

if __name__ == '__main__':
    app.run_server(debug=True, host=str_server, port=80)
