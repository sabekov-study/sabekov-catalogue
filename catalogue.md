# SABEKOV-Katalog

1. [Ablauf](#Ablauf)
    1. [Erstbesuch](#OPEN)
    2. [Registrierung](#REG)
    3. [Login](#LOG)
    4. [Verwendung](#USE)
    5. [Logout](#LOGOUT)
    6. [Löschung](#DEL)
2. [Kataloge](#cat)

**Hinweis**: Der Vermerk `<multi>` bei Antwortmöglichkeiten zeigt an, dass hier Mehrfachnennungen möglich sind.

## <a name="Ablauf"></a>Ablauf

### <a name="OPEN"></a>Erstbesuch (OPEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| OPEN_TLS | Ist https verfügbar, wenn man die Domain mit https:// aufruft? Leitet die Seite von http auf https um? | _nein_ / https verfügbar / automatische Umleitung |
| OPEN_NOJS | Erlaubt die Seite die Nutzung auch ohne aktives JavaScript? | ja / _nein_ | Nein, wenn man auf einer Landingpage landet, die einen auffordert JS zu aktivieren oder die Seite offensichtlich nicht wie erwartet funktioniert. |
| OPEN_TORBROWSER | Ergreift die Seite Maßnahmen gegen TorBrowser (mit aktiviertem JavaScript)? | denied access / captchas / _keine_ |


### <a name="REG"></a>Registrierung (REG)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| REG_SENDVIATLS | Werden bei der Registrierung alle Daten (v.a. Username, Passwort, E-Mail) immer über HTTPS übertragen, wenn man die Domain mit http:// aufruft? | ja / _nein_ | Dazu muss man in der Firefox Web Developer Extension die Network Console öffnen und den/die POST-Requests begutachten. Dort müssen alle URLs, bei denen Daten übertragen werden mit https:// beginnen. Achtung: Teilweise werden schon vor dem eigentlichen Submitten XHR-Requests mit Teilen (z.B. Username) übermittelt; die müssen dann auch mit https:// beginnen. |
| REG_[PWD_SYSGEN](#PWD_SYSGEN) |
| REG_[PWD_ENT](#PWD_ENT) |
| REG_[PWD_GEN](#PWD_GEN) |
| REG_EMAIL | Wird im Registrierungsprozess eine E-Mail-Adresse abgefragt? | muss / optional / _nein_ | Wichtig: Bei _optional_ trotzdem eine Adresse eingeben und entsprechend fortfahren. |
| REG_[EMAIL_GEN](#EMAIL_GEN) | | |
| REG_EMAIL_AUTOLOGIN | Wird man nach Aufrufen des Bestätigungslinks automatisch eingeloggt oder gelangt man auf eine Seite, auf der man das Account-Passwort festlegen kann? | ja / _nein_ / _kein Bestätigungslink_ | Nein, wenn man nach Klicken auf Bestätigungslink weder eingeloggt ist noch ein Passwort setzen kann. Vorgehen: Darauf achten, dass im verwendeten Browser nicht ohnehin bereits eine Sitzung für diese Seite aktiv ist, da sonst false-postives auftreten. Am besten extra Browser verwenden. Hintergrund: Beide Fälle erlauben es in Verbindung mit reusable Tokens, sich Zugang zu einem Account zu verschaffen wenn man später Zugriff auf die REG-Mail bekommt |
| REG_EMAIL_[TOKEN](#TOKEN) | | |
| REG_[NOT](#NOT) | | | Hier ist eine Registrierungsbestätigung (z.B. Willkommensmail) gemeint. |
| REG_[SSO](#SSO) | | | Hier geht es um SSO-Verwendung innerhalb des Registrierungsdialoges (sign up; z.B. Übernahme von Stammdaten von SSO-Provider), nicht um den Login (s. LOG_SSO)! |
| REG_[2FA_GEN](#2FA_GEN) | | | nur wenn die Seite einen 2. Faktor verpflichtend vorsieht, aktivieren wir hier 2FA, sonst nicht |
| REG_[SECQ_GEN](#SECQ_GEN) | | |  nur wenn die Seite bei der Registrierung direkt Sicherheitsfragen anbietet, beantworten wir sie an dieser Stelle |
| REG_USERNAME | Muss sich der Benutzer selbst einen Benutzernamen ausdenken? | benutzergewählter Benutzername / vom System vorgegebener Benutzername / _kein Benutzername_ | kein Benutzername, u.a. wenn die E-Mail-Adresse de facto der Benutzername ist |
| REG_MINDATA | Müssen neben den Credentials und der E-Mail-Adresse weitere Daten verpflichtend eingegeben werden? | ja / _nein_ | wenn ja: Freitext (welche Daten?), sonst: nein | 
| REG_TOSACK | Wird die Annahme von Nutzungsbedingungen verlangt? | explizit / implizit / _nein_ | explizit: man muss z.B. ein Häckchen setzen, implizit: es wird z.B. lediglich mit einem Link darauf hingewiesen |
| REG_TOSACK_PRIVACY | Wird zu den Nutzungsbedingungen auch auf Datenschutzbedingungen verwiesen? | ja / _nein_ |


### <a name="LOG"></a>Login (LOG)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| LOG_SENDVIATLS | Werden beim Login Username und Passwort über HTTPS übertragen, wenn man die Domain mit http:// aufruft? | ja / _nein_ / _Seite ist gar nicht per HTTP aufrufbar_ | Vorgehen: Dazu muss man in der Firefox Web Developer Extension die Network Console öffnen und den/die POST-Requests begutachten. Dort müssen alle URLs, bei denen Daten übertragen werden mit https:// beginnen. Achtung: Teilweise werden schon vor dem eigentlichen Submitten XHR-Requests mit sensiblen Daten (z.B. Username) übermittelt; die müssen dann auch mit https:// beginnen. |
| LOG_[PWD_ENT](#PWD_ENT) | |
| LOG_ERRMSGLEAK | Kann man anhand der Fehlermeldung bei fehlerhaftem Loginversuch auf ein existierendes Konto zurückschließen? | ja / _nein_ | Beispiel: „Es existiert kein Konto mit diesem Namen“ oder „Das eingegebene Passwort ist falsch.“ – Dazu muss man 1. einen Loginversuch mit einem garantiert nicht existierenden Konto durchführen und 2. einen Loginversuch mit einem existierenden Konto, aber falschem Passwort, durchführen. Nur wenn in beiden Fällen keine Rückschlüsse möglich sind. Wird die Frage mit „nein“ beantwortet. |
| LOG_[ROBOPREV](#ROBOPREV) |
| LOG_[SSO](#SSO) | | | Hier geht es um SSO innerhalb des Login-Prozesses (sign-in). Nicht um die Registrierung (s. REG_SSO)! |
| LOG_[2FA_ENT](#2FA_ENT) |
| LOG_[SECQ_ANS](#SECQ_ANS) |
| LOG_ANOMALY | Wie reagiert der Dienst auf einen Loginversuch mit korrekten Zugangsdaten aus dem Ausland? | <multi> Benachrichtigung des Kontobesitzers (z.B. per E-Mail) / Kontosperrung (egal ob temporär oder permanent) / keine besondere Reaktion. | Zu prüfende Anomalie: Login von einer ausländischen IP-Adresse (HTTP-Proxy; Endpunkt in den USA oder Japan, je nach Verfügbarkeit; Gewählten Proxy/Land in Notizen festhalten). |
| LOG_ID | Mit welchen Kennungen kann man sich identifizieren? | <multi> E-Mail / benutzergewählter Login / systemgeneriereter Login / sonstige |
| LOG_USERFORGOT | Gibt es eine „Benutzername vergessen“-Funktion? | ja / _nein_ |
| LOG_[PWD_RST](#PWD_RST) |

### <a name="LOGOUT"></a>Logout (LOGOUT)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| LOGOUT | Wie viele Interaktionen (Hovern über einem Menü-Button oder Klicken) sind erforderlich um einen Logout durchzuführen ausgehend von der Startsteite? | int | Vorgehen: man meldet sich an und geht dann im angemeldeten Zustand zur Startseite. Ab dort werden die Interaktionen bis zum Logout-Klick (mitzählen) gezählt. |



### <a name="USE"></a>Verwendung des Accounts (USE)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| USE_TLS | Wird die Account-bearbeiten-Seite über HTTPS abgerufen? | ja / _nein_ | Hier geht es nicht um den Submit, sondern warum, ob das "Laden" (GET) der Profilstammdaten verschlüsselt erfolgt. |
| USE_MOD_PWD | Kann der Nutzer das Passwort ändern? | ja / _nein_ / _kein Passwort vorhanden_ |
| USE_MOD_[PWD_GEN](#PWD_GEN) | | | wie wird das neue Passwort generiert? |
| USE_MOD_PWD_GEN_NOREUSE | Wird beim Ändern des Passworts verhindert, dass man das unmittelbar vorherige Passwort (das bis gerade jetzt verwendet wurde) erneut setzt? | ja / _nein_ |
| USE_MOD_[PWD_ENT](#PWD_ENT) | | | wie wird das neue Passwort eingegeben? |
| USE_MOD_PWD_[RAUT](#RAUT) | | | RAUT_PWD_ENT bezieht sich hier auf das alte Passwort |
| USE_MOD_PWD_SESTERM | Werden aktive Sessions nach erfolgreicher Passwortänderung terminiert? | ja / optional / _nein_ | Testen mit zweitem Browser |
| USE_MOD_PWD_[NOT](#NOT) | (Wird nach erfolgter Passwortänderung eine Benachrichtigung versendet?) |
| USE_MOD_EMAIL | Kann der Nutzer die E-Mail-Adresse ändern? | ja / _nein_ / _keine E-Mail-Adresse hinterlegt_ |
| USE_MOD_[EMAIL_GEN](#EMAIL_GEN) | (Fragen zur neuen E-Mail-Adresse) |
| USE_MOD_EMAIL_[RAUT](#RAUT) |
| USE_MOD_EMAIL_[NOT](#NOT) | (Wird nach erfolgter E-Mail-Adressänderung eine Benachrichtigung versendet?) |
| USE_MOD_EMAIL_NOT_PREVCH | Wird bei einer Änderung der E-Mail-Adresse eine Benachrichtigung an die alte Adresse gesendet? | ja / _nein_ |
| USE_MOD_USER | Kann der Nutzer den Benutzernamen ändern? | ja / _nein_ / _kein Benutzername vorhanden_ |
| USE_MOD_USER_[RAUT](#RAUT) |
| USE_MOD_USER_[NOT](#NOT) | (Wird nach erfolgter Benutzernamensänderung eine Benachrichtigung versendet?) |
| USE_MOD_LOGNOT | Kann man das Benachrichtigungsverfahren bei Login-Ereignissen einstellen? | ja / _nein_ |
| USE_[SECQ_GEN](#SECQ_GEN) | (Kann man nachträglich Sicherheitsfragen hinterlegen?) | | nur, wenn es verpflichtend ist, muss man die Sicherheitsfragen hier auch eingeben |
| USE_[2FA_GEN](#2FA_GEN) | (Kann man nachträglich 2FA aktivieren?) | | nur wenn es verpflichtend ist, muss man die 2FA hier auch aktivieren |
| USE_PWDLASTCHG | Wird in der Benutzeroberfläche angezeigt, wann das Passwort zuletzt geändert wurde? | ja / _nein_ |
| USE_LOGHIST | Gibt es ein einsehbares Protokoll der Login-Ereignisse? | ja / _nein_ |
| USE_[SES](#SES) |


### <a name="DEL"></a>Löschung (DEL)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| DEL_INFO | An welchen Stellen wird auf die Möglichkeit zum Löschen eines Accounts hingewiesen? | <multi> Kontoeinstellungen / Datenschutzerklärung / sonstige / keine | Zu kontrollieren sind hier immer sowohl die Kontoeinstellungen (alle Einstellungen und Menüeinträge mit Bezug zum eigenen Konto nach dem Login) als auch die Datenschutzerklärung. |
| DEL_CONTACT | Konnte eine Löschanfrage an den Support versendet werden? | Formular im nicht-eingeloggten Zustand / E-Mail / Formular im eingeloggten Zustand / _keine Kontaktmöglichkeit_ | Wichtig: Nur eine Löschanfrage pro Seite versenden um ein Misstrauen zu erregen. Erste unterstützte Versandmethode entsprechend der Reihenfolge der Antwortmöglichkeiten nutzen und Anfrage stellen. |
| DEL_CONTACT_RESULT | Wie hat der Anbieter auf die Löschanfrage reagiert? | Account (mit oder ohne Rückfrage) gelöscht / Account (mit oder ohne Rückfrage) deaktiviert / Verweis auf andere Kontaktmethoden mit höherer Sicherheit (z.B. Formular nach Login) / _Anfrage abgewiesen_ / _keine Antwort innerhalb von 7*24 Stunden_ | Wenn auf eine andere Kontaktmethode verwiesen wird, dann über diese Methode erneut anfragen. Beim 2. Versuch wird diese Prüffrage jedoch nicht mehr angefasst, sondern lediglich das finale Ergebnis in DELETED festgehalten. Im Falle einer Rückfrage durch den Support wird der Timeout zurückgesetzt. |
| DEL_CONTACT_[RAUT](#RAUT) | (Wird zum Löschen des Accounts eine Reauthentifizierung verlangt?) | | Hier geht es darum, ob der Kundensupport eine zusätzliche Authentifizierung verlangt hat und welche (z.B. indem er auf ein Kontaktformular nach vorherigem Login verweist oder verlangt, dass man Stammdaten oder andere Informationen zur Verfügung stellt, die zur Authentifizierung dienen können). Eine evtl. durchgeführte E-Mail-Validierung soll hier als 2FA verstanden werden. |
| DEL_CONTACT_CONFIRM | Wird vor der Löschung/Deaktivierung Rücksprache mit dem Account-Inhaber gehalten (z.B. indem der Anbieter eine Mail an die im Account hinterlegte E-Mail-Adresse schreibt und sich die Löschung dort bestätigen lässt)? | ja / _nein_ | Falls ja: Die Rückfrage positiv beantworten. |
| DEL_CONTACT_[DELETED](#DELETED) | | | Dieser Teilbaum ist zu bearbeiten falls die Löschung/Deaktivierung über den Kundensupport erfolgreich war. |
| DEL_PROG | Kann der Account über eine GUI-Funktion, also vom Nutzer selbst und ohne Interaktion mit einem Support-Mitarbeiter, gelöscht oder deaktiviert werden? | gelöscht / deaktiviert / _nein_ |
| DEL_PROG_WHERE | Wo befindet sich die GUI-Funktion? | Kontoeinstellungen / Datenschutzerklärung / sonstige | Zu kontrollieren sind hier also immer sowohl die Kontoeinstellungen als auch die Datenschutzerklärung (manche Anbieter verstecken den Link dort). |
| DEL_PROG_[RAUT](#RAUT) | (Wird zum Löschen des Accounts eine Reauthentifizierung verlangt?) | | Eine evtl. durchgeführte E-Mail-Validierung soll hier als 2FA verstanden werden. |
| DEL_PROG_CONFIRM | Wird vor der Löschung/Deaktivierung Rücksprache mit dem Account-Inhaber gehalten (z.B. indem der Anbieter eine Mail an die im Account hinterlegte E-Mail-Adresse schreibt und sich die Löschung dort bestätigen lässt)? | ja / _nein_ | Falls ja: Die Rückfrage positiv beantworten. |
| DEL_PROG_[DELETED](#DELETED) | | | Dieser Teilbaum ist zu bearbeiten falls die Löschung/Deaktivierung über eine GUI-Funktion möglich und erfolgreich war. |


## <a name="cat"></a>Unterkataloge


### <a name="DELETED"></a>Wiederbelebung (DELETED)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| DELETED | War eine Löschung/Deaktivierung erfolgreich? | ja / _nein_ | Erfolg misst sich anhand des Feedbacks aus DEL und nicht durch Loginversuch. |
| DELETED_[NOT](#NOT) | (Wird nach erfolgter Kontolöschung bzw. -deaktivierung eine Benachrichtigung versendet?) |
| DELETED_UNDELPROG | Gibt es in der GUI eine Funktion oder Hinweise um den gelöschten/deaktivierten Account wiederzubeleben? | programmatisch / nur Hinweise zum Vorgehen / _nein_ | Programmatisch: Hier ist zusätzlich zu überprüfen, ob man den Account durch einfaches Anmelden mit den früheren Zugangsadaten wiederbeleben kann. Es spielt für die Beantwortung keine Rolle ob das Wiederbeleben nur in einem festgelegten kurzen Zeitraum oder ewig möglich ist. |
| DELETED_UNDELPROG_WHERE | Wo befindet sich die Wiederbelebenfunktion bzw. die Hinweise? | <multi> Kontoeinstellungen / Datenschutzerklärung / in der Account-gelöscht-Bestätigungsmail / sonstige | Zu kontrollieren sind hier also immer sowohl die Kontoeinstellungen als auch die Datenschutzerklärung. Kontoeinstellungen bezieht sich auf den Dialog während der Löschung (z.B. für Hinweise). |
| DELETED_UNDELETED | War eine Wiederherstellung des Accounts möglich? | ja / _nein_ |
| DELETED_UNDELETED_[RAUT](#RAUT) | (Wird zur Wiederbelebung des Accounts eine Reauthentifizierung verlangt?) | | Eine evtl. durchgeführte E-Mail-Validierung soll hier als 2FA verstanden werden. |
| DELETED_UNDELETED_[NOT](#NOT) | (Wird nach erfolgter Kontowiederbelebung eine Benachrichtigung versendet?) |
| DELETED_REREG | Kann der gelöschte Account mit gleichem Username und gleicher E-Mail-Adresse erneut registriert werden? | ja / _nein_ |
| DELETED_HIJACK | Kann ein gelöschter/deaktivierter Account mit gleichem Usernamen, aber einer anderen E-Mail-Adresse neu registiert werden? | ja / _nein_ / _kein Username vorhanden_ / _nicht überprüfbar_ | Vorgehen: Anderen Account als bei UNDEL verwenden um Seiteneffekte auszuschließen. Wenn eine Löschung nur durch den Support möglich ist, dann ist diese Frage mit 'nicht überprüfbar' zu beantworten, um den Support nicht mit zu vielen Löschanfragen zu irritieren. |


### <a name="2FA_GEN"></a>Zwei-Faktor-Authentifizierung einrichten (2FA_GEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| 2FA_GEN | Lässt sich Zwei-Faktor-Authentifizierung in diesem Schritt einrichten? | mandatory / recommended / supported / _unsupported_ | _recommended_ wenn die Seite innerhalb des aktuell betrachteten Prozesses eine explizite Empfehlung ausspricht |
| 2FA_GEN_SMS | Werden Authentifizierungstokens per SMS angeboten? | ja / _nein_ |
| 2FA_GEN_SMS_[CHVAL](#CHVAL) |  | |
| 2FA_GEN_EMAIL | Werden Authentifizierungstokens per E-Mail angeboten? | ja / _nein_ |
| 2FA_GEN_[EMAIL_GEN](#EMAIL_GEN) | | | Nur auszuwerten, wenn hier eine neue E-Mail-Adresse eingegeben werden kann. Wenn hier vorhandene Adressen ausgewählt werden müssen, dann nicht. |
| 2FA_GEN_OTP | Werden Authentifizierungstokens per (T)OTP-Verfahren (z.B. U2F) angeboten? | ja / _nein_ | Bemerkung erheben: Welches Verfahren (z.B. Google Authenticator App, Facebook Security Code, Apple Security Code |
| 2FA_GEN_MISC | Werden sonstige 2FA-Verfahren angeboten? | welche |

### <a name="2FA_ENT"></a>Zwei-Faktor-Authentifizierung benutzen (2FA_ENT)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| 2FA_ENT | Ist Zwei-Faktor-Authentifizierung in diesem Schritt erforderlich? | ja / _nein_ |
| 2FA_ENT_SKIP | Lässt sich die 2FA in diesem Fall irgendwie überspringen? | ja / _nein_ |


### <a name="EMAIL_GEN"></a>E-Mail-Adressen wählen (EMAIL_GEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| EMAIL_GEN | Muss an dieser Stelle (z.B. REG) vom Nutzer eine E-Mail-Adresse eingegeben werden? | ja / _nein_ |  |
| EMAIL_GEN_PLUS | Werden E-Mail-Adressen der Form name+irgendwas@example.com akzeptiert? | ja / _nein_ | (Begründung: Mit Plus-Adressen kann man mehrere Mail-Adressen für dieselbe Inbox generieren, sodass man Spam zu seiner Quelle zurückverfolgen kann.) |
| EMAIL_GEN_DISPOSABLE | Werden Wegwerf-E-Mail-Adressen von _mailinator.com_ akzeptiert? | ja / _nein_ |  |
| EMAIL_GEN_[CHVAL](#CHVAL) |



### <a name="PWD"></a>Passwort (PWD)

#### <a name="PWD_GEN"></a>Erstellung (PWD_GEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| PWD_GEN | Muss an dieser Stelle (z.B. REG) vom Nutzer ein Passwort generiert werden? | ja / _nein_ | Bei nein bitte in Bemerkungen erläutern. |
| PWD_GEN_WORSTPWD | Wird nachstehendes Passwort der Länge 1 akzeptiert? | ja / _nein_ | Prüfpasswort: a |
| PWD_GEN_SHORTPWD | Wird nachstehendes Passwort der Länge 4 akzeptiert? | ja / _nein_ | Prüfpasswort: Ab-1 |
| PWD_GEN_LONGPWD | Wird nachstehendes Passwort der Länge 32 akzeptiert? | ja / _nein_ | Prüfpasswort: seeheiKughu5pheeto9Da7FahK-7UTei |
| PWD_GEN_PHRASE | Kann man als Passwort die Passphrase chickenmouthtabletrudy wählen? | ja / _nein_ | |
| PWD_GEN_NOUSERNAME | Wird die Verwendung des Benutzernamens als Passwort untersagt? | ja / _nein_ / _es gibt keinen Nutzernamen_ |
| PWD_GEN_EMAILADDR | Wird die Verwendung der aktuellen (primären) E-Mail-Adresse als Passwort untersagt? | ja / _nein_ / _es gibt keine E-Mail-Adresse_ | Ja, auch wenn Eingabe aufgrund anderer Regeln untersagt wird. |
| PWD_GEN_BLACKLIST | Wird die Verwendung bekannter (schwacher) Passwörter verhindert? (Blacklist) | ja / _nein_ | ja, wenn das Passwort _password_ (oder die im Folgenden erläuterte Ableitung davon) abgewiesen wird. Vorgehen: Widerspricht _password_  der Passwortpolicy, dann ist es wie folgt abzuwandeln, sodass es der Policy geradeso entspricht: Großbuchstabe am Anfang, Ziffer 1 am Ende, Ausrufezeichen am Ende, mit Ziffer 1 auffüllen falls noch zu kurz). Beispiel: Policy sieht vor dass Passwort mindestens einen Großbuchstaben und eine Ziffer enthält, dann ist _Password1_ zu verwenden. |
| PWD_GEN_FBSTREN | Wird dem Nutzer  während der Eingabe Feedback zur Stärke des gewählten Passworts gegeben? | ja / _nein_ | Gemeint ist hier _nicht_ die Fehlermeldung, dass ein Passwort die Policy nicht erfüllt. |
| PWD_GEN_GUIDE | Erhält der Nutzer Empfehlungen wie ein gutes Passwort zu wählen ist (an Ort und Stelle)? | ja / _nein_ | Guide meint: eine Sammlung von unverbindlichen Tipps (d.h. keine Policy); Guide kann aber durchaus mit der Policy vermischt angezeigt werden |
| PWD_GEN_HINTNOREUSE | Wird darauf hingewiesen, Passwörter nicht bei mehreren Diensten zu verwenden? | ja / _nein_ |
| PWD_GEN_POLICY | Gibt es eine Passwortrichtlinie, die explizit genannt wird? | ja / _nein_ |
| PWD_GEN_POLICY_NOTIFY | Wie werden die Regeln der Passwortrichtlinie kommuniziert? | bevor man das Passwort eingibt / wenn man ein Passwort eingibt, das die Policy verletzt / erst nach dem Submitten des Formulars |
| PWD_GEN_POLICY_CHARS | Sieht die Passwortrichtlinie die Verwendung von unterschiedlichen Zeichenklassen (z.B. Sonderzeichen) vor? | ja / _nein_ |
| PWD_GEN_POLICY_MINLEN | Welche Mindestlänge sieht die Richtlinie explizit vor? | Länge | Wenn nicht der Fall, dann 0 eingeben. |
| PWD_GEN_POLICY_MAXLEN | Welche Maximallänge sieht die Richtlinie explizit vor? | Länge | Wenn nicht der Fall, dann 0 eingeben. |
| PWD_GEN_POLICY_MISC | Sieht die Richtlinie weitere Anforderungen vor (z.B. Passwort ungleich Benutzername)? Dann diese Anforderungen hier pasten (sonst NULL eingeben). | Freitext |
| PWD_GEN_PWDHINT | Kann ein Passworthinweis hinterlegt werden? | ja / _nein_ |
| PWD_GEN_CONFIRM | Muss das neue Passwort zur Bestätigung wiederholt eingegeben werden? | ja / _nein_ |

#### <a name="PWD_SYSGEN"></a>Vom System erstellte Passwörter (PWD_SYSGEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| PWD_SYSGEN | Wird an dieser Stelle vom System ein Passwort generiert? | ja / _nein_ | bspw. ein Initialpasswort |
| PWD_SYSGEN_CHANGE | Muss der Nutzer das systemgenerierte Passwort zwingend ändern? | ja / _nein_ |
| PWD_SYSGEN_LEN | Wie lang ist das systemgenerierte Passwort? | int |
| PWD_SYSGEN_CHARSET | Aus welchen Zeichenklassen besteht es? | alpha / alphanum / mixalpha / mixalphanum / other | alpha: (Groß- oder) Kleinbuchstaben, alphanum: (Groß- oder) Kleinbuchstaben und Ziffern, mixalpha: Groß- und Kleinbuchstaben, mixalphanum: Groß- und Kleinbuchstaben und Ziffern |



#### <a name="PWD_ENT"></a>Eingabe (PWD_ENT)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| PWD_ENT | Wird an dieser Stelle die Eingabe eines Passworts gefordert? | ja / _nein_ | Bei LOG_PWD_RST_RAUT mit nein antworten, da eine Passworteingabe im Passwortresetprozess keinen Sinn ergibt. |
| PWD_ENT_PASTE | Ist das Einfügen von Passwörtern aus der Zwischenablage möglich? | ja / _nein_ | (wichtig für externe Passwortmanager) |
| PWD_ENT_PWDMGR | Ist das automatische Abspeichern (bei REG oder USE) und Einfügen (bei LOG) von Passwörtern durch den Passwortmanager des Browsers (Firefox) möglich? | ja / _nein_ | ja, wenn sowohl Username als auch Passwort gespeichert (REG, MOD) oder eingefügt (LOG, MOD) werden. |
| PWD_ENT_INPUTTYPEPWD | Wird als Passworteingabefeld der Inputtyp *password* verwenden? | ja / _nein_ |
| PWD_ENT_SHOW | Kann man sich das eingegebene Passwort im Klartext anzeigen lassen? | ja / _nein_ |

#### <a name="PWD_RST"></a>Reset (PWD_RST)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| PWD_RST | Wird an dieser Stelle ein Passwort-Reset angeboten? | ja / _nein_ |
| PWD_RST_TRIGGERINPUT | Welcher Identifier wird abgefragt um den Reset auszulösen? | <multi> Username / E-Mail / Telefonnummer / Sonstige | Sonstige in Notizen auflisten. |
| PWD_RST_MSGLEAK | Erhält man aus der Rückmeldung Informationen über die Existenz eines bestimmten Kontos? | ja / _nein_ | Z.B. Zu dieser Adresse liegt kein Konto vor. | 
| PWD_RST_OLDPLAIN | Wird das alte Passwort im Klartext zugesendet? | ja / _nein_ |
| PWD_RST_[PWD_SYSGEN](#PWD_SYSGEN) | Wird ein neues, systemgeneriertes Passwort im Klartext zugesendet? | ja / _nein_ |
| PWD_RST_[TOKEN](#TOKEN) | Wird ein Token zum Zurücksetzen des Passworts zugesendet? | ja / _nein_ |
| PWD_RST_TOKEN_INVALID | Werden ungenutzte Tokens bei der Anforderung neuer Tokens invalidiert? | ja / gleiches Token wird erneut verschickt / _nein_ / _keine erneute Anforderung möglich_ |
| PWD_RST_[RAUT](#RAUT) | Wird ein Reauthentifikationsmechanismus als Berechtigung für den Reset verwendet (z.B. Sicherheitsfrage, 2FA)? | | Fragen zu PWD_ENT sind dort nicht anwendbar (Einstiegsfrage mit 'nein' beantworten), weil das Passwort soll ja resettet werden |
| PWD_RST_[PWD_ENT](#PWD_ENT) | | | bezieht sich auf das neue Passwort, das am Ende des Reset-Prozesses eingegeben wird |
| PWD_RST_[PWD_GEN](#PWD_GEN) | | | bezieht sich auf das neue Passwort, das am Ende des Reset-Prozesses eingegeben wird |
| PWD_RST_[NOT](#NOT) | (Wird eine Benachrichtigung nach erfolgreichem Reset versendet?) |
| PWD_RST_SESTERM | Werden aktive Sessions nach erfolgreichem Passwort-Reset terminiert? | ja / optional / _nein_ | Testen mit zweitem Browser |
| PWD_RST_MAIL_SENDER | Wie lautet der Absender der Passwort-Reset-Mail? | E-Mail-Adresse |  |



### <a name="SECQ_GEN"></a>Sicherheitsfragen setzen (SECQ_GEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| SECQ_GEN | Kann bzw. muss man an dieser Stelle Sicherheitsfragen setzen? | mandatory / recommended / supported / _unsupported_ |
| SECQ_GEN_CUSTOM | Können die Fragen vom Nutzer selbst formuliert werden? | ja / _nein_ |
| SECQ_GEN_MINNUM | Wie viele Sicherheitsfragen müssen mindestens hinterlegt werden? | int | Müssen, ist hier unter der Voraussetzung zu verstehen, dass man sich zuvor für die Eingabe entschieden hat. |
| SECQ_GEN_MAXNUM | Wie viele Sicherheitsfragen können maximal hinterlegt werden? | int | 0 für keine Begrenzung |


### <a name="SECQ_ANS"></a>Sicherheitsfragen beantworten (SECQ_ANS)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| SECQ_ANS | Sind an dieser Stelle Sicherheitsfragen zu beantworten? | ja / _nein_ |
| SECQ_ANS_CHOICE | Kann die zu beantwortende Frage vom Nutzer ausgewählt werden? | ja / _nein_ |
| SECQ_ANS_NUM | Wie viele Sicherheitsfragen sind zu beantworten? | int |
| SECQ_ANS_ERRMSGLEAK | Wird bei einer fehlerhaften Beantwortung der Fragen angezeigt welche Frage falsch beantwortet wurde? | ja / _nein_ |



### <a name="TOKEN"></a>Token (TOKEN)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| TOKEN | Werden an dieser Stelle Tokens eingesetzt? | ja / _nein_ |
| TOKEN_REUSE | Können Tokens nach einmaligem Verwenden erneut verwendet werden? | ja / _nein_ | Im Fall von REG_EMAIL...: mit nein antworten, wenn der Wert von REG_EMAIL_AUTOLOGIN "nein" ist; Vorgehen: Reuse in einem anderen Browser testen (nicht nur anderes Fenster), im Fall von PWD_RST: dann mit ja beantworten, wenn ein erneutes Setzen des Passworts möglich ist. |
| TOKEN_EXPIREINFO | Wird darauf hingewiesen, dass das Token nur eine bestimmte Gültigkeitsdauer besitzt? | ja / _nein_ |
| TOKEN_CLICKABLE | Kann das Token verwendet werden indem man auf einen Link klickt? | ja / _nein_ |
| TOKEN_CLICKABLE_VISURL | Ist die URL, auf die der Link zeigt, sichtbar? | ja / ja, aber tatsächliche URL stimmt nicht mit angezeigter URL überein / _keine sichtbare URL_ | Definition von „sichtbar“: die URL steht direkt im Text, entweder direkt als Linktext oder z.B. hinter/unter dem Link/Button). Tooltips bzw. Mouseover zählt nicht als sichtbar. |
| TOKEN_CLICKABLE_SAMEORIGIN | Ist die 2nd-level Domain des Links identisch mit der der Seite auf der man die Aktion ausgelöst hat? | ja / _nein_ | Im Fall von nein, die URL in die Notizen. |
| TOKEN_CLICKABLE_TLS | Beginnt die beim Klick tatsächlich aufgerufene URL mit https://? | ja / _nein_ | Dazu in einem „ordentlichen“ E-Mail-Programm die Statuszeile prüfen, in der der tatsächliche Link steht. |


### <a name="SES"></a>Sitzungsverwaltung (SES)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| SES_REUSE_HOME | Kann eine offen gelassene Session wiederverwendet werden, wenn man auf die Startseite geht, nachdem der Browser zwischenzeitlich geschlossen worden ist? | ja / _nein_ | Cookies nicht löschen! Hintergrund: Prüft das Session-Mgmt der Seite in Bezug auf (nicht-permantente) Cookies und den Geltungsbereich (Hostname) des Cookies. |
| SES_REUSE_PROFILE | Kann eine offen gelassene Session wiederverwendet werden, wenn man auf die Accounteinstellungsseite (Deep Link zur Profilseite verwenden!) geht, nachdem der Browser zwischenzeitlich geschlossen worden ist? | ja / _nein_ | Cookies nicht löschen! Siehe SES_REUSE_HOME |
| SES_ACTLST | Gibt es eine Übersicht der aktiven Sessions? | ja / _nein_ |
| SES_KILL | Können aktive Sessions in der Übersicht terminiert werden? | ja / _nein_ | Ob Sessions einzeln oder nur gesamt terminierbar sind soll nicht unterschieden werden. |


### <a name="RAUT"></a>Re-Authentifizierung (RAUT)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| RAUT_[PWD_ENT](#PWD_ENT) |
| RAUT_[SECQ_ANS](#SECQ_ANS) |
| RAUT_[2FA_ENT](#2FA_ENT) |
| RAUT_MASTERDATA | Werden hinterlegte Stammdaten abgefragt (z.B. Postleitzahl, Geburtsdatum)? | Art der Stammdaten | _keine_ angeben, wenn keine abgefragt werden |


### <a name="SSO"></a>Single-Sign-On (SSO)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| SSO   | Kann man sich an dieser Stelle mittels SSO authentifizieren? | ja / _nein_ | Hinweis: SSO verwenden wir nur dann, wenn es keine andere Registrierungsmöglichkeit gibt (also meistens nicht). |
| SSO_PROVIDER | Welche SSO-Provider stehen zur Verfügung? | <multi> Facebook, Google, Twitter, Github, sonstige |

### <a name="NOT"></a>Notification (NOT)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| NOT | Wird an dieser Stelle eine Benachrichtigung versendet? | ja, _nein_ |
| NOT_MEDIUM | Welches Kommunikationsmedium wird für die Benachrichtigungen verwendet? | <multi> E-Mail, SMS, sonstige |
| NOT_SUPDATA | Welche Daten werden übermittelt, die von einem Angreifer verwendet werden könnten, aber eigentlich für die Benachrichtigung nicht notwendig sind? | Art der Daten | _keine_, wenn nicht zutreffend; "Nicht notwendig" sind alle Stammdaten, die für den Benachrichtigungszweck nicht erforderlich sind (z.B. Anschrift). Die Bekanntgabe des Benutzernamens ist bspw. nur dann _nicht überflüssig_, wenn es um die Benutzername-vergessen-Funktion geht. Hintergrund: Jede Information verhilft einem Angreifer den Account zu übernehmen, daher sind die Angaben auf ein Minimum zu reduzieren. |
| NOT_MAIL_SENDER | Falls es sich um eine E-Mail handelt: Wie lautet der Absender der Mail? | E-Mail-Adresse | |


### <a name="ROBOPREV"></a>Robot Prevention (ROBOPREV)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| ROBOPREV_LOCKOUT | Findet innerhalb von max. 10 Fehlversuchen ein Lockout statt? | dauerhaft mit Hinweis zur Entsperrung / dauerhaft ohne Hinweis zur Entsperrung / zeitlich beschränkt / _nein_ | nicht bei REG zu prüfen (da macht es keinen Sinn) |
| ROBOPREV_CAPTCHA | Werden Captchas verwendet? | immer / nach Fehlversuchen / _nie_ |
| ROBOPREV_[NOT](#NOT) | (Wird bei den max. 10 wiederholten Login-Fehlversuchen irgendwann eine Benachrichtigung an den Accountinhaber versendet?) | | Hintergrund: Nutzer wird mitgeteilt, dass evtl. gerade ein "Angriff" auf sein Konto stattfindet. |


### <a name="CHVAL"></a>Kanalvalidierung (CHVAL)

| Label | Prüffrage | Werte | Bemerkung |
| ----- | --------- | ----- | --------- |
| CHVAL | Wird der gerade betrachtete Kommunikationskanal (z.B. E-Mail-Adresse oder Handynummer) validiert, sodass sichergestellt ist, dass der Nutzer auf diesen Zugriff hat? | ja / _nein_ | Bsp.: Zusendung einer E-Mail mit einem Link, den man anklicken soll. |
| CHVAL_BLOCK| Muss die Validierung abgeschlossen werden bevor der Account weiter genutzt werden kann (oder kann man sich z.B. auch schon einloggen bevor man den Link geklickt hat)? | ja / eingeschränkt / _nein_ | Eingeschränkt ist zu wählen, wenn die offensichtlich oder explizit darauf hinweist, dass ohne Validierung nicht alle Funktionen verfügbar sind. |
| CHVAL_MAIL_SENDER | Falls es sich um eine E-Mail handelt: Wie lautet der Absender der Mail? | E-Mail-Adresse | |
