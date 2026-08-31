# Kann man einen Gletscher künstlich ersetzen? Kurze Antwort: nur teilweise

*Ein allgemeinverständliches Begleitdokument zu
`glacier-buffer-replacement-utac` (GenesisAeon P100). Bewusst auf
Deutsch und ohne Fachjargon geschrieben -- die technische Dokumentation
(README, DISCLAIMER, Quellcode) bleibt Englisch für das internationale
Ecosystem.*

## Abstract

Wenn Gletscher als natürlicher Wasserspeicher schrumpfen (siehe das
Schwesterpaket `glacier-buffer-utac`, P99), liegt die naheliegende Frage
nahe: Kann man diesen Verlust künstlich ausgleichen -- etwa durch
Stauseen, künstliche Grundwasseranreicherung oder andere Infrastruktur?
Die reale Forschung gibt eine klare, aber differenzierte Antwort: Ja,
teilweise, und mit einer physikalisch begründeten Obergrenze. Dieses
Paket unterscheidet bewusst zwischen zwei Vertrauensstufen: solide,
unabhängig nachgeprüfte Zahlen einerseits, und schwächer belegte oder
sogar unveröffentlichte Schätzwerte andererseits -- beide werden gezeigt,
aber niemals vermischt.

## Die physikalische Obergrenze: mehr geht einfach nicht

Der wichtigste Befund zuerst, weil er alles andere einordnet: Eine
Studie von 2016 zeigt, dass ein optimal platziertes Netz aus Stauseen
und Reservoirs in den Alpen höchstens 65 Prozent der erwarteten
sommerlichen Abflussveränderung bis Ende des Jahrhunderts ausgleichen
könnte -- und das unter idealen Bedingungen, ohne die zusätzlichen
Verluste durch Verlandung und Verdunstung, die dieses Paket separat
dokumentiert. Der Grund für diese Obergrenze ist keine technische
Beschränkung, sondern reine Physik: ein Wasserverteilungs-Netzwerk kann
kein neues Wasser erschaffen, es kann nur bereits gefallenen Niederschlag
zeitlich verschieben. Die verbleibenden mindestens 35 Prozent sind
grundsätzlich nicht durch Umverteilung erreichbar.

## Wie viel Potenzial gibt es konkret?

Eine Studie von 2022 identifiziert 683 mögliche neue Bergseen in der
Schweiz mit einem Gesamtvolumen von 1,16 Kubikkilometern. Wichtig dabei:
diese oft zitierte Gesamtzahl ist ein Endzustand, kein sofort
verfügbares Volumen -- bis 2050 wären davon real erst rund 10 Prozent
entstanden, bis 2100 rund 48 Prozent.

## Zwei reale, funktionierende Vorbilder von anderswo

Interessant sind zwei bereits heute funktionierende Systeme aus anderen
Weltregionen: Die "Amunas" bei Lima, Peru -- ein jahrhundertealtes
Infiltrationssystem der Inka-Zeit, das noch heute in Betrieb ist und
Wasser im Schnitt 45 Tage im Untergrund zurückhält. Und die "Acequias de
careo" in der spanischen Sierra Nevada, ein ähnliches, ebenfalls noch
aktives System, das die Grundwasserneubildung um 92 Prozent erhöht --
die bislang am ehesten mit den Alpen vergleichbare reale
Anwendung dieser Technik.

## Warum Stauseen selbst nicht ewig halten

Ein Stausee verlandet mit der Zeit, weil Sediment aus dem Gebirge sich
darin absetzt. Am Brienzersee wurden reale Verlandungsraten von
durchschnittlich 3 Zentimetern pro Jahr gemessen, nahe von Flussdeltas
sogar bis 4,7 Zentimeter -- ein physikalischer Grenzwert dafür, wie lange
ein solches Reservoir überhaupt nutzbar bleibt.

## Was schwächer belegt ist -- und bewusst getrennt bleibt

Zwei Bereiche dieses Pakets basieren auf deutlich schwächeren Quellen
und werden deshalb ausdrücklich als solche gekennzeichnet: Zahlen zu
Moor-Speicherkapazität stammen teils aus einem rechtlichen Dokument
statt einer hydrologischen Studie und teils aus einer nicht-alpinen
(brasilianischen) Messung -- beide sollten nicht zur Planung eines
echten Alpen-Projekts verwendet werden. Ein zweiter Bereich, der sogenannte
"Resilience Replacement Factor", stammt vollständig aus einem
KI-Recherchebericht ohne wissenschaftliche Primärquelle für die Formel
selbst -- er wird im Code durchgehend mit einer expliziten Warnung
ausgeliefert, dass er nicht wissenschaftlich begutachtet ist.

## Was wir NICHT behaupten

- Dass künstliche Infrastruktur einen Gletscher vollständig ersetzen
  kann -- die 65-Prozent-Obergrenze (vor Verlandungs- und
  Verdunstungsverlusten) schließt das bereits physikalisch aus.
- Dass die Moor-Zahlen oder der "Resilience Replacement Factor"
  gleichwertig zu den unabhängig nachgeprüften Kernzahlen sind -- sie
  sind es ausdrücklich nicht, und werden deshalb im Code immer mit einer
  Warnung versehen ausgeliefert.
- Dass die 683-Seen- oder 1,16-Kubikkilometer-Zahl sofort verfügbares
  Volumen beschreibt -- es ist ein Endzustand für das Jahr 2100 unter
  einem mittleren Szenario.
- Dieses Paket enthält bewusst **keine** UTAC/CREP/AFET-Verknüpfung --
  die reale Wasserwirtschaft steht für sich.

## Quellen

Vollständige Zitationen (Autor:innen, Journal, DOI) sowie die genaue
Trennung zwischen Kern- und optionaler Vertrauensstufe stehen in
[DISCLAIMER.md](DISCLAIMER.md) und [CITATION.cff](CITATION.cff). Der
begleitende Software-Baustein ist auf
[GitHub](https://github.com/GenesisAeon/glacier-buffer-replacement-utac)
veröffentlicht.
