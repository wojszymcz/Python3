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


@app.route('/reports')
@app.route('/reports/')
def reports():
    return template('reports')

@app.route('/reports/pst393')
def download():
    return static_file(filename="id_pst393.pdf", root="",download="id_pst393.pdf")
@app.route('/reports/pwe42')
def download():
    return static_file(filename="id_pwe42.pdf", root="",download="id_pwe42.pdf")
@app.route('/reports/pwe42')
def download():
    return static_file(filename="id_pwe42.pdf", root="",download="id_pwe42.pdf")
@app.route('/reports/pcz11')
def download():
    return static_file(filename="id_pcz11.pdf", root="",download="id_pcz11.pdf")
@app.route('/reports/pbr47')
def download():
    return static_file(filename="id_pbr47.pdf", root="",download="id_pbr47.pdf")
@app.route('/reports/pkr96')
def download():
    return static_file(filename="id_pkr96.pdf", root="",download="id_pkr96.pdf")
@app.route('/reports/pgr106')
def download():
    return static_file(filename="id_pgr106.pdf", root="",download="id_pgr106.pdf")
@app.route('/reports/pru76')
def download():
    return static_file(filename="id_pru76.pdf", root="",download="id_pru76.pdf")
@app.route('/reports/pty6')
def download():
    return static_file(filename="id_pty6.pdf", root="",download="id_pty6.pdf")
@app.route('/reports/pma1510')
def download():
    return static_file(filename="id_pma1510.pdf", root="",download="id_pma1510.pdf")
@app.route('/reports/ple212')
def download():
    return static_file(filename="id_ple212.pdf", root="",download="id_ple212.pdf")
@app.route('/reports/pmy21')
def download():
    return static_file(filename="id_pmy21.pdf", root="",download="id_pmy21.pdf")
@app.route('/reports/pci38')
def download():
    return static_file(filename="id_pci38.pdf", root="",download="id_pci38.pdf")
@app.route('/reports/pch204')
def download():
    return static_file(filename="id_pch204.pdf", root="",download="id_pch204.pdf")
@app.route('/reports/pma1081')
def download():
    return static_file(filename="id_pma1081.pdf", root="",download="id_pma1081.pdf")
@app.route('/reports/pdw12')
def download():
    return static_file(filename="id_pdw12.pdf", root="",download="id_pdw12.pdf")
@app.route('/reports/pdw12')
def download():
    return static_file(filename="id_pdw12.pdf", root="",download="id_pdw12.pdf")
@app.route('/reports/pno288')
def download():
    return static_file(filename="id_pno288.pdf", root="",download="id_pno288.pdf")
@app.route('/reports/pbi271')
def download():
    return static_file(filename="id_pbi271.pdf", root="",download="id_pbi271.pdf")
@app.route('/reports/pbi271')
def download():
    return static_file(filename="id_pbi271.pdf", root="",download="id_pbi271.pdf")
@app.route('/reports/ppa388')
def download():
    return static_file(filename="id_ppa388.pdf", root="",download="id_ppa388.pdf")
@app.route('/reports/ply18')
def download():
    return static_file(filename="id_ply18.pdf", root="",download="id_ply18.pdf")
@app.route('/reports/pva170')
def download():
    return static_file(filename="id_pva170.pdf", root="",download="id_pva170.pdf")
@app.route('/reports/pha527')
def download():
    return static_file(filename="id_pha527.pdf", root="",download="id_pha527.pdf")
@app.route('/reports/pbu145')
def download():
    return static_file(filename="id_pbu145.pdf", root="",download="id_pbu145.pdf")
@app.route('/reports/pmu412')
def download():
    return static_file(filename="id_pmu412.pdf", root="",download="id_pmu412.pdf")
@app.route('/reports/pbr274')
def download():
    return static_file(filename="id_pbr274.pdf", root="",download="id_pbr274.pdf")
@app.route('/reports/pza419')
def download():
    return static_file(filename="id_pza419.pdf", root="",download="id_pza419.pdf")
@app.route('/reports/pgu102')
def download():
    return static_file(filename="id_pgu102.pdf", root="",download="id_pgu102.pdf")
@app.route('/reports/pko253')
def download():
    return static_file(filename="id_pko253.pdf", root="",download="id_pko253.pdf")
