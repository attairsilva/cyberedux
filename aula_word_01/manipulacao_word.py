from docxtpl import DocxTemplate

template = DocxTemplate('template1.docx')

contexto = {
    'minha_variavel': 'Testando o docxtpl'
}

template.render(contexto)
template.save('teste.docx')