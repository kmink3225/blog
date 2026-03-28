---
name: "Dive into Deep Learning"
type: book-summary
authors: "Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola"
year: 2023
total_pages: 1089
language: en
keywords: [deep learning, PyTorch, CNN, RNN, transformer, attention, optimization, computer vision, NLP, GAN, recommender systems, Gaussian processes, hyperparameter optimization]
sources:
  - file: "Zhang-D2L_azure_full.md"
    tool: Document Intelligence
---

# Dive into Deep Learning — Summary

> Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola (2023), 1089 pages, 21 chapters + Appendix
> 수학, 코드, 실습을 결합하여 딥러닝을 처음부터 실행 가능하게 가르치는 대화형 교과서이다

## Contents

- Ch 1: Introduction
- Ch 2: Preliminaries
- Ch 3: Linear Neural Networks for Regression
- Ch 4: Linear Neural Networks for Classification
- Ch 5: Multilayer Perceptrons
- Ch 6: Builders' Guide
- Ch 7: Convolutional Neural Networks
- Ch 8: Modern Convolutional Neural Networks
- Ch 9: Recurrent Neural Networks
- Ch 10: Modern Recurrent Neural Networks
- Ch 11: Attention Mechanisms and Transformers
- Ch 12: Optimization Algorithms
- Ch 13: Computational Performance
- Ch 14: Computer Vision
- Ch 15: Natural Language Processing: Pretraining
- Ch 16: Natural Language Processing: Applications
- Ch 17: Reinforcement Learning
- Ch 18: Gaussian Processes
- Ch 19: Hyperparameter Optimization
- Ch 20: Generative Adversarial Networks
- Ch 21: Recommender Systems
- Appendix A: Mathematics for Deep Learning
- Appendix B: Tools for Deep Learning

---

## Chapter Summaries

### Ch 1: Introduction (pp. 1-29)
**핵심**: 전통적 프로그래밍과 머신러닝의 차이를 설명하고, 지도/비지도/강화학습 문제 유형을 소개한다. 딥러닝의 성공 사례와 본질을 논의하며, 이 분야의 역사적 발전 과정을 추적한다.
**키워드**: `machine learning problems`, `supervised learning`, `deep learning history`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 1 (line 3827)
전통적 프로그래밍은 규칙을 명시적으로 코딩하지만, 날씨 예측이나 이미지 인식처럼 패턴이 복잡하거나 시간에 따라 변하는 문제에는 머신러닝이 필요하다. 머신러닝은 데이터, 모델, 목적 함수, 최적화 알고리즘의 네 가지 핵심 구성 요소로 이루어진다. 지도 학습(회귀, 분류, 태깅, 검색, 추천, 시퀀스 학습), 비지도 학습(군집화, PCA, 인과관계 발견), 강화학습(탐색-활용, 환경과 상호작용) 등 다양한 문제 유형을 소개한다. 딥러닝의 역사적 뿌리로 신경과학적 영감, 통계 모델, 정보 이론의 기여를 추적하며, 1940년대부터 현재까지의 발전 흐름을 정리한다. 딥러닝 부흥의 핵심 동력으로 데이터 양의 폭발적 증가, GPU에 의한 연산 능력 향상, 효율적 프레임워크의 등장을 꼽는다. 컴퓨터 비전의 ImageNet 경진대회, 자연어 처리의 기계 번역, 게임 AI(AlphaGo) 등 딥러닝의 대표적 성공 사례를 설명한다. 딥러닝의 본질을 다층 변환을 통한 표현 학습으로 정의하고, 전통적 피처 엔지니어링을 대체하는 종단간(end-to-end) 학습의 이점을 강조한다. 모델 설계에서 매개변수(knobs)를 데이터로 조정하여 원하는 동작을 얻는 "데이터로 프로그래밍하기" 패러다임을 소개한다. 모델 가족, 학습 알고리즘, 훈련 과정(초기화→데이터 수집→조정→반복)의 전체 흐름을 개관한다. 이 장은 이후 장에서 다룰 모든 기법의 동기와 맥락을 제공하는 로드맵 역할을 한다.

### Ch 2: Preliminaries (pp. 30-78)
**핵심**: 데이터 조작(텐서 연산), 데이터 전처리, 선형대수, 미적분, 자동 미분, 확률과 통계의 기초를 다룬다. PyTorch를 사용한 실습 코드와 함께 딥러닝에 필요한 수학적 도구를 제공한다.
**키워드**: `tensor operations`, `autograd`, `probability`, `linear algebra`, `calculus`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 2 (line 32)
텐서(ndarray/Tensor)를 딥러닝의 기본 데이터 구조로 소개하고, PyTorch에서 생성, 인덱싱, 슬라이싱, 형상 변환, 원소별 연산, 브로드캐스팅을 실습 코드와 함께 설명한다. pandas를 사용한 데이터 전처리(결측값 처리, 범주형 변수 인코딩, 텐서 변환)의 기본 워크플로를 다룬다. 선형대수의 핵심 개념으로 스칼라, 벡터, 행렬, 텐서의 정의와 기본 연산, 노름(L1, L2, 프로베니우스), 행렬-벡터/행렬-행렬 곱셈을 코드로 구현한다. 미적분의 기초로 도함수, 편미분, 기울기, 체인 규칙을 설명하고, 딥러닝에서 기울기가 손실 함수를 최소화하는 방향을 결정하는 역할을 강조한다. 자동 미분(autograd)의 원리를 설명하고, PyTorch의 backward() 메서드를 통해 역전파를 자동화하는 방법을 실습한다. 계산 그래프의 구성과 기울기 누적, detach()를 통한 그래프 분리, 제어 흐름이 있는 함수의 미분 처리를 다룬다. 확률론의 기초로 확률 변수, 확률 분포, 기대값, 분산, 조건부 확률, 베이즈 정리를 설명하고 시뮬레이션으로 검증한다. 정보 이론의 핵심 개념인 엔트로피, 상호 정보량, KL 발산, 교차 엔트로피를 정의하고, 손실 함수 설계에서의 역할을 설명한다. API 문서를 활용하여 모듈의 함수, 클래스, 매개변수를 탐색하는 방법을 안내한다. 이 장은 이후 모든 장에서 반복적으로 사용되는 수학적 도구와 프로그래밍 기법의 기초를 제공한다.

