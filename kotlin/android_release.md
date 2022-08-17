### 배포버전 release 테스트

- 코드 난독화가 된 버전으로 release용 sha1키를 추가해야함 -> google map, firebase



### APK 파일 생성

- android studio 맨 왼쪽 밑 Build Variants에서 debug -> release로 바꾸기

https://android-dev.tistory.com/61

- key store path와 password 기억하기
- 애뮬레이터로 만들어진파일 드래그하면 설치가능



### release용 SHA-1 발급받기

- cmd 에서 자바 경로로 들어가기

  ```
  # 예시
  
  cd C:\Program Files\Java\jdk-11.0.15.1\bin
  ```

- key sotore path로 sha-1 생성

  ```
  # 예시
  
  >keytool -list -v -keystore C:\Users\DANI\ssafy7\semester2\S07P12D210\FrontEnd\daeun\release_key.jks
  ```

- 비밀번호 입력



### Proguard-rules

프로젝트 단위 폴더 -> app -> proguard-rules.pro

- progress 참고

모듈단위 build.gradle

```kotlin
    buildTypes {
        release {
            minifyEnabled true // [true 프로가드 사용 / false 프로가드 사용안함]
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro' // [프로가드 설정 파일 지정]
        }
        debug {
            minifyEnabled false // [true 프로가드 사용 / false 프로가드 사용안함]
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro' // [프로가드 설정 파일 지정]
        }
    }
```





### 실제 앱 배포는 aab로 진행될 예정