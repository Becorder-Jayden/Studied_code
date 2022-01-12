# 2022.01.11



## html 속성, a태그

```html
<a href = "어느 사이트의 url" target = "_blank" title = "링크의 이름"> 해당 링크가 표시되는 텍스트</a>
```

* **a** 태그 : 문서와 문서를 연결해줄 때 사용, anchor의 약자
* target : "_blank"를 지정하면 새로운 탭에서 해당 링크로 이동
* title : 링크의 이름, 마우스를 올려놓으면 title이 표시 됨 



## li 태그

```html
<ul>
 	<li>기술소개</li>
 	<li>기본문법</li>

</ul>
<ol>
	<li>유재석</li>
	<li>박명수</li>
</ol>
```

* **li** 태그 : 리스트 형태로 입력

* **ul** 태그 : 성격이 같은 항목끼리 묶기 위해 사용, unordered list

* **ol** 태그 : 리스트에 번호를 나타내도록 함, ordered list



## 문서의 구조

```html
<html>
<head>
<title>HTML - 수업소개</title>
<meta charset = "utf-8">
</head>

<body>
<h1>HTML</h1>
<h2>선행학습</h2>
</body>
</html>
```

* **title** 태그 : 탭의 제목 입력
* **meta** 태그 : html 페이지에 인코딩 적용, 한글의 경우 utf-8을 보통 사용
* **페이지 설정**의 경우 **head** 태그를 사용, **본문**인 경우 **body** 태그를 사용, 정리정돈을 위함
* head와 body 태그를 포함한 **전체**는 **html** 태그로 감싸준다



## DOCTYPE

```html
<!DOCTYPE html>
<html>
    ...
</html>
```

* DOCTYPE : 브라우저에게 어떤 표준을 따르고 있는지를 알려주는 것
* 이전까지는 다양한 html 타입이 있었지만, html5 이후로는 \<!DOCTYPE html>으로 알아두면 된다



## 기본 html 작성 연습

```html
<!DOCTYPE html>
<head>
    <title>HTML - 수업소개</title>
    <meta charset="UTF-8">
</head>

<body>
    <b1><a href = "1.html.html">HTML</a></b1>
    <ol>
        <li><a href = "2.html.html">기술소개</a></li>
        <li><a href = "3.html.html">기본문법</a></li>
        <li><a href = "4.html.html">하이퍼텍스트와 속성</a></li>
    </ol>

    <h2>하이퍼텍스트와 속성</h2>
    리스트는 li를 쓰고, ul이나 ol로 감싸서 사용합니다
</body>
```



## p 태그

```html
<p>
	단락 1    
</p>
<p>
    단락 2
</p>
```

* **p** 태그 : 단락별로 구분을 위해 사용하는 태그
* p 태그 간격을 CSS를 통해서 수정이 가능함

* html에서는 엔터로 단락을 구분하지 않음



## br 태그

```html
..
    <body>
        문단의 내용<br>
    </body>
..
```

* p 태그는 줄 바꿈의 간격이 고정되어 있어서, br 태그를 사용할 수 있다
* **br** 태그 : 단순히 줄바꿈을 나타냄, 내용이 없어도 적용가능 (ex_\</br> 사용 x)
* p 태그처럼 사용하기 위해 br을 여러번 사용하기도 함



## img 태그

```html
...
	<img src="이미지.jpg" width = "100" height = "300" alt= "산 이미지" title = "산 이미지">	
...
```

* 이미지가 왜곡되는 것을 방지하고 싶다면, height만 입력하는 방법을 사용할 수 있다

* alt 속성을 추가하는 것이 좋다 : 이미지가 깨졌을 경우 해당 이미지가 무엇인지 확인하기 위함, alternative text

* title 속성을 추가하면 tooltip을 통해 내용을 확인할 수 있다 



## TABLE

```html
..
	<table border = "1">
        <thead>
            <tr>
                <th>이름</th> <th>성별</th> <th>주소</th> <ht>회비</ht>
            </tr>
        </thead>
        
		<tbody>
            <tr>
                <td>최진혁</td> <td>남</td> <td rowsapn="2">청주</td> <td>1000</td>
            </tr>
            <tr>
                <td>최진아</td> <td>여</td>	<td>500</td>
            </tr>
		<tfoot>
        	<tr>
               	<td colspan="3">합계</td> <td>1500</td>
            </tr>	
        </tfoot>
        </tbody>
	</table>
..
```

* td 태그 : table data, 표의 각 데이터를 나타냄
* tr 태그 : table row, 표의 행을 구분
* table border 속성 : 테이블의 스타일을 지정, CSS를 통해 더 예쁜 스타일을 사용 가능
* thead, tbody는 필수사항은 아니지만 직접 할 줄 알아야 한다
* th 태그 : 테이블의 속성값을 나타낼 때 사용할 수 있다, table head
* tfoot 태그 : tfoot으로 묶여있는 태그는 자동으로 아래에 표시

