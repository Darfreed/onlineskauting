# ON-LINE SKAUTING

## ÚVOD
Hlavní cílem tohoto závěrečného projektu bylo vytvoření prostředí pro učení se skaut-ským dovednostem, která by byla přístupná a zábavná i pro malé děti. Vzhledem k situaci ohledně Covidu-19, byla zastavena veškerá skautská činnost. Děti mohli navštěvovat schůzky vedené on-line, ale pro většinu, která není technicky zdatná, byl tento způsob výuky nevhodný. Z tohoto důvodu vznikl nápad vytvořit webovou hru ON-LINE SKAUT. Hru, ve které hráč plní výzvy ze skautské dovednosti a díky tomu vylepšuje svou postavu skauta. Původně hra fungovala na komunikační platformě Discord, ale poté jsem se ji rozhodl přenést na webové stránky v rámci závěrečného projektu.

Webovky by měli jednoduché a responzivní, aby byli přístupné uživatelům všech věko-vých kategorií na jakékoliv platformě. Navíc by měli stránky obsahovat fórum, kde by si hráči navzájem sdělovali své úspěchy a snadný způsob administrace pro vyhodnocení hry.

V práci naleznete popis jednotlivých stránek a jejich funkci, seznam jednotlivých techno-logií, které jsem k zhotovení projektu použil a příklady postupů a řešení, které na webo-vých stránkách využívám.

## 1	ON-LINE SKAUTING

### 1.1	Úvodní stránka

Úvodní stránka by měla obsahovat stručný popis toho, co můžou uživatelé od stránky čekat. Z toho důvodu využívám podnadpis stránek „PLŇ VÝZVY - UČ SE NOVÉ VĚCI - VYLEPŠUJ SVÉHO SKAUTA“. Každé heslo má svůj vlastní oddíl s doplňujícím textem a jednoduchou ilustrací.

Úvod také vlastní přihlášení a registraci uživatelů. Ty lze vytvořit pomocí autentizace uživatelů Djanga, což zajistí jejich funkčnost a bezpečnost.

Objevují se zde i kontaktní údaje s tlačítkami odkazující na webové stránky a email skautského oddílu a na GitHub samotného projektu.

### 1.2	Profil

Každý uživatel vlastní profil (viz příloha č. 2). Jeho základem je přezdívka a krátký text o sobě. Vše si může uživatel na stránce kdykoliv editovat či smazat. 

Na stránce lze také nalézt avatara on-line skauta, kterému se přidává vybavení podle toho kolik a jaké výzvy uživatel splnil. Za splnění znalostní výzvy se avatarovi vylepší po-krývka hlavy. Za výzvy zaměřené avatar získává novou zbraň. A za výzvy přátelství se k avatarovi přidá zajímavější společník. Kolik výzev hráč splnil se zjistí podle počtu pun-tíků pod názvem kategorie.

### 1.3	Výzvy

Stránka určená pro výzvy má jediný význam, a to zobrazování výzev, které mohou hráči plnit. Na stránce se zobrazí vždy jedna z každé kategorie a mění se kaž-dý týden. Pokud hráč už výzvu splnil, zobrazí se u ní ikona splnění. Kategorie jsou:

- Znalosti

Kategorie je zaměřená na to co hráč zná a pamatuje si. Je označená modrou bar-vou a patří zde šifrované zprávy, poznávání zvířat, rostlin a historických postav a obecně znalosti jako takové.

- Schopnosti

Tato kategorie se zaměřuje na to co hráč dokáže nebo se naučí. Označuje se čer-venou barvou a úkoly jsou plné vázaní uzlů, kreslení, vyrábění a dovednostech, které umí hráč předvést.

- Přátelství

V poslední kategorii jde o socializaci a poznání svých přátel. Barva výzvy je zele-ná. Mezi zadání výzvy patří dobré skutky, zjišťování informací o svých kamará-dech a trávení času se svými bližními.

### 1.4	Fórum

Fórum je místo pro chatování (viz příloha č. 4). Uživatel jednoduše napíše do textového pole zprávu a odešle ji. Příspěvek se ihned objeví na stránce zároveň s datem zveřejnění a přezdívkou toho, kdo ji poslal.

### 1.5	Administrace

Aby se nemusel o hodnocení výzev, mazaní příspěvků a dalších věcí nemusel starat ad-ministrátor celého webu, využil jsem skupin v administraci Django. Vytvořil jsem skupi-nu vedoucí, jejiž členové se do administrace sice dostanou, ale mají v ní pouze omezené možnosti povolené hlavním administrátorem.  

