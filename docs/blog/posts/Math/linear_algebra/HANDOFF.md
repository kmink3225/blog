# Linear Algebra Series 정리 — 핸드오프 문서

> 마지막 작업일: 2026-04-11 (폴더 현황 재확인)
> 최신 커밋: `b107a023` (main)
> 목표: Gilbert Strang MIT 18.06 교재 기준으로 선형대수 포스트 완전 정리

---

## 완료된 작업

| 내용 | 비고 |
|---|---|
| 빈 템플릿 13개 삭제 | 10~19 시리즈, 07.determinants, 09.basic_tensor |
| 한국어/영어 이중복제 제거 | 01/02/03/04/06.identity |
| 09.orthogonality → mit-14, mit-17 보강 후 **삭제 완료** | 폴더에 없음 확인 |
| 09.eigenvalues → mit-21 보강 후 **삭제 완료** | 폴더에 없음 확인 |
| 11.linear_form + 11.bilinear_form → 08.quadratic_form 통합 | 원본 파일은 아직 잔존 |
| mit-23 내용 전면 교체 | 행렬식 중복 → 미분방정식 + e^{At} |
| Math/index.qmd 업데이트 | 삭제 파일 제거, MIT 시리즈 반영 |
| **mit-06-1 ~ mit-06-6 시리즈 신규 작성** | Ch.6 고유값 섹션 6개 포스트 완성 |
| mit-28 삭제 (사용자) → mit-06-5로 내용 흡수·확장 | 깨진 참조 15개 정리 작업 남음 |

---

## 현재 폴더의 파일 현황 (2026-04-11 기준)

### MIT 강의 시리즈 (mit-XX 파일)

| 파일 | 상태 |
|---|---|
| mit-00-gilbert-strang-overview.qmd | 정상 |
| mit-01-1 ~ mit-01-4 (4개) | 정상 |
| mit-02-1 ~ mit-02-7 (7개) | 정상 |
| mit-03-1 ~ mit-03-7 (7개) | 정상 |
| mit-04-1 ~ mit-04-5 (5개) | 정상 |
| mit-05-gilbert-strang-substitution.qmd | 정상 |
| mit-05-1 ~ mit-05-4 (4개) | 정상 |
| mit-06-gilbert-strang-column-space.qmd | 정상 (번호 체계 별도) |
| **mit-06-1 ~ mit-06-6 (6개)** | **신규 — 2026-04-10 작성** |
| mit-07-gilbert-strang-null-space.qmd | 정상 |
| mit-08-gilbert-strang-row-reduced-form.qmd | 정상 |
| mit-09-gilbert-strang-linear-independence.qmd | 정상 |
| mit-10-gilbert-strang-subspaces.qmd | 정상 |
| mit-11-gilbert-strang-matrix-space.qmd | 정상 |
| mit-12-gilbert-strang-graph.qmd | 정상 |
| mit-13-gilbert-strang-mid-review.qmd | 정상 |
| mit-14 ~ mit-20 | **없음 (미작성)** |
| mit-21-gilbert-strang-eigenvalue.qmd | 정상 |
| mit-22-gilbert-strang-diagonalization.qmd | 정상 |
| mit-23-gilbert-strang-differentiation.qmd | 정상 (내용 교체 완료) |
| mit-24-gilbert-strang-markov-matrix.qmd | 정상 |
| mit-25-gilbert-strang-mid-reviewe2.qmd | 정상 |
| mit-26-gilbert-strang-symmetric-matrices.qmd | 정상 |
| mit-27-gilbert-strang-complex-matrices.qmd | 정상 |
| mit-28 | **삭제됨** (→ mit-06-5로 대체) |
| mit-29-gilbert-strang-similar-matrices.qmd | 정상 (mit-06-6과 중복 검토 필요) |

### 레거시 파일 (정리 대상)

