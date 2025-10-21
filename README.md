# LabWordlist — Ethical Wordlist Generator (Lab / Research Only)

**IMPORTANT — Authorized Use Only**

`LabWordlist` is an educational tool to generate synthetic wordlists for **password-strength research, defensive testing, training, and lab-based penetration testing where you have explicit permission**.  
**Do NOT** use this tool against real systems, services, accounts, or people without clear, written authorization. Misuse may be illegal and unethical.

---

## Table of contents

- [About](#about)  
- [Highlights & Safe Modes](#highlights--safe-modes)  
- [Installation](#installation)  
- [Quick start — Safe demo](#quick-start---safe-demo)  
- [Recommended usage & safety controls](#recommended-usage--safety-controls)  
- [Design notes & suggested improvements](#design-notes--suggested-improvements)  
- [Contributing](#contributing)  
- [License](#license)  
- [Ethics & Legal](#ethics--legal)

---

## About

This repository contains a Python-based **wordlist generator** intended for:

- Creating **synthetic** randomness-based wordlists for password-strength experiments and fuzz-testing.
- Generating reproducible datasets for research and training in a contained lab environment.
- Teaching about the importance of strong passwords and how to defend against weak credentials.

It is adapted from an experimental script and must be used only in controlled, authorized environments.

---

## Highlights & Safe Modes

**Core idea:** produce wordlists that are safe to share publicly (randomized, non-personal). The default documentation below emphasizes a safe mode that **does not** accept victim information.

Recommended safe features to implement/enable (if you are the repo maintainer):

- `--lab-mode` (or `--safe-only`): prevents collection of personal/victim fields and disables functions that assemble victim-based lists. Default ON for public builds.
- `--random-only`: produce only randomized strings from vetted character sets.
- `--max-size`: hard cap on how many words can be generated in one run (e.g., default 100k) to avoid accidental generation of huge lists.
- Logging of runs to a local file with a notice of authorized use (for audit).

---

## Installation

> Tested with Python 3.9+ on Linux.

```bash
# clone
git clone https://github.com/Squidward-Quincy-J-Tentacles/mrkrab.git
cd mrkrab

# create venv (recommended)
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
