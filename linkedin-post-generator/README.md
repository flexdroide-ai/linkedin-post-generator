# LinkedIn Post Generator

Skill per Claude che trasforma notizie di un settore configurabile in post LinkedIn con tesi e punto di vista.

**Documentazione completa, build e guida alla personalizzazione:** [README del repository](../README.md)

## Quick start

1. Apri `config/profile.md` e sostituisci il contenuto con il tuo dominio.
   Template vuoto: `config/profile.template.md` — esempi pronti: `config/examples/`.
2. Usa i prompt in `engine/operating_prompts.md` per attivare la skill.
3. Per buildare un nuovo zip: `make build` dalla root del repository.

## Architettura in breve

| Cartella | Contenuto |
|----------|-----------|
| `engine/` | Motore editoriale generico — logica invariante |
| `config/` | Profilo attivo e template — qui si personalizza |
| `examples/` | Post di riferimento per calibrare tono e struttura |
