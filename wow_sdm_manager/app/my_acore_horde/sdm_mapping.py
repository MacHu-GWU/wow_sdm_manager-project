# -*- coding: utf-8 -*-

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

get_values = wow_sdm.get_values
concat_lists = wow_sdm.concat_lists
Client = wow_sdm.exp03_wotlk.Client
AccMap = wow_sdm.exp03_wotlk.AccLvlMapping
CharMap = wow_sdm.exp03_wotlk.CharLvlMapping
SdmMapping = wow_sdm.exp03_wotlk.SdmMapping

dir_here = Path.dir_here(__file__)
# Test dir
dir_game_client = dir_here.joinpath("tmp", "world_of_warcraft_zhCN")
# Real dir
# dir_game_client = Path(
#     r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-zhCN"
# )

client = Client(
    locale="zhCN",
    dir=dir_game_client,
)
all_accounts = AccGrpEnum.all_accounts
all_characters = CharGrpEnum.all_characters

# ==============================================================================
# START of manual editing
# ==============================================================================
# ------------------------------------------------------------------------------
# acc_macros
# ------------------------------------------------------------------------------
acc_macros = AccMap.make_many(AccGrpEnum.all_accounts, MacroGroupEnum.acc_common)

# ------------------------------------------------------------------------------
# char_macros
# ------------------------------------------------------------------------------
char_macros = concat_lists(
    CharMap.make_many(
        CharGrpEnum.paladin_protect_retri, MacroGroupEnum.paladin_protect_retri
    ),
    # CharMap.make_many(
    #     CharGrpEnum.shaman_elemental_resto, MacroGroupEnum.shaman_elemental_resto
    # ),
)

# ==============================================================================
# END of manual editing
# ==============================================================================
# ------------------------------------------------------------------------------
# wtf_mapping
# ------------------------------------------------------------------------------
sdm_mapping = SdmMapping(
    client=client,
    all_accounts=all_accounts,
    all_characters=all_characters,
    acc_macros=acc_macros,
    char_macros=char_macros,
)
