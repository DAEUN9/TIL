# Anaconda 환경설정하기

> colab에서만 돌리려면 안해도됩니다.
>
> 싸트북 기준입니다!
>
> 개인노트북은 nvidia driver설치 및 compute capability  확인 필요



1. cuda 10.2 설치
   - https://developer.nvidia.com/cuda-10.2-download-archive
2. Anaconda 설치
3. Anacoda frompt에서 가상환경 생성 및 활성화
   - codna create -n [NAME] python=3.7
   - conda activate [NAME]

4. 패키지 설치 - 버전을 맞춰야함

   - https://pytorch.kr/get-started/previous-versions/
     - 파이토치 CUDA 10.2 명령어 참고

5. 환경변수 경로 추가

   - anaconda3 설치경로
     - anaconda3
     - anaconda3/Library
     - anaconda3/Scripts

6. 프롬프트로 돌려보기

   - 파이썬 파일이있는 경로로 이동
   - python 파일.py

7. 파이참으로 돌려보기

   - prompt에서 바로 돌려도되지만 pycharm에서 돌려볼 수 있음

   - 프로젝트 생성할때 conda 가상환경경로로 환경을 설정해주거나

   - settings - python interpreter - 환경추가

     - conda 설치경로에 envs/[NAME]/python.exe 선택

     - ```python
       import torch
       
       # True 확인
       torch.cuda.is_available()
       ```

8. 주피터노트북으로 돌려보기

   - 아나콘다 프롬프트에서 가상환경 활성화

   - pip install jupyter notebook
     - kernel 연결
       - python -m ipykernel install --user --name [NAME]

   - jupyter notebook





---

## 기타명령어

- conda list
  - 가상환경 활성화되어있는 상태에서 명령어실행
  - 현재 설치된 패키지 목록

- conda env list
  - 가상환경 목록
- conda deactivate
  - 현재 가상환경 비활성화
- conda env remove -n [NAME]
  - 가상환경 삭제

- conda create --clone [ORIGIN_NAME] -n [NEW_NAME]
  - 가상환경 복제
- conda --version
  - 아나콘다 버전 확인
- conda info
  - 아나콘다 정보 조회
- conda update [PACKAGE_NAME]
  - 설치된 패키지 업데이트
- conda remove -r [ENV_NAME] [PACKAGE_NAME]
  - 설치된 패키지 삭제

- nvidia-smi
  - GPU  정보 확인
- nvcc -V
  - CUDA toolkit 확인