@app.route('/reports/pog49')
def download():
    return static_file(filename="id_pog49.pdf", root="",download="id_pog49.pdf")
@app.route('/reports/pwo115')
def download():
    return static_file(filename="id_pwo115.pdf", root="",download="id_pwo115.pdf")
@app.route('/reports/ppr266')
def download():
    return static_file(filename="id_ppr266.pdf", root="",download="id_ppr266.pdf")
@app.route('/reports/pse187')
def download():
    return static_file(filename="id_pse187.pdf", root="",download="id_pse187.pdf")
@app.route('/reports/pun47')
def download():
    return static_file(filename="id_pun47.pdf", root="",download="id_pun47.pdf")
@app.route('/reports/pja256')
def download():
    return static_file(filename="id_pja256.pdf", root="",download="id_pja256.pdf")
@app.route('/reports/pza314')
def download():
    return static_file(filename="id_pza314.pdf", root="",download="id_pza314.pdf")
@app.route('/reports/pma849')
def download():
    return static_file(filename="id_pma849.pdf", root="",download="id_pma849.pdf")
@app.route('/reports/pmi663')
def download():
    return static_file(filename="id_pmi663.pdf", root="",download="id_pmi663.pdf")
@app.route('/reports/pma2533')
def download():
    return static_file(filename="id_pma2533.pdf", root="",download="id_pma2533.pdf")
@app.route('/reports/pko138')
def download():
    return static_file(filename="id_pko138.pdf", root="",download="id_pko138.pdf")
@app.route('/reports/pgr230')
def download():
    return static_file(filename="id_pgr230.pdf", root="",download="id_pgr230.pdf")
@app.route('/reports/pgr440')
def download():
    return static_file(filename="id_pgr440.pdf", root="",download="id_pgr440.pdf")
@app.route('/reports/pmo1093')
def download():
    return static_file(filename="id_pmo1093.pdf", root="",download="id_pmo1093.pdf")
@app.route('/reports/psa706')
def download():
    return static_file(filename="id_psa706.pdf", root="",download="id_psa706.pdf")
@app.route('/reports/pfa181')
def download():
    return static_file(filename="id_pfa181.pdf", root="",download="id_pfa181.pdf")
@app.route('/reports/pst419')
def download():
    return static_file(filename="id_pst419.pdf", root="",download="id_pst419.pdf")
@app.route('/reports/pla607')
def download():
    return static_file(filename="id_pla607.pdf", root="",download="id_pla607.pdf")
@app.route('/reports/pko253')
def download():
    return static_file(filename="id_pko253.pdf", root="",download="id_pko253.pdf")
@app.route('/reports/pba889')
def download():
    return static_file(filename="id_pba889.pdf", root="",download="id_pba889.pdf")
@app.route('/reports/psk7')
def download():
    return static_file(filename="id_psk7.pdf", root="",download="id_psk7.pdf")
@app.route('/reports/ppa966')
def download():
    return static_file(filename="id_ppa966.pdf", root="",download="id_ppa966.pdf")
@app.route('/reports/ppi160')
def download():
    return static_file(filename="id_ppi160.pdf", root="",download="id_ppi160.pdf")
@app.route('/reports/pry61')
def download():
    return static_file(filename="id_pry61.pdf", root="",download="id_pry61.pdf")
@app.route('/reports/pva661')
def download():
    return static_file(filename="id_pva661.pdf", root="",download="id_pva661.pdf")
@app.route('/reports/pbu485')
def download():
    return static_file(filename="id_pbu485.pdf", root="",download="id_pbu485.pdf")
@app.route('/reports/pha872')
def download():
    return static_file(filename="id_pha872.pdf", root="",download="id_pha872.pdf")
@app.route('/reports/ple519')
def download():
    return static_file(filename="id_ple519.pdf", root="",download="id_ple519.pdf")
@app.route('/reports/psz52')
def download():
    return static_file(filename="id_psz52.pdf", root="",download="id_psz52.pdf")
@app.route('/reports/pka1244')
def download():
    return static_file(filename="id_pka1244.pdf", root="",download="id_pka1244.pdf")
@app.route('/reports/pgo656')
def download():
    return static_file(filename="id_pgo656.pdf", root="",download="id_pgo656.pdf")
