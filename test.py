from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen

url = 'http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList'
queryParams = '?' + urlencode(
    {quote_plus('ServiceKey'): '서비스키', quote_plus('desc_kor'): '바나나칩', quote_plus('pageNo'): '1',
     quote_plus('numOfRows'): '3', quote_plus('bgn_year'): '2017', quote_plus('animal_plant'): '(유)돌코리아'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)
