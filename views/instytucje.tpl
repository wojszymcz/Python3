% rebase('base.tpl', title='Kariera Ekonomistow Polskich')

<div class="container">
        <h1>Główne instytucje, w których pracują polscy ekonomiści</h1>
        <p>Wykres i tabela zawierają 14 instytucji z największą liczbą cytowań, w których pracują analizowani ekonomiści. W przypadkach, gdy osoba zadeklarowała afiliację do kilku instytucji, brano pod uwagę jedynie instytucję główną, którą ekonomista podałjako pierwszą. Z bazy usunięto te instytucje, w których pracowało jedynie po kilka osób.</p>
        <p>Poniżej znajduje się tabela ze statystykami dla instytucji.</p>
        <p><a href="/instytucje/download">Możesz też pobrać tabelę w formacie csv</a></p>
        <div id="tableContainer">
            {{!instytucje_html_plotly}}
            <hr>
            <p><a href="/main/">Wróć do Strony Głównej</a></p>
        </div>
    </div>

