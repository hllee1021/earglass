# 갖고 놀아볼 수 있는 스크립트 파일
# 원하면 gitignore에 추가 가능
from services import sample_service
from pprint import pprint

pprint(sample_service.get_all())
