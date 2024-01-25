<!DOCTYPE html>
<html lang="pl">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="Na tropie polskich ekonomistów">
  <meta name="author" content="Tymoteusz Mętrak & Wojciech Szymczak">

  <!-- Na potrzeby tworzenia aplikacji wyłączmy cachowanie zawartości.  -->
    <meta http-equiv="cache-control" content="max-age=0" />
    <meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="expires" content="0" />
    <meta http-equiv="expires" content="Tue, 01 Jan 1980 1:00:00 GMT" />
    <meta http-equiv="pragma" content="no-cache" />
<title>{{title or 'Polscy ekonomiści'}}</title>

  <!-- Bootstrap core CSS -->
  <link href="/static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

</head>

<body>

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
    <div class="container">
      <a class="navbar-brand" href="/">Polscy ekonomiści</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="/main">Strona Główna
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/oProjekcie">O projekcie</a>
          </li>

          <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Analiza</a>
                        <div class="dropdown-menu" aria-labelledby="dropdown01">
                            <a class="dropdown-item page-scroll" href="/KobietyDekady">Kobiety a mężczyźni</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item page-scroll" href="/Strategie">Strategie publikacyjne</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item page-scroll" href="/tabela">Tabela - ekonomiści</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item page-scroll" href="/instytucje">Tabela - instytucje</a>
                        </div>
                    </li>

          <li class="nav-item">
            <a class="nav-link" href="/reports">Raporty o ekonomistach</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Page Content -->
  <div class="container">
    <div class="row">
      <div class="col-lg-12 text-center">
        {{!base}}
      </div>
    </div>
    <!-- Page Footer -->
    <div class="row">
    <footer class="page-footer small">
      <div class="col-lg-12">
        <div>Kontakt: t.metrak@student.uw.edu.pl; w.szymczak2@student.uw.edu.pl</div>
      </div>
    </footer>
    </div>
  </div>

  <!-- Bootstrap core JavaScript -->
  <script src="/static/vendor/jquery/jquery.slim.min.js"></script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

</body>

</html>
