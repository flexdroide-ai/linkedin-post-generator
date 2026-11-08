# LinkedIn Post Generator

> Skill per Claude che trasforma notizie di qualsiasi settore in post LinkedIn con tesi e punto di vista reale.

Un **motore editoriale** generico (come si costruisce un buon post da una notizia) + un **profilo di dominio** che dice di cosa parli, a chi, con che voce. Un IT manager e un numismatico usano lo stesso motore e cambiano solo il profilo.

## Architettura

```
linkedin-post-generator/          ← entra nello zip
├── SKILL.md                      # entry point: frontmatter + istruzioni
├── engine/                       # motore generico, non toccare
│   ├── editorial_engine.md       # logica operativa (usa segnaposto {DOMINIO}, {AREE}, ...)
│   ├── operating_prompts.md      # prompt pronti da copiare
│   └── anti_patterns.md          # errori da evitare (validi per ogni dominio)
├── config/                       # qui si personalizza
│   ├── profile.md                # PROFILO ATTIVO (default: IT)
│   ├── profile.template.md       # schema vuoto da compilare
│   └── examples/
│       ├── profile.it-operations.md      # IT management (italiano)
│       ├── profile.numismatics.md        # numismatica romana (italiano)
│       └── profile.en-cybersecurity.md   # cybersecurity enterprise (english)
└── examples/
    ├── reference-post.it-operations.md
    └── post-library.template.md
```

Il motore legge i segnaposto (`{DOMINIO}`, `{AREE}`, `{PUBBLICO}`, `{ANGOLI}`, `{FONTI}`, `{HASHTAG}`, `{LINGUA}`, ...) e li riempie con i valori del profilo attivo. Non c'è codice da eseguire: è un sistema di istruzioni a livelli in markdown.

## Come creare un nuovo profilo

1. Copia `linkedin-post-generator/config/profile.template.md` in `config/profile.md` (sovrascrive il default).
2. Compila tutti i campi: `DOMINIO`, `LINGUA`, `PUBBLICO`, `POSIZIONAMENTO_AUTORE`, `AREE`, `CONCETTI_CHIAVE`, `ANGOLI`, `FONTI`, `TONO`, `TONO_DA_EVITARE`, `HASHTAG`, `ANTI_PATTERN_SPECIFICI`. Un campo vago produce output vago.
3. (Opzionale) Aggiungi un post di riferimento in `examples/` con il tuo dominio e riempi `post-library.template.md` con 6-10 post che rappresentano la tua voce.
4. Rebuilda lo zip (`make build`) e ricarica la skill.

Per capire quanto cambia cambiando solo il profilo, confronta [`config/examples/profile.it-operations.md`](linkedin-post-generator/config/examples/profile.it-operations.md) con [`config/examples/profile.numismatics.md`](linkedin-post-generator/config/examples/profile.numismatics.md): stesso schema, contenuti completamente diversi.

## Come buildare e caricare la skill

**Prerequisiti:** Python 3, `make`, `zip` (preinstallati su macOS e Linux).

```bash
# Controlla frontmatter, file referenziati, nessun file spazzatura
make validate

# Produce dist/linkedin-post-generator.zip (esegue validate prima)
make build

# Rimuove dist/
make clean
```

**Upload su Claude.ai:**
1. Vai su [claude.ai](https://claude.ai) → menu utente in alto a destra → **Customize** → **Skills**
2. Clicca **+** → **Create skill**
3. Carica `dist/linkedin-post-generator.zip`

> Lo zip contiene `linkedin-post-generator/` come cartella radice con `SKILL.md` dentro. Il Makefile garantisce che nessun file di tooling entri nello zip.

## Prima / Dopo — cosa cambia con la skill

### Profilo IT Operations

**PRIMA** (riassuntino senza tesi — si poteva scriverlo chiunque):

```
Gartner ha pubblicato un report sull'AI in ambito IT. I risultati mostrano che
molti progetti non raggiungono il ROI atteso. Le aziende devono capire meglio
come usare l'intelligenza artificiale e implementarla nel modo giusto.

#AI #IT #Innovation
```

**DOPO** (con la skill — hook, notizia, interpretazione, tesi, domanda):

```
Il problema non è più adottare l'AI. È farla funzionare davvero nell'operativo.

Il nuovo report Gartner su AI in Infrastructure & Operations dice una cosa
semplice ma scomoda: meno della metà delle iniziative AI nel perimetro IT
raggiunge il ROI atteso nel corso dell'anno.

Non è un problema dell'AI. È un problema di come la affrontiamo.

Ho visto organizzazioni con ottimi modelli, buoni vendor e piloti riusciti
che poi si fermano. Il motivo quasi sempre è lo stesso: workflow non
ridisegnati, dati di qualità insufficiente, KPI non ridefiniti, team non
coinvolti nell'adozione.

L'AI amplifica la maturità operativa. Non la sostituisce.

Domanda concreta: nelle vostre organizzazioni, l'AI è embedded nei processi
operativi o continua a girare in sandbox?

→ gartner.com/en/information-technology

#AI #ITSM #AIOps #ServiceManagement #Infrastructure
```

---

### Profilo Numismatica

**PRIMA** (riassuntino senza tesi):

```
Una rara moneta romana è stata venduta all'asta per una cifra record.
Il collezionismo numismatico è in crescita e le monete romane sono sempre
più apprezzate dai collezionisti di tutto il mondo. Un settore affascinante!

#Numismatica #MoneteRomane #Storia
```

**DOPO** (con la skill):

```
Un record d'asta non è un segnale di mercato. È un evento.

Da Roma Numismatics è passato un denario di Bruto del 42 a.C. — l'emissione
con i pugnali e il pileo, il pezzo propagandistico per eccellenza dell'antichità.
Aggiudicato a cifra record.

Il commento standard: "il mercato delle romane esplode".
Il commento onesto: questa moneta aveva tre cose insieme che non si vedono
quasi mai in un singolo pezzo — rarità assoluta del tipo, conservazione
eccezionale e pedigree documentato da una collezione degli anni '60.
Non ci dice nulla sul mercato generale.

Il vero trend degli ultimi anni non è il record sui pezzi irripetibili.
È che la distanza tra monete con provenienza documentata e monete senza
pedigree si sta allargando — e lo si vede nei prezzi reali, non nelle stime
di catalogo.

Domanda per chi compra: quanto peso date alla provenienza nelle vostre
decisioni di acquisto?

#Numismatica #MoneteRomane #AncientCoins #Collezionismo #Storia
```

## Workflow tipico

1. **"Trova le top news del settore"** → MODE 1: lista di 10 voci con fonte e motivo per postare.
2. Scegli un item → **"Scrivi un post da questa notizia"** → MODE 2: post pronto + nota pratica.
3. **"Dammi 3 varianti"** → MODE 3: tre versioni con angoli diversi (più autorevole, più engaging, più netta).
4. **"Migliora questo mio post"** → usa il PROMPT 4 da `engine/operating_prompts.md`.

## Nota di sicurezza

La skill **non esegue codice a runtime**: è un set di istruzioni in markdown che Claude legge e applica. Non ci sono API call nascoste, accesso a dati esterni o automazioni.

Gli script in `scripts/` (`validate.py`, `Makefile`) sono strumenti di sviluppo opzionali, usati solo in fase di build locale. Sono leggibili nella loro interezza nel repository.

## Contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md) per come proporre un nuovo profilo di dominio.

## Licenza

MIT — vedi [LICENSE](LICENSE).
