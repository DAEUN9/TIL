# Faster R-CNN

- 2 stage 대표 object detection
  1. region proposal
     - 물리적으로 있음직한 네모영역들 뽑기
  2. object detection
     - RPN(region proposal network)을 통해 features만들기
- RPN부분, Fast R-CNN 부분으로 나눌 수 있음



### RPN(Region Proposal Network)

- 관심있는 영역들을 출력해주는 Network

	#### RPN-Dataset

	1. 이미지에서 작은 변(s) 와 긴변(l)을 구함
	1. s를 600으로 resize, l 에는 (600/s) 를 곱해주어 aspect ratio를 지킴
	1. B = l x (600 / s)라 할때, 만약 B가 1000보다 크면 작은 값으로 만든 600에 (1000/B)를 곱해주어 600보다 작게만든다.
	1. 그렇지 않다면, s = 600이고 긴 변은 B로 rescailing

```python
# faster RCNN re-scaling

# size: 600, max_size: 1000
def get_size_with_aspect_ratio(image_size, size, max_size=None):
    w, h = image_size
    if max_size is not None:
        min_original_size = float(min((w, h)))	# s구하기
        max_original_size = float(max((w, h)))	# l구하기
        # max_original_size / min_original_size * size : s가 600일 때, l의 값(=B)
        if max_original_size / min_original_size * size > max_size:
            # size : l이 1000일 때, s의 값(<600)
            size = int(round(max_size * min_original_size / max_original_size))
      
     if (w<= h and w == size) or (h <= w and h == size):
        return (h,w)
    
    if w < h:
        ow = size
        oh = int(size * h/w)
    else:
        oh = size
        ow = int(size * w/h)
        
    return (oh, ow)
```

- horisontal flip 방식
  - annotation을 0.5의 확률로 오른쪽, 왼쪽을 뒤집음



#### RPN-Model

- paper에서는 VGG-16 사용
- 마지막, pooling layer는 RoI pooling 이용
- 1000 * 600 이미지가 60 * 40 * 9 로 변환된것으로 보아 stride는 약 16
- H x W x 3 의 이미지가 입력으로 들어가서 RPN 에 들어가면 H/16 x W/16 x 36 인 reg feature 와 , H/16 x W/16 x 18 인 cls feature 이 출력



#### RPN-branch

- cls layer와 regs layer 1*1 conv로 구현
- intermediate layer는 3*3 conv로 구현
- cls, reg 의 branch들은 각각 H x W x 18, H x W x 36의 shape 을 갖는 tensor를 출력
- ouput dimension은 anchor의 개수 이용





#### RPN-Loss

- Anchor box  사용
  - 보통 cneter-coordinates
- Assign anchor box
  - cross boundary anchors무시
  - GT와 겹치지 않는 많은 수의 anchor제거
    1. gt와 iou(Intersection-over-Union)가 가장 큰 anchor
    2. iou가 0.7이상일 anchor일 경우 positive
    3. 0.3이하일 경우는 negative와 같은 세가지 조건 만족
  - mini-batch로 사용될 때, sampling을 한다



### Fast R-CNN

1. Roi

   -  최대 2000개의 x1y1x2y2의 bbox

   - 즉, [2000, 4] 의 tensor로 표현할 수 있음

      1에서 2로 넘어갈때, roi에서 128개의 sample 을 뽑아서 sampled roi 생성 [128, 4] 

2. Fast RCNN
   -  cls head, reg head,와 roi pooling 으로 이루어짐
   - 간단하게 feature와 roi에서 sampling 한 sampled roi를 입력으로 받아서, cls, reg의 output을 내 주는 모듈

 	3. cls, reg
     - fast rcnn의 loss로 들어가서 학습
     -  cls, reg 은 각각 [128, num_classes], [128, num_classes * 4] 의 shape을 가짐

 

#### Fast R-CNN model

- 구성

  - RoI pooling

  - FCs

  - FC for cls (cls_head)

  - FC for reg (reg_head)

```python
self.roi_pool = RoIPool(output_size=(roi_size, roi_size), spatial_scale=1.)
self.FCs = nn.Sequential(
                Linear(in_features=25088, out_features=4096, bias=True),
                ReLU(inplace=True),
                Linear(in_features=4096, out_features=4096, bias=True),
                ReLU(inplace=True))
self.cls_head = nn.Linear(4096, num_classes)      
self.reg_head = nn.Linear(4096, num_classes * 4)
```



#### Faster R-CNN traning

1. Alternating Traning
   - 먼저 RPN을 학습시키고, RPN을 통해 나오는 roi로 Fast RCNN을 번갈아 가며 학습

2. Approximate Joint Traning
   - RPN과, Fast RCNN 의 loss 를 통합시켜서 한번에 학습
   - approximate 방법으로 비슷한 성능이 나왔고, 학습시간이 줄었다는 장점

3. Non-approximate Joint Training
   - 위의 방법이 RoI pooling layer 에 대하여 gradient 가 무시되는 문제를 가지고 있는데, 이를 해결하기 위하여 RoI Warping 을 사용한 학습 방법

**4-Step Alternating Traning**

**step 1** 에서는 Fast R-CNN 부분을 고정시키고, Extractor, RPN을 RPN Loss 로 학습

**step 2** 에서는 RPN을 고정시키고 roi를 이용해서 Extractor, Fast RCNN을 Fast RCNN Loss 로 학습

**step 3** 에서는 Extractor, Fast RCNN 을 고정시키고 RPN만 RPN Loss 로 학습

**step 4** 에서는 Extractor, RPN을 고정시키고 roi를 이용해서 Fast RCNN만 Fast RCNN Loss 로 학습

