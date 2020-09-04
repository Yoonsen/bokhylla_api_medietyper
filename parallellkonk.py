
import requests
import multiprocess as mp

word = 'vi'

def get_konks(urn, phrase, window = 500, n = 1000):
    
    querystring = '"'+ phrase +'"' 
    query = {
        'q':querystring,
        'fragments': n,
        'fragSize':window
       
    }
    r = requests.get("https://api.nb.no/catalog/v1/items/{urn}/contentfragments".format(urn=urn), params = query)
    res = r.json()
    results = []
    try:
        for x in res['contentFragments']:
            pid = x['pageid']
            hit = x['text']
            splits = hit.split('<em>')
            s2 = splits[1].split('</em>')
            before = splits[0]
            word = s2[0]
            after = s2[1]
            results.append({'urn': urn, 'before': before, 'word':word, 'after':after})
    except:
        True
    return results

def get_konkordanser(word = word, urns = None, window = 500, n = 1000):
    konks = []
    for u in urns:
        konks += get_konks(u, word, window = window, n = n)
    return konks



     