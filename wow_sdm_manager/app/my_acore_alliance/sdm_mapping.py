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
# dir_game_client = dir_here.joinpath("tmp", "world_of_warcraft_zhTW")
# Real dir
dir_game_client = Path(
    r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-zhTW"
)

client = Client(
    locale="zhTW",
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
    CharMap.make_many(
        CharGrpEnum.shaman_elemental_resto, MacroGroupEnum.shaman_elemental_resto
    ),
    CharMap.make_many(
        CharGrpEnum.druid_balance_resto, MacroGroupEnum.druid_balance_resto
    ),
    CharMap.make_many(CharGrpEnum.mage_arcane_fire, MacroGroupEnum.mage_arcane_fire),
    CharMap.make_many(
        CharGrpEnum.priest_shadow_disco, MacroGroupEnum.priest_shadow_disco
    ),
    CharMap.make_many(
        CharGrpEnum.warlock_demonology_affiliation,
        MacroGroupEnum.warlock_demonology_affiliation,
    ),
    CharMap.make_many(
        CharGrpEnum.hunter_marksmanship_survival,
        MacroGroupEnum.hunter_marksmanship_survival,
    ),
    CharMap.make_many(
        CharGrpEnum.paladin_holy_protect, MacroGroupEnum.paladin_holy_protect
    ),
    CharMap.make_many(
        CharGrpEnum.dk_blood_tank_unholy_dps, MacroGroupEnum.dk_blood_tank_unholy_dps
    ),
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
