# -*- coding: utf-8 -*-

import sys
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
from .sdm_mb_special import make_mb_special

get_values = wow_sdm.get_values
concat_lists = wow_sdm.concat_lists
Client = wow_sdm.exp03_wotlk.Client
AccMap = wow_sdm.exp03_wotlk.AccLvlMapping
CharMap = wow_sdm.exp03_wotlk.CharLvlMapping
SdmMapping = wow_sdm.exp03_wotlk.SdmMapping

dir_here = Path.dir_here(__file__)
# Test dir
dir_game_client_for_test = dir_here.joinpath("tmp", "world_of_warcraft_zhTW")
# Real dir
dir_game_client_for_windows = Path(
    r"C:\Users\husan\Documents\Games\WoW-Root\Client\World-of-Warcraft-3.3.5-zhTW"
)
IS_MAC = sys.platform == "darwin"
if IS_MAC:
    dir_game_client = dir_game_client_for_test
else:
    dir_game_client = dir_game_client_for_windows
    # dir_game_client = dir_game_client_for_test

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
acc_macros = concat_lists(
    AccMap.make_many(AccGrpEnum.all_accounts, MacroGroupEnum.acc_common),
    make_mb_special(),
)

# ------------------------------------------------------------------------------
# char_macros
# ------------------------------------------------------------------------------
char_macros = concat_lists(
    # --- paladin
    CharMap.make_many(
        CharGrpEnum.paladin_protect_retri,
        MacroGroupEnum.paladin_protect_retri,
    ),
    CharMap.make_many(
        CharGrpEnum.paladin_holy_protect,
        MacroGroupEnum.paladin_holy_protect,
    ),

    # --- dk
    CharMap.make_many(
        CharGrpEnum.dk_blood_tank_unholy_dps,
        MacroGroupEnum.dk_blood_tank_unholy_dps,
    ),
    # --- shaman
    CharMap.make_many(
        CharGrpEnum.shaman_elemental_resto,
        MacroGroupEnum.shaman_elemental_resto,
    ),
    CharMap.make_many(
        CharGrpEnum.shaman_resto_enhancement,
        MacroGroupEnum.shaman_resto_enhancement,
    ),
    # --- hunter
    CharMap.make_many(
        CharGrpEnum.hunter_marksmanship_survival,
        MacroGroupEnum.hunter_marksmanship_survival,
    ),

    # --- druid
    CharMap.make_many(
        CharGrpEnum.druid_balance_resto,
        MacroGroupEnum.druid_balance_resto,
    ),
    CharMap.make_many(
        CharGrpEnum.druid_feral_balance,
        MacroGroupEnum.druid_feral_balance,
    ),

    # --- warlock
    CharMap.make_many(
        CharGrpEnum.warlock_demonology_affiliation,
        MacroGroupEnum.warlock_demonology_affiliation,
    ),

    # --- mage
    CharMap.make_many(
        CharGrpEnum.mage_arcane_fire,
        MacroGroupEnum.mage_arcane_fire,
    ),

    # --- priest
    CharMap.make_many(
        CharGrpEnum.priest_holy_shadow,
        MacroGroupEnum.priest_holy_shadow,
    ),
    CharMap.make_many(
        CharGrpEnum.priest_shadow_disc,
        MacroGroupEnum.priest_shadow_disc,
    ),
    CharMap.make_many(
        CharGrpEnum.priest_disc_holy,
        MacroGroupEnum.priest_disc_holy,
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
