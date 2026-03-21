---
name: "Dive into Deep Learning"
type: book-summary
source_file: "Zhang-D2L_full.md"
authors: "Aston Zhang, Zachary C. Lipton, Mu Li, Alexander J. Smola"
year: 2023
total_pages: 1089
language: en
keywords: [deep learning, PyTorch, CNN, RNN, transformer, attention, optimization, computer vision, NLP, GAN, recommender systems, Gaussian processes, hyperparameter optimization]
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
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 1 (line 3827)

### Ch 2: Preliminaries (pp. 30-78)
**핵심**: 데이터 조작(텐서 연산), 데이터 전처리, 선형대수, 미적분, 자동 미분, 확률과 통계의 기초를 다룬다. PyTorch를 사용한 실습 코드와 함께 딥러닝에 필요한 수학적 도구를 제공한다.
**키워드**: `tensor operations`, `autograd`, `probability`, `linear algebra`, `calculus`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 2 (line 32)

### Ch 3: Linear Neural Networks for Regression (pp. 82-124)
**핵심**: 선형 회귀를 신경망 관점에서 재해석한다. 손실 함수, 최적화 알고리즘을 처음부터 구현하고, 프레임워크의 간결한 구현과 비교한다. 일반화, 가중치 감쇠(weight decay)를 다룬다.
**키워드**: `linear regression`, `loss function`, `weight decay`, `generalization`, `from scratch`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 3 (line 198)

### Ch 4: Linear Neural Networks for Classification (pp. 125-166)
**핵심**: 소프트맥스 회귀를 분류 문제의 기본 모델로 소개한다. 교차 엔트로피 손실, 정보 이론 기초를 설명한다. 환경 및 분포 변화(distribution shift) 문제와 공정성 이슈를 논의한다.
**키워드**: `softmax regression`, `cross-entropy`, `distribution shift`, `classification`, `fairness`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 4 (line 358)

### Ch 5: Multilayer Perceptrons (pp. 167-205)
**핵심**: 은닉 층과 활성화 함수(ReLU, sigmoid, tanh)를 통해 비선형성을 도입한다. 순전파/역전파의 계산 그래프를 설명하고, 수치 안정성, 초기화 전략, 드롭아웃을 다룬다. Kaggle 주택 가격 예측 실습을 포함한다.
**키워드**: `activation functions`, `backpropagation`, `dropout`, `numerical stability`, `Kaggle`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 5 (line 561)

### Ch 6: Builders' Guide (pp. 206-231)
**핵심**: PyTorch에서 모델을 구성하는 실무적 기법을 다룬다. 커스텀 모듈, 매개변수 관리(접근, 초기화, 공유), 지연 초기화, 커스텀 레이어, 파일 I/O, GPU 활용법을 설명한다.
**키워드**: `custom layers`, `parameter management`, `GPU`, `model serialization`, `lazy initialization`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 6 (line 717)

### Ch 7: Convolutional Neural Networks (pp. 233-266)
**핵심**: 완전연결층에서 합성곱으로의 전환을 불변성과 지역성 관점에서 동기화한다. 교차상관 연산, 패딩/스트라이드, 다중 입출력 채널, 풀링을 설명한다. LeNet을 구현하여 이미지 분류를 수행한다.
**키워드**: `convolution`, `padding`, `stride`, `pooling`, `LeNet`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 7 (line 799)

### Ch 8: Modern Convolutional Neural Networks (pp. 268-324)
**핵심**: AlexNet, VGG, NiN, GoogLeNet(Inception), 배치 정규화, ResNet/ResNeXt, DenseNet을 순서대로 소개한다. 각 아키텍처의 핵심 아이디어와 설계 원리를 코드와 함께 설명한다. RegNet을 통한 설계 공간 탐색도 다룬다.
**키워드**: `AlexNet`, `VGG`, `ResNet`, `batch normalization`, `DenseNet`, `GoogLeNet`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 8 (line 938)

### Ch 9: Recurrent Neural Networks (pp. 325-368)
**핵심**: 시퀀스 데이터의 자기회귀 모델링을 소개한다. 텍스트 전처리, 언어 모델, 퍼플렉시티를 설명한다. RNN의 구조를 정의하고, 처음부터 구현한 후 프레임워크 구현과 비교한다. BPTT의 기울기 분석을 제공한다.
**키워드**: `RNN`, `language model`, `perplexity`, `BPTT`, `gradient clipping`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 9 (line 1162)

### Ch 10: Modern Recurrent Neural Networks (pp. 369-408)
**핵심**: LSTM과 GRU의 게이트 메커니즘을 상세히 설명한다. 깊은 RNN, 양방향 RNN을 다루고, 기계 번역 데이터셋을 준비한다. 인코더-디코더 아키텍처와 시퀀스-투-시퀀스 학습, 빔 서치를 구현한다.
**키워드**: `LSTM`, `GRU`, `encoder-decoder`, `seq2seq`, `beam search`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 10 (line 1317)

