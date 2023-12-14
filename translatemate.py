import polib
from googletrans import Translator
from progress.bar import ShadyBar


def translate_text(text, target_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print('Error:', e," - Text:", text)
        return 'NoneType'

def create_new_translations(pot_file, po_file, target_language):
    count_new_translates = 0

    with ShadyBar('Creating new translations', suffix='%(percent).1f%% - %(eta)ds') as bar:
        for entry in pot_file:
            existing_translation = po_file.find(entry.msgid)
            if not existing_translation:
                count_new_translates += 1
                new_translation = translate_text(entry.msgid, target_language)
                entry.msgstr = new_translation
                po_file.append(entry)
            bar.next()
    bar.finish()

    return count_new_translates

def remove_deprecated_translations(pot_file, po_file):
    count_deprecated_translates = 0

    with ShadyBar('Removing deprecated translations', suffix='%(percent).1f%% - %(eta)ds') as bar:
        for entry in po_file:
            existing_msgid = pot_file.find(entry.msgid)
            if not existing_msgid:
                po_file.remove(entry)
                count_deprecated_translates += 1
            bar.next()
    bar.finish()

    return count_deprecated_translates

def merge_translations(pot_file, es_po_file, target_language):
    pot_file = polib.pofile(pot_file)
    po_file = polib.pofile(es_po_file)
    count_new_translates = 0
    count_deprecated_translates = 0

    count_new_translates = create_new_translations(pot_file, po_file, target_language)
    count_deprecated_translates = remove_deprecated_translations(pot_file, po_file)
    breakpoint()
    po_file.save()
    return count_new_translates, count_deprecated_translates

if __name__ == "__main__":
    pot_file_path = input("Enter the path to the .pot file: ")
    po_file_path = input("Enter the path to the es.po file: ")
    target_language = input("Enter the ISO 639-1 code of the target language (e.g., 'es' for Spanish): ")

    new_translations = merge_translations(pot_file_path, po_file_path, target_language)
    
    if new_translations[0] > 0 or new_translations[1] > 0:
        print("Translations merged and saved in:", po_file_path.split("/")[-1])
        print("Translates made:", new_translations[0])
        print("Removed deprecated translates:", new_translations[1])
