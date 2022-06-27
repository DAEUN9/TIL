# 입출력

### 입출력과 스트림

- 스트림: 데이터를 운반하는데 사용되는 연결통로



### 바이트 기반 스트림 - InputStream, OutputStream

| InputStream                          | OutputStream                           |
| ------------------------------------ | -------------------------------------- |
| abstract int read()                  | abstract void write(int b)             |
| int read(byte[] b)                   | void write(byte[] b)                   |
| int read(byte[] b, int off, int len) | void write(byte[] b, int off, int len) |



### 보조 스트림

- 입출력 기능 x
- 스트림 기능 향상시키거나 새로운 기능 추가



### 문자기반 스트림 - Render, Write

- ` InputStream` -> `Render`
- `OutputStream` -> `Writer`



### InputStream과 OutputStream

- 스트림의 종류에 따라 mark()와 reset()으로 이미 읽은 데이터 되돌려서 다시 읽기 가능
- 이 기능을 지원하는 스트림인지 markSupported()로 확인
- flush()는 버퍼가 있는 출력스트림인 경우에만 의미있음
- 모든 작업을 마치고 난 후 close()호출 필수
- 그러나 ByteArrayInputStream과 같이 메모리 사용하는 스트림과 System.in, System.out같은 표준 입출력 스트림 안닫아도 O



### FileInputStream과 FileOutputStream



### FilterInputStream과 FilterOutputStream

- 생성자

```java
protected FilterInputStream(InputStream in)
public FilterOutputStream(OutputStream out)
```

- 상속을 통해 원하는 작업을수행하도록 읽고 쓰는 메서드 오버라이딩해야함

```java
public class FilterInputStream extends InputStream {
    protected volatile InputStream in;
    
    protected FilterInputStream(InputStream in) {
        this.in = in;
    }
    
    public int read() throws IOException {
        return in.read();
    }
    ...
}
```



### BufferedInputStream

- 버퍼 이용해서 한 번에 여러 바이트 입출력



### BufferedOutputStream

- 버퍼가 가득 찼을 때만 출력소스에 출력
- 버퍼에 남아있는 채로 프로그램이 종료될 수 있다
- close()나 flush()를 호출해서 마지막에 모든 내용 출력되도록 해야함



### SequenceInputStream

- 여러 개의 입력스트림을 연속적으로 연결해서 하나의 스트림으로부터 데이터를 읽는 것과 같이 처리할 수 있도록 도움



### printStream

- 문자기반 스트림의 역할을 수행
- printWriter가 다양한 언어의 문자처리에 적합하므로 권장
  - printStream보다



### 문자 기반 스트림 - Reader/Writer

- byte배열 대신 char배열 사용
- 유니코드(UTF-16)간의 변환 자동처리
- Render: 특정 인코딩을 읽어서 유니코드로 변환
- Writer: 유니코드를 특정 인코딩으로 변환하여 저장



### FileReader와 FileWriter

- 파일로부터 텍스트 데이터를 읽고, 파일에 씀



### StringReader와 StringWriter

- 입출력 대상이 메모리인 스트림

```java
// StringWriter에 출력한 데이터가 저장된 StringBuffer를 반환
StringBuffer getBuffer()
    
// StringWriter에 출력된 (StringBuffer에 저장된) 문자열을 반환
String toString()
```



### BufferedReader와 BufferedWriter

- 입출력 효율이 좋아짐
- readLine(): 데이터를 라인단위로 읽음
- newLine(): 줄바꿈



### InputStreamReader, OutputStreamWriter

- 바이트기반 스트림을 문자기반 스트림으로 연결
- 바이트기반 스트림의 데이터를 지정된 인코딩의 문자데이터로 변환
- Scanner로 간단 처리가능



### 표준 입출력

- System.in: 콘솔로부터 데이터를 입력받는데 사용
- System.out: 콘솔로 데이터를 출력하는데 사용
- System.err: 콘솔로 데이터를 출력하는데 사용



### 표준 입출력의 대상변경

- static void setOut(PrintStream out)
- static void setErr(PrintStream err)

- static void setIn(InputStream in)



### 직렬화

- 객체를 데이터 스트림으로 만드는 것을 뜻함



### ObjectInputStream, ObjectOutputStream

- `objectInputStream(InputStream in)`: 역직렬화
- `objectOutputStream(OutputStream out)`: 직렬화

- 직렬화 시간 단축하려면 메서드 2개 직접 구현 필요

```java
private void writeobject(ObjectOutputStream out)
    throws IOException {
    // write메서드를 사용해서 직렬화 수행
}

private void readObject(ObjectInputStream in)
    throws IOException, ClassNotFoundException
```



### 직렬화가 가능한 클래스 만들기

- 직렬화하고자 하는 클래스가 java.io.Serializable인터페이스를 구현하도록 함
- `public interface Serializable {}` : 직렬화를 구려하여 작성한 클래스인지 판단하는 기준
- 구현안하면 직렬화 대상에서 제외



### 직렬화 대상에서 제외시키기 - transient

- Object는 직렬화 불가
- String은 직렬화 가능
- transient: 직렬화 대상에서 제외
  - 그 타입의 기본값으로 직렬화될 수 있음