@app.route('/reports/pst268')
def download():
    return static_file(filename="id_pst268.pdf", root="",download="id_pst268.pdf")
@app.route('/reports/pci76')
def download():
    return static_file(filename="id_pci76.pdf", root="",download="id_pci76.pdf")
@app.route('/reports/pba1023')
def download():
    return static_file(filename="id_pba1023.pdf", root="",download="id_pba1023.pdf")
@app.route('/reports/psu231')
def download():
    return static_file(filename="id_psu231.pdf", root="",download="id_psu231.pdf")
@app.route('/reports/pwo83')
def download():
    return static_file(filename="id_pwo83.pdf", root="",download="id_pwo83.pdf")
@app.route('/reports/pwe261')
def download():
    return static_file(filename="id_pwe261.pdf", root="",download="id_pwe261.pdf")
@app.route('/reports/pst759')
def download():
    return static_file(filename="id_pst759.pdf", root="",download="id_pst759.pdf")
@app.route('/reports/prz6')
def download():
    return static_file(filename="id_prz6.pdf", root="",download="id_prz6.pdf")
@app.route('/reports/pko417')
def download():
    return static_file(filename="id_pko417.pdf", root="",download="id_pko417.pdf")
@app.route('/reports/pko566')
def download():
    return static_file(filename="id_pko566.pdf", root="",download="id_pko566.pdf")
@app.route('/reports/pda247')
def download():
    return static_file(filename="id_pda247.pdf", root="",download="id_pda247.pdf")
@app.route('/reports/pbi147')
def download():
    return static_file(filename="id_pbi147.pdf", root="",download="id_pbi147.pdf")
@app.route('/reports/pkn38')
def download():
    return static_file(filename="id_pkn38.pdf", root="",download="id_pkn38.pdf")
@app.route('/reports/ppi193')
def download():
    return static_file(filename="id_ppi193.pdf", root="",download="id_ppi193.pdf")
@app.route('/reports/pzy3')
def download():
    return static_file(filename="id_pzy3.pdf", root="",download="id_pzy3.pdf")
@app.route('/reports/pko493')
def download():
    return static_file(filename="id_pko493.pdf", root="",download="id_pko493.pdf")
@app.route('/reports/pza223')
def download():
    return static_file(filename="id_pza223.pdf", root="",download="id_pza223.pdf")
@app.route('/reports/ppa826')
def download():
    return static_file(filename="id_ppa826.pdf", root="",download="id_ppa826.pdf")
@app.route('/reports/pwe437')
def download():
    return static_file(filename="id_pwe437.pdf", root="",download="id_pwe437.pdf")
@app.route('/reports/pma1062')
def download():
    return static_file(filename="id_pma1062.pdf", root="",download="id_pma1062.pdf")
@app.route('/reports/psz65')
def download():
    return static_file(filename="id_psz65.pdf", root="",download="id_psz65.pdf")
@app.route('/reports/psz48')
def download():
    return static_file(filename="id_psz48.pdf", root="",download="id_psz48.pdf")
@app.route('/reports/pja168')
def download():
    return static_file(filename="id_pja168.pdf", root="",download="id_pja168.pdf")
@app.route('/reports/pst555')
def download():
    return static_file(filename="id_pst555.pdf", root="",download="id_pst555.pdf")
@app.route('/reports/pal855')
def download():
    return static_file(filename="id_pal855.pdf", root="",download="id_pal855.pdf")
@app.route('/reports/pgo201')
def download():
    return static_file(filename="id_pgo201.pdf", root="",download="id_pgo201.pdf")
@app.route('/reports/pfi197')
def download():
    return static_file(filename="id_pfi197.pdf", root="",download="id_pfi197.pdf")
@app.route('/reports/pgr291')
def download():
    return static_file(filename="id_pgr291.pdf", root="",download="id_pgr291.pdf")
@app.route('/reports/pja352')
def download():
    return static_file(filename="id_pja352.pdf", root="",download="id_pja352.pdf")
@app.route('/reports/pko104')
def download():
    return static_file(filename="id_pko104.pdf", root="",download="id_pko104.pdf")
@app.route('/reports/pwe303')
def download():
    return static_file(filename="id_pwe303.pdf", root="",download="id_pwe303.pdf")
@app.route('/reports/pko431')
def download():
    return static_file(filename="id_pko431.pdf", root="",download="id_pko431.pdf")
