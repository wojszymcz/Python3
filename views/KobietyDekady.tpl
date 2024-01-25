% rebase('base.tpl', title='Kariera Ekonomistow Polskich')
<!DOCTYPE html>
<html lang="en">
</head>
<body>
    <div class="container">
        <h2>Różnice w osiągnięciach publikacyjnych między kobietami a mężczyznami</h2>
        <h3> Ekonomiści i Ekonomistki, a Indeks Hirscha </h3>
        <p> Poniżej prezentujemy wykres skrzypcowy pokazujący różnice w indeksie Hirscha między kobietami a mężczyznami. Widzimy, że wśród naukowców, którzy zaczęli pracę naukową a latach 1975 - 1995, żadna z ekonomistek nie jest w bazie Repec. W latach późniejszych, kobiety pojawiają się w rankingu RePec, ale wciąż osiągają wyniki niższe niż mężczyźni </p>
        <p> Wśród kobiet, rozkład gęstości jest bardziej skupiony wokół mediany. W kontraście, wśród mężczyzn widzimy więcej obserwacji odstających.
        <div id="plotlyContainer1">
            {{!plot_html1}}
        </div>
        <p></p>
        <h3> Które Instytucje promują równość między kobietami a mężczyznami? </h3>
        <p> Pod względem Cytowań, i H-index dobrze wypadają przede wszystkim GRAPE, PAN</p>
        <p> Wykres prezentujący liczbę naukowców ujętych w rankingu znacznie odbiega od rankingu cytowań i H-index </p>
          <div id="plotlyContainer2">
            {{!plot_html2}}
        </div>
    </div>
    <h3> Czy instytucje, w których wyniki kobiet są porównywalne do mężczyzn, są wyżej w rankingu?</h3>
    <p> Zdrowa konkurencja między kobietami a mężczyznami może stanowić podstawę do wyższych wyników dla  </p>
    <p> W kontraście, ścisła przewaga jednej z płci może stanowić "sufit" i zniechęcać do efektywnej pracy. Jednocześnie, instytucje charakteryzujące się równością płci mogą wewnętrznie wprowadzać plany zapewniające równość płci (np. IBS, GRAPE).  </p>
     <div id="plotlyContainer3">
            {{!plot_html3 }}
     </div>
     <div id="plotlyContainer4">
            {{!plot_html4}}
     </div>
    <hr>
            <p><a href="/">Wróć do Strony Głównej</a></p>

</body>
</html>


