# mrkrab — Wordlist Generator (Lab / Research Only)

**IMPORTANT — Authorized Use Only**

`mrkrab` is an interactive wordlist generator intended **only** for educational, defensive, research, and lab-based use where you have **explicit written permission**.
**Do NOT** use `mrkrab` against real accounts, online services, or people without authorization. Misuse may be illegal and unethical.

---

## Quick summary

`mrkrab` is a terminal-based, interactive Python program that generates wordlists. It supports three main generation flows:

* Randomized wordlists from selectable character sets.
* Fixed-length randomized wordlists.
* Full combinatorial generation across a specified start/end length.

The script also contains an interactive option to collect simple "victim" fields (name and birth components) and include them in generated lists. This option exists in the current code but must be used **only** in authorized, offline lab environments.

---

## Installation

Requirements: Python 3.8+ and `psutil`.

1. Place `mrkrab.py` in a folder (or clone the repository).

```bash
git clone https://github.com/<your-username>/mrkrab.git
cd mrkrab
```

2. (Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the tool:

```bash
python3 mrkrab.py
```

---

## Run / Interactive menu (exact behavior in current code)

When you run the script it prints an ASCII header with brief system info (username, RAM, disk, OS, time/date) and then shows the main menu.

**Main menu options:**

* `[01] Random Word List` — interactive generation using a chosen character set.
* `[02] Wordlist with Victim Information` — prompts for first/middle/last name and birth components and can combine those with selected character sets.
* `[03] Exit` — exit the program.

If you select option `1` or `2`, the script shows a **sub-menu** with three generation methods:

* `[01] Random Range`

  * Prompts: how many words to generate.
  * Uses a default safe min/max length (in the script) and chooses a random length for each generated word.
* `[02] Provide Number of Character`

  * Prompts: exact length for each word and how many words to generate.
  * Produces `num_words` each of the specified `length`.
* `[03] Provide Start & End Value`

  * Prompts for a size scale using the format `start:end` (e.g., `1:8` is provided as `1:8` or `1:8` equivalent in the prompts).
  * For each length in the range it generates every combination using `itertools.product(charset, repeat=length)` and writes them to the output file.

After you choose a generation method, the script asks for character-set choices (for `Random Word List`) or victim fields (for `Wordlist with Victim Information`) and then asks for an output filename. The resulting wordlist is written to the file, one entry per line.

**Character-set prompts (current behavior)**

* `Do You Want Special Characters? [Y/n]`
* `Do You Want Lowercase? [Y/n]`
* `Do You Want Uppercase? [Y/n]`
* `Do You Want Numeric Characters? [Y/n]`

The special characters list in the script is: `!\][/?.,~-=";:><@#$%&*()_+' ` (as implemented in the code).

**Victim info prompts (current behavior)**

* `[*] First Name:`
* `[*] Middle Name:`
* `[*] Last Name:`
* `[*] Birth Date:`
* `[*] Birth Month:`
* `[*] Birth Year:`

The script concatenates these fields and (depending on follow-up prompts) appends other character categories if requested.

---

## Output

* The tool writes plain text files in the current working directory.
* Each generated password/entry is written on its own line.
* For combinatorial generation (`Start & End`) the output size can grow very large — the current code will iterate through all combinations without an internal hard cap.

---

## Example (safe, recommended)

To run a safe demo in the current code (use randomized-only options and do not enter victim data):

1. Run the script:

```
python3 mrkrab.py
```

2. Choose `Random Word List` → `Random Range` → select character sets (lowercase, uppercase, digits, special) → provide an output filename → enter number of words (e.g., `1000`).

This creates `output_filename` containing 1000 randomized strings.

---

## Important safety notes (reflects current tool state)

* The `Wordlist with Victim Information` option **collects personal data** if used. Do not use this option except in fully authorized, offline lab environments.
* Combinatorial mode (`Start & End`) can produce extremely large files; the current script does not enforce a maximum output size — use extreme caution.
* Always run `mrkrab` in a controlled, local environment (VM/container) with no access to systems you do not own when experimenting.

---

## License & attribution

Add a `LICENSE` file to your repository. If you choose MIT, include the full MIT license text in `LICENSE` and replace the copyright placeholders.

---

If this is ready, I can save this exact `README.md` content into the repository files for you. No additional features or suggested flags were added—the file documents only the current behavior present in the code.
