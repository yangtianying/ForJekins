import  unittest
from api2018.Sendhttp import SendHttp
from api2018 import Common

#计算运费
class getTransportFee(unittest.TestCase):
    def setUp(self):
        self.url= "/common/getTransportFee"

    def getTransportFee(self):
        user = {"phoneArea": "86", "phoneNumber": "200000000066", "password": "netease123"}
        result=SendHttp().sent_get_bycookies(self.url,Common.getcookies(user))
        print(result)