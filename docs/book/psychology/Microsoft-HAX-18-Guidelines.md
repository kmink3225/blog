# Microsoft HAX: 18 Guidelines for Human-AI Interaction

> Source: https://www.microsoft.com/en-us/haxtoolkit/
> Reference Paper: Amershi et al., "Guidelines for Human-AI Interaction" (CHI 2019)
> 20년 이상의 연구를 종합한 증거 기반 AI 사용자 경험 설계 가이드라인

---

## Category 1: Initially (초기 상호작용 시)

### G1: Make clear what the system can do

AI 시스템이 무엇을 할 수 있는지 사용자가 이해하도록 돕는다.

- 기능의 범위를 명확히 제시
- 과대 약속 금지
- 온보딩 시 구체적 예시로 기능 시연

### G2: Make clear how well the system can do what it can do

AI 시스템이 얼마나 자주 실수할 수 있는지 사용자가 이해하도록 돕는다.

- 정확도/신뢰도를 솔직하게 전달
- 불확실한 영역을 사전에 고지
- 사용자가 시스템의 한계를 인지한 상태에서 사용하도록 유도

---

## Category 2: During Interaction (상호작용 중)

### G3: Time services based on context

사용자의 현재 작업과 환경에 기반하여 행동하거나 중단할 시점을 결정한다.

- 사용자가 집중 중일 때 불필요한 알림 금지
- 맥락에 맞는 타이밍으로 정보 제공
- 사용자의 작업 흐름을 방해하지 않는 개입 설계

### G4: Show contextually relevant information

사용자의 현재 작업과 환경에 관련된 정보를 표시한다.

- 현재 상황에 맞는 추천/정보만 제공
- 무관한 정보로 인한 인지 부하 감소
- 동적 맥락 인식 기반 UI 조정

### G5: Match relevant social norms

사용자의 사회적/문화적 맥락에 맞는 방식으로 경험을 전달한다.

- 문화적 기대에 부합하는 언어와 행동 사용
- 지역/맥락별 적절한 커뮤니케이션 스타일 적용
- 사용자가 불편하지 않은 상호작용 패턴 설계

### G6: Mitigate social biases

AI 시스템의 언어와 행동이 바람직하지 않고 불공정한 고정관념과 편향을 강화하지 않도록 보장한다.

- 학습 데이터의 편향 식별 및 완화
- 출력에서 성별, 인종, 연령 등의 고정관념 제거
- 정기적 편향 감사 수행
- 다양한 사용자 그룹에 대한 공평한 성능 보장

### G7: Support efficient invocation

필요할 때 AI 시스템의 서비스를 호출하거나 요청하기 쉽게 만든다.

- 직관적 접근 경로 설계
- 최소 단계로 AI 기능 활성화
- 자주 사용하는 기능에 대한 단축 경로 제공

### G8: Support efficient dismissal

원하지 않는 AI 시스템 서비스를 쉽게 무시하거나 닫을 수 있게 만든다.

- 원클릭 닫기/무시 기능
- AI 제안을 거부해도 패널티 없음
- 사용자의 "아니오"를 존중하는 설계
- 거부 후 동일 제안 반복 금지

---

## Category 3: When Wrong (AI가 틀렸을 때)

### G9: Support efficient correction

AI 시스템이 틀렸을 때 편집, 개선, 복구를 쉽게 만든다.

- 간단한 수정 메커니즘 제공
- 실행 취소/되돌리기 기능
- 사용자가 올바른 답을 직접 제공할 수 있는 경로
- 수정 사항이 향후 결과에 반영됨을 전달

### G10: Scope services when in doubt

사용자의 목표가 불확실할 때 명확화를 시도하거나 AI 시스템의 서비스를 우아하게 축소한다.

- 불확실 시 가정 대신 질문
- 애매한 요청에 대해 좁은 범위의 안전한 응답
- 과도한 추론보다 겸손한 응답 선호
- "모르겠다"를 인정하는 설계

### G11: Make clear why the system did what it did

AI 시스템이 왜 그렇게 행동했는지에 대한 설명에 접근할 수 있도록 한다.

