% rebase('base.tpl', title='Kariera Ekonomistow Polskich')

<div class="container">
        <h1>Raporty PDF o polskich ekonomistach</h1>
        <p>Poniżej znajduje się lista, z której można wybrać ekonomistę, o którym raport chce się pobrać. Raporty w formacie PDF zawierają podstawowe informacje o karierze naukowej: afiliację, liczbę cytowań i autocytowań, a także H-index. Ponadto, w raporcie znajdują się wybrane publikacje (wraz z adresem DOI) pobrane z usługi CrossRef na podstawie imienia i nazwiska.</p>

    </div>


<select id="postacie" onchange="pokazDane()">
  <option value="pst393">Oded Stark</option>
  <option value="pwe42">Rafal Weron</option>
  <option value="pko253">Marcin Kolasa</option>
  <option value="pcz11">Mikolaj Czajkowski</option>
  <option value="pbr47">Michal Brzoza-Brzezina</option>
  <option value="pkr96">Michal Wiktor Krawczyk</option>
  <option value="pgr106">Jakub Growiec</option>
  <option value="pru76">Michal Rubaszek</option>
  <option value="pty6">Joanna Tyrowicz</option>
  <option value="pma1510">Katarzyna Maciejowska</option>
  <option value="ple212">Piotr Lewandowski</option>
  <option value="pmy21">Michal Myck</option>
  <option value="pci38">Andrzej Cieslik</option>
  <option value="pch204">Wojciech W. Charemza</option>
  <option value="pma1081">Krzysztof Makarski</option>
  <option value="pdw12">Piotr Dworczak</option>
  <option value="pno175">Jakub Nowotarski</option>
  <option value="pno288">Andrzej Nowak</option>
  <option value="pbi271">Marcin Bielecki</option>
  <option value="pkl107">Andrzej Klimczuk</option>
  <option value="ppa388">Aleksandra Parteka</option>
  <option value="ply18">Tomasz Lyziak</option>
  <option value="pva170">Andre van Stel</option>
  <option value="pha527">Jan Hagemejer</option>
  <option value="pbu145">Domenico Buccella</option>
  <option value="pmu412">Jakub Muck</option>
  <option value="pbr274">Michal Brzezinski</option>
  <option value="pza419">Adam Zaremba</option>
  <option value="pgu102">Henryk Gurgul</option><option value="pko253">Marcin Kolasa</option>
  <option value="pog49">Wlodzimierz Ogryczak</option>
  <option value="pwo115">Joanna Wolszczak-Derlacz</option>
  <option value="ppr266">Jacek Prokop</option>
  <option value="pse187">Dobromil Serwa</option>
  <option value="pun47">Bartosz Uniejewski</option>
  <option value="pja256">Joanna Janczura</option>
  <option value="pza314">Ewa Zawojska</option>
  <option value="pma849">Iga Magda</option>
  <option value="pmi663">Slawomir Smiech</option>
  <option value="pma2533">Grzegorz Marcjasz</option>
  <option value="pko138">Przemyslaw Kowalski</option>
  <option value="pgr230">Lukasz Grzybowski</option>
  <option value="pgr440">Marek Gora</option>
  <option value="pmo1093">Marian W. Moszoro</option>
  <option value="psa706">Karolina Safarzynska</option>
  <option value="pfa181">Jan Falkowski</option>
  <option value="pst419">Pawel Strzelecki</option>
  <option value="pla607">Krzysztof Drachal</option>
  <option value="pko253">Lukasz Lach</option>
  <option value="pba889">Anna Malgorzata Bartczak</option>
  <option value="psk7">Marinko Skare</option>
  <option value="ppa966">Monika Papiez</option>
  <option value="ppi160">Michal Bernard Pietrzak</option>
  <option value="pry61">Krzysztof Rybinski</option>
  <option value="pva661">Lucas Augusto van der Velde</option>
  <option value="pbu485">Wiktor Budzinski</option>
  <option value="pha872">Wojciech Hardy</option>
  <option value="ple519">Robert Slepaczuk</option>
  <option value="psz52">Katarzyna Sznajd-Weron</option>
  <option value="pka1244">Magdalena Kapelko</option>
  <option value="pgo656">Karolina Goraus-Tanska</option>
  <option value="pst268">Anna Staszewska-Bystrova</option>
  <option value="pci76">Piotr Cizkowicz</option>
  <option value="pba1023">Lukasz Balbus</option>
  <option value="psu231">Jacek Suda</option>
  <option value="pwo83">Lukasz Patryk Wozny</option>
  <option value="pwe261">Aleksander Welfe</option>
  <option value="pst759">Ewa Stanislawska</option>
  <option value="prz6">Andrzej Rzonca</option>
  <option value="pko417">Andrzej Kociecki</option>
  <option value="pko566">Anna Kowalska-Pyzalska</option>
  <option value="pda247">Marek Pawel Dabrowski</option>
  <option value="pbi147">Yuriy Bilan</option>
  <option value="pkn38">Malgorzata Knauff</option>
  <option value="ppi193">Mateusz Pipien</option>
  <option value="pzy3">Tomasz Zylicz</option>
  <option value="pko493">Martyna Kobus</option>
  <option value="pza223">Katarzyna Zawalinska</option>
  <option value="ppa826">Malgorzata Pawlowska</option>
  <option value="pwe437">Aleksander Weron</option>
  <option value="pma1062">Anna Matysiak</option>
  <option value="psz65">Karol Szafranek</option>
  <option value="psz48">Krzysztof Szczygielski</option>
  <option value="pja168">Maciej Jakubowski</option>
  <option value="pst555">Piotr Leszek Stanek</option>
  <option value="pal855">Maciej Albinowski</option>
  <option value="pgo201">Lukasz Goczek</option>
  <option value="pfi197">Piotr Fiszeder</option>
  <option value="pgr291">Michal Gradzewicz</option>
  <option value="pja352">Anna Jaskiewicz</option>
  <option value="pko104">Oskar Kowalewski</option>
  <option value="pwe303">Grzegorz Wesolowski</option>
  <option value="pko431">Jacek Kotlowski</option>
  <option value="pra573">Ryszard Rapacki</option>
  <option value="pki34">Olga Kiuila</option>
  <option value="pmi274">Jan Jakub Michałek</option>
  <option value="pwi380">Jan Witajewski-Baltvilks</option>
  <option value="psa2033">Muhammad Sadiq</option>
  <option value="pst197">Pawel Strawinski</option>
  <option value="pbe727">Barbara Bedowska-Sojka</option>
  <option value="pch564">Tomasz Chmielewski</option>
  <option value="pkl141">Magdalena Klimczuk-Kochanska</option>
  <option value="pkl118">Agata Kliber</option>
  <option value="pwo54">Cezary Wojcik</option>
  <option value="pba1247">Adam P. Balcerzak Sr.</option>
  <option value="pdb2">Marek A. Dabrowski</option>
  <option value="psk39">Pawel Skrzypczynski</option>
  <option value="pja353">Marcin Jakubek</option>
  <option value="pgr382">Wojciech Grabowski</option>
  <option value="pbu210">Krzysztof Burnecki</option>
  <option value="pto209">Andrzej Toroj</option>
  <option value="pmy15">Jerzy Mycielski</option>
  <option value="ple411">Ewa Lechman</option>
  <option value="pko306">Ryszard Kokoszczynski</option>
  <option value="pbr27">Tomasz Brodzicki</option>
  <option value="pga765">Pawel Gajewski</option>
  <option value="pst899">Marcin Waldemar Staniewski</option>
  <option value="pkw4">Witold Kwasnicki</option>
  <option value="pko518">Katarzyna Kopczewska</option>
  <option value="pru58">Mario Arturo Ruiz Estrada</option>
  <option value="pby15">Victor Bystrov</option>
  <option value="psz40">Adam Szulc</option>
  <option value="pne161">Natalia Nehrebecka</option>
  <option value="pma2182">Kamil Makiela</option>
  <option value="pmi197">Piotr Misztal</option>
  <option value="pka834">Pawel Kaczmarczyk</option>
  <option value="psk53">Dorota Skala</option>
  <option value="pba904">Marcin Blazejowski</option>
  <option value="pko886">Pawel Kopiec</option>
  <option value="ppr218">Jan Przystupa</option>
  <option value="pol97">Magdalena Olczyk</option>
  <option value="pol176">Malgorzata Anna Olszak</option>
  <option value="pha1168">Aleksandra Halka</option>
  <option value="pma2968">Joanna Mackiewicz-Lyziak</option>
  <option value="pka509">Bogumil Kaminski</option>
  <option value="pka958">Mariusz Kapuscinski</option>
  <option value="pbr646">Jan Brzozowski</option>
  <option value="pko856">Aleksandra Kordalska</option>
  <option value="pch1469">Marcin Chlebus</option>
  <option value="pko340">Tadeusz Kowalski</option>
  <option value="pka912">Renata Karkowska</option>
  <option value="pos69">Magdalena Beata Osinska</option>
  <option value="pse644">Tomasz Serafin</option>
  <option value="pcu159">Ewa Cukrowska-Torzewska</option>
  <option value="pde1449">Lukasz Delong</option>
  <option value="pwe470">Tomasz Weron</option>
  <option value="pab510">Kanat Abdulla</option>
  <option value="ppa1025">Anna Pajor</option>
  <option value="pbr449">Joanna Bruzda</option>
  <option value="pku368">Wioleta Kucharska</option>
  <option value="pha727">Iraj Hashi</option>
  <option value="psh760">Alexander Shapoval</option>
  <option value="pbr427">Michal Brzozowski</option>
  <option value="pbi381">Anna Agnieszka Bialek-Jaworska</option>
  <option value="pni435">Weronika Nitka</option>
  <option value="pso638">Dimitrios Sotiros</option>
  <option value="psa1533">Katarzyna Salach-Drozdz</option>
  <option value="ppi301">Arkadiusz Andrzej Piwowar</option>
  <option value="pmi961">Mateusz Mikutowski</option>
  <option value="pwi440">Aleksandra Wisniewska</option>
  <option value="pza316">Katarzyna Zagorska</option>
  <option value="pki624">Grzegorz Kinelski</option>
  <option value="pdy22">Piotr Dybka</option>
  <option value="pha661">Christopher Andrew Hartwell</option>
  <option value="pkr327">Vitaliy Krupin</option>
  <option value="ple518">Katarzyna Sledziewska</option>
  <option value="pmu665">Ida Musialkowska</option>
  <option value="pry42">Jakub Rybacki</option>
  <option value="pan562">Michal Antoszewski</option>
  <option value="ppi478">Jacek Pietrucha</option>
  <option value="psz13">Mateusz Szczurek</option>
  <option value="pga595">Ewa Galecka-Burdziak</option>
  <option value="pba1340">Pawel Baranowski</option>
  <option value="pwe514">Adi Weidenfeld</option>
  <option value="pna591">Mateusz Najsztub</option>
  <option value="pto568">Mateusz Tomal</option>
  <option value="pci152">Anna Agata Martikainen</option>
  <option value="pan556">Katarzyna Andrzejczak Swierczynska</option>
  <option value="pch1803">Yash Chawla</option>
  <option value="pra935">Joanna Rachubik</option>
  <option value="pki490">Aneta Kielczewska</option>
  <option value="pjd1">Arkadiusz Jedrzejewski</option>
  <option value="pwo314">Henryk Wojtaszek Sr.</option>
  <option value="ppi491">Piotr Spiewanowski</option>
  <option value="psa504">Pawel Sakowski</option>
  <option value="pgt6">Marta Anna Goetz</option>

</select>

<script>
    function pokazDane() {
    // Pobierz wybraną wartość z listy rozwijanej
    var wybranaPostac = document.getElementById("postacie").value;

    // Sprawdź, czy istnieje poprzedni link, i usuń go, jeśli istnieje
    var poprzedniLink = document.getElementById("raportLink");
    if (poprzedniLink) {
        poprzedniLink.remove();
    }

    var a = document.createElement('a');
    var linkText = document.createTextNode("Pobierz raport");
    a.appendChild(linkText);
    a.title = "Pobierz raport";
    a.href = "/reports/" + wybranaPostac;
    a.id = "raportLink";  // Nadaj unikalne ID, aby móc łatwo odnaleźć link później
    document.body.appendChild(a);
  }

</script>

<div class="container">
    <hr>
    <p><a href="/main/">Wróć do Strony Głównej</a></p>
    </div>