@app.route('/reports/pra573')
def download():
    return static_file(filename="id_pra573.pdf", root="",download="id_pra573.pdf")
@app.route('/reports/pki34')
def download():
    return static_file(filename="id_pki34.pdf", root="",download="id_pki34.pdf")
@app.route('/reports/pmi274')
def download():
    return static_file(filename="id_pmi274.pdf", root="",download="id_pmi274.pdf")
@app.route('/reports/pwi380')
def download():
    return static_file(filename="id_pwi380.pdf", root="",download="id_pwi380.pdf")
@app.route('/reports/psa2033')
def download():
    return static_file(filename="id_psa2033.pdf", root="",download="id_psa2033.pdf")
@app.route('/reports/pst197')
def download():
    return static_file(filename="id_pst197.pdf", root="",download="id_pst197.pdf")
@app.route('/reports/pbe727')
def download():
    return static_file(filename="id_pbe727.pdf", root="",download="id_pbe727.pdf")
@app.route('/reports/pch564')
def download():
    return static_file(filename="id_pch564.pdf", root="",download="id_pch564.pdf")
@app.route('/reports/pkl141')
def download():
    return static_file(filename="id_pkl141.pdf", root="",download="id_pkl141.pdf")
@app.route('/reports/pkl118')
def download():
    return static_file(filename="id_pkl118.pdf", root="",download="id_pkl118.pdf")
@app.route('/reports/pwo54')
def download():
    return static_file(filename="id_pwo54.pdf", root="",download="id_pwo54.pdf")
@app.route('/reports/pba1247')
def download():
    return static_file(filename="id_pba1247.pdf", root="",download="id_pba1247.pdf")
@app.route('/reports/pdb2')
def download():
    return static_file(filename="id_pdb2.pdf", root="",download="id_pdb2.pdf")
@app.route('/reports/psk39')
def download():
    return static_file(filename="id_psk39.pdf", root="",download="id_psk39.pdf")
@app.route('/reports/pja353')
def download():
    return static_file(filename="id_pja353.pdf", root="",download="id_pja353.pdf")
@app.route('/reports/pgr382')
def download():
    return static_file(filename="id_pgr382.pdf", root="",download="id_pgr382.pdf")
@app.route('/reports/pbu210')
def download():
    return static_file(filename="id_pbu210.pdf", root="",download="id_pbu210.pdf")
@app.route('/reports/pto209')
def download():
    return static_file(filename="id_pto209.pdf", root="",download="id_pto209.pdf")
@app.route('/reports/pmy15')
def download():
    return static_file(filename="id_pmy15.pdf", root="",download="id_pmy15.pdf")
@app.route('/reports/ple411')
def download():
    return static_file(filename="id_ple411.pdf", root="",download="id_ple411.pdf")
@app.route('/reports/pko306')
def download():
    return static_file(filename="id_pko306.pdf", root="",download="id_pko306.pdf")
@app.route('/reports/pbr27')
def download():
    return static_file(filename="id_pbr27.pdf", root="",download="id_pbr27.pdf")
@app.route('/reports/pga765')
def download():
    return static_file(filename="id_pga765.pdf", root="",download="id_pga765.pdf")
@app.route('/reports/pst899')
def download():
    return static_file(filename="id_pst899.pdf", root="",download="id_pst899.pdf")
@app.route('/reports/pkw4')
def download():
    return static_file(filename="id_pkw4.pdf", root="",download="id_pkw4.pdf")
@app.route('/reports/pko518')
def download():
    return static_file(filename="id_pko518.pdf", root="",download="id_pko518.pdf")
@app.route('/reports/pru58')
def download():
    return static_file(filename="id_pru58.pdf", root="",download="id_pru58.pdf")
@app.route('/reports/pby15')
def download():
    return static_file(filename="id_pby15.pdf", root="",download="id_pby15.pdf")
@app.route('/reports/psz40')
def download():
    return static_file(filename="id_psz40.pdf", root="",download="id_psz40.pdf")
@app.route('/reports/pne161')
def download():
    return static_file(filename="id_pne161.pdf", root="",download="id_pne161.pdf")
@app.route('/reports/pma2182')
def download():
    return static_file(filename="id_pma2182.pdf", root="",download="id_pma2182.pdf")