### Ch 3: Linear Neural Networks for Regression (pp. 82-124)
**핵심**: 선형 회귀를 신경망 관점에서 재해석한다. 손실 함수, 최적화 알고리즘을 처음부터 구현하고, 프레임워크의 간결한 구현과 비교한다. 일반화, 가중치 감쇠(weight decay)를 다룬다.
**키워드**: `linear regression`, `loss function`, `weight decay`, `generalization`, `from scratch`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 3 (line 198)
선형 회귀를 단일 층 신경망으로 재해석하고, 가중치와 편향을 매개변수로 하는 아핀 변환 ŷ = Xw + b를 정의한다. 손실 함수로 평균 제곱 오차(MSE)를 도입하고, 정규 방정식을 통한 해석적 해와 확률적 해석(조건부 가우시안으로의 최대우도추정)을 비교한다. 미니배치 SGD의 알고리즘을 유도하고, 학습률과 배치 크기의 선택이 학습에 미치는 영향을 논의한다. 객체지향 설계 원칙에 따라 Module, DataModule, Trainer 클래스를 정의하여 재사용 가능한 학습 프레임워크를 구축한다. 선형 회귀를 처음부터(from scratch) 구현하고, 합성 데이터에서 학습하여 실제 매개변수와 학습된 매개변수를 비교 검증한다. PyTorch의 nn.Linear와 옵티마이저를 사용한 간결한 구현을 from-scratch 버전과 대비하여 프레임워크의 편의성을 보여준다. 일반화 이론의 기초로 훈련 오차와 일반화 오차의 차이, 과적합/과소적합, 모델 복잡도와 데이터 양의 관계를 설명한다. VC 차원과 래드마허 복잡도를 통한 일반화 한계의 이론적 분석을 소개하지만, 딥러닝에서는 이론과 실무의 괴리가 있음을 인정한다. 가중치 감쇠(L2 정규화)의 원리를 수학적으로 유도하고, from-scratch 및 간결한 구현을 통해 정규화 효과를 실험적으로 확인한다. 학습 과정의 시각화(학습 곡선 플롯)를 통해 과적합 진단과 하이퍼파라미터 조정의 실무를 다룬다.

### Ch 4: Linear Neural Networks for Classification (pp. 125-166)
**핵심**: 소프트맥스 회귀를 분류 문제의 기본 모델로 소개한다. 교차 엔트로피 손실, 정보 이론 기초를 설명한다. 환경 및 분포 변화(distribution shift) 문제와 공정성 이슈를 논의한다.
**키워드**: `softmax regression`, `cross-entropy`, `distribution shift`, `classification`, `fairness`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 4 (line 358)
분류 문제에서 원-핫 인코딩으로 레이블을 표현하고, 소프트맥스 함수를 통해 로짓을 확률 분포로 변환하는 소프트맥스 회귀를 정의한다. 교차 엔트로피 손실을 정보 이론의 관점에서 유도하고, 이것이 참 분포와 모델 분포 간의 KL 발산 최소화와 동치임을 보인다. 소프트맥스의 수치 안정화를 위해 로짓에서 최댓값을 빼는 기법과 LogSumExp 트릭을 설명한다. Fashion-MNIST 데이터셋을 소개하고, DataLoader를 통한 미니배치 로딩과 이미지 시각화 유틸리티를 구현한다. 소프트맥스 회귀를 처음부터 구현하고, PyTorch의 nn.CrossEntropyLoss를 사용한 간결한 구현과 비교한다. 분류에서의 일반화를 논의하며, 훈련 오차와 테스트 오차의 관계, 경험적 오차 최소화의 한계를 설명한다. 분포 변화(distribution shift) 문제로 공변량 변화(covariate shift), 레이블 변화, 개념 변화를 구분하고 각각의 보정 방법을 제시한다. 비정상성(non-stationarity) 환경에서 모델이 시간에 따라 적응해야 하는 필요성을 논의한다. 머신러닝의 공정성 문제를 제기하며, 편향된 데이터가 차별적 예측으로 이어질 수 있음을 경고한다. 실무에서 분포 변화 탐지와 대응 전략(중요도 가중, 도메인 적응)의 기본 원리를 소개한다.

### Ch 5: Multilayer Perceptrons (pp. 167-205)
**핵심**: 은닉 층과 활성화 함수(ReLU, sigmoid, tanh)를 통해 비선형성을 도입한다. 순전파/역전파의 계산 그래프를 설명하고, 수치 안정성, 초기화 전략, 드롭아웃을 다룬다. Kaggle 주택 가격 예측 실습을 포함한다.
**키워드**: `activation functions`, `backpropagation`, `dropout`, `numerical stability`, `Kaggle`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 5 (line 561)
은닉 층과 활성화 함수를 도입하여 선형 모델의 한계를 극복하는 다층 퍼셉트론(MLP)의 구조를 설명한다. 활성화 함수로 ReLU, 시그모이드, tanh의 그래프, 도함수, 장단점을 비교하며, ReLU가 기울기 소실 완화에 유리함을 보인다. 범용 근사 정리를 소개하고, 단일 은닉 층 MLP가 이론적으로 임의의 연속 함수를 근사할 수 있지만 실용적 한계가 있음을 논의한다. 순전파(forward propagation)를 계산 그래프로 표현하고, 역전파(backpropagation)가 체인 규칙을 통해 기울기를 효율적으로 계산하는 과정을 수학적으로 유도한다. 수치 안정성 문제로 기울기 소실과 기울기 폭발을 설명하고, 초기화 전략(Xavier, He)이 분산을 유지하는 원리를 분석한다. 대칭성 깨뜨리기(symmetry breaking)를 위해 가중치를 무작위로 초기화해야 하는 이유를 설명한다. 딥러닝에서의 일반화를 고전 이론과 대비하며, 과매개변수화(overparameterization)에도 좋은 일반화가 가능한 현상을 논의한다. 드롭아웃의 원리를 확률적 정규화 기법으로 설명하고, 훈련 시 뉴런을 무작위 탈락시키되 추론 시에는 전체 네트워크를 사용하는 방식을 구현한다. MLP를 처음부터 구현하고 PyTorch의 nn.Sequential로 간결하게 재구현하여 비교한다. Kaggle 주택 가격 예측 경진대회를 사례로 데이터 전처리, 모델 설계, k-폴드 교차 검증, 제출까지의 전체 파이프라인을 실습한다.

