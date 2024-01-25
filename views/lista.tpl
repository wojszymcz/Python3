% rebase('base.tpl', title='Kariera Ekonomistow Polskich')


<select id="postacie" onchange="pokazDane()">
  <option value="Oded Stark">Oded Stark</option>
  <option value="Rafal Weron">Rafal Weron</option>
  <option value="Marcin Kolasa	">Marcin Kolasa</option>
  <!-- Dodaj więcej postaci, jeśli potrzebujesz -->
</select>


<script>
  function pokazDane() {
    // Pobierz wybraną wartość z listy rozwijanej
    var wybranaPostac = document.getElementById("postacie").value;

    // Odczytaj plik CSV (symulacja, w rzeczywistości możesz użyć Fetch API lub innej metody)
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'Polish_all_economists_24_01.csv', true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        // Podziel dane CSV na wiersze i kolumny
        var wiersze = xhr.responseText.split('\n');
        var kolumny = wiersze[0].split(',');

        // Znajdź indeks kolumny "Autor"
        var indeksKolumny = kolumny.indexOf('Autor');

        // Szukaj danych o wybranej postaci
        for (var i = 1; i < wiersze.length; i++) {
          var dane = wiersze[i].split(',');
          if (dane[indeksKolumny] == wybranaPostac) {
            var h_index = dane[kolumny.indexOf('H_index')];
            var cytowania = dane[kolumny.indexOf('Cytowania')];
            var articles = dane[kolumny.indexOf('Artykuły')];
            var books = dane[kolumny.indexOf('Książki')];
            var institution = dane[kolumny.indexOf('Instytucja_short')];

            // Wyświetl dane w elemencie o id "wynik"
            document.getElementById("wynik").innerHTML = "H_index: " + h_index + ", Cytowania: " + cytowania + ", Artykuły: " + articles + ", Książki: " + books + ", Instytucja: " + institution;
            break;  // Zakończ pętlę po znalezieniu danych
          }
        }
      }
    };
    xhr.send();
  }
  pokazDane()
</script>

<!-- Wyświetlacz danych o postaci -->
<div id="wynik"></div>