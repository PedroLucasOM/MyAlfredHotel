class HotelModel:
    def __init__(self, id, nome, classificacao, cep, logradouro, bairro, cidade, estado):
        self.id = id
        self.nome = nome
        self.classificacao = classificacao
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def json(self):
        return {
            'id' : self.id,
            'nome' : self.nome,
            'cep' : self.cep,
            'logradouro' : self.logradouro,
            'bairro' : self.bairro,
            'cidade' : self.cidade,
            'estado' : self.estado
        }
