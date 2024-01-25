# Szymczak Wojciech, Mętrak Tymoteusz
# Język Python dla Analityków Danych

# Importujemy potrzebne pakiety
from bottle import Bottle, run, view, template, static_file
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import networkx as nx

# Inicjujemy aplikację
app = Bottle()

# Strona Główna
@app.route('/')
@app.route('/main')
@app.route('/main/')
def glowna():

    # Wczytujemy pakiet danych do wizualizacji sieciowej
    df_edges = pd.read_csv("df_edges.csv")
    df_edges = df_edges[pd.notna(df_edges["Instytucja_shorter"])]

    # Inicujemy graf
    G = nx.Graph()

    # Tworzymy węzły + dodajemy atrybuty
    for index, row in df_edges.iterrows():
        person = row['Instytucja_shorter']
        decade = row['decade']
        sex = row['Płeć']
        G.add_node(person, decade=decade, sex=sex)

    # Dodajemy połączenia
    for index, row in df_edges.iterrows():
        person = row['Instytucja_shorter']
        contact = row['Instytucja_2_shorter']
        # Skip adding edge if either 'person' or 'contact' is None
        if pd.notna(person) and pd.notna(contact):
            G.add_edge(person, contact, weight=1)
    # Wykorzystujemy arf layout
    pos = nx.arf_layout(G)

    # Modyfikujemy zbiór danych pod rysunek
    # Ekstraktujemy dane o połączeniach
    node_x = [pos[node][0] for node in G.nodes]
    node_y = [pos[node][1] for node in G.nodes]

    # Węzły
    edge_x = []
    edge_y = []
    for edge in G.edges:
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Rysunek dla połączeń
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        showlegend= False
    )

    # Rysunek dla węzłów
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    # Tworzymy labele dla opisania instytucji
    label_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=list(G.nodes),
        textposition="bottom center",
        marker=dict(size=10, color='orange')
    )

    # Zapisujemy do wykresu z plotly
    network = go.Figure(data=[edge_trace, node_trace, label_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=0),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    # Zapisujemy do html
    network_html = network.to_html()

    # Zwracamy stronę z index_old2 + argument jako utworzoną sieć
    return template('index_old2', network_html = network_html)

# Strona robocza do edycji
@app.route('/old')
def glowna():
    return template('index_old2')

# Informacje o projekcie
@app.route('/oProjekcie')
def oProjekcie():
    return template('o_projekcie')

# Równość płci
@view('KobietyDekady.tpl')
@app.route('/KobietyDekady')
def index():
    # Wczytujemy dane
    data = pd.read_csv("data_updcated.csv")

    # Tworzymy wykresy skrzypcowe dla płci
    fig1 = go.Figure()
    fig1.add_trace(go.Violin(x = data['decade'][data['Płeć'] == 'M'],
                            y = data['H_index'][data['Płeć'] == 'M'],
                            legendgroup = 'M', scalegroup = 'M', name = 'M',
                            side = 'positive',
                            line_color='#543345')
                  )
    fig1.add_trace(go.Violin(x=data['decade'][data['Płeć'] == 'K'],
                            y=data['H_index'][data['Płeć'] == 'K'],
                            legendgroup='K', scalegroup='K', name='K',
                            side = 'negative',
                            line_color = '#e2b3ab')
                  )
    fig1.update_traces(meanline_visible=True,
                      points='all',  # show all points
                      jitter=0.05,  # add some jitter on points for better visibility
                      scalemode='count')  # scale violin plot area with total count
    fig1.update_layout(
        title_text="Rozkład Indeksu Hirscha według płci i dekady",
        violingap=0, violinmode='overlay')
    fig1.update_yaxes(showgrid=False)

    # Konwertujemy wykres do html
    plot_html1 = fig1.to_html(full_html = False)

    # Wczytujemy drugi zbiór danych
    aggs_wide = pd.read_csv("data_aggregated.csv")

    # Sortujemy dane (zbieramy indeksy), żeby narysować wykresy słupkowe według wartości na osi OX
    # Citation_ratio
    sorted_indices_citation = aggs_wide['Citation_ratio'].sort_values(ascending=False).index
    # Sortujemy dane
    sorted_data_citation = aggs_wide.loc[sorted_indices_citation]

    # H_index_ratio
    sorted_indices_h_index = aggs_wide['H_index_ratio'].sort_values(ascending=False).index
    # Sortujemy dane
    sorted_data_h_index = aggs_wide.loc[sorted_indices_h_index]

    # Number_ratio
    sorted_indices_number = aggs_wide['Number_ratio'].sort_values(ascending=False).index
    # Sortujemy dane
    sorted_data_number = aggs_wide.loc[sorted_indices_number]

    # Tworzymy wspólny wykres - 3 rzędy w jednej kolumnie
    fig2 = make_subplots(rows=3,
                         cols=1,
                         subplot_titles=('Citation Ratio', 'H-Index Ratio', 'Number Ratio'))

    # Plot Citation Ratio
    fig2.add_trace(go.Bar(x=sorted_data_citation['Instytucja_shorter'], y=sorted_data_citation['Citation_ratio'],
                          customdata=[sorted_data_citation['Instytucja_shorter'],
                                      sorted_data_citation['Citation_ratio']],
                          marker=dict(color="blue")),
                   row=1, col=1)

    # Plot H-Index Ratio
    fig2.add_trace(go.Bar(x=sorted_data_h_index['Instytucja_shorter'], y=sorted_data_h_index['H_index_ratio'],
                          customdata=[sorted_data_h_index['Instytucja_shorter'], sorted_data_h_index['H_index_ratio']],
                          marker=dict(color="green")),
                   row=2, col=1)

    # Plot Number Ratio
    fig2.add_trace(go.Bar(x=sorted_data_number['Instytucja_shorter'], y=sorted_data_number['Number_ratio'],
                          customdata=[sorted_data_number['Instytucja_shorter'], sorted_data_number['Number_ratio']],
                          marker=dict(color="orange")),
                   row=3, col=1)

    fig2.update_layout(
        xaxis = dict(tickangle=-90),
        height = 2000,  # You can adjust the height as needed
        showlegend=False,
        title_text = "Wskaźniki dla instytucji naukowych ",
        title_x=0.5,  # Center the title
        margin=dict(b=200, t=50, r = 10)
    )

    # Zmieniamy kąt nachylenia osi OX
    fig2.update_xaxes(tickangle=-45, row=1, col=1)
    fig2.update_xaxes(tickangle=-45, row=2, col=1)
    fig2.update_xaxes(tickangle=-45, row=3, col=1)

    # Konwertujemy do  HTML
    plot_html2 = fig2.to_html(full_html=False)

    # Wczytujemy dane
    aggs_total = pd.read_csv("aggs_total.csv")

    # Rysujemy dwa scatter ploty
    fig3 = px.scatter(aggs_total, x="H_index_ratio", y="H_index",
                     size='Auto_cytowania', hover_data=['Auto_cytowania'],
                     marginal_x="histogram", marginal_y="rug",
                     trendline="ols")

    fig4 = px.scatter(aggs_total, x = "Citation_ratio", y = "Cytowania",
                      size = 'Auto_cytowania', hover_data = ['Auto_cytowania'],
                      marginal_x = "histogram", marginal_y = "rug",
                      trendline = "ols")

    plot_html3 = fig3.to_html()
    plot_html4 = fig4.to_html()


    # Zwracamy stronę + skonwertowane pliki HTML
    return template('KobietyDekady', plot_html1 = plot_html1,  plot_html2 = plot_html2, plot_html3 = plot_html3, plot_html4 = plot_html4)

# # Route for serving static files (CSS in this case)
# @app.route('/static/<filename:path>')
# def serve_static(filename):
#     return static_file(filename, root = './static')

# Sekcja dotycząca eksportu danych - o ekonomsitach
@app.route('/tabela')
def tabela():
    data_all = pd.read_csv("Polish_all_economists_24_01.csv")
    data_all = data_all.drop(data_all.columns[0], axis = 1)

# Korzystamy z tabeli z plotly dla poprawienia estetyki
    data_tabela = go.Figure(data=[go.Table(
        header=dict(values=['Autor',
                            'ID',
                            'Instytucja',
                            'Płeć',
                            'H_index',
                            'i10_index',
                            'Cytowania',
                            'Auto_cytowania'],
                    fill_color='#a0606e',
                    align='left'),
        cells=dict(values = [data_all['Autor'],
                                data_all['ID'],
                                data_all['Rank'],
                                data_all['W.Rank'],
                                data_all['Instytucja'],
                                data_all['Płeć'],
                                data_all['H_index'],
                             data_all['i10_index'],
                             data_all['Cytowania'],
                             data_all['Auto_cytowania']] ,
                   fill_color= '#e2b3ab',
                   align='left'
                   ))
    ])
    data_tabela.update_layout(
        autosize=True)

    tabela_plotly_html = data_tabela.to_html()
    return template('tabela', data = data_all, tabela_plotly_html = tabela_plotly_html)

# Sciezka z pobraniem tabeli
@app.route('/tabela/download/')
@app.route('/tabela/download')
def download():
    return static_file(filename = "Polish_all_economists_24_01.csv", root = "",download = "Polish_all_economists_24_01.csv")

# Tabela z instytucjami
@app.route('/instytucje')
@app.route('/instytucje/')
def instytucje():
    data_inst = pd.read_csv("Leading_institutions.csv")
    data_inst = data_inst.drop(data_inst.columns[0], axis=1)
    tabela_instytucje = go.Figure(data=[go.Table(
        header=dict(values=['Nazwa instytucji',
                            'Cytowania Kobiety',
                            'Cytowania Mężczyźni',
                            'H-index Kobiety',
                            'H-index Mężczyźni',
                            'Auto cytowania Kobiety',
                            'Auto cytowania Mężczyźni'],
                    fill_color='#a0606e',
                    align='left'),
        cells=dict(values=[ data_inst['Instytucja_shorter'],
                            data_inst['Cytowania K'],
                            data_inst['Cytowania M'],
                            data_inst['H_index K'],
                            data_inst['H_index M'],
                            data_inst['Auto_cytowania K'],
                            data_inst['Auto_cytowania M']],
                   fill_color='#e2b3ab',
                   align='left'
                   ))
    ])
    tabela_instytucje.update_layout(
        autosize=True)
    instytucje_html_plotly = tabela_instytucje.to_html()
    return template('instytucje', data = data_inst, instytucje_html_plotly = instytucje_html_plotly)

# Pobierz dane o instytucjach
@app.route('/instytucje/download/')
@app.route('/instytucje/download')
def download():
    return static_file(filename="Leading_institutions.csv", root="",download="Leading_institutions.csv")

@app.route('/lista')
def lista():
    return template('lista')

# Wizualizacja różnic w strategiach
@app.route('/Strategie')
def Strategie():
    # Wczytanie danych
    data = pd.read_csv("data_updcated.csv")
    zbior = data[["Artykuły", "Książki", "decade"]]
    zbior.Książki[np.isnan(zbior.Książki)] = 0
    colors = ['#543345', '#724354', '#a0606e', '#dd8a95', '#e2b3ab']
    books = go.Figure()
    papers = go.Figure()

    # Modyfikujemy dane - iterujemy po parach danych dekada, utworzony kolor
    for category, color in zip(zbior["decade"].sort_values().unique(), colors):
        # Wybieramy dane tylko dla okreslonej dekady
        books_data = zbior['Książki'][zbior.decade == category]

        # Rysujemy wykres skrzypcowy dla wybranej dekady
        books.add_trace(go.Violin(x= books_data, y=[category] * len(books_data),
                                line_color=color, meanline_visible = True))

    # Update layout + charakterystyki wykresu
    books.update_traces(orientation = 'h', side = 'positive', width = 2, points = False)
    books.update_layout(xaxis_showgrid = False, xaxis_zeroline = False, yaxis = dict(categoryorder = 'category ascending'))

    books_html = books.to_html()

    # To samo dla artykułów
    for category, color in zip(zbior["decade"].sort_values().unique(), colors):

        papers_data = zbior['Artykuły'][zbior.decade == category]

        papers.add_trace(go.Violin(x= papers_data, y=[category] * len(papers_data),
                                line_color = color, meanline_visible = True))

    papers.update_traces(orientation='h', side='positive', width=2, points=False)
    papers.update_layout(xaxis_showgrid=False, xaxis_zeroline=False, yaxis=dict(categoryorder='category ascending'))

    papers_html = papers.to_html()
    return template('Strategie', data = data, books_html = books_html, papers_html = papers_html)


# Start aplikacji

if __name__ == '__main__':
    run(app, host='localhost', port = 8080, debug = True)



