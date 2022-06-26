# 쓰레드

### 멀티쓰레딩의 장단점

- 장점
  - CPU 사용률 향상
  - 자원을 보다 효율적으로 사용
  - 사용자에 대한 응답성 향상
  - 작업이 분리되어 코드가 간결
- 단점
  - 동기화 및 교착상태...



### 쓰레드의 구현과 실행

1. Thread클래스를 상속

```java
class MyThread extends Thread {
    public void run() { /* 작업내용 */ }	// Thread클래스의 run()오버라이딩
}
```

2. Runnable인터페이스를 구현

```java
class MyThread implements Runnable {
    public void run() { /* 작업내용 */ }	// Runnable인터페이스를 run()을 구현
}
```



### 쓰레드의 실행 - start()

- 실행대기상태에서 차례까 되면 실행
- 종료된 쓰레드는 다시 실행 불가능



### start()와 run()

- run()은 생성된 쓰레드를 실행시키는 것이 아니라 단순히 클래스에 선언된 메서드 호출
- start()는 실행마다 새로운 호출스택 생성되고 종료되면 소멸
  1. main메서드에서 쓰레드 start()호출
  2. start()는 새로운 쓰레드를 생성, 쓰레드가 작업하는데 사용될 호출스택 생성
  3. 새로 생성된 호출스택에 run() 호출, 쓰레드가 독립된 공간에서 작업 수행
  4. 이제 호출스택이 2개이므로 스케줄러가 정한 순서에 의해 번갈아 가면서 실행



### 쓰레드의 I/O블락킹

- 두 쓰레드가 서로 다른 자원을 사용하는 경우 멀티쓰레드가 효율적
  -   ex) 데이터 입력받는 작업



### 쓰레드의 우선순위

- 쓰레드가 가질 수 있는 우선순위는 1~10
- 우선순위는 쓰레드를 생성한 쓰레드로부터 상속받음

```java
void setPriority(int new Priority) // 쓰레드의 우선순위를 지정한 값으로 변경
int getPriority()	// 쓰레드의 우선순위를 반환
    
public static final int MAX_PRIORITY = 10 // 최대우선순위
public static final int MIN_PRIORITY = 1 // 최소우선순위
public static final int NORM_PRIORITY = 5 // 보통우선순위
```



### 쓰레드 그룹

- 쓰레드 그룹에 다른 쓰레드 그룹 포함 가능
- 모든 쓰레드는 반드시 쓰레드 그룹에 포함

```java
ThreadGroup getThreadGroup() // 쓰레드 자신이 속한 쓰레드 그룹 반환
void uncaughtException(Thread t, throwable e)
    // 처리되지 않은 예외에 의해 쓰레드 그룹의 쓰레드가 실행이 종료되었을 때,
    // JVM에 의해 이 메서드가 자동적으로 호출
```



### 데몬 쓰레드

- 일반 쓰레드의 작업을 돕는 쓰레드
- 특정 조건이 만족되면 작업 수행하고 다시 대기

```java
boolean isDaemon()	// 쓰레드가 데몬 쓰레드면 true 반환

void setDaemon(boolean on)	// 쓰레드를 데몬 쓰레드로 또는 사용자 쓰레드로 변경
    // 매개변수 on의 값을 true로 지정하면 데몬 쓰레드가 됨
```



### 쓰레드의 상태

| 상태                        | 설명                                                         |
| --------------------------- | ------------------------------------------------------------ |
| NEW                         | 쓰레드가 생성되고 아직 start()가 호출되지 않은 상태          |
| RUNNABLE                    | 실행 중 또는 실행 가능한 상태                                |
| BLOCKED                     | 동기화블럭에 의해 일시정지된 상태(lock이 풀릴 때까지 기다리는 상태) |
| WAITING.<br />TIMED_WAITING | 쓰레드의 작업이 종료되지는 않았지만 실행가능하지않은 일시정지 상태.<br />TIMED_WAITING은 일시정지시간이 지정된 경우를 의미 |
| TERMINATED                  | 쓰레드의 작업이 종료된 상태                                  |



### 쓰레드의 실행제어

- 스케줄링 메서드...❗



###  sleep()

- 지정된 시간동안 쓰레드를 멈춤

```java
static void sleep(long millis)
static void sleep(long millis, int nanos)
```

- 항상 try-catch문으로 예외처리 해줘야함

```java
void delay(long millis) {
    try {
        Thread.sleep(millis);
    } catch(InterruptedException e) {}
}
```



### interrupt()

- 쓰레드에게 작업을 멈추라고 요청

- interrupted()는 쓰레드에 대해 interrupt()가 호출되었는지 알려줌

```java
void interrupt()	// 쓰레드의 interrupted상태를 false에서 true로 변경
boolean isInterrupted()	// 쓰레드의 interrupted상태를 반환
static boolean interrupted()	// 현재 쓰레드의 interrupted상태를 반환 후, false로 변경
```