### Ch 11: Attention Mechanisms and Transformers (pp. 409-467)
**핵심**: 쿼리-키-값 프레임워크로 어텐션을 정의한다. 스케일드 닷 프로덕트 어텐션, Bahdanau 어텐션, 멀티헤드 어텐션, 셀프 어텐션과 위치 인코딩을 설명한다. 트랜스포머 아키텍처를 완전히 구현하고, Vision Transformer와 대규모 사전학습(BERT, GPT, T5)을 개관한다.
**키워드**: `transformer`, `self-attention`, `multi-head attention`, `positional encoding`, `ViT`, `BERT`, `GPT`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 11 (line 1489)

### Ch 12: Optimization Algorithms (pp. 468-545)
**핵심**: 최적화와 딥러닝의 관계, 볼록성의 개념을 설명한다. 경사 하강법부터 SGD, 미니배치 SGD, 모멘텀, Adagrad, RMSProp, Adadelta, Adam까지 순서대로 알고리즘을 유도하고 구현한다. 학습률 스케줄링 전략을 다룬다.
**키워드**: `SGD`, `Adam`, `momentum`, `learning rate scheduling`, `convexity`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 12 (line 1672)

### Ch 13: Computational Performance (pp. 547-591)
**핵심**: 컴파일러/인터프리터 패러다임, 비동기 계산, 자동 병렬화를 설명한다. CPU/GPU/네트워크 하드웨어 특성을 분석하고, 다중 GPU 학습(데이터 병렬화)과 파라미터 서버 아키텍처를 구현한다.
**키워드**: `GPU`, `data parallelism`, `parameter server`, `asynchronous computation`, `hardware`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 13 (line 1923)

### Ch 14: Computer Vision (pp. 592-688)
**핵심**: 이미지 증강, 파인튜닝, 객체 검출(앵커 박스, SSD, R-CNN), 의미적 분할(FCN), 전치 합성곱, 신경 스타일 전이를 다룬다. Kaggle CIFAR-10, ImageNet Dogs 실습을 포함한다.
**키워드**: `fine-tuning`, `object detection`, `SSD`, `R-CNN`, `semantic segmentation`, `style transfer`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 14 (line 2086)

### Ch 15: Natural Language Processing: Pretraining (pp. 690-743)
**핵심**: Word2vec(Skip-gram, CBOW), GloVe, 서브워드 임베딩(BPE, fastText)을 설명한다. 단어 유사도와 비유 과제를 수행하고, BERT의 사전학습(MLM, NSP) 과정을 구현한다.
**키워드**: `word2vec`, `GloVe`, `BPE`, `BERT`, `pretraining`, `masked language model`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 15 (line 2397)

### Ch 16: Natural Language Processing: Applications (pp. 744-779)
**핵심**: 감정 분석(RNN, CNN 기반), 자연어 추론(SNLI 데이터셋, 어텐션 모델), BERT 파인튜닝을 다룬다. 시퀀스 수준/토큰 수준 분류, 질문 응답 등 다양한 NLP 태스크에 BERT를 적용한다.
**키워드**: `sentiment analysis`, `NLI`, `BERT fine-tuning`, `question answering`, `textCNN`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 16 (line 2590)

### Ch 17: Reinforcement Learning (pp. 781-796)
**핵심**: MDP 정의, 할인 수익, 가치 함수를 소개한다. 가치 반복(value iteration)과 Q-learning 알고리즘을 유도하고, 탐색-활용 트레이드오프와 자기 교정 특성을 설명한다.
**키워드**: `MDP`, `value iteration`, `Q-learning`, `exploration`, `discount factor`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 17 (line 2739)

### Ch 18: Gaussian Processes (pp. 797-826)
**핵심**: 가우시안 프로세스(GP)의 직관적 도입부터 GP 사전(RBF 커널, 신경망 커널), GP 사후 추론(회귀)까지 다룬다. 커널 하이퍼파라미터 학습과 GPyTorch를 사용한 실습을 포함한다.
**키워드**: `Gaussian process`, `RBF kernel`, `posterior inference`, `GPyTorch`, `kernel hyperparameters`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 18 (line 2843)

### Ch 19: Hyperparameter Optimization (pp. 828-845)
**핵심**: HPO 문제를 정의하고, 랜덤 서치, 비동기 랜덤 서치를 구현한다. 다중 충실도 최적화(successive halving, ASHA)를 통한 효율적 탐색 전략을 설명한다.
**키워드**: `hyperparameter optimization`, `random search`, `successive halving`, `ASHA`, `multi-fidelity`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 19 (line 2937)

### Ch 20: Generative Adversarial Networks (pp. 853-892)
**핵심**: GAN의 기본 원리(생성기 vs 판별기)를 설명하고, 간단한 GAN을 구현한다. DCGAN을 통해 포켓몬 이미지를 생성하는 실습을 수행한다.
**키워드**: `GAN`, `DCGAN`, `generator`, `discriminator`, `adversarial training`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 20 (line 3005)

### Ch 21: Recommender Systems (pp. 893-895)
**핵심**: 추천 시스템의 개요를 제공한다. 협업 필터링, 명시적/암시적 피드백, 추천 태스크의 분류를 소개한다.
**키워드**: `recommender systems`, `collaborative filtering`, `implicit feedback`
**상세**: → `Dive into Deep Learning (D2L) _full.md` Ch 21 (line 3092)
