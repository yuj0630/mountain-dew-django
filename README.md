# mountain-dew

날이 갈수록 등산에 대한 수요가 높아지는 와중에 등산로 추천 웹사이트를 만들어보면 어떨까 싶어 만들게 된 웹사이트입니다.

## 정보

* 팀 이름 => 마운틴듀(산이슬)

팀원
- 정영운 : backend(django), frontend(react)
- 유수빈 : 자료조사, db 구축(mysql), frontend(react)
- 한종훈 : db 구축(postgresql), backend(django)
- 정다예 : frontend(react)

## Stack
- IDE : vscode, pycharm
- frontend : html, css, javascript, react(material ui)
- backend : django, node.js
- DB : mysql, postgresql
- tool : wix, miro, stackblitz, folium, QGIS

## problem

- django, react, postgresql 모두 처음 시도하는 기술이었고, 중간에 1명이 개인 사정으로 빠지면서 어려움이 생겼습니다.
> 공식문서, 유튜브, 클론 코딩 등을 참조하면서 하루에 약 10~12시간 정도 코딩을 함으로서 해결했습니다.

- 공간 데이터를 담아서 지도에 표시해야 했기에 데이터 정제에 관련된 어려움이 있었습니다.
> (folium이라는 python 지도 생성 툴로 해결했고, 때문에 spring이 아닌 django를 썼습니다.)

- mysql에 shp, gpx 데이터를 담기가 어려웠으며, mysql과 postgresql에 데이터를 분할해서 담았습니다. 

## backend 설명

### api 

* models.py : 데이터베이스 설정용
* urls.py : 경로 설정용 
* migrations : 안에 지금은 임시로 넣어놨는데 DB 마이그레이션 용으로 쓴다고 합니다.
* tests.py : 테스트 케이스 작성하는 파일입니다.
* views.py : request와 response로 하여금 정보 불러오는 역할을 합니다.
* serialization.py : 데이터베이스 안의 정보를 json으로 바꾼뒤 다시 돌아오게 하는 역할입니다.

### mountainsite

* setting.py : 장고 템플릿을 전체적인 설정을 바꿔주는 데 사용합니다.
* urls.py : 역시 경로 설정용 파일입니다.

### templates

* index_html : html로 작성된 템플릿들 표시하기 위한 html입니다.
* map_view_html : 지도 표시하기 위해 만들어놓은 html입니다.
