class User:
    def __init__(self, name):
        self.name = name
        self.email = name + '@example.com'
        self.password = name + '123'
        self.phoneNumber = 0
        self.address = 'Calle 123'
        self.subscription = Subscription(self)
        self.paymentMethod = PaymentMethod(self)

class Subscription:
    def __init__(self, user):
        self.user = user
        self.status = 'active'
        self.plan = 'free'


class PaymentMethod:
    def __init__(self, user):
        self.user = user
        self.cardNumber = '123456789'
        self.expirationDate = '01/01/2020'
        self.cvv = '123'

class ProductTrackList:
    def __init__(self, user):
        self.user = user
        self.tracks = []


class UserCustomSites:
    def __init__(self, user):
        self.user = user
        self.sites = []


class UserProducts:
    def __init__(self, user):
        self.user = user
        self.products = []