### Ch 6: Builders' Guide (pp. 206-231)
**핵심**: PyTorch에서 모델을 구성하는 실무적 기법을 다룬다. 커스텀 모듈, 매개변수 관리(접근, 초기화, 공유), 지연 초기화, 커스텀 레이어, 파일 I/O, GPU 활용법을 설명한다.
**키워드**: `custom layers`, `parameter management`, `GPU`, `model serialization`, `lazy initialization`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 6 (line 717)
PyTorch의 nn.Module을 상속하여 커스텀 모델 블록을 구성하는 객체지향 설계 패턴을 체계적으로 설명한다. nn.Sequential을 사용한 레이어 순차 구성과, forward 메서드를 오버라이드한 유연한 모델 설계를 비교한다. 매개변수 관리(접근, 초기화, 공유)의 세부 기법을 다루며, named_parameters()와 state_dict()를 통한 매개변수 탐색을 실습한다. 다양한 초기화 전략(정규 분포, 균일 분포, Xavier, 상수, 커스텀 초기화)의 구현과 적용 방법을 보여준다. 매개변수 공유(tied weights)를 통해 여러 층이 동일한 가중치를 사용하도록 설정하고, 기울기 누적 효과를 확인한다. 지연 초기화(lazy initialization)의 개념을 소개하며, 입력 크기를 미리 지정하지 않고도 첫 순전파 시 자동으로 매개변수를 결정하는 메커니즘을 설명한다. 매개변수를 갖지 않는 커스텀 레이어와 매개변수를 갖는 커스텀 레이어를 각각 구현하는 방법을 보여준다. 모델의 저장과 로드를 위한 torch.save/torch.load와 state_dict 기반 직렬화를 실습한다. GPU 디바이스 관리(CPU/GPU 간 텐서 이동, 모델의 GPU 배치)와 다중 GPU 환경에서의 기본 사용법을 설명한다. 이 장은 이후 복잡한 아키텍처를 구현하기 위한 실무적 빌딩 블록을 제공한다.

### Ch 7: Convolutional Neural Networks (pp. 233-266)
**핵심**: 완전연결층에서 합성곱으로의 전환을 불변성과 지역성 관점에서 동기화한다. 교차상관 연산, 패딩/스트라이드, 다중 입출력 채널, 풀링을 설명한다. LeNet을 구현하여 이미지 분류를 수행한다.
**키워드**: `convolution`, `padding`, `stride`, `pooling`, `LeNet`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 7 (line 799)
완전연결 층에서 합성곱 층으로의 전환을 이동 불변성(translation invariance)과 지역성(locality)의 두 원칙으로 동기화한다. 교차상관(cross-correlation) 연산을 수학적으로 정의하고, 2차원 입력과 커널에 대해 출력 특징 맵을 계산하는 과정을 코드로 구현한다. 합성곱 층의 매개변수(커널 가중치, 편향)가 역전파를 통해 학습되는 과정을 에지 검출 예제로 시연한다. 패딩을 통해 출력 크기를 조절하고, 스트라이드를 통해 출력 해상도를 줄이는 방법을 설명하며, 출력 크기 공식을 유도한다. 다중 입력 채널에서 각 채널에 대응하는 커널로 합성곱을 수행한 후 합산하고, 다중 출력 채널은 출력 채널 수만큼의 커널 집합을 사용한다. 1x1 합성곱이 채널 간의 선형 조합을 수행하여 채널 차원에서의 정보 혼합 역할을 함을 설명한다. 풀링(최대 풀링, 평균 풀링)의 목적을 입력의 작은 이동에 대한 불변성 확보와 공간 해상도 감소로 설명하고 구현한다. 풀링에서도 패딩과 스트라이드를 적용할 수 있으며, 다중 채널 입력에 대해 각 채널 독립적으로 풀링이 수행됨을 보인다. LeNet-5 아키텍처를 구현하여 합성곱-풀링-완전연결의 기본 CNN 패턴을 보여주고, Fashion-MNIST에서 학습한다. 이 장은 CNN의 기본 구성 요소를 원리부터 구현까지 체계적으로 다루어, 이후 현대적 아키텍처의 이해를 위한 토대를 마련한다.

### Ch 8: Modern Convolutional Neural Networks (pp. 268-324)
**핵심**: AlexNet, VGG, NiN, GoogLeNet(Inception), 배치 정규화, ResNet/ResNeXt, DenseNet을 순서대로 소개한다. 각 아키텍처의 핵심 아이디어와 설계 원리를 코드와 함께 설명한다. RegNet을 통한 설계 공간 탐색도 다룬다.
**키워드**: `AlexNet`, `VGG`, `ResNet`, `batch normalization`, `DenseNet`, `GoogLeNet`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 8 (line 938)
AlexNet이 2012년 ImageNet에서 심층 CNN의 우수성을 입증한 과정을 설명하고, ReLU 활용, 드롭아웃, 데이터 증강 등 핵심 설계 결정을 분석한다. VGG는 3x3 합성곱의 반복 적층과 2x2 풀링으로 구성되는 "블록" 설계를 도입하여 아키텍처의 체계적 확장을 가능하게 하였다. NiN(Network in Network)은 1x1 합성곱으로 채널 간 비선형 혼합을 수행하고, 전역 평균 풀링으로 완전연결 층을 대체하여 과적합을 줄인다. GoogLeNet의 Inception 모듈은 다양한 커널 크기(1x1, 3x3, 5x5)와 풀링을 병렬로 수행한 후 채널 방향으로 연결하여 다중 스케일 특징을 동시에 추출한다. 배치 정규화(batch normalization)는 각 미니배치에서 층의 입력을 정규화하여 학습을 안정화하고 가속하며, 학습 가능한 스케일/시프트 매개변수를 포함한다. ResNet의 잔차 연결(skip connection)은 기울기 소실 없이 수백 층까지 학습 가능하게 하며, 항등 매핑이 기본이 되어 층이 잔차만 학습하도록 설계된다. ResNeXt는 그룹 합성곱을 통해 병렬 경로를 도입하여 ResNet을 확장하고, 카디널리티(cardinality) 개념을 제시한다. DenseNet은 모든 이전 층의 출력을 채널 방향으로 연결하여 특징 재사용을 극대화하며, 전이 층으로 채널 수를 조절한다. RegNet은 설계 공간(design space) 접근법으로 너비, 깊이, 그룹 수의 관계를 체계적으로 탐색하여 최적 아키텍처를 도출한다. 각 아키텍처의 핵심 아이디어를 코드와 함께 구현하고 Fashion-MNIST 또는 축소된 ImageNet에서 학습하여 성능을 비교한다.

