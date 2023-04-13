dados_pessoais = 'Manoel Edvan de Sousa Fonseca Junior, 24 anos, solteiro, 097.366.424-02'
endereco = 'Rua Porfírio da costa, 153, apartamento 302, Santo Antônio, Patos, PB, 59891-920'

import re #Regular Expression -- RegEx

padrao = re.compile('[0123456789]{5}[-]{0,1}[0123456789]{3}')
padrao_cpf = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')

busca = padrao.search(endereco) #Match
busca_cpf = padrao_cpf.search(dados_pessoais)
if busca:
    cep = busca.group()
    cpf = busca_cpf.group()
    print(cep)
    print(cpf)
