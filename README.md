# Projektowanie Obiektowe
---

**Zadanie 1** Paradygmaty

:white_check_mark: 3.0 | Procedura do generowania 50 losowych liczb od 0 do 100 [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/fd380eed97f61e3bf9cabf1bd9b3c79790ef9cf0)

:white_check_mark: 3.5 | Procedura do sortowania liczb [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/8053dd0f74d062429eb41f1a4dc5cc6c96544038)

:white_check_mark: 4.0 | Dodanie parametrów do procedury losującej określającymi zakres losowania: od, do, ile [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/72942607b7a888f2bab9fb1d618d9627110db25c)

:white_check_mark: 4.5 | 5 testów jednostkowych testujące procedury [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/f458213fc4e5751f4859345191c6bdccbdde47a5)

:white_check_mark: 5.0 | Skrypt w bashu do uruchamiania aplikacji w Pascalu via docker [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/abc1a36f5669632c335d2048cdce6cd684321d71)

Kod: [Zadanie1](./zadanie1/) <br>
Demo: [zadanie1_po_demo.zip](./demos/zadanie1_po_demo.zip)


**Zadanie 2** Wzorce architektury

:white_check_mark: 3.0 | Należy stworzyć jeden model z kontrolerem z produktami, zgodnie z CRUD [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/bad8fbffd60d57c10680e214e3ec3c7d3b3ce94a)

:white_check_mark: 3.5 | Należy stworzyć skrypty do testów endpointów via curl [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/92aa3014396785d468e6deeefcf5a0481165056d)

