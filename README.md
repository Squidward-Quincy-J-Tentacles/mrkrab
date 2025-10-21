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
