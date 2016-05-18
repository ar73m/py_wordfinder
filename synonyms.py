# -*- coding: utf-8 -*-
import sys
import requests
from lxml import etree

def main(argv):
    if len(argv) < 2:
        print("Use: py -3 synonyms.py <word>")
    word = argv[1]
    array_synonyms = get_synonyms(word)
    print("Синонимы для слова: {0}".format(word))
    print()
    print(array_synonyms)
    
def get_synonyms(word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
        'Cookie': 'beget=begetok'
    }
    r = requests.get("http://www.classes.ru/search-item.php?i=44&q={word}&limit=10".format(word=word), headers=headers)
    text = r.text.strip()
    array_word = text.split("\n")
    if len(array_word) > 0:
        try:
            number = array_word[0].split("|")[1]
            r = requests.get("http://www.classes.ru/all-russian/russian-dictionary-synonyms-term-{number}.htm".format(number=number), headers=headers)
            tree = etree.HTML(r.text)
            text = tree.xpath('//p[@class="par1"]/text()')
            return text[0].encode('cp866', 'replace').decode('cp866')
        except:
            return "\"Не найдено\""
        
    return "\"Не найдено\""
    

if __name__ == "__main__":
    main(sys.argv)