| 파일 | 처리 방침 |
|---|---|
| `01.basic_vector.qmd` | 삭제 검토 |
| `02.norm_dot-product.qmd` | mit-01-1에 병합 완료 → 삭제 대기 |
| `03.vector_equation.qmd` | mit-01 보강 후 삭제 예정 |
| `04.matrix_operations.qmd` | mit-03 병합 후 삭제 예정 |
| `05.matrix_multiplication.qmd` | mit-03 병합 후 삭제 예정 |
| `06.system_of_lineqr_equations.qmd` | mit-02 병합 후 삭제 예정 |
| `09.special_matrix.qmd` | 파일명 정규화 예정 (`ch02-special-matrix.qmd`) |
| `09.temp-reference.qmd` | 내용 확인 후 삭제 또는 유지 |
| `09.vector_space.qmd` | mit-06~10 통합 후 삭제 예정 |
| `10.linear_transformation.qmd` | 파일명 정규화 예정 (`ch08-linear-transformation.qmd`) |
| `11.bilinear_form.qmd` | 08.quadratic_form 통합 완료 → 삭제 대기 |
| `11.linear_form.qmd` | 08.quadratic_form 통합 완료 → 삭제 대기 |
| `derivative_matrix_vector.qmd` | 통합 후 삭제 예정 |
| `derivative_vector_matrix.qmd` | 통합 후 삭제 예정 |

> `08.quadratic_form.qmd`, `09.cholesky_decomposition.qmd` — 폴더에 없음. 이미 삭제됐거나 다른 경로에 있을 수 있음. 확인 필요.

---

## 남은 작업 — 다음 세션에서 이어서

### 작업 1. mit-28 깨진 참조 정리 ⚠️ 우선 처리 권장

아래를 참조: 이 문서 하단 "[신규] mit-28 깨진 참조 정리" 섹션.

### 작업 2. `06.system_of_lineqr_equations.qmd` → `mit-02` 병합
- 3D matplotlib 시각화 코드 (3개 평면 교차점, line 134~188) → mit-02 "실사용 예시" 앞에 추가
- 완료 후 `06.system_of_lineqr_equations.qmd` 삭제

### 작업 3. `04/05.matrix` → `mit-03` 병합
- `04.matrix_operations.qmd`: 행렬 동형사상 개념, 용어 정리
- `05.matrix_multiplication.qmd`: 선형 전이 관점 해석
- 완료 후 두 파일 삭제

### 작업 4. `03.vector_equation.qmd` → `mit-01` 보강
- 평면의 방정식, 재매개변수화 내용 추가
- 완료 후 `01/02/03.qmd` 삭제 (02는 mit-01-1에 병합 완료)

### 작업 5. `09.vector_space.qmd` → `mit-06~10` 비교 통합
- 벡터 공간 8가지 공리 → mit-06
- 고유 R 코드 예시 → 해당 mit 파일
- 완료 후 `09.vector_space.qmd` 삭제

### 작업 6. `derivative_matrix_vector.qmd` + `derivative_vector_matrix.qmd` → 통합
- 새 파일명: `matrix-calculus-derivatives.qmd`
- 두 파일 비중복 내용 합치기
- 완료 후 소스 2개 삭제, index.qmd 링크 업데이트

### 작업 7. 레거시 파일 삭제 (병합 완료 확인 후)
- `11.linear_form.qmd`, `11.bilinear_form.qmd` (→ 08.quadratic_form 통합 완료)
- `02.norm_dot-product.qmd` (→ mit-01-1 병합 완료)
- `09.temp-reference.qmd` (내용 확인 후)

### 작업 8. 파일명 정규화 (병합 모두 완료 후)
| 현재 파일명 | 변경 후 |
|---|---|
| `09.special_matrix.qmd` | `ch02-special-matrix.qmd` |
| `10.linear_transformation.qmd` | `ch08-linear-transformation.qmd` |

### 작업 9. mit-29 중복 검토
- `mit-29-gilbert-strang-similar-matrices.qmd`와 `mit-06-6-gilbert-strang-similar-matrices.qmd`가 공존 중
- 내용 비교 후 mit-29를 mit-06-6으로 대체하거나 보완 후 삭제

---

## 최종 목표 폴더 구조

```
linear_algebra/
├── mit-00 ~ mit-13          ← 기초 (벡터, 연립방정식, 행렬, 부분공간)
├── mit-14 ~ mit-20          ← 미작성 (직교성, Gram-Schmidt, 행렬식 응용 등)
├── mit-21 ~ mit-27, mit-29  ← 고유값, 대칭행렬, 복소행렬 등
├── mit-06-1 ~ mit-06-6      ← Ch.6 심화 시리즈
├── ch02-special-matrix.qmd
├── ch08-linear-transformation.qmd
└── matrix-calculus-derivatives.qmd
```

---

## 주의사항

