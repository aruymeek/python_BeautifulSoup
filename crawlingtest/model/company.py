class CompanyModel:

    def __init__(self, _name, _cate, _country, _score, _rank20, _rank19):
        self.name = _name
        self.category = _cate
        self.country = _country
        self.score = _score
        self.rank2020 = _rank20
        self.rank2019 = _rank19

    def SaveFormat(self):
        #CompanyModel 내의 변수들(name, category, ...)을 이용하여 만드는 메서드이므로,
        #이 메서드는 매개변수 따로 필요 X / self는 반드시 필요!
        data = '{0};{1};{2};{3};{4};{5}'.format(self.name, self.category, self.country, self.score, self.rank2020, self.rank2019)

        return data
