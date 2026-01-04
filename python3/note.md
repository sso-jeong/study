- [[#1 프로젝트 구조]]

---

# 1 프로젝트 구조

```bash
my_project/
├─ pyproject.toml          # 패키지/의존성/도구 설정(요즘 표준)
├─ README.md               # 프로젝트 설명, 실행 방법
├─ .gitignore              # git에 올리면 제외할 파일들
├─ src/
│  └─ my_project/          # 실제 패키지(모듈) 코드
│     ├─ __init__.py
│     ├─ main.py           # 진입점(실행)
│     └─ utils.py          # 공용 함수들
├─ tests/
│  ├─ __init__.py
│  └─ test_utils.py        # 테스트 코드(pytest)
└─ scripts/
   └─ run_local.py         # 실행/도우미 스크립트
```

- **src/**: 진짜 코드가 들어가는 곳
- **tests/**: 테스트 코드 (보통 `pytest` 사용)
- **scripts/**: 로컬 실행, 데이터 준비, 배포 등 도우미 스크립트
- **pyproject.toml**: 의존성, 포맷터/린터 설정까지 한 곳에 모으는 최신 방식
- **README.md**: 사용법/설명
- **.gitignore**: `.venv/`, `__pycache__/` 같은 거 git에 안 올리게