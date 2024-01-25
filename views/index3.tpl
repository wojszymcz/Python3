<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/styles.css">
    <link rel="stylesheet" type="text/css" href="/static/font.css">
    <title>O projekcie</title>
</head>
<body>
    <div class="container">
        <h1>O projekcie</h1>
        <h3> Tymoteusz Mętrak & Wojciech Szymczak </h3>
<div>
<p style="text-align: justify;">Nasza praca ma na celu zbadanie najbardziej cytowanych polskich ekonomist&oacute;w według platformy REPEC.</p>
<p style="text-align: justify;">Zczytuję nazwiska i imiona najbardziej cytowanych polskich ekonomist&oacute;w według bazy repec ze strony: https://ideas.repec.org/top/top.poland.html. Do tego wykorzystam m.in. pakiet Beautiful Soup. Z tej strony otrzymam dwie tabele zawierające:</p>
<ul style="text-align: justify;">
<li>imię i nazwisko ekonomisty;</li>
<li>instytucję, do kt&oacute;rej jest afiliowany;</li>
<li>link do jego strony na <a href="https://ideas.repec.org;">REPEC;</a></li>
<li>unikalne ID wsp&oacute;lne dla całej sieci REPEC;</li>
<li>numer rankingowy;'score', czyli wyliczoną przez REPEC statystykę stanowiącą o jakości naukowca; im niższa, tym lepszy ekonomista.</li>
</ul>
<p style="text-align: justify;">Jedna z tabel będzie zawierać najbardziej cytowanych polskich ekonomist&oacute;w wszech czas&oacute;w, a druga tych najbardziej cytowanych w ostatnich 10 latach. Na dalszym etapie połączymy obie tabele.<br />Z powyższej strony kluczową informacją będzie dla mnie ID. Wykorzystam je p&oacute;źniej, aby pobrać dane o cytowaniach, publikacjach itp., kt&oacute;re są dostępne na stronie <a href="https://citec.repec.org/p/index.html">CITEC</a>.</p>
<div>
<p>W dalszej części wykorzystujemy zebrane dane do wizualizacji informacji o polskich ekonomistach. Zasadniczo ta część ma na celu atrakcyjne zaprezentowanie danych, przed rozpoczęciem szerszej analizy empirycznej.</p>
<h5>Przy pomocy narzędzi wizualizacji danych, spr&oacute;bujemy odpowiedzieć na następujące pytania:</h5>
<ul>
<li>Czy pozycja ekonomistek jest znacząco niższa niż ekonomist&oacute;w? Jeśli tak, to czy są instytucje, kt&oacute;re szerzej promują r&oacute;wnościowy rozw&oacute;j mężczyzn i kobiet? Czy wpływa to na konkurencyjność jednostki?</li>
<li>Czy na przełomie lat obserwujemy zmianę w zakresie preferowanych form upubliczniania wiedzy? Czy starsi autorzy publikowali więcej książek, a młodsi artykuł&oacute;w?</li>
<li>Czy autorzy, kt&oacute;rych nazwisko zaczyna się na jedną z pierwszych liter alfabetu, mogą liczyć na więcej cytowań?</li>
</ul>
<p>Finalnie, na podstawie analizy sieci społecznych odpowiemy na pytania dotyczących powiązań między ekonomistami w kraju. </p>
<h5> Zweryfikujemy: </h5>
<ul>
<li>Jak przebiega wsp&oacute;łpraca między instytucjami naukowymi w Polsce;</li>
<li>Jak przebiega wsp&oacute;łpraca między generecjami;</li>
<li>Kt&oacute;re z ośrodk&oacute;w są centralne dla wsp&oacute;łracy w Polsce</li>
</ul>
<p>Finalnie, użytkownik będzie m&oacute;gł pobrać dokument pdf zawierający szczeg&oacute;łowe dane dotyczące pracownika naukowego.&nbsp;&nbsp;</p>
</div>
<hr>
<p><a href="/">Wróć do Strony Głównej</a></p>
    </div>
</body>
</html>