- 결정 근거의 투명한 제시
- 요청 시 상세 설명 접근 가능
- 기술적 복잡성을 사용자 수준에 맞게 조정
- 반직관적 결과에 대해 특히 명확한 설명 제공

---

## Category 4: Over Time (시간이 지남에 따라)

### G12: Remember recent interactions

단기 기억을 유지하고, 사용자가 그 기억을 효율적으로 참조할 수 있게 한다.

- 이전 대화/상호작용 맥락 유지
- "아까 말한 것"에 대한 참조 지원
- 세션 간 연속성 보장
- 불필요한 반복 질문 금지

### G13: Learn from user behavior

사용자의 행동으로부터 학습하여 시간에 따라 경험을 개인화한다.

- 사용 패턴에서 선호 추론
- 명시적 요청 없이도 점진적 개선
- 학습 중인 내용을 투명하게 전달
- 개인화 수준을 사용자가 제어할 수 있도록 허용

### G14: Update and adapt cautiously

AI 시스템의 행동을 업데이트하고 적응할 때 파괴적 변경을 제한한다.

- 급격한 행동 변화 금지
- 점진적 변화로 사용자 적응 시간 제공
- 주요 변경 전 사용자 동의 구하기
- 이전 행동으로 되돌릴 수 있는 옵션 제공

### G15: Encourage granular feedback

AI 시스템과의 정기적 상호작용 중 선호를 나타내는 피드백을 제공할 수 있게 한다.

- 간편한 피드백 메커니즘 (좋아요/싫어요, 평점)
- 상호작용 맥락 안에서 자연스러운 피드백 수집
- 피드백이 어떻게 활용되는지 설명
- 피드백 제공이 부담이 되지 않도록 설계

### G16: Convey the consequences of user actions

사용자 행동이 AI 시스템의 향후 행동에 미치는 영향을 즉시 업데이트하거나 전달한다.

- "이 행동으로 인해 향후 X가 변경됩니다" 명시
- 피드백→결과의 인과관계를 투명하게 표시
- 예상치 못한 부작용에 대한 사전 경고
- 사용자가 결과를 이해하고 의도적으로 행동하도록 유도

### G17: Provide global controls

AI 시스템이 모니터링하는 것과 행동 방식을 사용자가 전역적으로 커스터마이징할 수 있게 한다.

- 전체 설정 페이지/대시보드 제공
- 데이터 수집 범위 제어
- AI 기능별 온/오프 토글
- 개인화 수준 조절 슬라이더
- 전체 초기화 옵션

### G18: Notify users about changes

AI 시스템이 기능을 추가하거나 업데이트할 때 사용자에게 알린다.

- 새 기능/변경 사항에 대한 명확한 알림
- 변경 이유 설명
- 사용자가 변경을 검토하고 수용/거부할 시간 제공
- 강제 업데이트 최소화

---

## 카테고리별 요약

| Category | Guidelines | 핵심 원칙 |
|---|---|---|
| **Initially** | G1, G2 | 기능과 한계를 솔직하게 전달하여 적절한 기대치 설정 |
| **During Interaction** | G3~G8 | 맥락에 맞는 서비스 제공, 편향 완화, 호출/무시를 모두 쉽게 |
| **When Wrong** | G9~G11 | 쉬운 수정, 불확실 시 겸손, 투명한 설명 |
| **Over Time** | G12~G18 | 학습과 적응을 신중하게, 사용자 제어 보장, 변경 알림 |

---

## 적용 프레임워크: HAX Toolkit 4단계

1. **Learn**: Guidelines와 Design Library를 학습
2. **Plan**: HAX Workbook으로 팀과 우선순위 논의
3. **Design**: Design Library의 디자인 패턴 적용
4. **Prototype**: HAX Playbook으로 AI 실패 시나리오 대비

---

## 참고

- 원본 논문: Amershi, S. et al. (2019). "Guidelines for Human-AI Interaction." CHI 2019.
- HAX Toolkit: https://www.microsoft.com/en-us/haxtoolkit/
- HAX Design Library: https://www.microsoft.com/en-us/haxtoolkit/library/
