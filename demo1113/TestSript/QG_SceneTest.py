import  unittest
from api2018.Sendhttp import SendHttp
from api2018 import Common
class SceneTest(unittest.TestCase):
    def setUp(self):
        Login_url = "/common/fgadmin/login"
        AddressList_url = "/fgadmin/address/list"

    #登录
    def Login_Test(self):
        user = {"phoneArea": "86", "phoneNumber": "20000000000", "password": "netease123"}
        result = SendHttp().run_http(self.Login_url, "POST", user)
        print(result)
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], 'success')

    #查询收货地址
    def test_address_by_Login(self):
        user = {"phoneArea": "86", "phoneNumber": "200000000066", "password": "netease123"}
        result = SendHttp().sent_get_bycookies(self.url, Common.getcookies(user))
        print(result)

    #添加收货地址
    def test_address_by_Login(self):
        user = {"phoneArea": "86", "phoneNumber": "200000000066", "password": "netease123"}
        Address={"id":"","receiverName":"杨天莹","cellPhone":"15211111111","province":"新疆维吾尔自治区","city":"乌鲁木齐市","area":"天山区","addressDetail":"城南区"}
        result = SendHttp().send_post_bycookie(self.url, Address,Common.getcookies(user))
        print(result)
        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], 'success')

    #

