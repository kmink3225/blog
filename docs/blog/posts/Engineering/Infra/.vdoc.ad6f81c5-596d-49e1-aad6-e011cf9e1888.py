# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# 1. PyTorch 설치 (CUDA 12.1 권장)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# 2. transformers 및 관련 패키지
pip install transformers
pip install accelerate
pip install datasets  # 데이터셋 사용시

import torch

print(f"PyTorch 버전: {torch.__version__}")
print(f"CUDA 사용 가능: {torch.cuda.is_available()}")
print(f"CUDA 버전 (PyTorch): {torch.version.cuda}")
print(f"GPU 이름: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")
#
#
#
#
pip install tensorflow[and-cuda]

# pytorch 설치 후 텐서플로우 설치 시 제거
#pip uninstall tensorflow tensorflow-gpu tensorflow-cpu
#pip uninstall tensorboard tensorboard-plugin-wit
## 캐시 정리
#pip cache purge
#
#
#
#
#
#
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    
    # 간단한 텐서 연산
    a = torch.randn(1000, 1000).to(device)
    b = torch.randn(1000, 1000).to(device)
    
    # GPU에서 행렬 곱셈
    c = torch.matmul(a, b)
    
    print("✅ GPU 텐서 연산 성공!")
    print(f"결과 shape: {c.shape}")
    print(f"GPU 메모리 사용량: {torch.cuda.memory_allocated()/1024**2:.1f} MB")
    
    # 메모리 정리
    torch.cuda.empty_cache()

#
#
#
#
# 더 가벼운 모델로 테스트
model_name = "prajjwal1/bert-tiny"  # 매우 작은 모델

try:
    from transformers import AutoTokenizer, AutoModel
    
    print("모델 다운로드 중...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)
    
    print("GPU에서 추론 실행 중...")
    text = "GPU 테스트입니다"
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    print("✅ 작은 모델로 GPU 테스트 성공!")
    print(f"출력 shape: {outputs.last_hidden_state.shape}")
    print(f"GPU 메모리 사용량: {torch.cuda.memory_allocated()/1024**2:.1f} MB")
    
except Exception as e:
    print(f"여전히 오류: {e}")
#
#
#
import torch
from transformers import AutoModel, AutoTokenizer

print("=== PyTorch GPU 테스트 ===")
print(f"PyTorch 버전: {torch.__version__}")
print(f"CUDA 사용 가능: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA 버전: {torch.version.cuda}")
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    
    # transformers 테스트
    device = torch.device("cuda")
    model_name = "distilbert-base-uncased"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name).to(device)
        
        text = "GPU test with transformers"
        inputs = tokenizer(text, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model(**inputs)
        
        print("✅ transformers GPU 테스트 성공!")
        print(f"출력 shape: {outputs.last_hidden_state.shape}")
        print(f"GPU 메모리 사용량: {torch.cuda.memory_allocated()/1024**2:.1f} MB")
        
    except Exception as e:
        print(f"❌ 오류: {e}")
else:
    print("❌ CUDA를 사용할 수 없습니다.")
#
#
#
#
#
#
# 배치 크기 조정

# VRAM에 따른 권장 배치 크기
# 6GB VRAM: batch_size = 16-32
# 8GB VRAM: batch_size = 32-64  
# 12GB VRAM: batch_size = 64-128

batch_size = 32  # VRAM 용량에 맞게 조정

# 혼합 정밀도 훈련
# PyTorch AMP 사용
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for data, target in dataloader:
    optimizer.zero_grad()
    
    with autocast():
        output = model(data)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
#
#
#
#
# PyTorch 메모리 정리
torch.cuda.empty_cache()

# 메모리 사용량 확인
print(f"Allocated: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
print(f"Reserved: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")
#
#
#
#
#
#
import torch
import time

def benchmark_gpu():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # 큰 행렬 생성
    a = torch.randn(5000, 5000).to(device)
    b = torch.randn(5000, 5000).to(device)
    
    # 성능 측정
    start_time = time.time()
    for _ in range(100):
        c = torch.mm(a, b)
    end_time = time.time()
    
    print(f"Device: {device}")
    print(f"Time: {end_time - start_time:.2f} seconds")
    print(f"GPU Memory: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")

benchmark_gpu()
#
#
#
#
import torch
import torch.nn as nn
import time

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(1000, 2000),
            nn.ReLU(),
            nn.Linear(2000, 1000),
            nn.ReLU(),
            nn.Linear(1000, 10)
        )
    
    def forward(self, x):
        return self.layers(x)

def train_benchmark(device):
    model = SimpleModel().to(device)
    optimizer = torch.optim.Adam(model.parameters())
    criterion = nn.CrossEntropyLoss()
    
    # 더미 데이터
    data = torch.randn(1000, 1000).to(device)
    targets = torch.randint(0, 10, (1000,)).to(device)
    
    start_time = time.time()
    
    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
    
    end_time = time.time()
    print(f"{device} training time: {end_time - start_time:.2f} seconds")

# CPU vs GPU 비교
train_benchmark('cpu')
train_benchmark('cuda')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