:x: 4.0 | Należy stworzyć dwa dodatkowe kontrolery wraz z modelami [Link do commita 3](https://github.com/kprzystalski/workshop_template/commit/hash)

:x: 4.5 | Należy stworzyć widoki do wszystkich kontrolerów [Link do commita 4](https://github.com/kprzystalski/workshop_template/commit/hash)

:x: 5.0 | Stworzenie panelu administracyjnego z mockowanym logowaniem [Link do commita 5](https://github.com/kprzystalski/workshop_template/commit/hash)

Kod: [Zadanie2](./zadanie2/) <br>
Demo: [zadanie2_po_demo.zip](./demos/zadanie2_po_demo.zip)


**Zadanie 3** Wzorce kreacyjne

:white_check_mark: 3.0 | Należy stworzyć jeden kontroler wraz z danymi wyświetlanymi z listy na endpoint’cie w formacie JSON - Kotlin + Spring Boot [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/b7cc18f020a5c48a4eaf554c942f614e0c33d800)

:white_check_mark: 3.5 | Należy stworzyć klasę do autoryzacji (mock) jako Singleton w formie eager [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/ceca2e20fe8abe5b2d93bd84fe2309f2764e4142)

:white_check_mark: 4.0 | Należy obsłużyć dane autoryzacji przekazywane przez użytkownika [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/6651ef236fe1cdf1c76c10c85c4258e9265b3354)

:white_check_mark: 4.5 | Należy wstrzyknąć singleton do głównej klasy via @Autowired [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/c315225ae7f0a26b420cf991f85434b027012a57)

:white_check_mark: 5.0 | Obok wersji Eager do wyboru powinna być wersja Singletona w wersji lazy [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/c23557970eb835369999b466443883f6b0a07c3d)

Kod: [Zadanie3](./zadanie3/) <br>
Demo: [zadanie3_po_demo.zip](./demos/zadanie3_po_demo.zip)


**Zadanie 4** Wzorce strukturalne

:white_check_mark: 3.0 | Należy stworzyć aplikację we frameworki echo w j. Go, która będzie miała kontroler Pogody, która pozwala na pobieranie danych o pogodzie (lub akcjach giełdowych) [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/ceb942a5299a07542bb43f6e3a6e7efd8674171d)

:white_check_mark: 3.5 | Należy stworzyć model Pogoda (lub Giełda) wykorzystując gorm, a dane załadować z listy przy uruchomieniu [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/1eeab55c6b232db83ecf6fe6da172d1b304295d7)

:white_check_mark: 4.0 | Należy stworzyć klasę proxy, która pobierze dane z serwisu zewnętrznego podczas zapytania do naszego kontrolera [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/353c9c3e121a18a573648fa442e9ca6e429abed0)

:white_check_mark: 4.5 | Należy zapisać pobrane dane z zewnątrz do bazy danych [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/f02416a1add1b463e45195a98f8581f73f8678ac)

:white_check_mark: 5.0 | Należy rozszerzyć endpoint na więcej niż jedną lokalizację (Pogoda), lub akcje (Giełda) zwracając JSONa [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/96a4274c6ade5fad8c7c34af3fe1fb722702bd5b)

Kod: [Zadanie4](./zadanie4/) <br>
Demo: [zadanie4_po_demo.zip](./demos/zadanie4_po_demo.zip)


**Zadanie 5** Wzorce behawioralne

:white_check_mark: 3.0 | W ramach projektu należy stworzyć dwa komponenty: Produkty oraz Płatności; Płatności powinny wysyłać do aplikacji serwerowej dane, a w Produktach powinniśmy pobierać dane o produktach z aplikacji serwerowej; [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/a5dba1849218b29042af63930056ee7331c84f56)

:white_check_mark: 3.5 | Należy dodać Koszyk wraz z widokiem; należy wykorzystać routing [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/d982a93184b174353a7ea6a7fae2c4b991718f68)

:white_check_mark: 4.0 | Dane pomiędzy wszystkimi komponentami powinny być przesyłane za pomocą React hooks [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/b7f3c043f32438ed6b659fd0f942d4436fb2e572)

:white_check_mark: 4.5 | Należy dodać skrypt uruchamiający aplikację serwerową oraz kliencką na dockerze via docker-compose [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/cf83ed14acb41f6bc3ce4ff7610a0772b27b27e8)

:white_check_mark: 5.0 | Należy wykorzystać axios’a oraz dodać nagłówki pod CORS [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/7a9736109a5c3e31d37763712f3643faba79ef5a)

Kod: [Zadanie5](./zadanie5/) <br>
Demo: [zadanie5_po_demo.zip](./demos/zadanie5_po_demo.zip)

**Zadanie 6** Zapaszki

:white_check_mark: 3.0 | Należy dodać eslint w hookach gita [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/ebde7e2de7bc243bf4178671c131f3165a760472)

:white_check_mark: 3.5 | Należy wyeliminować wszystkie bugi w kodzie w Sonarze (kod aplikacji klienckiej) [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/ebde7e2de7bc243bf4178671c131f3165a760472)

:x: 4.0 | Należy wyeliminować wszystkie zapaszki w kodzie w Sonarze (kod aplikacji klienckiej) [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 4.5 | Należy wyeliminować wszystkie podatności oraz błędy bezpieczeństwa w kodzie w Sonarze (kod aplikacji klienckiej) [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 5.0 | Zredukować duplikaty kodu do 0% [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

Kod: [Zadanie6](./zadanie6/) <br>
Demo: [zadanie6_po_demo.zip](./demos/zadanie6_po_demo.zip)

**Zadanie 7** Antywzorce

:white_check_mark: 3.0 | Należy stworzyć kontroler wraz z modele Produktów zgodny z CRUD w ORM Fluent [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/329f65b2d583acd135277438781aab90688b6896)

:white_check_mark: 3.5 | Należy stworzyć szablony w Leaf [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/35f0afda2ec50cacc1925e0b7c25179c0fa71595)

:x: 4.0 | Należy stworzyć drugi model oraz kontroler Kategorii wraz z relacją [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 4.5 | Należy wykorzystać Redis do przechowywania danych [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 5.0 | Wrzucić aplikację na heroku [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

Kod: [Zadanie7](./zadanie7/) <br>
Demo: [zadanie7_po_demo.zip](./demos/zadanie7_po_demo.zip)


**Zadanie 8** Testy

:white_check_mark: 3.0 | Należy stworzyć 30 przypadków testowych w Pythonie w WebDriverze [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/ba58282e0fbb28ba0f54615743d0bd6b662e25fb)

:white_check_mark: 3.5 | Należy rozszerzyć testy funkcjonalne, aby zawierały minimum 100 asercji [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/abdece8b163f401947830fae1ed21e69db9d8752)

:white_check_mark: 4.0 | Należy stworzyć testy jednostkowe do wybranego wcześniejszego projektu z minimum 100 asercjami [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/abdece8b163f401947830fae1ed21e69db9d8752)

:x: 4.5 | Należy dodać testy API, należy pokryć wszystkie endpointy z minimum jednym scenariuszem negatywnym per endpoint [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 5.0 | Należy uruchomić testy funkcjonalne na Browserstacku na urządzeniu mobilnym [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

Kod: [Zadanie8](./zadanie8/) <br>
Demo: [zadanie8_po_demo.zip](./demos/zadanie8_po_demo.zip)

**Zadanie 9** Mobile First

:white_check_mark: 3.0 | Stworzyć listę kategorii oraz produktów [Link do commita 1](https://github.com/kreciszj/projektowanie-obiektowe/commit/884036106874244b0e9b92185e2a112ef7ac2968)

:white_check_mark: 3.5 | Dodać widok koszyka [Link do commita 2](https://github.com/kreciszj/projektowanie-obiektowe/commit/2bf2302468b9d2e8ee0328429c80d11e2a074d38)

:white_check_mark: 4.0 | Stworzyć bazę w Realmie [Link do commita 3](https://github.com/kreciszj/projektowanie-obiektowe/commit/24b038cd39342b9143a1b74265d054fc68f8a0ff)

:x: 4.5 | Dodać płatności w Stripe [Link do commita 4](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

:x: 5.0 | dodać logowanie i rejestrację via Oauth2 [Link do commita 5](https://github.com/kreciszj/projektowanie-obiektowe/commit/)

Kod: [Zadanie9](./zadanie9/) <br>
Demo: [zadanie9_po_demo.zip](./demos/zadanie9_po_demo.zip)
