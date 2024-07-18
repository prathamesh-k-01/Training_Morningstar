class Company():
    def __init__(self, symbol, company_name, current_price, shares_available) -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.current_price = current_price
        self.shares_available = shares_available

    def total_value(self):
        value = self.current_price * self.shares_available
        return value
    
    def add_attribute(self, attribute_name, attribute_value):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value



Apple = Company(symbol="AAPL", company_name="Apple Inc.", current_price=150.0, shares_available=1000)
Tesla = Company(symbol="TSLA", company_name='Tesla Inc.', current_price=650, shares_available=500)

Apple.add_attribute('market_sector', 'Technology')
Tesla.add_attribute('market_sector', 'motor')

value = Apple.total_value()
print("The total value of the company is ",value)
print(Apple.__dict__)
print(Tesla.__dict__)