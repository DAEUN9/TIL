# Git

> 분산 버전 관리 프로그램

- 변경 사항만 저장
- 변경 이유는 알 수 없으므로 추가입력 필요



#### 중앙 집중식 버전 관리

- 변경 이력을 중앙에서 관리



#### 분산 버전 관리

- 변경 이력을 분산해서 관리





# GitHub

> Git 호스팅 서비스



### Git 상태

- `untracked`(빨간색) : staging area에 올라가기 전. 처음으로 관리되는 대상

- `tracked` : 관리되고 있는 대상
  - `modifed`
  - `unmodified`



### 로컬 저장소 commits (git)

- `git init` : 저장소 생성(초기화)

- working directory -> staging area : `git add`

- staging area -> commits : `git commit`

  

  커밋창 닫는 법

  - `ESC` ->  `shift + ;` -> `wq` 

    


- `git commit -m '메시지'`: 메시지 추가



### 원격 저장소 commits (github)

1. 원격 저장소 정보등록(url)
   - `git remote add origin 깃허브주소`
2. 올리기
   - `git push`



`윈도우 + shift + s` : 캡처

`윈도우 + v` : 클립보드 이전 목록

`git remote remove origin` : origin 삭제

