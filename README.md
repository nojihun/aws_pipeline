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
   
   
   ## 프로젝트내 역할 
   
  - 데이터가 실시간으로 들어오는 것처럼 만들기 위해서 kinesis를 활용해 유사 실시간 환경을 구축
  - 데이터를 변환 및 압축하는 함수 구현
  - aws lambda 와 api gateway를 이용해서 데이터를 불러오는 API 구현 


  ## 파이프 라인 
  
  1. kinesis 를 통해서 데이터가 순차적으로 s3에 인코딩과 압축 후 저장
  2. api 를 통해서 쿼리가 들어옴
  3. aws glue와 아테나를 통해서 데이터가 수집이됨
  4. lambda 를 통해서 데이터의 압축을 해제하고 디코딩을 하게 됨
  5. 데이터가 나오게 된다.
 
 ## 프로젝트 결과
 
 1. 데이터 파이프 라인을 작성하였다.
 2. 데이터는 인코딩과 압축을 통해서 약 90%의 용량을 줄일 수 있었다.
 3. sql 쿼리를 통해서 데이터를 원하는 개수 만큼 가져올수 있다.
 4. 데이터를 가져오는 속도
  -10개에 2.37 초 
  -100개에 2.56초
  -1000개에 5.67초
  - 10000개에 27.42.초
 