### Ch 9: Recurrent Neural Networks (pp. 325-368)
**핵심**: 시퀀스 데이터의 자기회귀 모델링을 소개한다. 텍스트 전처리, 언어 모델, 퍼플렉시티를 설명한다. RNN의 구조를 정의하고, 처음부터 구현한 후 프레임워크 구현과 비교한다. BPTT의 기울기 분석을 제공한다.
**키워드**: `RNN`, `language model`, `perplexity`, `BPTT`, `gradient clipping`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 9 (line 1162)
시퀀스 데이터의 통계적 구조를 자기회귀(autoregressive) 모델로 포착하는 방법을 소개하고, 고정 길이 입력 모델과 잠재 자기회귀 모델을 비교한다. 텍스트 전처리 파이프라인(토큰화, 어휘 사전 구축, 코퍼스의 토큰-인덱스 변환)을 H.G. Wells의 "The Time Machine"을 데이터로 구현한다. 언어 모델링을 n-그램 관점에서 설명하고, 라플라스 스무딩과 Zipf 법칙(단어 빈도의 멱법칙 분포)을 분석한다. 퍼플렉시티(perplexity)를 언어 모델의 평가 지표로 정의하고, 교차 엔트로피 손실과의 관계를 유도한다. RNN의 은닉 상태가 시간 단계 간 정보를 전달하는 구조를 정의하고, 매개변수 공유의 이점을 설명한다. RNN을 처음부터 구현하면서 원-핫 인코딩, 은닉 상태 초기화, 순전파, 문자 단위 텍스트 생성을 단계별로 진행한다. 기울기 클리핑(gradient clipping)의 필요성을 기울기 폭발 문제의 관점에서 설명하고, 전역 노름 기반 클리핑을 구현한다. 훈련 루프에서 시퀀스 분할 전략(무작위 분할 vs 순차 분할)이 은닉 상태 초기화에 미치는 영향을 비교한다. PyTorch의 nn.RNN을 사용한 간결한 구현을 from-scratch 버전과 대비하여 보여준다. 시간을 통한 역전파(BPTT)의 기울기 계산을 수학적으로 분석하고, 잘림(truncation), 무작위화, 전체 계산 간의 트레이드오프를 논의한다.

### Ch 10: Modern Recurrent Neural Networks (pp. 369-408)
**핵심**: LSTM과 GRU의 게이트 메커니즘을 상세히 설명한다. 깊은 RNN, 양방향 RNN을 다루고, 기계 번역 데이터셋을 준비한다. 인코더-디코더 아키텍처와 시퀀스-투-시퀀스 학습, 빔 서치를 구현한다.
**키워드**: `LSTM`, `GRU`, `encoder-decoder`, `seq2seq`, `beam search`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 10 (line 1317)
LSTM의 셀 상태, 입력 게이트, 망각 게이트, 출력 게이트의 수학적 정의와 기울기 흐름 개선 메커니즘을 상세히 설명하고 from-scratch 구현을 제공한다. GRU는 리셋 게이트와 업데이트 게이트만으로 LSTM과 유사한 성능을 달성하는 단순화된 게이트 메커니즘으로, 계산 효율이 높다. 깊은 RNN은 은닉 상태를 여러 층으로 쌓아 시퀀스 데이터의 더 복잡한 패턴을 포착하며, 층 간 은닉 상태 전달 방식을 설명한다. 양방향 RNN은 순방향과 역방향 은닉 상태를 결합하여 과거와 미래 양쪽 문맥을 활용하지만, 미래 토큰 예측에는 부적합함을 경고한다. 기계 번역 과제를 위한 영어-프랑스어 데이터셋의 전처리(토큰화, 어휘 구축, 시퀀스 패딩/잘림)를 구현한다. 인코더-디코더 아키텍처의 추상적 설계를 정의하고, 인코더가 가변 길이 입력을 고정 크기 상태로 변환하는 역할을 설명한다. 시퀀스-투-시퀀스(seq2seq) 모델을 GRU 기반으로 구현하고, 교사 강제(teacher forcing) 훈련 전략을 적용한다. 디코딩 시 <bos> 토큰에서 시작하여 <eos> 토큰이 나올 때까지 자기회귀적으로 예측하는 추론 과정을 구현한다. BLEU 점수를 번역 품질 평가 지표로 정의하고, n-그램 정밀도와 간결함 패널티의 계산을 상세히 유도한다. 빔 서치(beam search)를 탐욕적 탐색과 완전 탐색의 중간 전략으로 소개하고, 빔 크기에 따른 품질-비용 트레이드오프를 분석한다.

