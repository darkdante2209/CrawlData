import scrapy
import json

class DeliveryDetail(scrapy.Spider):
    name = 'fedex'
    # headers = {
    #     "Accept": "*/*",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "en-US,en;q=0.9",
    #     "Connection": "keep-alive",
    #     "Content-Length": "456",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Cookie": "fdx_cbid=30711172601637120405206610382551; fdx_locale=en_US; s_ecid=MCMID%7C75917150661705088664609225557820944807; Rbt=f0; isTablet=false; isMobile=false; isWireless=false; AMCVS_1E22171B520E93BF0A490D44%40AdobeOrg=1; s_cc=true; Nina-nina-fedex-session=%7B%22loginStatus%22%3A%22loggedOut%22%2C%22locale%22%3A%22en_us%22%2C%22lcstat%22%3Afalse%7D; SMIDENTITY=FDpspiaEqNohy6coGLXTNPIctwQ496NMjG8d7LMTV90M1JHlvMrQm1lUbEABvnWDc9Cs9E59Z6g7Dpr7VVUaxwpwCeM9otAY2b5XM4ce9byMgli6qb/KZeCoTq3/U1lARKr79r7ntht/ZNlEaTMZ1pMzxKKLNICR6g1gosi6+NsNCs38RDFiCcOMuWA+1f9Cj+SRz5pLAx+sEbjho2unGTy4tOMTlGC7bXNO1kDFDSHq7pMeNxUrF5RqorhROl/0Gm15AYQAEeEVIYnSbEMicMI0XLvR+MCd7M6OdDjXkjBQqctRUN87tYuE2M1kEoxQ6EVktOHcyrumXrtbbYBv1KT0RT1xSCNt4B4qqLKPXRxSrt6uGotTx0eF8YBexv7g+YSUKdSFzBPLrhEy5uAloMMwsHoes0WKb6DvCNl1YrtEPdfRzYI0IgYG4lAAXsmC3X9o65n4AkuTxDo1uP7Kdo5RsCaofktlzMA/ubpQC68XC83jkG5DxQeTMfL2HNHjbe8pLRZtRoGftQh5fMAuQ6lFU8iochKe; xacc=VN; bm_sz=5B48E4B778FD505B112C4C4DB64EE0B4~YAAQ1tYwF5KhbTB9AQAA2B5gfw2Vb5H+a4mh8GzZCUKLe53w2OmC/PXhVzF4SPQOg0LoYrzeZ8olmUGGsi0uXcVnB0vcu+g8wDH7H3303pFslsdp5PIDeMmILEijiB/kiygaqWFol+JhVTE7OdAyhTnG1gO6O6+9YAQyn3lagmS378prjvupS0aD7/IsnZ4sYb4Srwmh671q8ukrJwU8lNq5Sk0zAUkv519VCuee52AwhyAJlXY8y/7BfLNS1SMkG7D16FAeiI0JzkDwoxyoLBrMpPj4bOxi+JcrrfS4x9ZPxg==~3162929~4471091; PIM-SESSION-ID=HKc8F1OquEOvxFoT; ak_bmsc=6DC029671D4FCEF60DAA01B168FE8A68~000000000000000000000000000000~YAAQ1tYwF5ShbTB9AQAApSNgfw2Mowg83cL+rNjGImH6JYMFFFJ4USkGy5ZVMNf9h/iaO53H3w4mVH2KOZZvMK8cvABgs5Lw9Z1vS8O9Apx8zjTRde2jQ6aeN6hH2rnL/2pm0MTdRMbImV7gordix+luds7B1iFDmyAhjtiR/YwmQHzDqfzfsK0osf0fAE53YZNWGO5hJlZU/mjWesGDg40V4D5a1yWl6htYpcQ1ibYCPe2WqZRJWQkfzTzArVMwvHobg3bMS8k2lzkU2+0KW81HkrlY8bqZfJAiNCqN5upN0RDXiidSKTO/xiQXcu7p5uLPQY7kbjeT0Zc1je/dkzydMcbgAPk8N2YnifcfpoMBATp69DUZeibDzFpnAI6hTQKXADoCBe4ZDdoMQ7zprTMX2xFxqHBfTij52XFTp2GdVx+ZDnwygr351D18hjbUm6kTpvCGVIwymxiPoLCO5z50iY/S9kiatUJ0cHV6; s_sess=%20setLink%3D%3B%20s_ppv%3Dfedex%252Fhero%25257Ctrack%3B%20SC_LINKS%3D%3B; s_pers=%20gpv_pageName%3Dfedex%252Fhero%257Ctrack%7C1638521348499%3B%20s_vnum%3D1638550800197%2526vn%253D2%7C1638550800197%3B%20s_invisit%3Dtrue%7C1638521348507%3B; s_sq=%5B%5BB%5D%5D; QSI_HistorySession=https%3A%2F%2Fwww.fedex.com%2Ffedextrack%2F~1638499212844%7Chttps%3A%2F%2Fwww.fedex.com%2Ffedextrack%2F%3Faction%3Dtrack%26tracknumbers%3D536539312478%26locale%3Den_US%26cntry_code%3Dus%26wsch%3Dtrue~1638499216542%7Chttps%3A%2F%2Fwww.fedex.com%2Ffedextrack%2F%3Ftrknbr%3D536539312478%26trkqual%3D12022~536539312478~FDEG~1638519548829%7Chttps%3A%2F%2Fwww.fedex.com%2Ffedextrack%2F%3Ftrknbr%3D536539312478%26trkqual%3D12022~536539312478~FDEG~1638519548989; _abck=82EF6CEF55E667F532C6948F3421AFFF~0~YAAQ5tYwF0Fs5i19AQAA7S5gfwZfI5x3NjD5VwfRXBXn8GUn71ezve0TWpgszwyOGbMgI/4mg0AeYaiTcKn/2eyc6Yb1fTvrr9evirdjtMWNW1EXBvZsHazgybb8YR6ywmNiCn1zeNI7CsVaS8MdbMh6s3OMgeMyMHjUnPPcuXQjFiPf51MYcLVcCP+3nmaiTnEUmTsplnOF+T8wnhv8J9OLLLjMDA6N4EJLEyxivHDfiqI3UBbRXbVA0FTCwSH1nmZlbD+q/Ps/1rkKuYXBWHxppw+0Vh0I2hZBmxmd+8E6C6bZ0/hD0tAm28RBvBzi1bbwDOYvMPqYBhy1cFIH00VjZ8edvSwBP5OyWLgUu8tmoGMWJdWEIu3vL9oqIBF1rXCglwPJwok9ap7R1uJNi1nuWyz1nSM=~-1~-1~-1; QSI_S_ZN_a8yTxtP35n9W4qq=r:50:2; ADRUM=s=1638519948010&r=https%3A%2F%2Fwww.fedex.com%2Ffedextrack%2F%3F-610235371; AMCV_1E22171B520E93BF0A490D44%40AdobeOrg=359503849%7CMCIDTS%7C18965%7CMCMID%7C75917150661705088664609225557820944807%7CMCAAMLH-1639124749%7C3%7CMCAAMB-1639124749%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1638527149s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.0.1; siteDC=edc; aemserver=PROD-P-dotcom-c0015882.prod.cloud.fedex.com; bm_sv=6F7D7BA68F3048D0E5B802F91CDCACF7~EfTGFvSyODMWBCafPQvkWi5gAuc6nDXuGh/46rcOWvMPs+2Xhc06yX5sSI3rGonrt6hsNsBmin8Xhf7NWDoiFJSw+1iff1jNlQBmu7ljAYutRxco7iFYDpM5DLJ0Eq2JU7JFK9BVm0tHtBVNAgH8NZeg+Ly/509S43pRIljV/lY=",
    #     "Host": "www.fedex.com",
    #     "Origin": "https://www.fedex.com",
    #     "Referer": "https://www.fedex.com/fedextrack/?trknbr=536539312478&trkqual=12022~536539312478~FDEG",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    # }

    def start_requests(self):
        yield scrapy.Request('https://www.fedex.com/fedextrack/?trknbr=286812732479&trkqual=12022~286812732479~FDEG', meta={'playwright': True})

    def parse(self, response):
        yield {
            'text': response.text
        }
