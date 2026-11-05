# Lesson 4 What-If Science 웹앱 모음

2026학년도 2학기 영어Ⅱ Lesson 4 수업용 웹앱입니다.

| 주소 | 내용 |
|---|---|
| `/` | 웹앱 모음 (첫 화면) |
| `/buildup.html` | 빌드업 학습지. `#s12`는 1·2차시, `#s34`는 3·4차시 |
| `/lab.html` | 사고 실험실. `#A`~`#E`로 실험 5가지 중 하나를 바로 연다 |
| `/step.html` | 한 걸음 학습지. `#1`~`#4`로 차시를 바로 연다 |

## 배포 (Netlify)

1. 이 저장소를 GitHub에 올립니다.
2. Netlify에서 **Add new site → Import an existing project → GitHub**를 고르고 이 저장소를 선택합니다.
3. 설정은 `netlify.toml`에 들어 있어서 그대로 **Deploy**를 누르면 됩니다. 빌드 명령은 없고, 배포 폴더는 `public`입니다.
4. 이후에는 GitHub에 push할 때마다 Netlify가 자동으로 다시 배포합니다.

## 고치는 방법

원본 HTML은 상위 폴더(`학습지 연구하기`)에 있습니다. 원본을 고친 뒤 아래 명령으로 `public/`을 다시 만들고 commit·push합니다.

```
python build_site.py
```

`public/index.html`(웹앱 모음)은 직접 고칩니다.
