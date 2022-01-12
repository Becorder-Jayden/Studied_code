HTML : 정보를 어떻게 가장 잘 표현할 것인가

CSS : HTML의 정보를 어떻게 디자인 할 것인가 



## html에 css 삽입하는 방법

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            h2{color:blue}
        </style>
    </head>
    <body>
        <h1 style="color:red">Hello World</h1>
        <h2>Hello World</h2>
    </body>
</html>
```

* sytle 태그에 CSS를 담는다
* CSS 언어 문법에 따라 html 스타일을 지정하게 된다
* html 내에 직접 style을 지정하는 방법도 가능



## 선택자와 선언

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            li{
                color:red;
           		textdecoration:underline;
        </style>
    </head>
    <body>
        <ul>
            <li>HTML</li>
        	<li>CSS</li>
        	<li>JavaScript</li>
        </ul>
    </body>
</html>
```

* 구글 images에 css selector를 검색하면 css 문법 명을 확인할 수 있다



## 선택자의 종류

```html
..
	<style>
        li{
        	color:red;
           	textdecoration:underline;
        	}
        #select{
            font-size:50px;
        	}
        .deactive{
            text-decoration: line-through;
        }
    </head>
	</style>
    <body>
        <ul>
            <li class id="deactive">HTML</li>
        	<li id="select">CSS</li>
        	<li class id="deactive">JavaScript</li>
        </ul>
    </body>
</html>
```

* id : 특정 부분의 스타일을 다르게 하고 싶을 때 사용
* id라는 속성을 주고 속성값을 주면 css에서 사용할 때 #을 기입

* 클래스를 대상으로 css에서 사용할 때 .을 기입

* 세 가지의 선택자 : 태그 선택자, id 선택자, class 선택자

* id 선택자는 단 한번, class 선택자는 여러번 등장해서 그룹핑 한다



## 부모 자식 선택자

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            ul li{
                color:red;
            }
            #lecture>li{
                border:1px solid red;
                color:blue;
            }
            ul, ol{
                background-color:powederblue:
            }
        </style>
    </head>
    <body>
        <ul>
            <li>HTML</li>
        	<li>CSS</li>
        	<li>JavaScript</li>
        </ul>
        <ol id="lecture">
            <li>HTML</li>
            <li>CSS
            	<ol>
                    <li>selector</li>
                    <li>declaration</li>
            	</ol>
            </li>
        	<li>JavaScript</li>
        </ol>
    </body>
</html>
```

* ul li : 띄어쓰기를 하게 되면 ul 아래의 li가 선택됨

* ol>li : ol 바로 밑에 있는 li에만 대상으로 스타일이 적용, 부모 자식 관계
* ul, ol : ul과 ol을 동시에 설정할 수 있다, 대등 관계



## 선택자 팁

* fluckout.github.io 페이지 참고. CSS 선택자 연습이 가능한 사이트

* 구글 이미지 css cheatsheet selector 검색



## PSEUDO CLASS SELECTOR

```html
<!DOCTYPE html>
<html>
    <head>
        <style>
            a:link{
                color:black;
            }
            a:visited{
                color:red;
            }
            a:active{
                color:green;
            }
            a:hover{
                color:yellow;
            }
        </style>
    </head>
    <body>
        <a href="https://opentutorials.org">방문함</a>
        <a href="http://a.a">방문안함</a>
    </body>
</html>
```

* 가상 클래스 선택자
* hover : 마우스를 올려놨을 때 색상 변화
* visited : 방문한 이력이 있으면 색상 변화
* active : 활성화 되면 색상 변화
* link : 링크일 때 색상 변화

