import  unittest
from api2018.Sendhttp import SendHttp
from api2018 import Common

class Addaddress(unittest.TestCase):
    def setUp(self):
        self.url= "/fgadmin/address/new"

    def test_address_by_Login(self):
        user = {"phoneArea": "86", "phoneNumber": "200000000066", "password": "netease123"}
        Address={"id":"","receiverName":"杨天莹","cellPhone":"15211111111","province":"新疆维吾尔自治区","city":"乌鲁木齐市","area":"天山区","addressDetail":"城南区"}
        result = SendHttp().send_post_bycookie(self.url, Address,Common.getcookies(user))
        print(result)
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], 'success')