### Ch 11: Attention Mechanisms and Transformers (pp. 409-467)
**핵심**: 쿼리-키-값 프레임워크로 어텐션을 정의한다. 스케일드 닷 프로덕트 어텐션, Bahdanau 어텐션, 멀티헤드 어텐션, 셀프 어텐션과 위치 인코딩을 설명한다. 트랜스포머 아키텍처를 완전히 구현하고, Vision Transformer와 대규모 사전학습(BERT, GPT, T5)을 개관한다.
**키워드**: `transformer`, `self-attention`, `multi-head attention`, `positional encoding`, `ViT`, `BERT`, `GPT`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 11 (line 1489)
어텐션 메커니즘을 쿼리(query), 키(key), 값(value) 프레임워크로 정의하고, 나다라야-왓슨 커널 회귀를 통해 어텐션 풀링의 직관적 기초를 설명한다. 어텐션 점수 함수로 가산(additive) 어텐션과 스케일드 닷 프로덕트 어텐션을 유도하고, 후자가 행렬 연산으로 효율적임을 보인다. Bahdanau 어텐션은 seq2seq 모델에서 디코더가 인코더의 모든 시간 단계 출력에 동적으로 가중치를 부여하여 고정 문맥 벡터의 병목을 해소한다. 멀티헤드 어텐션은 서로 다른 선형 투영을 통해 여러 표현 부분공간에서 병렬로 어텐션을 수행하고 결합한다. 셀프 어텐션은 시퀀스의 각 위치가 같은 시퀀스의 다른 모든 위치에 직접 주의를 기울이며, CNN/RNN과 계산 복잡도, 최대 경로 길이를 비교한다. 위치 인코딩은 시퀀스의 순서 정보를 사인/코사인 함수로 인코딩하여 순서 불변인 셀프 어텐션에 위치 정보를 주입한다. 트랜스포머 아키텍처를 인코더(셀프 어텐션 + FFN)와 디코더(마스크드 셀프 어텐션 + 교차 어텐션 + FFN)의 블록 구조로 완전히 구현한다. 잔차 연결과 층 정규화(LayerNorm)가 깊은 트랜스포머의 학습 안정성에 기여하는 역할을 설명한다. Vision Transformer(ViT)가 이미지를 패치 시퀀스로 처리하여 CNN 없이도 시각 태스크에 적용 가능함을 보인다. 대규모 사전학습 모델(BERT, GPT, T5)이 트랜스포머를 기반으로 인코더 전용, 디코더 전용, 인코더-디코더 구조로 발전한 흐름을 개관한다.

### Ch 12: Optimization Algorithms (pp. 468-545)
**핵심**: 최적화와 딥러닝의 관계, 볼록성의 개념을 설명한다. 경사 하강법부터 SGD, 미니배치 SGD, 모멘텀, Adagrad, RMSProp, Adadelta, Adam까지 순서대로 알고리즘을 유도하고 구현한다. 학습률 스케줄링 전략을 다룬다.
**키워드**: `SGD`, `Adam`, `momentum`, `learning rate scheduling`, `convexity`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 12 (line 1672)
최적화와 딥러닝의 관계를 명확히 하고, 딥러닝의 목표가 훈련 손실 최소화가 아니라 일반화 오차 최소화임을 강조한다. 볼록 집합, 볼록 함수, 볼록 제약의 정의를 소개하고, 볼록 최적화에서 지역 최솟값이 전역 최솟값과 동치이지만 딥러닝은 비볼록임을 설명한다. 경사 하강법의 기본 알고리즘을 1차원과 다차원에 대해 유도하고, 학습률 선택의 중요성을 시각적으로 시연한다. 뉴턴 법이 헤시안 정보를 활용하여 이차 수렴을 달성하지만, 비볼록 문제에서 안장점으로 수렴할 위험이 있음을 경고한다. SGD가 미니배치 기울기의 확률적 근사를 사용하여 전체 기울기 계산을 회피하는 원리와, 학습률의 동적 감소 전략을 설명한다. 미니배치 SGD의 배치 크기 선택이 계산 효율(GPU 병렬화)과 통계적 효율(분산 감소)에 미치는 영향을 분석한다. 모멘텀은 과거 기울기의 지수 가중 이동 평균으로 갱신 방향을 안정화하고, 안장점 주변에서의 탈출을 돕는다. Adagrad는 매개변수별로 누적 기울기 제곱합의 역수로 학습률을 조정하며, 희소 특징에 유리하지만 학습률이 조기 감소하는 문제가 있다. RMSProp과 Adadelta는 Adagrad의 학습률 감소 문제를 지수 이동 평균으로 해결하고, Adam은 모멘텀과 RMSProp을 결합하며 편향 보정을 추가한다. 학습률 스케줄링 전략으로 코사인 어닐링, 워밍업, 다항식/계단형 감쇠를 비교하고 구현한다.

### Ch 13: Computational Performance (pp. 547-591)
**핵심**: 컴파일러/인터프리터 패러다임, 비동기 계산, 자동 병렬화를 설명한다. CPU/GPU/네트워크 하드웨어 특성을 분석하고, 다중 GPU 학습(데이터 병렬화)과 파라미터 서버 아키텍처를 구현한다.
**키워드**: `GPU`, `data parallelism`, `parameter server`, `asynchronous computation`, `hardware`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 13 (line 1923)
컴파일러(기호적 프로그래밍)와 인터프리터(명령형 프로그래밍) 패러다임을 비교하고, 하이브리드 프로그래밍(torch.jit)을 통한 최적화를 설명한다. 비동기 계산의 원리를 GPU의 비차단(non-blocking) 연산과 프론트엔드-백엔드 분리 관점에서 분석하고, 동기화 지점의 배치를 논의한다. 자동 병렬화가 CPU-GPU 간 및 GPU 내의 독립 연산을 동시에 실행하여 처리량을 높이는 메커니즘을 실험으로 확인한다. 컴퓨터 하드웨어(CPU, GPU, 메모리 계층, 버스)의 특성이 딥러닝 연산의 병목에 미치는 영향을 체계적으로 분석한다. 메모리 대역폭, 캐시 계층, SIMD/텐서 코어 등 하드웨어 구조가 연산 효율에 결정적임을 설명한다. 다중 GPU 학습을 위한 데이터 병렬화의 원리를 설명하고, 기울기 올리듀스(AllReduce)와 링 올리듀스(ring AllReduce)를 비교한다. 단일 머신에서 from-scratch 데이터 병렬 학습을 구현하고, 각 GPU에 미니배치를 분할하여 기울기를 합산하는 과정을 보여준다. PyTorch의 nn.DataParallel을 사용한 간결한 다중 GPU 구현을 제공한다. 파라미터 서버 아키텍처를 통한 분산 학습에서 키-값 저장소, 동기화 전략, 통신 비용 최적화를 다룬다. 데이터 전처리와 네트워크 통신의 파이프라이닝을 통해 학습 처리량을 극대화하는 전략을 논의한다.

