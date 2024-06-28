[![DOI](https://sandbox.zenodo.org/badge/795712401.svg)](https://sandbox.zenodo.org/doi/10.5072/zenodo.53479)

![image](https://github.com/kangmg/aimDIAS/assets/59556369/cb3a401d-6ea2-4a26-85e4-085c143d6485)

aim(AIMNet2) + DIAS(distortion interaction analysis)
---
`aimDIAS` is a Python package compatible with IPython that enables SUPER-FAST Distortion Interaction Analysis (or activation strain analysis) using aimnet2 models.

<br/>

## Colab Tutorials
aimDIAS is currently in ***beta version***. Functions may change depending on the version, so please check the version number.

|notebook| aimDIAS version|description|
|:-:|:-:|:-:|
|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kangmg/aimDIAS/blob/main/notebooks/aimDIAS_tutorials.ipynb) | v. 1.0 | basic tutorials |

<br/>

## Basic Usage
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

aimDIAS_run(trajFile="h2o.xyz",
            fragments_params=fp,
            mode="plot",
            axis_type="distance",
            geo_param=gp)
```

<br/>

## Gallery

### ***Diels-Alder reaction***

> ![image](https://github.com/kangmg/aimDIAS/assets/59556369/08b1132b-0a18-4f75-bfa9-2144504804fe)

<br/>

### ***Wittig Rection***

> ![image](https://github.com/kangmg/aimDIAS/assets/59556369/a19417f7-6334-4e4a-a702-7eb37b748f4e)



<br/>

## How to Install
> ***pip***
- 
  ```shell
  pip install aimDIAS # old version

  pip install git+https://github.com/kangmg/aimDIAS.git # current version
  ```

> ***git clone***
- terminal
  ```shell
  ### terminal ###
  git clone https://github.com/kangmg/aimDIAS

  
  pip install -q -r path/to/aimDIAS/requirements.txt
  ```
- ipython
  ```python
  ### python ###
  import sys
  sys.path.append("path/to/aimDIAS")
  ```
<br/>

## Requirements
python >= 3.10.0

<br/>

## Share your Data

> Share your files and contribute to the community!

By sharing your xyz trajectory files in the ***Discussion section***, you can make them available as sample data for everyone to use. Please refer to this [discussion link](https://github.com/kangmg/aimDIAS/discussions/2) for more information:

![image](https://github.com/kangmg/aimDIAS/assets/59556369/45aa5c96-32ca-4b03-b721-df1785c9339c)

Files posted in the Discussion section will be uploaded to the `samples/` directory in the project repository for easy download and utilization with the `load_data()` function.

<br/>

## Bug Report
kangmg@korea.ac.kr or [issue in github](https://github.com/kangmg/aimDIAS/issues)

> ***I'm always happy to hear feedback and suggestions. Feel free to contact me anytime.***

<br/>

