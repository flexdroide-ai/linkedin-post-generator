# Changelog

All notable changes to this project will be documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [2.1.0] - 2026-06-26

### Added
- `config/examples/profile.en-cybersecurity.md` — English-language profile for cybersecurity (CISO/SOC audience), demonstrating multilingual support.
- `scripts/validate.py` — validation script (stdlib-only) that checks SKILL.md frontmatter, naming rules, description length, and missing file references.
- `Makefile` — reproducible build: `make validate`, `make build`, `make clean`.
- `CONTRIBUTING.md` — guide for proposing new domain profiles.
- Repo-level `README.md` with before/after post examples and upload instructions.

### Changed
- `SKILL.md` frontmatter aligned to agentskills.io spec:
  - `version` moved from top-level field to `metadata.version` (top-level `version` is non-standard).
  - Added standard optional fields: `license`, `compatibility`.
- Repo restructured: skill folder (`linkedin-post-generator/`) is now a subfolder of the repo root, with tooling (scripts, Makefile) at repo level and outside the zip.

### Spec divergence noted
- agentskills.io allows `description` up to 1024 chars; Claude.ai enforces 200 chars.
  The validator uses 200 as the limit (more restrictive wins for upload compatibility).
- agentskills.io spec does not mention a `claude` reserved-word restriction on `name`;
  Claude.ai does. Both constraints are enforced by the validator.

## [2.0.0] - 2026-06-25

### Added
- Separation of engine and profile: `engine/` is domain-agnostic, `config/profile.md` is domain-specific.
- Configurable domain: any sector, not just IT. Placeholders `{DOMINIO}`, `{AREE}`, `{PUBBLICO}`, etc.
- Example profile: numismatics / Roman coins (`config/examples/profile.numismatics.md`).
- Profile template: `config/profile.template.md` — blank schema to fill in for a new domain.

### Changed
- `SKILL.md` decoupled from the IT context; engine operates via placeholders resolved at runtime from the active profile.

## [1.x]

Initial version, hardcoded to the IT domain (ITSM, Infrastructure & Operations, AI applied to IT). Engine and profile were merged into a single file.