- `09.temp-reference.qmd` 내용 확인 후 빈 파일이면 삭제 (`09.temp.qmd`에서 이름 바뀐 것으로 추정)
- 모든 작업 완료 후 `Math/index.qmd` 최종 점검
- 파일명 변경 시 `git mv` 사용 (삭제+추가로 처리됨)
- mit-14 ~ mit-20 (7개) 미작성 — 직교성(14), Projections(15~16), Gram-Schmidt(17), SVD(18), 복습(19~20) 예상

---

## [신규] mit-28 깨진 참조 정리 — 2026-04-11 추가

### 배경

- `mit-28-gilbert-strang-positive-definite-matrices.qmd`를 **사용자가 의도적으로 삭제**했다 (2026-04-10 대화에서 확인).
- 내용은 **새 포스트 `mit-06-5-gilbert-strang-positive-definite-matrices.qmd`** (2026-04-10 작성)에 완전히 흡수·확장됨.
- 현재 15개 파일에 깨진 참조가 존재하며 Quarto 렌더 시 `WARN: Unable to resolve link target` 경고가 발생한다.

### 작업: 깨진 참조 15개 파일 목록

| # | 파일 | 라인 |
|---|------|------|
| 1 | `docs/blog/posts/Math/index.qmd` | 142 |
| 2 | `docs/blog/posts/Math/linear_algebra/09.special_matrix.qmd` | 562 |
| 3 | `docs/blog/posts/Math/linear_algebra/mit-01-1-gilbert-strang-vectors-overview.qmd` | 394 |
| 4 | `docs/blog/posts/Math/linear_algebra/mit-02-3-gilbert-strang-elimination-idea.qmd` | 786 |
| 5 | `docs/blog/posts/Math/linear_algebra/mit-02-4-gilbert-strang-matrix-elimination.qmd` | 804 |
| 6 | `docs/blog/posts/Math/linear_algebra/mit-06-1-gilbert-strang-eigenvalue-overview.qmd` | 476 |
| 7 | `docs/blog/posts/Math/linear_algebra/mit-06-2-gilbert-strang-diagonalization.qmd` | 530 |
| 8 | `docs/blog/posts/Math/linear_algebra/mit-06-3-gilbert-strang-differential-equations.qmd` | 548 |
| 9 | `docs/blog/posts/Math/linear_algebra/mit-06-4-gilbert-strang-symmetric-matrices.qmd` | 672 |
| 10 | `docs/blog/posts/Math/linear_algebra/mit-06-5-gilbert-strang-positive-definite-matrices.qmd` | 777 (자기참조 → 삭제 또는 다른 링크로 교체) |
| 11 | `docs/blog/posts/Math/linear_algebra/mit-21-gilbert-strang-eigenvalue.qmd` | 204 |
| 12 | `docs/blog/posts/Math/linear_algebra/mit-25-gilbert-strang-mid-reviewe2.qmd` | 110 |
| 13 | `docs/blog/posts/Math/linear_algebra/mit-26-gilbert-strang-symmetric-matrices.qmd` | 157 |
| 14 | `docs/blog/posts/Math/linear_algebra/mit-27-gilbert-strang-complex-matrices.qmd` | 140 |
| 15 | `docs/blog/posts/Math/linear_algebra/mit-29-gilbert-strang-similar-matrices.qmd` | 137 |

### 권장 해결 방법 (Option A)

모든 `mit-28-gilbert-strang-positive-definite-matrices.qmd` 링크를 `mit-06-5-gilbert-strang-positive-definite-matrices.qmd`로 치환한다.

**주의사항**:
- 파일마다 상대경로 형태가 다름 (`./mit-28-...` vs `./linear_algebra/mit-28-...`)
- 각 파일을 Grep으로 먼저 확인한 뒤 Edit 도구로 치환
- 10번 자기참조(mit-06-5 내부)는 해당 라인을 삭제하거나 의미 있는 다른 링크로 교체
- **15개 일괄 수정이므로 Stop-and-Ask 규칙에 따라 사용자 승인 후 실행**

### 검증 명령

```
Grep pattern: mit-28-gilbert-strang-positive-definite-matrices
path: docs/blog/posts/Math
```

정리 완료 후 결과 0개여야 한다.

### 완료 후 배포

```bash
bash render.sh
```

커밋 메시지:
```
fix: mit-28 깨진 참조를 mit-06-5로 일괄 갱신 (15개 파일)
```
