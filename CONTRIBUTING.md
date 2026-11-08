# Contributing

## Proposing a new domain profile

A new profile is a single markdown file that teaches the engine a new domain. Here is how to do it:

1. Copy `linkedin-post-generator/config/profile.template.md` to a new file:
   `linkedin-post-generator/config/examples/profile.<lang>-<domain>.md`
   (e.g. `profile.en-cybersecurity.md`, `profile.it-finanza.md`).

2. Fill in **all** fields: `DOMINIO`, `LINGUA`, `PUBBLICO`, `POSIZIONAMENTO_AUTORE`,
   `AREE`, `CONCETTI_CHIAVE`, `ANGOLI`, `FONTI`, `TONO`, `TONO_DA_EVITARE`,
   `HASHTAG`, `ANTI_PATTERN_SPECIFICI`.
   Leave no field blank. A vague field produces vague output.

3. Add at least one example post in `linkedin-post-generator/examples/` that shows
   the skill in action with your profile. Name it `reference-post.<lang>-<domain>.md`.
   Use an invented-but-realistic news item as the starting point.

4. Before opening a PR, run `make validate` from the repo root and confirm exit code 0.

5. In the PR body, state: domain, target audience, and how the profile differs from
   existing examples.

## Post quality standard

Every reference example must show the difference between a weak post and a skill-generated one:

- **Tesi obbligatoria**: every post must take a clear position. A summary without
  an opinion is not acceptable.
- **No hype**: no superlatives, no "this will change everything", no excitement
  unanchored to data.
- **Concreteness**: the point of view must be recognizable to someone who actually
  works in the domain.

## Before opening a PR

- `make validate` must pass with exit code 0.
- The profile must have all fields from the template — no empty sections.
- The example must show a before/after: mediocre post (summary, no thesis) vs
  skill-generated post (hook, news, interpretation, thesis, question, hashtags).

## Code / tooling changes

If you modify `scripts/validate.py` or `Makefile`:
- Keep `validate.py` stdlib-only (no external dependencies).
- Verify that `make build` produces a clean zip: run `unzip -l dist/linkedin-post-generator.zip`
  and confirm no `__MACOSX`, `.DS_Store`, or `._*` entries.
