# -*- coding: utf-8 -*-
import requests
session = requests.session()
headers = {
"Accept":"application/json, text/plain, */*",
"Content-Type":"application/x-www-form-urlencoded",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}
url_1 = 'https://ipassport.ele.me/newlogin/sms/send.do?appName=eleme&fromSite=-2'
data_1 = {
"phoneCode":"86",
"loginId":"13713762959",
"countryCode":"CN",
"ua":"121#f4GlkCHpjYwlVlhQGV2SllXY3cYj4ujVZdQOxbTIiMxuOs/VT3evlkKYAcfdK5j9lGgY+zp5pMl9n7mD95DIllLmRcffK7jAbyRNxaPIDgtlO3rJqRD5lwLYAcfdK5jVlmuY+zLIKM9VA3rnEkDIll9YAiEdKujlxdNwAXqhlP2gebCs8yVy/5ggsPGGJXb0CO3LzPBhbZseCeILFtZ0bZi0njClpw95X9D/83BhCjV3CHHaQtbs3w99nnxS56b0CZe78G/mCbibCeIaFtFbbZsbJjx9p2ibCZ0T83BhbZsbMHIaFIQ9pP8jn8gAoqShkYTf+mBddg/0dH1nF9cVC6ibngG9lZE2ASYrJZhdBMirofLFDpLR0cBzWKLqo/5XCgpeG26EeByvlpXdX1MT/5SgGgCm1ZtiysdbkNdVi8efdSymJKANZc7ty87kGbFsT4XKEBy6nQNm/mf4MjNjLw68vqXTFZQnrBIpjJrFhMnT0hhX2wDdo5NXVrqSuyLZyqC02b+P4SdGyL0stZmEyxV4Lgj/OTlxhzKqWRDWSosfH1rheVMKGq18SlbMAap39DgDo7Er8bI1uXeiGHFGQ2nbFQ+6TMvnkYS2NCKIfQpn8JSfbw/qdNO+rlm1ywGyGc4anErG9Cd4qQhGyA5zOJn89ys0goPvL1Ekrg46QpBeQLwKgx8T36YqM7UiuBbYNxVSg7Tv3YCac4LvdWUgGIm/EtEqArKdY7FzlpXuvZm5Mhm66XDM91NGni+23Mxi9seIVOmrQD2wJm0DZEGuXb2O4wDP84u0WpMMXwhG47/Y7lpjsdHpaDgtF404LhSjbKskfTFYIcwqGGQAo9Or5k+fU1OErlKCy7dyCV7rP+wXt/LGOxKuJqTJucoIxMcrikLKr/XpyoJXJc9meTzu7Wp198P9bixt59IeLGMxPqhg69gdYccwsslrgBCqbRMssjlossFT/LVeWqx4hWPiG8zh/hubFBmrMGfSawqvI0m77WukhKUfswYiIcm612JyyH2LVUXnZrn2I4dEFDTiyhUIf2EHOqzQejJ8paa1cevu3QqPlmvxUU4ZL2wydJYqHJRGQ8nf2h3P+fKbLw06pTfIR+tZeypP6sbyQ6Nub5bS7oqZLHkzYMm/4EENY/Re7Nc2CsvoeHUbHCVejcxdfMTaRO1U5wVXx8Z7il==",
"umidGetStatusVal":"255",
"screenPixel":"1440x960",
"navlanguage":"zh-CN",
"navUserAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
"navPlatform":"Win32",
"appEntrance":"eleme_sms_h5",
"appName":"eleme",
"bizParams":"",
"csrf_token":"ehTDEGZ7RM46LDb1mMFseF",
"fromSite":"-2",
"hsiz":"138f306012656b16500c151864ba4957",
"isMobile":"false",
"lang":"zh_CN",
"mobile":"false",
"returnUrl":"",
"umidToken":"09ef30b2e35b0a8d2218f5d7ccb4a034883d1f54"
}

session_send=session.post(url_1, headers=headers, data=data_1)
print(session_send.status_code)
print(session_send.text)
smstoken =session_send .json()["content"]['data']['smsToken']
print(smstoken)

