from docxtpl import DocxTemplate

template = DocxTemplate('carros_modelo.docx')

carros = [
         ['AVX-0101','Fiat','Toro','Branco'],
         ['TRF-2328','Nissan','Leaf','Prata'],
         ['AVX-3891','Chevrolet','Primas','Branco']
]

contexto = {
    'carros': carros
}
template.render(contexto)
template.save('carros_01.docx')