## 2	VYUŽITÉ TECHNOLOGIE

### 2.1	Python

Python je programovací jazyk, který umožňuje programátorovi pracovat rychle a efektiv-ně. Je v něm napsaný framework Django (viz níže), proto se stal nedílnou součástí mého projektu. Také nabízí velkou řadu různých modulů, které v projektu využívám pro funkč-ní vlastnosti webu.

### 2.2	Framework Django

Django je webový aplikační framework napsaný v Pythonu, který podporuje rychlé tvoře-ní webových stránek. Díky něho je možné vytvořit komplexní, databází řízené webové aplikace. Zaměřuje se na znovupoužitelnost a propojitelnost komponent, rychlý vývoj, vždy v duchu „DRY“ (Don’t Repeat Yourself) – neopakovat se. 

Součástí projektu bylo naučit se v Djangu používat to se dařilo díky je rozšířené doku-mentaci ze které jsem čerpal.

### 2.3	SQLite databáze

SQLite je nejrozšířenější databázový systém ve světě. Je napsaný v jazyce C a je obsaže-ný v relativně malé knihovně. To je hlavní rozdíl od databází založených na principu kli-ent-server, kde je databázový server spuštěn jako samostatný proces. SQLite používám, protože pro účely mého projektu stačí, ale mohl jsem využít databázový systém MySQL nebo PostgreSQL.

### 2.4	Bootstrap 4 a JQuery

Pro úpravu typografie, formulářů, tlačítek, navigace využívám Bootstrap 4. Výhodou to-hoto souboru nástrojů je snadné zpracování jakéhokoliv uživatelského rozhraní ve webo-vé aplikaci. Je dostupný s několika JavaScriptovými komponenty ve formě jQuery plug-inů. Já v projektu používám rozšiřující možnosti uživatelského rozhraní jako jsou dialo-gová okna. 

### 2.5	Font Awesome

Font Awesome je sada fontů a ikon založená na CSS a LESS. Většina ikon, které nalezne-te na mých stránkách jsou právě z této sady. Velmi rychle ikony zobrazuje a všechny mají nádherný jednoduchý design.

### 2.6	Inkscape

Na tvorbu grafiky pro webové stránky jsem použil editor vektorové grafiky Inkscape. Používal jsem ho v původní verzi On-line skautingu pro rychlou editaci postav a hlavně kvůli vytváření vektorových obrázků. Pro webové stránky má účel v návrhu grafiky, pro-tože ta se vytvoří jen jednou a exportuje se do statických souborů stránek.

## 3  ZPŮSOBY ŘEŠENÍ A POUŽITÉ POSTUPY

### 3.1	Datové modely databáze

Nebylo pro mě jednoduché vytvořit databázi pro mé účely, kvůli tomu jsem zbytečně hodně času strávil na jejím opravování a vylepšení.
Na obrázku níže můžete vidět konečný model databáze pro webové stránky ON-LINE SKAUTING. 

### 3.2	LoginRequiredMixin

Jelikož používám view.py založený na třídách a chtěl jsem dosáhnou stejného výsledku jako při používání login_required, využil jsem třídu LoginRequiredMixin. Ta zajišťu-je, že se na stránky pod třídou dostanou jen přihlášení uživatelé a automaticky nepřihlá-šené uživatele odkáže na stránku kde se mohou přihlásit.

### 3.3	Zobrazení bodů uživatele

V ukázce kódu můžete vidět způsob jakým zobrazuju na stránce „Profilu“ kolik má uži-vatel bodů. Nejdřív ve view.py získám potřebné informace z databáze pomocí filtrování a seřazení. Až poté je vykreslím potřebným stylem na webovou stránku v HTML. A to vše za pomoci Djanga.

### 3.4	Výpis a zápis příspěvků

Django také používám k přidávání příspěvků na stránce „Fórum“. Ve view.py získávám informaci z forms.py, jaké údaje uživatel zadává a poté je ukládá do databáze. V HTML používám již připravený formulář.

## ZÁVĚR

Cílem projektu bylo vytvořit hru ve formě webové stránky, která by sloužila jako výuko-vý nástroj pro skautský oddíl. Díky tohoto projektu jsem získal znalosti o programování a používání Pythonu a frameworku Django společně s praktickou zkušeností vytváření we-bových stránek.

Ale tím to nekončí, protože projekt by potřeboval spoustu vylepšení, například přesun databáze na modernější databázový systém, lepší přístup pro administraci nebo přidávání obrázkůk výzvám a k příspěvkům na fóru.
