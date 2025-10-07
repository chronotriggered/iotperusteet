
IOT Perusteet 2025 Syksy
/ Elmo Käppi

Embed(ded):

Vaaditut tehtävät ensimmäisestä osiosta diagrammeineen numeroituna e_01 - e_09.
Jokainen tehtävä omassa kansiossaan.

Backend:

Onnistuin poistamaan nämä jo kerran. Käytin epähuomiossa komentoa:
git reset --hard HEAD~1

Databases:

Onnistuin poistamaan nämä jo kerran. Käytin epähuomiossa komentoa:
git reset --hard HEAD~1

Frontend:

Onnistuin poistamaan nämä, enkä kerennyt tehdä enää uudestaan ennen deadlinea. Käytin epähuomiossa komentoa:
git reset --hard HEAD~1

Pipeline:

Täysi pipeline, jossa seuraavat:

main.py / micropython koodi rautaan liittyen, lähettää tiedot thingspeakiin

server.js / serverilogiikka ja thingspeak datan hakeminen expressillä databaseen
--> lähettää tietoa myös webhookkina discordiin, jos raja-arvot ylittyvät

line_chart.html sekä chart.js / hakee serveriltä datan ja luo tämän avulla kaavion