url_2 = 'https://ipassport.ele.me/newlogin/sms/login.do?appName=eleme&fromSite=-2'
smscode = input('请输入手机验证码：')
data_2 = {
"loginId":"13713762959",
"phoneCode":"86",
"countryCode":"CN",
"smsCode":smscode,
"smsToken":smstoken,
"keepLogin":"false",
"ua":"121#dBGlkkWKelwlVlIvGV2SllXY3cYj4ujVZdQOxbTIiMxuOs/VT3evlkKYAcfdK5j9lGgY+zp5pMl9n7mD95DIllLmRcffK7jAbyRNxaPIDgtlO3rJqRD5lwLYAcfdK5jVlmuY+zLIKM9VA3rnEkDIll9YAiEdKujlxdNwAXqhlP2gebCs8yVy/5ggsPGGJXb0CO3LzPBhbZseCeILFtZ0bZi0njClpw95X9D/83BhCjV3CHHaQtbs3w99nnxS56b0CZe78G/mCbibCeIaFtFbbZsbJjx9p2ibCZ0T83BhbZsbMHIaFIQ9pP8jn8gAoqShkYTf+mBddg/0dH1nF9cVC6ibnvySlnMcLSYrv47XVwts3sZQgWMMpETlRWqoCjia426XlNON28r8Ap9Hi8Gjxz/CVfzRmo6Sl8XYrvleDZGaG1Mb0vP+88j1ZHk11NlsqZrEcCr1dG3MdHFRhvj3QaG/EIGuoNbIH38+msKQeMS1EG126y/QoMZnB3Ht+QVMbvjADaVD65ok8vqzioQcM3Pu//XFLsN7iEuG8h8M6zSZNX8H3MTzvhpJfWx9dyLEdEsE17WHGzuX3Lt5mtE96rVvRcFC8m7BajFKPV51f4PkO0SLf60se/ls9EJDka4fxEIWD1bXS9HubOg0FaWWpD2F4PUrbzMb6mw8Qm/IyDq+wR6gnVl/MQ8XMbC07fBm1+kHV8dgKAwEKB/IaZXDGon4PW5iSaXp3uKY3acVlPFI4/vZSBT910l9nfNuc+hhVOZKVPzu8Vpo4c7IgQg4x/m64sf52VaxcktcFGq9Ba/gR6RtkfwK3FOG9xjYEet3JMFNwPZBpTc5EjE+8q+0dT7vJjjbURyLeIXMLga6eo5cdjxTFTcOlr9zJnjUhKret7iVymRvuMN10KihLBO2aPDXkQOEhv8jhdjkL85iC1wlXPFdo9LXdzUr/05WeplVlfhd0l3/298pvz2n8Jq2UbWYWScAQZGQQff1s7lkvEoY57tZay91190iSBapaI7OXtO0me1TWLXsx17JyHwRuqIlogSI45K7HLMSLeg7tJoysS+b+B1sdxh+hABF86oO16ynKDNBSrjUTMviqJ6s0FVVFwaf8kuC3zquvVEhQvGnprXT+y5SDCARXBCR6pp846TEbB4WWvFfXlOZtL9lgz6r1HiADUeWxupQiMsAZcaIz3H6FEV0OzogFbW7SU7NFVfCd3o0a1Ki4mqbKVuPvXVrxy9bC3gM51Wlo6j4Hjp9fAtlxuLg",
"umidGetStatusVal":"255",
"screenPixel":"1440x960",
"navlanguage":"zh-CN",
"navUserAgent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
"navPlatform":"Win32",
"appEntrance":"eleme_sms_h5",
"appName":"eleme",
"bizParams":"",
"csrf_token":"ehTDEGZ7RM46LDb1mMFseF",
"fromSite":"-2",
"hsiz":"138f306012656b16500c151864ba4957",
"isMobile":"false",
"lang":"zh_CN",
"mobile":"false",
"returnUrl":"",
"umidToken":"09ef30b2e35b0a8d2218f5d7ccb4a034883d1f54"
}

session_login=session.post(url_2,headers=headers,data=data_2)
print(session_login.status_code)
print(session_login.text)