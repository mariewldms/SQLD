## SQL 기본 및 활용

기본에서 나아가 크게 그룹함수, 윈도우함수, 계층함수 세 가지가 핵심 개념이다.

- 그룹함수
  - 특정 기준으로 그룹핑하고, 그룹으로 나누어 상황에 따라 소계를 구하는 역할
   ![image](https://github.com/user-attachments/assets/b33c75de-9be5-411e-92dd-b5b022211af4)

<br> 

- 윈도우함수     
   ![image](https://github.com/user-attachments/assets/934fbf54-a479-4071-913b-f4ee1cc42508)

<br>
      
- 계층함수(계층형 질의)
    - 상사와 직원처럼 상위, 하위 관계를 가지는 계층 DB 질의
    - CONNECT BY: 트리형태의 구조로 쿼리 수행
    - START WITH: 계층 구조 전개의 시작 위치 (최상위행) 지정
    - CONNECT_BY_ROOT/ISLEAF: 최상위/하위 계층값
    - SYS_CONNECT_BY_PATH: 계층 구조의 전개 경로
    - ORDER BY SIBLINGS BY: 형제 노드 사이에서 정렬
