import pypinyin
from pypinyin.contrib.tone_convert import to_tone, to_normal
import json

def process_character(char):
    pinyin_list = pypinyin.pinyin(char, style=pypinyin.Style.TONE3, heteronym=True)[0]
    results = []
    for pinyin_entry in pinyin_list:
        pinyin_str = to_tone(pinyin_entry)
        jianpin = to_normal(pinyin_entry)
        results.append({"hanzi": char, "pinyin": pinyin_str, "jianpin": jianpin})
    return results

def main():
    with open("ziku.txt", "r", encoding="utf-8") as f:
        text = f.read()

    all_results = []
    for char in text:
        if char.strip():  # Ignore whitespace
            all_results.extend(process_character(char))

    with open("Simplified.json", "w", encoding="utf-8") as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()