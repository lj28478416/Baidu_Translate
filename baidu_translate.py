import requests
import re
from jsonpath import jsonpath
import execjs


class Baidu_Spider:
    def __init__(self, str1):
        self.str1 = str1
        self.data = {
            'from': None,
            'to': None,
            'query': self.str1,
            # 'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': None,
            'token': None
        }
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': str(len(self.str1)),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BIDUPSID=5F41AD72DE2B70C7E5B720C1AAC5D934; PSTM=1520767606; __cfduid=d80aee4399f1af462023406b1186041001521651362; BDUSS=dIODJYZUliaUpjM0ZLT2FWQlczdVZMWHdLODhuWHdGeGZGdjVPZ045a0ctdHBhQVFBQUFBJCQAAAAAAAAAAAEAAABAWnAJ1b25-rXEs~bX4rO1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZts1oGbbNaUl; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID=9FB74B58935632576109BF783DAA9891:FG=1; H_PS_PSSID=1452_26459_21103_22073; BDSFRCVID=DCCsJeC629o9EeO7s9P4Ur6YL_gB6hcTH6aoAYcV90HgLjMCvnQkEG0PDx8g0Kub-jINogKK3gOTH4nP; H_BDCLCKID_SF=tJPqoCtKtCvHfP8k-tcH244Hqxby26n-fRneaJ5n0-nnhP3vXqKbKPuVjUnRqPb-benabUoMJnOG8RKRy6C-jTvBDG_eq-JQ2C7WsJjs24ThD6rnhPF3XlKvKP6-3MJO3b7CLR0KJ-OVh43SMn3D3h8mqt6baf3A0ekeohFLtDKKMD-CDT035n-Wql702-6MaC6y0njVanI_Hn7zentbQbtpbt-qJj5L3CO03K3b3hbA8DbC2xTV5njQhh5nBT5Ka26CQ4jCbUj0VnKwjUJV3btkQN3T0nkO5bRiLRoLBxTcDn3oyTbJXp0njMTTqjDJfRCJoCPyfbP_etbg-trSMDCShUFs547C-2Q-5KL-fRABsJ5FjnbnQhLIjhjEWJvn2DTCLfbdJJjoEfTn36u2y--TM4cm-t6I22TxoUJgMInJhhvG-Cc8yfCebPRiJ-b9Qg-JWftLtDKbbD-Cj6-3Mb03K2TEaPcQ2C6X0njVanI_HnurbhOzKUI8LNDHtjcvWe3B_-O-5M7lqxb9Mt_hD-443bO7ttoyt6CfoJ3JyloDEnP9KljSeML1Db3BW6vMtg3t3tQ6aDnoepvoDPJc3Mv3hR0EJjLJJbkJoCLQb-3bK43ph4Oo5tFQqxby26nvWgneaJ5nJDohExo50RKbKTFh-noHtqcr565KsCJvQpP-HJ7DbRQD5bFiMbj33q58JCrCKl0MLpbWbb0xynoDDqKvKfnMBMPe52OnaIb8LIFKMKIlj5LWe5PJqxoJKPo0aIKX3b7EfhbTEPO_bf--D6Feeto-W5befG4J-4_KylRrep_CM-bxy5K_hPQk5hK8tgbM2ncz0-Q_VJvHQT3mQbvbbN3i-4DL2e5wWb3cWKOJ8UbSj-Tme4tX-NFqJTKj3f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531655355,1531655743,1531656413,1531656420; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531656420; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
            'Host': 'fanyi.baidu.com',
            'Origin': 'http://fanyi.baidu.com',
            'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_token_gtk(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'BIDUPSID=5F41AD72DE2B70C7E5B720C1AAC5D934; PSTM=1520767606; __cfduid=d80aee4399f1af462023406b1186041001521651362; BDUSS=dIODJYZUliaUpjM0ZLT2FWQlczdVZMWHdLODhuWHdGeGZGdjVPZ045a0ctdHBhQVFBQUFBJCQAAAAAAAAAAAEAAABAWnAJ1b25-rXEs~bX4rO1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZts1oGbbNaUl; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID=9FB74B58935632576109BF783DAA9891:FG=1; H_PS_PSSID=1452_26459_21103_22073; BDSFRCVID=DCCsJeC629o9EeO7s9P4Ur6YL_gB6hcTH6aoAYcV90HgLjMCvnQkEG0PDx8g0Kub-jINogKK3gOTH4nP; H_BDCLCKID_SF=tJPqoCtKtCvHfP8k-tcH244Hqxby26n-fRneaJ5n0-nnhP3vXqKbKPuVjUnRqPb-benabUoMJnOG8RKRy6C-jTvBDG_eq-JQ2C7WsJjs24ThD6rnhPF3XlKvKP6-3MJO3b7CLR0KJ-OVh43SMn3D3h8mqt6baf3A0ekeohFLtDKKMD-CDT035n-Wql702-6MaC6y0njVanI_Hn7zentbQbtpbt-qJj5L3CO03K3b3hbA8DbC2xTV5njQhh5nBT5Ka26CQ4jCbUj0VnKwjUJV3btkQN3T0nkO5bRiLRoLBxTcDn3oyTbJXp0njMTTqjDJfRCJoCPyfbP_etbg-trSMDCShUFs547C-2Q-5KL-fRABsJ5FjnbnQhLIjhjEWJvn2DTCLfbdJJjoEfTn36u2y--TM4cm-t6I22TxoUJgMInJhhvG-Cc8yfCebPRiJ-b9Qg-JWftLtDKbbD-Cj6-3Mb03K2TEaPcQ2C6X0njVanI_HnurbhOzKUI8LNDHtjcvWe3B_-O-5M7lqxb9Mt_hD-443bO7ttoyt6CfoJ3JyloDEnP9KljSeML1Db3BW6vMtg3t3tQ6aDnoepvoDPJc3Mv3hR0EJjLJJbkJoCLQb-3bK43ph4Oo5tFQqxby26nvWgneaJ5nJDohExo50RKbKTFh-noHtqcr565KsCJvQpP-HJ7DbRQD5bFiMbj33q58JCrCKl0MLpbWbb0xynoDDqKvKfnMBMPe52OnaIb8LIFKMKIlj5LWe5PJqxoJKPo0aIKX3b7EfhbTEPO_bf--D6Feeto-W5befG4J-4_KylRrep_CM-bxy5K_hPQk5hK8tgbM2ncz0-Q_VJvHQT3mQbvbbN3i-4DL2e5wWb3cWKOJ8UbSj-Tme4tX-NFqJTKj3f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531655355,1531655743,1531656413,1531656420; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531659240',
            'Host': 'fanyi.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        }
        url1 = 'http://fanyi.baidu.com/?'
        response = requests.get(url1, headers=headers).content.decode()
        partten = re.compile(r"token:\s'(.*?)',")
        token = re.search(partten, response).group(1)
        partten1 = re.compile(r"window.gtk\s=\s'([\d\.]+?)';")
        gtk = re.search(partten1, response).group(1)
        self.data['token'] = token
        self.gtk = gtk

    def get_language_class(self):
        url = 'http://fanyi.baidu.com/langdetect'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BIDUPSID=5F41AD72DE2B70C7E5B720C1AAC5D934; PSTM=1520767606;'
                      ' __cfduid=d80aee4399f1af462023406b1186041001521651362;'
                      ' BDUSS=dIODJYZUliaUpjM0ZLT2FWQlczdVZMWHdLODhuWHdGeGZGdj'
                      'VPZ045a0ctdHBhQVFBQUFBJCQAAAAAAAAAAAEAAABAWnAJ1b25-rXEs'
                      '~bX4rO1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
                      'AAAAAAAAAAAAAAAAAAAZts1oGbbNaUl; REALTIME_TRANS_SWITCH=1;'
                      ' FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1;'
                      ' SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0;'
                      ' BAIDUID=9FB74B58935632576109BF783DAA9891:FG=1;'
                      ' H_PS_PSSID=1452_26459_21103_22073;'
                      ' BDSFRCVID=DCCsJeC629o9EeO7s9P4Ur6YL_gB6hcTH6ao'
                      'AYcV90HgLjMCvnQkEG0PDx8g0Kub-jINogKK3gOTH4nP; '
                      'H_BDCLCKID_SF=tJPqoCtKtCvHfP8k-tcH244Hqxby26n-fRnea'
                      'J5n0-nnhP3vXqKbKPuVjUnRqPb-benabUoMJnOG8RKRy6C-jTvBD'
                      'G_eq-JQ2C7WsJjs24ThD6rnhPF3XlKvKP6-3MJO3b7CLR0KJ-OVh'
                      '43SMn3D3h8mqt6baf3A0ekeohFLtDKKMD-CDT035n-Wql702-6Ma'
                      'C6y0njVanI_Hn7zentbQbtpbt-qJj5L3CO03K3b3hbA8DbC2xTV5n'
                      'jQhh5nBT5Ka26CQ4jCbUj0VnKwjUJV3btkQN3T0nkO5bRiLRoLBxTc'
                      'Dn3oyTbJXp0njMTTqjDJfRCJoCPyfbP_etbg-trSMDCShUFs547C-2'
                      'Q-5KL-fRABsJ5FjnbnQhLIjhjEWJvn2DTCLfbdJJjoEfTn36u2y--T'
                      'M4cm-t6I22TxoUJgMInJhhvG-Cc8yfCebPRiJ-b9Qg-JWftLtDKbbD-'
                      'Cj6-3Mb03K2TEaPcQ2C6X0njVanI_HnurbhOzKUI8LNDHtjcvWe3B_-O'
                      '-5M7lqxb9Mt_hD-443bO7ttoyt6CfoJ3JyloDEnP9KljSeML1Db3BW6v'
                      'Mtg3t3tQ6aDnoepvoDPJc3Mv3hR0EJjLJJbkJoCLQb-3bK43ph4Oo5tF'
                      'Qqxby26nvWgneaJ5nJDohExo50RKbKTFh-noHtqcr565KsCJvQpP-HJ7'
                      'DbRQD5bFiMbj33q58JCrCKl0MLpbWbb0xynoDDqKvKfnMBMPe52OnaIb'
                      '8LIFKMKIlj5LWe5PJqxoJKPo0aIKX3b7EfhbTEPO_bf--D6Feeto-W5b'
                      'efG4J-4_KylRrep_CM-bxy5K_hPQk5hK8tgbM2ncz0-Q_VJvHQT3mQbv'
                      'bbN3i-4DL2e5wWb3cWKOJ8UbSj-Tme4tX-NFqJTKj3f; Hm_lvt_64ec'
                      'd82404c51e03dc91cb9e8c025574=1531655355,1531655743,15316'
                      '56413,1531656420; locale=zh; to_lang_often=%5B%7B%22valu'
                      'e%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%'
                      '7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%'
                      '22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22spa%22%'
                      '2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%2'
                      '2value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7'
                      'D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u'
                      '8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574='
                      '1531659249',
            'Host': 'fanyi.baidu.com',
            'Origin': 'http://fanyi.baidu.com',
            'Referer': 'http://fanyi.baidu.com/?',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.117 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'query': self.str1
        }
        if len(data['query']) >= 50:
            data['query'] = data['query'][:50]
        language_class_response = requests.post(url, headers=headers, data=data).json()
        language_class = jsonpath(language_class_response, '$..lan')[0]
        if language_class == 'zh':
            self.data['from'] = 'zh'
            self.data['to'] = 'en'
        else:
            self.data['from'] = 'en'
            self.data['to'] = 'zh'

    def get_sign(self):
        self.data['sign'] = execjs.compile(open(r"sign.js").read()).call('hash', self.str1, self.gtk)

    def open_url(self):
        url2 = 'http://fanyi.baidu.com/v2transapi'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'BIDUPSID=5F41AD72DE2B70C7E5B720C1AAC5D934; PSTM=1520767606; __cfduid=d80aee4399f1af462023406b1186041001521651362; BDUSS=dIODJYZUliaUpjM0ZLT2FWQlczdVZMWHdLODhuWHdGeGZGdjVPZ045a0ctdHBhQVFBQUFBJCQAAAAAAAAAAAEAAABAWnAJ1b25-rXEs~bX4rO1AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZts1oGbbNaUl; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID=9FB74B58935632576109BF783DAA9891:FG=1; H_PS_PSSID=1452_26459_21103_22073; BDSFRCVID=DCCsJeC629o9EeO7s9P4Ur6YL_gB6hcTH6aoAYcV90HgLjMCvnQkEG0PDx8g0Kub-jINogKK3gOTH4nP; H_BDCLCKID_SF=tJPqoCtKtCvHfP8k-tcH244Hqxby26n-fRneaJ5n0-nnhP3vXqKbKPuVjUnRqPb-benabUoMJnOG8RKRy6C-jTvBDG_eq-JQ2C7WsJjs24ThD6rnhPF3XlKvKP6-3MJO3b7CLR0KJ-OVh43SMn3D3h8mqt6baf3A0ekeohFLtDKKMD-CDT035n-Wql702-6MaC6y0njVanI_Hn7zentbQbtpbt-qJj5L3CO03K3b3hbA8DbC2xTV5njQhh5nBT5Ka26CQ4jCbUj0VnKwjUJV3btkQN3T0nkO5bRiLRoLBxTcDn3oyTbJXp0njMTTqjDJfRCJoCPyfbP_etbg-trSMDCShUFs547C-2Q-5KL-fRABsJ5FjnbnQhLIjhjEWJvn2DTCLfbdJJjoEfTn36u2y--TM4cm-t6I22TxoUJgMInJhhvG-Cc8yfCebPRiJ-b9Qg-JWftLtDKbbD-Cj6-3Mb03K2TEaPcQ2C6X0njVanI_HnurbhOzKUI8LNDHtjcvWe3B_-O-5M7lqxb9Mt_hD-443bO7ttoyt6CfoJ3JyloDEnP9KljSeML1Db3BW6vMtg3t3tQ6aDnoepvoDPJc3Mv3hR0EJjLJJbkJoCLQb-3bK43ph4Oo5tFQqxby26nvWgneaJ5nJDohExo50RKbKTFh-noHtqcr565KsCJvQpP-HJ7DbRQD5bFiMbj33q58JCrCKl0MLpbWbb0xynoDDqKvKfnMBMPe52OnaIb8LIFKMKIlj5LWe5PJqxoJKPo0aIKX3b7EfhbTEPO_bf--D6Feeto-W5befG4J-4_KylRrep_CM-bxy5K_hPQk5hK8tgbM2ncz0-Q_VJvHQT3mQbvbbN3i-4DL2e5wWb3cWKOJ8UbSj-Tme4tX-NFqJTKj3f; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531655355,1531655743,1531656413,1531656420; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531659249; PSINO=7; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
            'Host': 'fanyi.baidu.com',
            'Origin': 'http://fanyi.baidu.com',
            'Referer': 'http://fanyi.baidu.com/?',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/66.0.3359.117 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(self.data['query'])
        translate_respons = requests.post(url2, data=self.data, headers=headers).json()
        translate = jsonpath(translate_respons, "$..dst")[0]
        print(translate)

    def main(self):
        self.get_token_gtk()
        self.get_language_class()
        self.get_sign()
        self.open_url()


if __name__ == '__main__':
    while True:
        word = input('---------------请输入要翻译的内容:--------------\n')
        baidu_spider = Baidu_Spider(word)
        baidu_spider.main()
