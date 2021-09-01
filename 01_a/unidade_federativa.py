class UnidadeFederativa:

    @staticmethod
    def get_lista_uf():
        v_unidades_federativas = ["Acre - AC","Amazonas - AM","Amapá - AP", "Pará - PA", "Rondônia - RO", "Roraima - RO", "Tocantins",
                        "Alagoas - AL ", "Bahia - BA", "Ceará - CE", "Maranhão - MA", "Paraíba - PB", "Pernambuco - PE", "Piauí - PI", "Rio Grande do Norte - RN", "Sergipe - SE",
                        "Paraná - PR", "Rio Grande do sul - RS", "Santa Catarina - SC",
                        "Espirito Santo - ES", "Minas Gerais - MG ", "Rio de Janeiro - RJ ", "São Paulo - SP",
                        "Goiás - GO", "Mato Grosso - MT ", "Mato Grosso do Sul - MS", "Distrito Federal - DF"]
        return v_unidades_federativas

    @staticmethod
    def get_UF(sigla):
        if sigla == 'SC':
            return 'Santa Catarina'
        elif sigla == 'RS':
            return 'Rio Grande do Sul'
        elif sigla == 'PR':
            return 'Paraná'
        elif sigla == 'SP':
            return 'São Paulo'
        elif sigla == 'RJ':
            return 'Rio de Janeiro'
        elif sigla == 'ES':
            return 'Espirito Santo'
        elif sigla == 'MG':
            return 'Minas Gerais'
        elif sigla == 'MT':
            return 'Mato Grosso'
        elif sigla == 'MS':
            return 'Mato Grosso do Sul'
        elif sigla == 'GO':
            return 'Goias'
        elif sigla == 'DF':
            return 'Distrito Federal'
        elif sigla == 'AM':
            return 'Amazonas'
        elif sigla == 'PA':
            return 'Pará'
        elif sigla == 'AC':
            return 'Acre'
        elif sigla == 'RO':
            return 'Rondônia'
        elif sigla == 'RR':
            return 'Roraima'
        elif sigla == 'TO':
            return 'Tocantins'
        elif sigla == 'RN':
            return 'Rio Grande do Norte'
        elif sigla == 'BA':
            return 'Bahia'
        elif sigla == 'BA':
            return 'Bahia'
        elif sigla == 'AL':
            return 'Alagoas'
        elif sigla == 'CE':
            return 'Ceará'
        elif sigla == 'MA':
            return 'Maranhão'
        elif sigla == 'PB':
            return 'Paraíba'
        elif sigla == 'PB':
            return 'Paraíba'
        elif sigla == 'PE':
            return 'Pernambuco'
        elif sigla == 'PI':
            return 'Piauí'
        elif sigla == 'SE':
            return 'Sergipe'
