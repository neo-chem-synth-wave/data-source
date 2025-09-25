# Data Source
[![Static Badge](https://img.shields.io/badge/data__source-2025.9.1-%23E68E36?logo=github&style=flat)](https://github.com/neo-chem-synth-wave/data-source/releases/tag/2025.9.1)
[![Static Badge](https://img.shields.io/badge/Institute%20of%20Science%20Tokyo-%231C3177?style=flat)](https://www.isct.ac.jp)
[![Static Badge](https://img.shields.io/badge/Elix%2C%20Inc.-%235EB6B3?style=flat)](https://www.elix-inc.com)

Welcome to the computer-assisted chemical synthesis **data source** research project !!!

Thanks for your interest in contributing! This repository welcomes feedback, bug reports, and improvements. This guide explains how to:
- Share feedback and report problems using GitHub Issues.
- Propose code or data improvements by opening Pull Requests (PRs).

If anything here is unclear, please open an issue and we’ll help.

---

## Ground rules

- Be respectful and constructive. We follow the spirit of the Contributor Covenant (https://www.contributor-covenant.org/).
- Do not commit secrets, credentials, or private data.
- For data contributions, ensure proper licensing, anonymization, and provenance.

By contributing, you agree that your contributions will be licensed under the project’s license.

---

## How to submit feedback (GitHub Issues)

Use Issues for:
- Bug reports (something is broken or incorrect)
- Feature requests (new capability or enhancement)
- Questions or clarifications
- Documentation improvements
- Data requests or data-quality reports

Before filing:
- Search existing issues to avoid duplicates.
- If you find a related issue, add a comment or reaction instead of opening a new one.

When filing a new issue, please include:
- A clear, descriptive title
- What happened vs. what you expected
- Steps to reproduce (if applicable)
- Environment details (tooling versions, OS) if relevant
- Screenshots, logs, or minimal examples (if safe to share)
- For data issues: data source, affected files/tables, row counts or sample rows (redacted/anonymized), and any observed constraints or schema mismatches

Recommended labels (if available):
- bug, enhancement, question, documentation, data, performance, good first issue

Tip: If you’re unsure which category to use, open the issue anyway—maintainers will help triage.

---

## How to suggest improvements (Pull Requests)

Pull Requests are the best way to propose code, documentation, or data pipeline improvements.

General guidelines:
- Keep PRs focused and scoped (small, incremental changes are easier to review).
- For larger changes, open an issue first to discuss the approach.
- Link related issues using “Fixes #123” or “Closes #123” in the PR description.
- Include tests and documentation updates when applicable.
- Ensure CI checks pass.

Typical workflow:
1. Fork the repo and create a topic branch:
   - Suggested naming: `feature/short-description`, `fix/short-description`, or `chore/short-description`
2. Make your changes
   - Follow existing patterns and style in the repository.
   - Add or update tests if the project has a test suite.
   - Update docs, READMEs, and examples as needed.
3. Run local checks
   - If the repo provides scripts or tooling (linting, formatting, tests), run them before pushing.
   - If no tooling is configured, ensure your changes are consistent and build/run locally where applicable.
4. Push your branch and open a PR
   - Fill out the PR template if present.
   - Provide context: what changed, why, and how you validated it.
   - Add screenshots, sample outputs, or logs when helpful.

Commit messages:
- Prefer clear, imperative subject lines (e.g., “Add X”, “Fix Y”).
- Conventional Commits are welcome (e.g., `feat:`, `fix:`, `docs:`, `chore:`), but not required.

Review process:
- Maintainers will review and may request changes.
- Please be responsive to feedback; small follow-up commits are fine.
- The PR will be merged once it meets project standards and passes checks.

---

## Data-specific contributions

If this repository handles datasets or data pipelines, please follow these additional guidelines:

Data quality and ethics:
- Do not include sensitive or personal data. Anonymize and aggregate where applicable.
- Confirm you have rights to use and share the data (respect licenses and terms).
- Include data provenance (source, date of retrieval, method of collection).
- Document schemas: field names, types, units, nullability, constraints.

Files and size:
- Avoid committing large binaries directly. If Git LFS is enabled, use it for large files; otherwise open an issue to discuss alternatives (external storage, downloads at build-time).
- Prefer diff-friendly formats (CSV, JSON Lines, Parquet) and avoid proprietary formats when possible.

Reproducibility:
- Provide scripts or instructions to fetch, clean, and transform data when feasible.
- Include versioning or snapshots so results are reproducible.

Validation:
- If the repo includes data validators or checks (schemas, tests), run them and include results in your PR description.

---

## Documentation

- Update README and any relevant docs for user-facing changes.
- Include examples or usage notes if behavior changes.
- Add inline comments where non-obvious logic exists.

---

## Security

- Do not include secrets, tokens, or credentials in code, configs, or data.
- If you discover a security vulnerability, do not open a public issue. Instead, please contact the maintainers privately if a SECURITY policy is provided; otherwise open a minimal issue asking for a private channel to report details.

---

## Getting help

- Not sure where to start? Look for `good first issue` or `help wanted` labels.
- Have questions? Open an issue with the `question` label.

We appreciate your time and contributions—thank you for helping improve neo-chem-synth-wave/data-source!
