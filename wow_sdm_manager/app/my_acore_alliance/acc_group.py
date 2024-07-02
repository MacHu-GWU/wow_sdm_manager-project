# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from ...vendor.importer import wow_sdm
from .acc_enum import AccountEnum, CharacterEnum

get_values = wow_sdm.get_values


# ==============================================================================
# START of manual editing
# ==============================================================================
class AccountGroupEnum:
    all_accounts = get_values(AccountEnum)


class CharacterGroupEnum:
    all_characters = get_values(CharacterEnum)

    paladin_protect_retri = [
        CharacterEnum.fat01_AzerothCore_ra,
    ]

    shaman_elemental_resto = [
        CharacterEnum.fat02_AzerothCore_rb,
    ]

    druid_balance_resto = [
        CharacterEnum.fat03_AzerothCore_rc,
        CharacterEnum.fat08_AzerothCore_rh,
    ]

    mage_arcane_fire = [
        CharacterEnum.fat04_AzerothCore_rd,
    ]

    priest_shadow_disco = [
        CharacterEnum.fat05_AzerothCore_re,
    ]

    warlock_demonology_affiliation = [
        CharacterEnum.fat06_AzerothCore_rf,
    ]

    hunter_marksmanship_survival = [
        CharacterEnum.fat07_AzerothCore_rg,
    ]

    paladin_holy_protect = [
        CharacterEnum.fat09_AzerothCore_ri,
    ]

    dk_blood_tank_unholy_dps = [
        CharacterEnum.fat10_AzerothCore_rj,
    ]


# ==============================================================================
# END of manual editing
# ==============================================================================