* td에 rowsapn, colspan 속성으로 셀 병합이 가능

  ```html
  # 다음과 같이 나오게 된다
  |  이름  | 성별 | 주소 | 회비 |
  | ----- | --- |  ---- | ---- |
  | 최진혁 |  남  | 청주 | 1000  |
  | 최진아 |  여  |      |  500  |
  | 합계                | 1500  |
  ```



## FORM 

```html
..
<form action = "http://localhost/login.php">
    <p>아이디 : <input type="text" name="id" value="default value"></p>
    <p>비밀번호 : <input type="password" name="pwd" value="default value"</p>
    <p>주소 : <input type="text" name="address" valeu=""></p>
    <p>textarea :
    	<textarea cols="50" rows="2" value="default value"></textarea>
    </p>
    <input type = "submit">
</form>
..
```

* type = "password" : 입력값이 보이지 않도록 할 수 있다
* type = "submit" : 입력값이 서버로 보내질 수 있도록 하는 버튼이 만들어짐

* form action = "주소" : 해당 주소의 서버로 전송

* textarea : 여러줄을 입력할 수 있는 text 공간이 생성
* textarea cols = "50" rows = "2" : 50개의 단어를 2열에 입력할 수 있도록 공간 한정



## DROPDOWN LIST

```html
..
	<form action="http://localhost.color.php">
        <h1>색상</h1>
        <select name="color">
            <option value="red">붉은색</option>
            <option value="black">검은색</option>
            <option value="blue">파란색</option>
        </select>
		<h1>색상2 (다중선택)</h1>
		<select name="color2" multiple>
            <option value="red">붉은색</option>
            <option value="black">검은색</option>
            <option value="blue">파란색</option>
        </select>
        <input type="submit">
	</form>
..
```



* 제한된 공간에서 여러개를 선택할 수 있도록 하는 list, combo box
* option value = "red" : 컴퓨터가 읽기 편한 방식으로 값을 전송
* selet multiple : 다중선택에서 ctrl 키를 누른 상태에서 여러 선택 가능



## 선택

```html
..
    <p>
  		<h1>색상(단일선택)</h1>
        <input type="radio" name="color">
        <input type="radio" name="color">
        <input type="radio" name="color2">
	</p>
    <p>
		<h1>사이즈(다중선택)</h1>
        95 : <input type="chekbox" name="size" value="95" checked>
        100 : <input type="chekbox" name="size" value="100">
        105 : <input type="chekbox" name="size" value="105">
    </p>
    <input type="submit">  
..
```

* type="radio" : 선택할 수 있는 버튼
* 라디오버튼은 같은 name을 갖고 있는 값끼리 그룹지어짐
* checked 속성을 사용하면 기본적으로 표시되도록 설정할 수 있음



## 버튼

```html
..
	<form action="http://localhost/form.php">
        <input type="text">
        <input type="submit" value="전송">
        <input type="button" value="버튼" onclick="alert('hello world')">
        <input type="reset">
	</form>
..
```

* type="onclick" 속성 : 자바스크립트를 사용할 때 활용할 수 있는 버튼
* type="reset" 속성 : 사용자가 이력한 내용을 리셋시킴



## HIDDEN FIELD

```html
..
	<form action="http://localhost/hidden.php">
	<input type="text" name="id">
    <input type="hidden" name="hide" value="egoing">
    <input type="submit">
..
```

* type="hidden" : ui가 없지만 서버로 어떤 값을 전송하고 싶을 때 사용



## LABEL

```html
..
	<p>
        <label for="id_txt">text</label> :
		<input id="id_txt" type="text" name="id" value="default value">
	</p>
	<p>
        <label for="password">password</label> :
        <input id="password" type="password" name="pwd" value="default value">
	</p>
	<p>
        <label for="comment">textarea :
            <textarea rows="2">default value</textarea>
        </label>
	</p>
	<p>
        <label>
        	<input type="checkbox" name="color" value="red">
        </label>
        <label for="color_blue">
        	<input id="color_blue" type="checkbox" name="color" value="red">
        </label>
	</p>
..
```

* label  태그 : 무언가의 이름표

* text를 클릭하면 해당 부분이 id를 나타내는 곳의 이름표이기 때문에, id 부분에 커서가 이동하게 됨
* label을 표현하는 방법은 2가지가 있다
* label for를 통해 어떤 값을 갖는 id를 직접 라벨링하는 방법과, label로 전체를 씌우는 방법
* 사용하지 않아도 되지만, 웹페이지의 구성을 정리하기 위해 사용을 권고



## METHOD

```html
..
	<form action="http://localhost/method.php" method="post">
        <input type="text" name="id">
   		<input type="password" name="password">
        <input type="submit">
	</form>
..
```

* url을 통해서 전송하는 방식은 get 방식, url이 아닌 다른 방법으로 숨겨서 전송하는 방식은 post 방식 
* form 태그를 이용해 데이터를 전송한다면 post 방식을 사용



