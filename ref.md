# 2020.07.15 todo list
- 사용자 kml 추가 기능
- 기관 관리자. kml 데이터 생성 페이지 구현
    - 방법1 : 날짜와 확진자 번호를 정하고 지도에서 찍게한다.
    - 방법2 : 날짜를 저장하고 확진자 번호와 좌표를 입력하게 한다.
    - 파일 형태로 저장하게 할 것인가?(json으로?)
    - 검색기능을 제공하는 것은 피해야 하지않나? 특정 가게가 피해를 볼 수 있다.(일부러 제한을 둬야?)
    - map 객체의 data 부분을 추출하여 json으로 저장하면 되지 않을까?
- 사용자 여러 날짜 비교 할 수 있게 구현해야함.
- 지역구 select 구현 해야함. select로 할까 datalist로 구현할까?
- side bar의 기능 구현을 먼저? 지도 맵 구현을 먼저?
- 15일 지나면 조회할 수 없도록 막거나 삭제 시켜야함.

# 2020.08.19
- naverapi reference
- https://docs.ncloud.com/ko/naveropenapi_v3/maps/web-sdk/v3/start.html
- https://navermaps.github.io/maps.js.ncp/

### How to upload and show kml file on map from user memory
- https://stackoverflow.com/questions/56571122/how-to-upload-and-show-kml-file-on-map-from-user-memory/56571665

### filereader api
- https://medium.com/@pks2974/file-api-%EC%A0%95%EB%A6%AC%ED%95%98%EA%B8%B0-729fa6a3a0ba

### XML Applications
- https://www.w3schools.com/xml/ajax_applications.asp


### 레이어 다른 스타일 지정하기, 이벤트 지정하기
- https://navermaps.github.io/maps.js.ncp/docs/tutorial-2-DataLayer.html
- https://navermaps.github.io/maps.js.ncp/docs/naver.maps.Data.html#~StyleOptions