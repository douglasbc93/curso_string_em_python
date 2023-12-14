# re = Regular Expression - também chamado de RegEx
import re

endereco = "Rua conde de bonfim, 149, tijuca - 20520-050"

cep_padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = cep_padrao.search(endereco)

if busca:
    cep_padrao = busca.group()
    print(cep_padrao)
