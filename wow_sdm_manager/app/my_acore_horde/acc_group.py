# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from ...vendor.wow_sdm.api import get_values
from .acc_enum import AccountEnum, CharacterEnum


# ==============================================================================
# START of manual editing
# ==============================================================================
class AccountGroupEnum:
    all_accounts = get_values(AccountEnum)


class CharacterGroupEnum:
    all_characters = get_values(CharacterEnum)

    paladin_protect_retri = [
        CharacterEnum.rab01_AzerothCore_sa,
    ]

    shaman_elemental_resto = [
        CharacterEnum.rab02_AzerothCore_sb,
        CharacterEnum.rab03_AzerothCore_sc,
        CharacterEnum.rab04_AzerothCore_sd,
        CharacterEnum.rab05_AzerothCore_se,
    ]


# ==============================================================================
# END of manual editing
# ==============================================================================
