from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'

    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(100))
    classificacao = banco.Column(banco.Float(precision=1))
    cep = banco.Column(banco.String(20))
    logradouro = banco.Column(banco.String(100))
    bairro = banco.Column(banco.String(100))
    cidade = banco.Column(banco.String(100))
    estado = banco.Column(banco.String(100))

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
