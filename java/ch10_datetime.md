# 날짜와 시간 & 형식화



### Calendar클래스

- 추상 클래스

```java
Calendar cal = new Calendar();	// 에러!!! 추상클래슨느 인스턴스 생성 불가
// OK, getInstance()메서드는 Calendar클래스를 구현한 클래스의 인스턴스를 반환
Calendar cal = Calendar.getInstance();
```



### Date와 Calendar간의 변환

```java
// 1. Calendar를 Date로 변환
    Calendar cal = Calendar.getInstance();
    ...
    Date d = new Date(cal.getTimeInMillis)

// 2. Date를 Calendar로 변환
    Date d = new Date();
		...
    Calendar cal = Calendar.getInstance();
	cal.setTime(d)
```



### 형식화 클래스

- 숫자, 날짜, 텍스트 데이터를 일정한 형식에 맞게 표현



### DecimalFormat

1. 원하는 출력형식의 패턴 작성
2. DecimalFormat인스턴스를 생성
3. 출력하고자 하는 문자열로 format메서드를 호출



### SimpleDateFormat

- 원하는 출력 형식의 패턴 작성
- SimpleDateFormat인스턴스 생성
- 출력하고자 하는 Date인스턴스를 가지고 format 호출

```java
Date today = new Date();
SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");

//오늘 날짜를 yyyy-MM-dd 형태로 변환하여 반환
String result = df.format(today);
```

