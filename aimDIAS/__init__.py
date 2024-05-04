"""
Descriptions
============
Module for performing Activation Strain Model (ASM) & Distortion/Interaction (D/I) analysis using AIMNet2 calculator.

This module provides functions to perform ASM & D/I analysis on XYZ trajectory files using the AIMNet2 calculator. It includes functions for running calculations, plotting results, and handling geometric parameters.

This code implements ASM & D/I analysis based on two reference papers
1) Svatunek, D., & Houk, K. N. (2019). autoDIAS: a python tool for an automated distortion/interaction activation strain analysis. Journal of Computational Chemistry (Vol. 40, Issue 28, pp. 2509–2515). Wiley. https://doi.org/10.1002/jcc.26023
2) van Zeist, W.-J., & Bickelhaupt, F. M. (2010). The activation strain model of chemical reactivity. Organic & Biomolecular Chemistry (Vol. 8, Issue 14, p. 3118). Royal Society of Chemistry (RSC). https://doi.org/10.1039/b926828f
"""

header = """\033[34m
            ███                  ██████████   █████   █████████    █████████ 
           ░░░                  ░░███░░░░███ ░░███   ███░░░░░███  ███░░░░░███
  ██████   ████  █████████████   ░███   ░░███ ░███  ░███    ░███ ░███    ░░░ 
 ░░░░░███ ░░███ ░░███░░███░░███  ░███    ░███ ░███  ░███████████ ░░█████████ 
  ███████  ░███  ░███ ░███ ░███  ░███    ░███ ░███  ░███░░░░░███  ░░░░░░░░███
 ███░░███  ░███  ░███ ░███ ░███  ░███    ███  ░███  ░███    ░███  ███    ░███
░░████████ █████ █████░███ █████ ██████████   █████ █████   █████░░█████████ 
 ░░░░░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░░░░░░   ░░░░░ ░░░░░   ░░░░░  ░░░░░░░░░  


  * Project page  : https://github.com/kangmg/aimDIAS 
  * Developer     : Kang Mingi
  * Email         : kangmg@korea.ac.kr
\033[0m"""

__version__ = '1.0.2'

from .samples import *
from .DIAS import *
from .utilities import *
from .aimnet2ase import *