@app.route('/reports/pmi197')
def download():
    return static_file(filename="id_pmi197.pdf", root="",download="id_pmi197.pdf")
@app.route('/reports/pka834')
def download():
    return static_file(filename="id_pka834.pdf", root="",download="id_pka834.pdf")
@app.route('/reports/psk53')
def download():
    return static_file(filename="id_psk53.pdf", root="",download="id_psk53.pdf")
@app.route('/reports/pba904')
def download():
    return static_file(filename="id_pba904.pdf", root="",download="id_pba904.pdf")
@app.route('/reports/pko886')
def download():
    return static_file(filename="id_pko886.pdf", root="",download="id_pko886.pdf")
@app.route('/reports/ppr218')
def download():
    return static_file(filename="id_ppr218.pdf", root="",download="id_ppr218.pdf")
@app.route('/reports/pol97')
def download():
    return static_file(filename="id_pol97.pdf", root="",download="id_pol97.pdf")
@app.route('/reports/pol176')
def download():
    return static_file(filename="id_pol176.pdf", root="",download="id_pol176.pdf")
@app.route('/reports/pha1168')
def download():
    return static_file(filename="id_pha1168.pdf", root="",download="id_pha1168.pdf")
@app.route('/reports/pma2968')
def download():
    return static_file(filename="id_pma2968.pdf", root="",download="id_pma2968.pdf")
@app.route('/reports/pka509')
def download():
    return static_file(filename="id_pka509.pdf", root="",download="id_pka509.pdf")
@app.route('/reports/pka958')
def download():
    return static_file(filename="id_pka958.pdf", root="",download="id_pka958.pdf")
@app.route('/reports/pbr646')
def download():
    return static_file(filename="id_pbr646.pdf", root="",download="id_pbr646.pdf")
@app.route('/reports/pko856')
def download():
    return static_file(filename="id_pko856.pdf", root="",download="id_pko856.pdf")
@app.route('/reports/pch1469')
def download():
    return static_file(filename="id_pch1469.pdf", root="",download="id_pch1469.pdf")
@app.route('/reports/pko340')
def download():
    return static_file(filename="id_pko340.pdf", root="",download="id_pko340.pdf")
@app.route('/reports/pka912')
def download():
    return static_file(filename="id_pka912.pdf", root="",download="id_pka912.pdf")
@app.route('/reports/pos69')
def download():
    return static_file(filename="id_pos69.pdf", root="",download="id_pos69.pdf")
@app.route('/reports/pse644')
def download():
    return static_file(filename="id_pse644.pdf", root="",download="id_pse644.pdf")
@app.route('/reports/pcu159')
def download():
    return static_file(filename="id_pcu159.pdf", root="",download="id_pcu159.pdf")
@app.route('/reports/pde1449')
def download():
    return static_file(filename="id_pde1449.pdf", root="",download="id_pde1449.pdf")
@app.route('/reports/pwe470')
def download():
    return static_file(filename="id_pwe470.pdf", root="",download="id_pwe470.pdf")
@app.route('/reports/pab510')
def download():
    return static_file(filename="id_pab510.pdf", root="",download="id_pab510.pdf")
@app.route('/reports/ppa1025')
def download():
    return static_file(filename="id_ppa1025.pdf", root="",download="id_ppa1025.pdf")
@app.route('/reports/pbr449')
def download():
    return static_file(filename="id_pbr449.pdf", root="",download="id_pbr449.pdf")
@app.route('/reports/pku368')
def download():
    return static_file(filename="id_pku368.pdf", root="",download="id_pku368.pdf")
@app.route('/reports/pha727')
def download():
    return static_file(filename="id_pha727.pdf", root="",download="id_pha727.pdf")
@app.route('/reports/psh760')
def download():
    return static_file(filename="id_psh760.pdf", root="",download="id_psh760.pdf")
@app.route('/reports/pbr427')
def download():
    return static_file(filename="id_pbr427.pdf", root="",download="id_pbr427.pdf")
@app.route('/reports/pbi381')
def download():
    return static_file(filename="id_pbi381.pdf", root="",download="id_pbi381.pdf")
@app.route('/reports/pni435')
def download():
    return static_file(filename="id_pni435.pdf", root="",download="id_pni435.pdf")