## UPLOAD

```html
..
	<form action="http://localhost/upload.php" method="post" enctype="multipart/form-data">
		<input type="file" name="profile">
		<input type="submit">	
	</form>
..
```

* 파일을 업로드 하는 기능이 하나라도 있다면 method= "post ", enctype="multipart/form-data"으로 해줘야 한다는 것 정도만 기억해두자

* input 태그를 통해 파일을 선택하는 기능을 만들 수 있다 
* 자세한 내용은 서버 쪽 내용과 관련해 배워야 이해할 수 있다



## FONT

```html
..
	<font size="1" color="red">Hello</font> world
..
```

* font 태그는 사용하지 않는 것이 좋다 - 퇴출된 태그
* 그러나 사용하고 있는 페이지가 있을 수 있으므로 알아둘 필요는 있다

* size는 1~7 사이의 옵션을 가짐, 3이 기본 사이즈 값
* 폰트태그는 꾸며주는 것 외에 특별한 정보를 담고 있는 태그가 아님, 디자인으로 인해 html 용량이 커지는 것은 불필요함
* CSS라는 별도의 언어를 고안해서 디자인을 담당하도록 함



## META	

```html
..
	<head>
      	<meta charset="utf-8">
        <meta name="description" content="생활코딩의 소개자료">
		<meta name="keywords" content="코딩,coding,생활코딩,프로그래밍,html,css,javascript">
        <meta name="author" content="egoing">
        <meta http-equiv="refresh" content="30">
	</head>
	..
```

* meta 태그 : 데이터를 설명을 위한 태그

* 브라우저의 정보를 컴퓨터에 저장 : 인코딩
* 저장된 내용을 꺼내서 화면에 표시하는 과정 : 디코딩

* meta content 속성에 페이지를 잘 나타내는 설명이나 키워드를 입력 함
* http-equiv="refresh" 페이지를 새로고침하는 간격을 나타냄



## SEMANTIC

```html
<nav>
	<ol>
    	<li><a href="1.html">기술소개</a></li>
        <li><a href="2.html">기본분법</a></li>
    </ol>
</nav>

<footer>
    <ul>
        <li><a href="privacy.html">개인보호정책</a></li>
        <li><a href="about.html">회사소개</a></li>
    </ul>
</footer>

<section>
    <article>
        <h2>선행학습</h2>
        수업에 대한 내용
    </article>
    <article>
        <h2>선행학습</h2>
        수업에 대한 내용
	</article>    
</section>    
```

* '의미론적인'의 의미, 큰 정보는 없지만 의미를 명확하게 표현하기 위한 태그

* 몇 가지 semantic 태그가 존재, 찾아서 확인해볼 것
* article, aside, details, figure, footer, header, main, mark, nav, section, time등이 있다



## 검색엔진 최적화

* SEO : search engine optimizer 



## 모바일 지원

```html
..
	<meta name="viewport" content="device-width", initial-scale="1.0">
..
```

* content="device-width" : 화면이 디바이스 크기에 따라 보기 적절하게 조정
* initial-scale="1.0" : 줌 상태, 1.0이면 기본 값



## input types

```html
..
<form action"form.php">
	<input type="number" min="10" max="15"> 
   	<input type="date" name="datev">
    <input type="month" name="monthv">
    <input type="week" name="weekv">
    <input type="time" name="timev">
    <input type="email" name="emailv">
    <input type="serch" name="searchv">
    <input type="tel" name="telv">
    <input type="url" name="urlv">
    <input type="range" name="rangev" min="0" max="10">    
    <input type="submit">
</form>
..
```



* color, date, datetime, datetime-local, email, month, number range, search, tel, time ,url , week 가 있다

* type="number"의 경우 최대, 최소값을 정할 수 있다

* type="range"는 정도를 나타내는 막대 바를 나타냄

  

## 추가 속성

```html
..
	<form action="login.php" autocomplete="on">
        <input type="text" name="id" placeholder="id를 입력해주세요." autofocus>
        <input type="password" name="password" autocomplete="off" placeholder="비밀번호를 입력해주세요.">
        <input type="submit">
        
</form>
..
```

* cutocomplete="on" : 자동완성기능 활성화, 아래 입력값들의 로그인 기록을 불러올 수 있도록 함
* input 속성으로 autocompelete 를 넣어서 개별 설정이 가능
* placeholder="텍스트" : 입력전에 보이는 값을 나타낼 수 있음
* autofocus : 페이지가 열렸을 때 자동으로 활성화 되도록 함



```html
..
	<form action="register.php">
  		<input type="text" name="id" placeholder="아이디를 입력" required pattern="[a-zA-Z].+[0-9]">
        <input type="email" name="email" placeholer="이메일 입력">
        <input type="submit">
	</form>
..
```

* required : 입력하지 않으면 서버로 데이터가 제출되지 않도록 함
* required pattern을 통해 필수 조건을 설정할 수 있다 ← 정규표현식 활용