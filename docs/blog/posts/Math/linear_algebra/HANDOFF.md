# Linear Algebra Series 정리 — 핸드오프 문서

> 마지막 작업일: 2026-04-06  
> 최신 커밋: `9a30640e` (main)  
> 목표: Gilbert Strang MIT 18.06 교재 기준으로 선형대수 포스트 완전 정리

---

## 완료된 작업 (7/13)

| 내용 | 비고 |
|---|---|
| 빈 템플릿 13개 삭제 | 10~19 시리즈, 07.determinants, 09.basic_tensor |
| 한국어/영어 이중복제 제거 | 01/02/03/04/06.identity |
| 09.orthogonality → mit-14, mit-17 보강 | 직교벡터, Gram-Schmidt, QR 분해 |
| 09.eigenvalues → mit-21 보강 | PD/PSD/ND 분류표, Python 코드 |
| 11.linear_form + 11.bilinear_form → 08.quadratic_form 통합 | 하단에 섹션 추가 |
| mit-23 내용 전면 교체 | 행렬식 중복 → 미분방정식 + e^{At} |
| Math/index.qmd 업데이트 | 삭제 파일 제거, MIT 시리즈 반영 |

---

## 남은 작업 (6개) — 다음 세션에서 이어서

### 1. `06.system_of_lineqr_equations.qmd` → `mit-02` 병합
- 3D matplotlib 시각화 코드 (3개 평면 교차점, line 134~188) → mit-02 "실사용 예시" 앞에 추가
- 완료 후 `06.system_of_lineqr_equations.qmd` 삭제

### 2. `04/05/06.identity` → `mit-03` 병합
- `04.matrix_operations.qmd`: 행렬 동형사상 개념, 용어 정리
- `05.matrix_multiplication.qmd`: 선형 전이 관점 해석
- `06.identity_matrix.qmd`: 열 분해 관점
- 완료 후 3개 파일 삭제

### 3. `03.vector_equation.qmd` → `mit-01` 보강
- 평면의 방정식, 재매개변수화 내용 추가
- 완료 후 `01/02/03.qmd` 삭제 (02는 mit-01-1에 병합 완료)

### 4. `09.vector_space.qmd` → `mit-06~10` 비교 통합
- 벡터 공간 8가지 공리 → mit-06
- 고유 R 코드 예시 → 해당 mit 파일
- 완료 후 `09.vector_space.qmd` 삭제

### 5. `derivative_matrix_vector.qmd` + `derivative_vector_matrix.qmd` → 통합
- 새 파일명: `matrix-calculus-derivatives.qmd`
- 두 파일 비중복 내용 합치기
- 완료 후 소스 2개 삭제, index.qmd 링크 업데이트

### 6. 파일명 정규화 (병합 모두 완료 후)
| 현재 파일명 | 변경 후 |
|---|---|
| `08.quadratic_form.qmd` | `ch06-quadratic-form.qmd` |
| `09.special_matrix.qmd` | `ch02-special-matrix.qmd` |
| `09.cholesky_decomposition.qmd` | `ch06-cholesky-decomposition.qmd` |
| `10.linear_transformation.qmd` | `ch08-linear-transformation.qmd` |

---

## 최종 목표 폴더 구조

```
linear_algebra/
├── mit-01 ~ mit-25          ← 메인 강의 시리즈 (Strang 교재)
├── ch02-special-matrix.qmd
├── ch06-quadratic-form.qmd
├── ch06-cholesky-decomposition.qmd
├── ch08-linear-transformation.qmd
└── matrix-calculus-derivatives.qmd
```

---

## 병합 완료 → 삭제 대기 중인 파일

아래 파일들은 내용이 MIT 시리즈로 이전 완료됐으나 아직 삭제 안 됨:

- `09.orthogonality.qmd` (→ mit-14/17)
- `09.eigenvalues.qmd` (→ mit-21)
- `11.linear_form.qmd` (→ 08.quadratic_form)
- `11.bilinear_form.qmd` (→ 08.quadratic_form)
- `02.norm_dot-product.qmd` (→ mit-01-1)

---

## 주의사항

- `09.temp.qmd` 내용 확인 후 빈 파일이면 삭제
- 모든 작업 완료 후 `Math/index.qmd` 최종 점검
- 파일명 변경 시 `git mv` 사용 (삭제+추가로 처리됨)
