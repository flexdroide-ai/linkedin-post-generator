---
name: linkedin-post-generator
description: Trasforma notizie e trend di un settore configurabile in post LinkedIn credibili, con tesi e punto di vista. Il dominio (IT, numismatica, ecc.) si definisce in config/profile.md.
license: MIT
compatibility: Claude.ai Skills. Pure markdown instructions — no code execution at runtime.
metadata:
  version: "2.1.0"
---

# LinkedIn Post Generator

Skill editoriale per trasformare notizie, report e annunci di **un qualsiasi
settore** in post LinkedIn credibili, di taglio professionale e con un punto
di vista reale.

A differenza della v1 (cablata sul mondo IT), questa versione separa due cose:

- **Il motore editoriale** (`engine/`): la logica generica, indipendente dal
  dominio. Come scegliere una notizia, come costruire hook + tesi + struttura,
  come evitare il riassuntino senza opinione, come controllare la qualità.
- **Il profilo di dominio** (`config/profile.md`): tutto ciò che cambia da un
  utente all'altro. Settore, aree di interesse, pubblico, voce, angoli
  editoriali, fonti da privilegiare, hashtag, anti-pattern specifici.

Un IT manager e un numismatico usano **lo stesso motore** e cambiano **solo il
profilo**.

## Come funziona (leggere prima di produrre output)

Ogni volta che la skill viene attivata, **prima di scrivere qualsiasi cosa**:

1. Leggi `config/profile.md`: è il profilo ATTIVO. Definisce dominio, pubblico,
   voce, aree, angoli, fonti, hashtag, lingua di output.
2. Applica `engine/editorial_engine.md` come logica operativa, sostituendo i
   segnaposto `{DOMINIO}`, `{AREE}`, `{PUBBLICO}`, `{ANGOLI}`, `{FONTI}`,
   `{HASHTAG}`, `{LINGUA}` con i valori del profilo.
3. Consulta gli altri file solo quando servono (vedi sotto).

Se `config/profile.md` non è stato personalizzato (contiene ancora valori di
esempio), segnalalo all'utente e proponi di compilarlo, ma procedi comunque
usando i valori presenti.

## Quando usare questa skill

Attivala quando l'utente chiede di:

- trovare notizie o trend rilevanti nel suo settore da commentare;
- scegliere la notizia migliore su cui costruire un post;
- scrivere un post LinkedIn a partire da una notizia;
- generare più varianti dello stesso post;
- migliorare un post per renderlo più credibile o più incisivo.

## File del pacchetto

Motore (generico, di norma non si tocca):

- `engine/editorial_engine.md` - logica operativa completa: ruolo, obiettivi, regole sulle fonti, struttura del post, output mode, quality bar.
- `engine/operating_prompts.md` - prompt pronti, con segnaposto che si riempiono dal profilo.
- `engine/anti_patterns.md` - errori da evitare validi per qualsiasi dominio.

Configurazione (questo lo personalizza l'utente):

- `config/profile.md` - PROFILO ATTIVO. Di default contiene il profilo IT, così la skill funziona subito.
- `config/profile.template.md` - modello vuoto da compilare per un nuovo dominio.
- `config/examples/profile.it-operations.md` - profilo IT (uguale al default).
- `config/examples/profile.numismatics.md` - profilo numismatica (monete romane): dimostra come cambia tutto cambiando solo il profilo.
- `config/examples/profile.en-cybersecurity.md` - profilo cybersecurity enterprise in inglese: dimostra il supporto multilingua.

Esempi e materiale di riferimento:

- `examples/reference-post.it-operations.md` - esempio di post (caso Gartner AI ROI) legato al profilo IT, utile come riferimento di tono e logica.
- `examples/post-library.template.md` - modello da riempire con post che rappresentano la voce desiderata.

- `README.md` - documentazione, architettura, come creare un nuovo profilo.

## Regola finale

Il compito non è ammirare la notizia, ma estrarne un punto di vista
professionale credibile e trasformarlo in un post che aiuti l'autore a
costruire reputazione e qualità di rete, qualunque sia il settore definito
nel profilo.
