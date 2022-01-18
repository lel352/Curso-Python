"""
Documentção:
https://pythonhosted.org/PyPDF2/
Exemplos:
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
"""

import PyPDF2
import os

caminho_dos_pdfs = r'C:\Users\desen\Downloads\serie2'


novo_pdf = PyPDF2.PdfFileMerger() # chamando um classe que Uni
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        if file in '.pdf':
            caminho_completo_arquivo = os.path.join(root, file)

            # arquivo_pdf = open(caminho_completo_arquivo,'rb')  # rb modo de leitura bytes,
            # não é bom abrir arquivo desse modo

            with open(caminho_completo_arquivo, 'rb') as arquivo_pdf:
                novo_pdf.append(arquivo_pdf)


with open(fr'{caminho_dos_pdfs}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)



with open(r'C:\Users\desen\Downloads\serie2\a.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()
    print(num_paginas)

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(fr'C:\Users\desen\Downloads\serie2\{num_paginas}.pdg', 'wb') as novo_pdf:
            escritor.write(novo_pdf)

