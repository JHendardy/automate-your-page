line_space = '''
                  '''
line_space2 ='''
              '''
def generate_concept_HTML(concept_title, body_text):
    html_text = '''
        <div class="idea-name">
           <h3>''' + concept_title + '''</h3>
           <div class="idea-concept">
               <p> ''' + line_space + body_text + line_space2 + ''' </p>
           </div>
        </div>'''
    return html_text

def make_HTML(concept):
    concept_title = concept[0]
    body_text = concept[1]
    return generate_concept_HTML(concept_title, body_text)

LIST_OF_CONCEPTS = [ ['title 1', 'description 1'],
                     ['title 2', 'description 2'],
                     ['title 3', 'description 3'] ]


def make_HTML_for_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_concepts(LIST_OF_CONCEPTS)