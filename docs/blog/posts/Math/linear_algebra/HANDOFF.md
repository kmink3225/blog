# Linear Algebra Series 정리 — 핸드오프 문서

> 마지막 작업일: 2026-04-14
> 상태: **전체 레거시 정리 완료**
> 참고 커밋: `eb28b4e0` (B1) → `6d1ec96f` (B5)

---

## 완료 작업 요약 (2026-04-14)

13개 레거시 파일과 1개 중복 mit 파일을 정리하고, 유니크 콘텐츠를 mit 시리즈 및 2개 신규 포스트로 흡수했다.

### 배치별 커밋

| 배치 | 커밋 | 대상 파일 | 흡수 위치 |
|---|---|---|---|
| B1 | `eb28b4e0` | 01.basic_vector, 02.norm_dot-product, 03.vector_equation | mit-01-2 (위치벡터·8공리·벡터방정식), mit-01-3 (Inner vs Dot callout, 코사인 대안 유도) |
| B2 | `ac1b8ca6` | 04.matrix_operations, 05.matrix_multiplication, 06.system_of_lineqr_equations, **mit-01-4 중복** | mit-02-2 (3D 평면·열벡터 시각화) |
| B3 | `3b345dd5` | 09.vector_space, 09.special_matrix | 삭제 / `special-matrices-catalog.qmd`로 정규화 |
| B4 | `f7f29e8a` | 10.linear_transformation, 11.linear_form, 11.bilinear_form | mit-02-5 (Trace), mit-06-5 (Bilinear Form), mit-07-1 (Linear Form + Dual Basis) |
| B5 | `6d1ec96f` | 09.temp-reference, derivative_matrix_vector, derivative_vector_matrix | `matrix-calculus-derivatives.qmd` 신규 |

**누적: +450 insertions, −6,881 deletions, 14개 파일 삭제, 2개 신규.**

### 자동 해소

- **mit-28 깨진 참조 15개**: B1~B5 진행 중 해당 링크가 있던 파일들이 모두 삭제되거나 mit-06-5로 교체되면서 자연 해소. Grep 확인 결과 콘텐츠 파일 내 0건.
- **mit-21~mit-29 구번호 파일**: 존재하지 않음. 모두 mit-04-x / mit-06-x 신번호 체계로 이미 재편된 상태.

### 최종 마무리 (Task 7)

- Math/index.qmd의 broken 경로 1건 제거 (`mit-01-gilbert-strang-overview.qmd` — 존재하지 않던 파일)
- `_cache` 폴더 2개 삭제: `mit-06-4-...-matrices_cache`, `mit-21-gilbert-strang-eigenvalue_cache`
- 고아 PNG 2개 삭제: `Figure_07_02.png`, `Figure_10_01.png` (참조처 없음)

---

## 현재 폴더 구조

```
linear_algebra/
├── mit-00 ~ mit-10-4             ← MIT 18.06 Strang 강의 시리즈 (전 Chapter 완성)
├── mit-appendix-*.qmd            ← 행렬 분해 요약
├── 12.xtx-variance-covariance.qmd           ← 통계 연결 포스트 (보존)
├── special-matrices-catalog.qmd             ← 특수 행렬 카탈로그 (B3 정규화)
├── matrix-calculus-derivatives.qmd          ← 행렬 미적분 공식 (B5 신규)
├── linear_algebra_functions.r               ← R 유틸리티
├── images/                                  ← 포스트 삽화
└── HANDOFF.md                               ← 본 문서
```

---

## 향후 작업 (선택)

- mit-14 ~ mit-20 (기존 구번호 체계의 직교성·투영·SVD 섹션): 신번호 체계에서는 mit-04-x / mit-06-7 / mit-07-3에 흡수됐으므로 별도 작성 불필요
- 콘텐츠 품질 개선은 각 mit-X 포스트에서 개별 진행
