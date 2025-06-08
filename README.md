# Naver Cafe User Scan

🔍 네이버 카페에서 특정 게시글에 댓글 단 사용자들의 정보를 수집하고 분석할 수 있는 도구입니다.

> Python 기반으로 작성된 이 프로젝트는 네이버 카페 API를 활용하여 게시글에 댓글, 게시글을 작성한 유저들의 ID, 닉네임, 유저 네이버카페 고유키값 등을 수집합니다.  

---

## ✅ 주요 기능

- 특정 네이버 카페 글에 댓글 단 사용자 목록 수집
- 닉네임, 유저 ID, 유저 네이버카페 고유키값 추출
- 페이지네이션 자동 처리

---

## 🛠 설치 방법

```bash
git clone https://github.com/ByHRG/Naver-Cafe-User-Scan.git
cd Naver-Cafe-User-Scan
pip install requests selenium
```

필수 라이브러리:
- `requests`
- `selenium`
---


## 📄 참고사항

- 네이버 카페 API는 공개 문서가 없으며, 변경될 가능성이 있습니다.
- 댓글 수가 많은 경우 여러 페이지를 자동 순회하며 수집합니다.
- 너무 빠른 요청은 차단의 원인이 될 수 있으므로 주의하세요.

---

## 📬 문의

이슈나 기능 제안은 [Issues](https://github.com/ByHRG/Naver-Cafe-User-Scan/issues) 탭을 통해 남겨주세요.

---

## 🪪 라이선스

MIT License
