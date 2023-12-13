# TranslateMate 🧉

**Script to simplify the management of translations in `.po` files by integrating automatic translation services.**

## Key Features

- **Automatic Translation Generation:** Utilizing the `googletrans` library, the script automatically translates messages without translation in a `.po` file to a language specified by the user.

- **Addition of New Messages (msgid):** Automatically identifies and adds new messages (msgid) found in a `.pot` file to the `.po` file. This ensures that all new text strings are included in the translations.

- **Removal of Obsolete Messages (msgid):** Detects and removes obsolete messages (msgid) from the `.po` file. This keeps translations up-to-date and avoids the presence of unnecessary text strings.

## Usage Instructions

1. **Environment Setup:**
    - Create a virtual environment using `virtualenv`.
    - Activate the virtual environment.

2. **Dependencies Installation:**
    - Run `pip install -r requirements.txt` to install the necessary libraries.

3. **Script Execution:**
    - Run the script using the command `python your_script.py`.
    - You will be prompted for the location of the `.pot` and `.po` files.
    - Enter the language code in ISO 639-1 format for the desired translation (e.g., 'es' for Spanish).

4. **Review of Results:**
    - The script will provide information about the performed translations, newly added messages, and removed obsolete messages.