### Ch 14: Computer Vision (pp. 592-688)
**핵심**: 이미지 증강, 파인튜닝, 객체 검출(앵커 박스, SSD, R-CNN), 의미적 분할(FCN), 전치 합성곱, 신경 스타일 전이를 다룬다. Kaggle CIFAR-10, ImageNet Dogs 실습을 포함한다.
**키워드**: `fine-tuning`, `object detection`, `SSD`, `R-CNN`, `semantic segmentation`, `style transfer`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 14 (line 2086)
이미지 증강(뒤집기, 자르기, 색상 변환)을 통해 훈련 데이터의 다양성을 확대하고, 각 변환이 모델의 불변성 학습에 기여하는 원리를 설명한다. 파인튜닝(fine-tuning)의 원리로 사전학습된 모델의 특징 추출기를 재사용하고 출력 층만 새로 학습하거나, 전체 네트워크를 작은 학습률로 미세조정하는 전략을 비교한다. 객체 검출의 기본 개념(바운딩 박스, IoU, 앵커 박스)을 정의하고, 앵커 박스 생성과 비최대 억제(NMS)를 구현한다. 다중 스케일 객체 검출의 필요성을 설명하고, 특징 피라미드에서 서로 다른 크기의 앵커를 할당하는 방법을 다룬다. SSD(Single Shot Multibox Detection)의 다중 스케일 특징 맵, 클래스 예측, 바운딩 박스 예측을 완전히 구현하고 학습한다. R-CNN 계열(R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN)의 발전 과정을 영역 제안(region proposal) 메커니즘의 진화 관점에서 추적한다. 의미적 분할(semantic segmentation)을 위한 Pascal VOC 데이터셋 처리와 픽셀 단위 레이블링을 구현한다. 전치 합성곱(transposed convolution)의 수학적 정의와 업샘플링 역할을 설명하고, FCN(Fully Convolutional Network)을 구현하여 의미적 분할을 수행한다. 신경 스타일 전이(neural style transfer)를 콘텐츠 손실과 스타일 손실(그람 행렬)의 최적화로 구현한다. Kaggle 경진대회(CIFAR-10 분류, ImageNet Dogs 품종 분류)를 통해 전체 학습 파이프라인을 실습한다.

### Ch 15: Natural Language Processing: Pretraining (pp. 690-743)
**핵심**: Word2vec(Skip-gram, CBOW), GloVe, 서브워드 임베딩(BPE, fastText)을 설명한다. 단어 유사도와 비유 과제를 수행하고, BERT의 사전학습(MLM, NSP) 과정을 구현한다.
**키워드**: `word2vec`, `GloVe`, `BPE`, `BERT`, `pretraining`, `masked language model`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 15 (line 2397)
Word2vec의 두 모델인 Skip-gram(중심 단어로 문맥 예측)과 CBOW(문맥으로 중심 단어 예측)의 확률 모델을 수학적으로 정의한다. 근사 훈련 방법으로 네거티브 샘플링(negative sampling)과 계층적 소프트맥스(hierarchical softmax)를 소개하고, 전자가 실용적으로 더 널리 사용됨을 설명한다. 사전학습용 데이터셋 구축 과정(서브샘플링, 중심-문맥 쌍 추출, 네거티브 샘플 생성)을 PTB 코퍼스를 사용하여 단계별로 구현한다. Word2vec 모델을 처음부터 구현하고 학습하여, 의미적으로 유사한 단어가 벡터 공간에서 가까이 위치함을 확인한다. GloVe가 전역 동시출현(co-occurrence) 통계를 활용하여 Word2vec의 지역적 학습과 행렬 인수분해를 통합하는 원리를 설명한다. 서브워드 임베딩으로 BPE(Byte Pair Encoding)와 fastText의 문자 n-그램 접근법을 소개하고, 미등록어(OOV) 처리의 이점을 논의한다. 사전학습된 임베딩을 로드하여 단어 유사도(코사인 유사도)와 단어 비유(word analogy) 과제를 수행한다. BERT의 아키텍처(양방향 트랜스포머 인코더)와 두 사전학습 과제인 마스크드 언어 모델(MLM)과 다음 문장 예측(NSP)을 상세히 설명한다. BERT 사전학습용 데이터셋을 WikiText-2에서 구축하고, MLM과 NSP 인스턴스 생성 과정을 구현한다. BERT 사전학습의 전체 파이프라인(데이터 로딩, 모델 정의, 훈련 루프)을 구현하여 소규모 데이터에서 학습한다.

