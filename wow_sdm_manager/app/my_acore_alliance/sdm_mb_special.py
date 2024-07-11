# -*- coding: utf-8 -*-

"""
这个模块是专门用来切换用于不同战斗场景下的 Special 宏的.
"""

import typing as T
from pathlib_mate import Path
from ...vendor.importer import wow_sdm
from .acc_enum import (
    AccountEnum as AccEnum,
    CharacterEnum as CharEnum,
)
from .acc_group import (
    AccountGroupEnum as AccGrpEnum,
    CharacterGroupEnum as CharGrpEnum,
)
from .sdm_enum import MacroEnum
from .sdm_group import MacroGroupEnum

AccMap = wow_sdm.exp03_wotlk.AccLvlMapping


def make_placeholder() -> T.List[AccMap]:
    return AccMap.make_many(
        AccGrpEnum.all_accounts,
        MacroGroupEnum.acc_common_mb_special,
    )


def make_r_abcdefghij_solo_icc_boss1() -> T.List[AccMap]:
    """
    这是一个例子, 实现了在打 ICC Boss1 的时候, Special 宏是选中骨刺.
    """
    return AccMap.make_many(
        AccGrpEnum.alliance_r_1_to_10,
        [
            MacroEnum.f_00_common__6001_mb_special1_icc_boss1_target_bone_zhTW,
            MacroEnum.f_00_common__6002_mb_special2,
            MacroEnum.f_00_common__6003_mb_special3,
        ],
    )


def make_mb_special() -> T.List[AccMap]:
    """
    注意, 这个函数中至少要返回一个 AccMap 实例. 如果返回的是空列表会导致 SDM 插件例的宏
    命令定义找不到, 使得游戏中的动作条上的按钮丢失. 如果你并不需要打任何 Boss 战, 你就可以
    用 make_placeholder() 这个函数来返回一个默认的 Special 宏命令.
    """
    # return make_placeholder()
    return make_r_abcdefghij_solo_icc_boss1()
