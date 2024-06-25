# -*- coding: utf-8 -*-

"""
有时候我们需要对 wow_sdm 这个包进行一些定制化的修改, 这时我们就会将整个代码库拷贝到 vendor 中,
开发完成后再迁徙回 wow_sdm-project 中. 不过最终我们还是要将 wow_sdm 以第三方的包的形式安装的.
这个模块可以方便我们在两种模式之间切换.
"""

# Import from pip install
import wow_sdm.api as wow_sdm
# Import from verndor
# from .wow_sdm import api as wow_sdm
