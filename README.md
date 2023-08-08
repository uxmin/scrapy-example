# MarkCloud Data Stars
마크클라우드의 데이터 수집기입니다.<br/>
쿠팡, 네이버쇼핑 등 각 쇼핑몰은 하나의 스파이더로 실행됩니다.
<br/><br/>


## Teck Stack
- poetry
- scrapy

<br/>


### Poetry
효율적인 패키지 관리를 위해 강력한 패키지 관리 도구인 ```Poetry```를 사용합니다.<br/>
기존 패키지 관리 도구인 ```pip```를 대체합니다.<br/>
```bash
# 가상환경 활성화
poetry shell
# poetry 패키지 설치
poetry install

# 패키지를 추가하는 경우
poetry add <패키지>
```

poetry를 통해 가상환경에서 프로그램을 실행하는 경우,<br/>
```poetry run``` 을 앞에 삽입해서 실행합니다.

```bash
poetry run python main.py
```
<br/>

### Scrapy
데이터 수집 프레임워크로 ```Scrapy```를 사용합니다.<br/>
해당 프레임워크는 bs4, Selenium 등 데이터 수집 라이브러리를 포함하고 있습니다.<br/>
Data Stars 라는 프로젝트 하위에 여러 스파이더를 생성하여 데이터 수집 프로그램을 관리합니다.

```bash
# Scrapy 프로젝트 진입
cd data_stars

# Spider 실행
poetry run scrapy crawl <스파이더명>
```
