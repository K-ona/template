from stanfordcorenlp import StanfordCoreNLP
import json

nlp = StanfordCoreNLP(r'D:\Python\stanford-corenlp-4.1.0')

text = '''The Indian strategic forces got a major boost on Sunday after the Defence Research and Development Organisation (DRDO) 
tested a 3,500-kilometre range submarine-launched K-4 ballistic missile off the Vizag coast, with the nuclear weapon meeting all its target objectives, 
officials with direct knowledge of the matter said. '''

props = {'annotators': 'openie','pipelineLanguage':'en','outputFormat':'json'}
props2 = {'annotators': 'tokenize, ssplit, pos, lemma, parse, ner, coref, kbp',
            'pipelineLanguage':'en','outputFormat':'json'}


core_nlp_output = json.loads(nlp.annotate(text, properties=props))
core_nlp_output2 = json.loads(nlp.annotate(text, properties=props2))

triples = []
triples2 = []
for sentence in core_nlp_output['sentences']:
    for triple in sentence['openie']:
        triples.append({
            'subject': triple['subject'],
            'relation': triple['relation'],
            'object': triple['object']
        })

for sentence in core_nlp_output2['sentences']:
    for entity in sentence['entitymentions']:
        print(entity['text'])
    for triple in sentence['kbp']:
        triples2.append({
            'subject': triple['subject'],
            'relation': triple['relation'],
            'object': triple['object']
        })
# if triples2 == triples:
#     print('same')
# else :

    # print(triples)
for _ in triples:
    print(_)
nlp.close()