### Ch 16: Natural Language Processing: Applications (pp. 744-779)
**핵심**: 감정 분석(RNN, CNN 기반), 자연어 추론(SNLI 데이터셋, 어텐션 모델), BERT 파인튜닝을 다룬다. 시퀀스 수준/토큰 수준 분류, 질문 응답 등 다양한 NLP 태스크에 BERT를 적용한다.
**키워드**: `sentiment analysis`, `NLI`, `BERT fine-tuning`, `question answering`, `textCNN`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 16 (line 2590)
감정 분석(sentiment analysis)을 위한 대규모 영화 리뷰 데이터셋(IMDb)의 전처리와 데이터 로더 구축을 구현한다. RNN 기반 감정 분석 모델을 양방향 LSTM으로 구현하고, 사전학습된 GloVe 임베딩을 초기화에 활용한다. 1차원 합성곱(textCNN)을 사용한 감정 분석 모델은 다양한 커널 크기로 n-그램 패턴을 포착하고, 전역 최대 풀링으로 가변 길이 입력을 처리한다. 자연어 추론(NLI) 과제를 SNLI 데이터셋으로 정의하고, 전제-가설 쌍의 함의/모순/중립 관계를 분류하는 문제를 설정한다. 어텐션 기반 NLI 모델(분해 가능 어텐션 모델)을 attend-compare-aggregate 구조로 구현하고, 교차 어텐션으로 전제와 가설을 정렬한다. BERT의 파인튜닝을 시퀀스 수준 태스크(단일 텍스트 분류, 텍스트 쌍 분류)와 토큰 수준 태스크(텍스트 태깅)에 적용하는 방법을 설명한다. BERT를 감정 분석에 파인튜닝할 때 [CLS] 토큰의 표현을 분류기 입력으로 사용하고, 전체 매개변수를 미세조정하는 과정을 구현한다. BERT를 자연어 추론에 파인튜닝할 때 전제와 가설을 [SEP]로 연결하여 입력하고, [CLS] 표현으로 3-클래스 분류를 수행한다. 질문 응답(question answering)에서 BERT의 토큰 수준 출력으로 답변의 시작/끝 위치를 예측하는 방식을 소개한다. 사전학습-파인튜닝 패러다임이 다양한 NLP 태스크에 걸쳐 통일된 접근법을 제공함을 종합적으로 논의한다.

### Ch 17: Reinforcement Learning (pp. 781-796)
**핵심**: MDP 정의, 할인 수익, 가치 함수를 소개한다. 가치 반복(value iteration)과 Q-learning 알고리즘을 유도하고, 탐색-활용 트레이드오프와 자기 교정 특성을 설명한다.
**키워드**: `MDP`, `value iteration`, `Q-learning`, `exploration`, `discount factor`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 17 (line 2739)
마르코프 결정 과정(MDP)을 상태 집합, 행동 집합, 전이 확률, 보상 함수의 네 요소로 형식적으로 정의한다. 할인 수익(discounted return)의 개념을 도입하고, 할인 인자 γ가 즉각적 보상과 미래 보상 간의 트레이드오프를 조절하는 역할을 설명한다. 마르코프 가정(미래 상태가 현재 상태에만 의존)의 의미와 한계를 논의하고, 실제 문제에서의 적용 가능성을 분석한다. 확률적 정책(stochastic policy) π(a|s)와 결정적 정책을 구분하고, 정책이 에이전트의 행동 전략을 정의함을 설명한다. 상태 가치 함수 V^π(s)와 행동 가치 함수 Q^π(s,a)를 정의하고, 벨만 방정식을 통한 재귀적 관계를 유도한다. 동적 프로그래밍의 원리를 적용하여 최적 가치 함수와 최적 정책을 벨만 최적성 방정식으로 특성화한다. 가치 반복(value iteration) 알고리즘을 유도하고, FrozenLake 환경에서 구현하여 최적 정책을 계산한다. Q-learning은 모델 프리(model-free) 알고리즘으로, 전이 확률을 모르는 상황에서 Q 함수를 샘플 기반으로 학습한다. ε-탐욕 전략을 통한 탐색-활용(exploration-exploitation) 트레이드오프와, Q-learning의 자기 교정(self-correcting) 특성을 설명한다. CliffWalking 환경에서 Q-learning을 구현하고, 학습된 정책의 수렴 과정을 시각화한다.

