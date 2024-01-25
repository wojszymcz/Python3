% rebase('base.tpl', title='Posty')
{{!zawartosc or ''}}

% for tytul, tresc in posty:
<div>
<h3>TYTUŁ: {{tytul}}</h3>
<p> {{tresc}} </p>
</div>
% end
