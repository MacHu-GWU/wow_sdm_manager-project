# -*- coding: utf-8 -*-

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
    return AccMap.make_many(
        AccGrpEnum.alliance_r_1_to_10,
        [
            MacroEnum.f_00_common__6001_mb_special1_icc_boss1_target_bone_zhTW,
            MacroEnum.f_00_common__6002_mb_special2,
            MacroEnum.f_00_common__6003_mb_special3,
        ],
    )


def make_mb_special() -> T.List[AccMap]:
    # return make_placeholder()
    return make_r_abcdefghij_solo_icc_boss1()
