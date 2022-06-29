<div align="center">
  <h1> 데이터 엔지니어링 Project </h1>
  AWS를 이용한 실시간 데이터 파이프라인 구성
 
  
  ### 👤 팀원 소개
  |김석재|김예린|노지훈|
  |:---:|:---:|:---:|
  |<img src="https://avatars.githubusercontent.com/u/86823305?v=4" width="100"/> | <img src="https://avatars.githubusercontent.com/u/86868063?v=4" width="100"/> | <img src="https://avatars.githubusercontent.com/u/86717381?v=4" width="100"/> |
  |[Github](https://github.com/Cloudblack)|[Github](https://github.com/yello-ow)|[Github](https://github.com/nojihun)|
  <br>
  
 </div>
 
 ***

  ## 프로젝트 개요
  
   기업에서 발생하는 데이터를 데이터 분석팀에서 쓰기 위해서 데이터를 저장하고 불러오는 api를 작성하는게 목표이다. 


  ## 파이프 라인 코드 설명
  table 폴더안에 최종적으로 쓰인 코드들이다. 
  안에 설명을 따로 만들었다.
  
  delete_params.py, gamer_id.py, inDate.py, tableAndColumn 인코딩 디코딩.py, url 파라미터 제거.py : 데이터의 용량을 줄이기 위한 인코딩함수들
  kinesis_producer_ksj.py : 키네시스 스트림에 데이터를 넣는 코드이다. 데이터가 순차적으로 들어오는것처럼 보이게 만듬
  kinesis_consumer.py:키네시스 스트림에 들어있는 데이터를 받아서 인코딩 후 s3에 저장하는 코드
  lambd_function-데이터 전체.py: 람다에 들어가는 코드. s3 에 저장되어 있는 데이터를 한번에 받아와서 json으로 내려보내는 코드
  lambda_test_inDate.py: 시간을 퀄리로 받아서 시간별로 쿼리를 받는 코드
  
  다 여러 이유로  만들어진 파이프라인에 들어가지 못한 코드들입니다.
  
 
 
 ## 프로젝트 결과
 
 1. 데이터 파이프 라인을 작성하였다.
 2. 데이터는 인코딩과 압축을 통해서 약 90%의 용량을 줄일 수 있었다.
 3. sql 쿼리를 통해서 데이터를 원하는 개수 만큼 가져올수 있다.
 4. 데이터를 가져오는 속도
  -10개에 2.37 초 
  -100개에 2.56초
  -1000개에 5.67초
  - 10000개에 27.42.초
 
