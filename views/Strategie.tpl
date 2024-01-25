% rebase('base.tpl', title='Kariera Ekonomistow Polskich')
<!DOCTYPE html>
<html lang="en">
</head>
<body>
    <div class="container">
        <h2>Strategie publikacyjne według dekad działalności naukowej</h2>
        <h3>Czyli czy kiedyś pisało się więcej książek?</h3>
        <p> Strategie naukowców ulegają zmiany w czasie. Część, nierzadko starszych ekonomistów, uważa, że potencjał naukowy ujawnia się przede wszystkim w książkach. Stanowią one dojrzałe spojrzenie na problem i wymagają większego nakładu czasu. </p>
        <p> Z drugiej strony, przygotowanie artykułów również wymaga czasu, a częściej docierają do szerszej międzynarodowej populacji. </p>
        <p> Wykresy zaprezentowane poniżej pokazują ewidentne zmiany w prowadzeniu kariery naukowej wśród ekonomistów </p>

        <div id="plotlyContainer2">
        <h3> Książki </h3>
            {{!books_html}}
        </div>
        <p></p>
        <p></p>
          <div id="plotlyContainer2">
          <h3> Publikacje naukowe </h3>
            {{!papers_html}}
            <hr>
            <p><a href="/">Wróć do Strony Głównej</a></p>
        </div>
    </div>
</body>
</html>
