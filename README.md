# Djano-Simple-Todo

Django framework를 이용해 간단한 todo api를 구현합니다.

django 의 패턴인 MVT패턴을 통해 구현

## model

간단히 사용할수있는 sqlite를 사용하여 모델을 정의 하고 이를 마이그레이션하여 테이블을 얻습니다.

django 자체에 내장되어 있는 orm 객체를 이용하여 디비를 조회 수정 삭제 삽입 을 수행합니다.

## DRF, serializer

django rest framwork로 rest api 를 쉽게 구현할수있도록 도움을 줍니다.

DRF에 존재하는 serializer 라는 강력한 기능으로 데이터를 직렬화 하여 json 형태로 데이터를 볼수있게 해주고

serializer 에서 validation 처리 간단한 비즈니스 로직을 가지게 됩니다.

## view 

mixin view 를 이용해 엔드포인트에 응답할 데이터를 보내주고 status-code를 보내줍니다.

## template

client 와 연결하는 부분인 template를 작성하여 보여줍니다.

