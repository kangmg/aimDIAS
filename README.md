![image](https://github.com/kangmg/aimDIAS/assets/59556369/cb3a401d-6ea2-4a26-85e4-085c143d6485)

aim(aimnet2) + DIAS(distortion interaction analysis)
---
`aimDIAS` is a Python package compatible with IPython that enables SUPER-FAST Distortion Interaction Analysis (or activation strain analysis) using aimnet2 models.

## Colab Tutorials
aimDIAS is currently in ***beta version***. Functions may change depending on the version, so please check the version number.

|notebook| aimDIAS version|description|
|:-:|:-:|:-:|
|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](link) | v. 1.0.1 | basic tutorials |

## Usage
For detail, see `docs/*`, `notebooks/*`

- Draw your molecule
```python
from aimDIAS import draw_xyz

draw_xyz("h2o.xyz", charge=0)
```
  
- Run calculation
```python
from aimDIAS import aimDIAS_run

fp = {
  "frag_1" : (-1, [1, 2]),
  "frag_2" : (+1, [3])
  }

aimDIAS_run(trajFile="h2o.xyz", fragments_params=fp)
```

- Plot your Result without calculation
```python
from aimDIAS import aimDIAS_run

gp = {"distance" : "1 2"}

fp = {
  "frag_1" : (-1, [1, 2]),
  "frag_2" : (+1, [3])
  }

aimDIAS_run(trajFile="h2o.xyz", fragments_params=fp, mode="plot", axis_type="distance", geo_param=gp)
```

## Install
1. pip 
```shell
pip install aimDIAS
```

2. git clone
```shell
# in terminal #

git clone https://github.com/kangmg/aimDIAS

# since `git clone` doesn't directly install git lfs files, it contains metadata only. You'll need to manually remove it. Models will be automatically downloaded.
rm path/to/aimDIAS/aimDIAS/models/*

pip install -q -r path/to/aimDIAS/requirements.txt
```
```python
# in python #

import sys
sys.path.append("path/to/aimDIAS")
```

## Requirements
python >= 3.10.0

## Bug Report
kangmg@korea.ac.kr or [issue in github](https://github.com/kangmg/aimDIAS/issues)

> *I'm always happy to hear feedback and suggestions. Feel free to contact me anytime.*

## TODO
- add auto_fragmentation
- user-friendly fragmentation GUI
- enhance the plot style for publication-quality
- json to table formatter
- more sample data
- fp enables support for string format
- axis validation plot
- add GPU mode
