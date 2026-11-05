"""Lesson 4 What-If Science 웹앱을 public/ 폴더로 모은다.

원본 HTML은 이 폴더의 상위 폴더(학습지 연구하기)에 있다.
원본을 고친 뒤 이 스크립트를 다시 돌리면 public/ 이 새로 만들어진다.

    python build_site.py
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent
OUT = HERE / "public"

PAGES = {
    "buildup.html": "Lesson4_웹앱학습지_빌드업_1-4차시.html",
    "lab.html": "Lesson4_사고실험실_웹앱.html",
    "step.html": "Lesson4_한걸음학습지_2-1_2-4반.html",
}

HOME_LINK = '<a href="./" style="color:#ffd37a;font-size:14px;font-weight:700;text-decoration:none;margin-left:12px">🏠 웹앱 모음</a>'


def replace_once(text: str, old: str, new: str, name: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"{name}: 바꿀 부분을 찾지 못했습니다 → {old[:60]}")
    return text.replace(old, new)


def build() -> None:
    OUT.mkdir(exist_ok=True)
    texts = {dst: (SRC / src).read_text(encoding="utf-8") for dst, src in PAGES.items()}

    # 빌드업 학습지: 실험실 링크를 사이트 주소로, 모음 링크 추가
    t = texts["buildup.html"]
    t = replace_once(t, 'href="Lesson4_사고실험실_웹앱.html" data-alt="lab.html"', 'href="lab.html"', "buildup")
    t = replace_once(t, '<a class="lablink"', '<a class="lablink" href="./" style="background:rgba(255,255,255,.16);color:#fff;margin-left:auto">🏠 모음</a><a class="lablink" style="margin-left:0"', "buildup")
    texts["buildup.html"] = t

    # 사고 실험실: 빌드업 링크를 사이트 주소로, 모음 링크 추가
    t = texts["lab.html"]
    t = replace_once(t, 'href="Lesson4_웹앱학습지_빌드업_1-4차시.html" data-alt="index.html">← 빌드업 학습지</a>',
                     'href="buildup.html">← 빌드업 학습지</a>' + HOME_LINK, "lab")
    texts["lab.html"] = t

    # 한 걸음 학습지: 머리말에 모음 링크 추가
    t = texts["step.html"]
    t = replace_once(t, '<h1>👣 한 걸음 학습지</h1>', '<h1>👣 한 걸음 학습지</h1><a href="./" style="color:#ffd37a;font-size:14px;font-weight:700;text-decoration:none">🏠 웹앱 모음</a>', "step")
    texts["step.html"] = t

    for name, text in texts.items():
        (OUT / name).write_text(text, encoding="utf-8")
        print("wrote", OUT / name)


if __name__ == "__main__":
    build()