### Ch 18: Gaussian Processes (pp. 797-826)
**핵심**: 가우시안 프로세스(GP)의 직관적 도입부터 GP 사전(RBF 커널, 신경망 커널), GP 사후 추론(회귀)까지 다룬다. 커널 하이퍼파라미터 학습과 GPyTorch를 사용한 실습을 포함한다.
**키워드**: `Gaussian process`, `RBF kernel`, `posterior inference`, `GPyTorch`, `kernel hyperparameters`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 18 (line 2843)
가우시안 프로세스(GP)를 직관적으로 소개하며, 유한한 점 집합에서의 함수 값이 다변량 가우시안 분포를 따르는 함수 공간의 분포로 정의한다. GP 사전(prior)을 평균 함수와 공분산 함수(커널)로 정의하고, 커널 선택이 함수의 사전 가정(평활성, 주기성 등)을 결정함을 설명한다. 가중치 공간에서의 베이지안 선형 회귀를 함수 공간으로 변환하여 GP가 자연스럽게 도출되는 과정을 보여준다. RBF(방사 기저 함수) 커널의 정의와 길이 스케일 매개변수가 함수의 평활성을 조절하는 역할을 시각적으로 시연한다. 신경망 커널(Neal의 결과)을 통해 무한 너비 단일 은닉 층 신경망이 GP에 수렴함을 설명한다. GP 회귀에서 관측 데이터를 조건으로 한 사후 분포(posterior)를 닫힌 형태(closed-form)로 유도하고, 예측 평균과 불확실성을 계산한다. 커널 하이퍼파라미터(길이 스케일, 출력 스케일, 잡음 분산)를 주변 우도(marginal likelihood)의 최대화를 통해 학습하는 과정을 설명한다. 주변 우도가 데이터 적합도와 모델 복잡도 간의 자동 균형(automatic Occam's razor)을 제공함을 분석한다. GP 회귀를 처음부터 NumPy로 구현하고, 합성 데이터에서 사후 추론과 하이퍼파라미터 학습을 수행한다. GPyTorch 라이브러리를 사용한 간결한 GP 구현을 제공하고, 실용적 응용에서의 확장성 문제(O(n³) 계산 비용)를 논의한다.

### Ch 19: Hyperparameter Optimization (pp. 828-845)
**핵심**: HPO 문제를 정의하고, 랜덤 서치, 비동기 랜덤 서치를 구현한다. 다중 충실도 최적화(successive halving, ASHA)를 통한 효율적 탐색 전략을 설명한다.
**키워드**: `hyperparameter optimization`, `random search`, `successive halving`, `ASHA`, `multi-fidelity`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 19 (line 2937)
하이퍼파라미터 최적화(HPO) 문제를 정의하고, 하이퍼파라미터 설정 공간에서 검증 오차를 최소화하는 구성을 찾는 것이 목표임을 명확히 한다. HPO의 핵심 어려움으로 평가 비용이 높고(전체 학습 필요), 설정 공간이 복잡하며, 객관 함수의 형태를 알 수 없음을 제시한다. HPO API를 설계하여 스케줄러(탐색 전략)와 튜너(실행 관리)의 역할을 분리하고, 재사용 가능한 프레임워크를 구축한다. 랜덤 서치(random search)를 기본 HPO 방법으로 구현하고, 그리드 서치보다 저차원 중요 하이퍼파라미터 탐색에 효율적임을 설명한다. 비동기 랜덤 서치를 구현하여 병렬 워커(worker)가 독립적으로 구성을 평가하도록 하고, 유휴 시간을 줄이는 방법을 보여준다. 다중 충실도(multi-fidelity) 최적화의 원리를 소개하며, 적은 에포크로 빠르게 평가하여 유망하지 않은 구성을 조기에 제거하는 전략을 설명한다. 연속 이분법(successive halving, SH)은 균등 자원 배분 후 반복적으로 하위 절반을 탈락시키며, 자원 배분과 구성 수의 트레이드오프를 분석한다. ASHA(Asynchronous Successive Halving Algorithm)는 SH를 비동기적으로 확장하여 병렬 환경에서 효율적으로 동작하며, 승격 규칙을 통해 유망한 구성에 추가 자원을 할당한다. 각 알고리즘을 Fashion-MNIST와 2층 MLP를 사용한 실험으로 비교하고, 최적 학습률과 배치 크기를 탐색한다. HPO가 실무에서 모델 성능 개선에 필수적이며, 자동화된 탐색이 수동 조정보다 체계적이고 재현 가능함을 강조한다.

### Ch 20: Generative Adversarial Networks (pp. 853-892)
**핵심**: GAN의 기본 원리(생성기 vs 판별기)를 설명하고, 간단한 GAN을 구현한다. DCGAN을 통해 포켓몬 이미지를 생성하는 실습을 수행한다.
**키워드**: `GAN`, `DCGAN`, `generator`, `discriminator`, `adversarial training`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 20 (line 3005)
GAN의 기본 원리를 생성기(generator)와 판별기(discriminator)의 적대적 게임으로 정의하고, 미니맥스 목적 함수를 유도한다. 판별기는 실제 데이터와 생성된 데이터를 구별하도록 학습하고, 생성기는 판별기를 속이도록 학습하며, 내쉬 균형에서 생성 분포가 데이터 분포와 일치한다. 1차원 정규 분포를 목표로 하는 간단한 GAN을 구현하여, 생성기와 판별기의 교대 학습 과정을 시각적으로 확인한다. 학습의 불안정성(모드 붕괴, 기울기 소실)과 이를 완화하기 위한 실용적 기법(특징 매칭, 라벨 스무딩)을 논의한다. DCGAN(Deep Convolutional GAN)은 전치 합성곱을 사용한 생성기와 스트라이드 합성곱을 사용한 판별기로 구성되며, 배치 정규화와 LeakyReLU를 활용한다. 포켓몬 이미지 데이터셋을 준비하고 DCGAN으로 64x64 해상도의 새로운 포켓몬 이미지를 생성하는 전체 파이프라인을 구현한다. 생성기가 잠재 벡터 z에서 이미지를 생성하는 과정을 전치 합성곱의 점진적 업샘플링(4x4→8x8→...→64x64)으로 설명한다. 판별기가 이미지의 진위를 판별하는 과정을 스트라이드 합성곱의 점진적 다운샘플링으로 설명한다. 학습 과정에서 판별기와 생성기의 손실 변화를 모니터링하고, 생성된 이미지의 품질 변화를 에포크별로 관찰한다. GAN이 이미지 생성, 초해상도, 스타일 변환 등 다양한 생성 과제의 기반 기술임을 논의한다.

### Ch 21: Recommender Systems (pp. 893-895)
**핵심**: 추천 시스템의 개요를 제공한다. 협업 필터링, 명시적/암시적 피드백, 추천 태스크의 분류를 소개한다.
**키워드**: `recommender systems`, `collaborative filtering`, `implicit feedback`
**상세**: → `Dive into Deep Learning (D2L) _azure_full.md` Ch 21 (line 3092)
추천 시스템의 개요를 제공하며, 사용자에게 관련성 높은 아이템을 개인화하여 제안하는 것이 핵심 목표임을 설명한다. 협업 필터링(collaborative filtering)은 유사한 사용자나 아이템의 행동 패턴을 활용하여 추천하며, 사용자-아이템 상호작용 행렬이 기본 데이터 구조이다. 명시적 피드백(평점, 리뷰)과 암시적 피드백(클릭, 구매, 체류 시간)의 차이를 설명하고, 암시적 피드백이 더 풍부하지만 해석이 복잡함을 논의한다. 추천 태스크를 평점 예측, 탑-k 추천, 시퀀스 인식 추천 등으로 분류하고, 각 태스크의 평가 지표(RMSE, Hit Rate, NDCG)를 소개한다. 콘텐츠 기반 필터링이 아이템의 속성 정보를 활용하여 유사한 아이템을 추천하는 방식을 설명한다. 행렬 인수분해(matrix factorization)가 사용자-아이템 행렬을 저차원 잠재 요인으로 분해하여 결측 항목을 예측하는 원리를 다룬다. 추천 시스템에서의 콜드 스타트 문제(새로운 사용자/아이템에 대한 정보 부족)와 이를 완화하기 위한 하이브리드 접근법을 논의한다. 딥러닝 기반 추천(신경 협업 필터링, 오토인코더 기반 등)의 가능성과 전통적 방법과의 비교를 간략히 언급한다. 추천 시스템의 실무적 고려사항으로 확장성, 실시간 처리, 다양성-정확도 균형을 제시한다. 이 장은 추천 시스템의 기본 개념과 문제 정의를 소개하는 개관적 성격을 갖는다.