@app.route('/reports/pso638')
def download():
    return static_file(filename="id_pso638.pdf", root="",download="id_pso638.pdf")
@app.route('/reports/psa1533')
def download():
    return static_file(filename="id_psa1533.pdf", root="",download="id_psa1533.pdf")
@app.route('/reports/ppi301')
def download():
    return static_file(filename="id_ppi301.pdf", root="",download="id_ppi301.pdf")
@app.route('/reports/pmi961')
def download():
    return static_file(filename="id_pmi961.pdf", root="",download="id_pmi961.pdf")
@app.route('/reports/pwi440')
def download():
    return static_file(filename="id_pwi440.pdf", root="",download="id_pwi440.pdf")
@app.route('/reports/pza316')
def download():
    return static_file(filename="id_pza316.pdf", root="",download="id_pza316.pdf")
@app.route('/reports/pki624')
def download():
    return static_file(filename="id_pki624.pdf", root="",download="id_pki624.pdf")
@app.route('/reports/pdy22')
def download():
    return static_file(filename="id_pdy22.pdf", root="",download="id_pdy22.pdf")
@app.route('/reports/pha661')
def download():
    return static_file(filename="id_pha661.pdf", root="",download="id_pha661.pdf")
@app.route('/reports/pkr327')
def download():
    return static_file(filename="id_pkr327.pdf", root="",download="id_pkr327.pdf")
@app.route('/reports/ple518')
def download():
    return static_file(filename="id_ple518.pdf", root="",download="id_ple518.pdf")
@app.route('/reports/pmu665')
def download():
    return static_file(filename="id_pmu665.pdf", root="",download="id_pmu665.pdf")
@app.route('/reports/pry42')
def download():
    return static_file(filename="id_pry42.pdf", root="",download="id_pry42.pdf")
@app.route('/reports/pan562')
def download():
    return static_file(filename="id_pan562.pdf", root="",download="id_pan562.pdf")
@app.route('/reports/ppi478')
def download():
    return static_file(filename="id_ppi478.pdf", root="",download="id_ppi478.pdf")
@app.route('/reports/psz13')
def download():
    return static_file(filename="id_psz13.pdf", root="",download="id_psz13.pdf")
@app.route('/reports/pga595')
def download():
    return static_file(filename="id_pga595.pdf", root="",download="id_pga595.pdf")
@app.route('/reports/pba1340')
def download():
    return static_file(filename="id_pba1340.pdf", root="",download="id_pba1340.pdf")
@app.route('/reports/pwe514')
def download():
    return static_file(filename="id_pwe514.pdf", root="",download="id_pwe514.pdf")
@app.route('/reports/pna591')
def download():
    return static_file(filename="id_pna591.pdf", root="",download="id_pna591.pdf")
@app.route('/reports/pto568')
def download():
    return static_file(filename="id_pto568.pdf", root="",download="id_pto568.pdf")
@app.route('/reports/pci152')
def download():
    return static_file(filename="id_pci152.pdf", root="",download="id_pci152.pdf")
@app.route('/reports/pan556')
def download():
    return static_file(filename="id_pan556.pdf", root="",download="id_pan556.pdf")
@app.route('/reports/pch1803')
def download():
    return static_file(filename="id_pch1803.pdf", root="",download="id_pch1803.pdf")
@app.route('/reports/pra935')
def download():
    return static_file(filename="id_pra935.pdf", root="",download="id_pra935.pdf")
@app.route('/reports/pki490')
def download():
    return static_file(filename="id_pki490.pdf", root="",download="id_pki490.pdf")
@app.route('/reports/pjd1')
def download():
    return static_file(filename="id_pjd1.pdf", root="",download="id_pjd1.pdf")
@app.route('/reports/pwo314')
def download():
    return static_file(filename="id_pwo314.pdf", root="",download="id_pwo314.pdf")
@app.route('/reports/ppi491')
def download():
    return static_file(filename="id_ppi491.pdf", root="",download="id_ppi491.pdf")
@app.route('/reports/psa504')
def download():
    return static_file(filename="id_psa504.pdf", root="",download="id_psa504.pdf")
@app.route('/reports/pgt6')
def download():
    return static_file(filename="id_pgt6.pdf", root="",download="id_pgt6.pdf")


if __name__ == '__main__':
    run(app, host='localhost', port = 8080, debug = True)



