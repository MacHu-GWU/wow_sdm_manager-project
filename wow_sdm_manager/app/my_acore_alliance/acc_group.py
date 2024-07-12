# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from ordered_set import OrderedSet
from ...vendor.importer import wow_sdm
from .acc_enum import AccountEnum, CharacterEnum

get_values = wow_sdm.get_values


# ==============================================================================
# START of manual editing
# ==============================================================================
class AccountGroupEnum:
    all_accounts = get_values(AccountEnum)

    alliance_r_1_to_10 = [
        AccountEnum.fat01,
        AccountEnum.fat02,
        AccountEnum.fat03,
        AccountEnum.fat04,
        AccountEnum.fat05,
        AccountEnum.fat06,
        AccountEnum.fat07,
        AccountEnum.fat08,
        AccountEnum.fat09,
        AccountEnum.fat10,
    ]
    alliance_r_1_to_10 = OrderedSet(alliance_r_1_to_10)

    alliance_r_1_to_25 = [
        AccountEnum.fat01,
        AccountEnum.fat02,
        AccountEnum.fat03,
        AccountEnum.fat04,
        AccountEnum.fat05,
        AccountEnum.fat06,
        AccountEnum.fat07,
        AccountEnum.fat08,
        AccountEnum.fat09,
        AccountEnum.fat10,
        AccountEnum.fat11,
        AccountEnum.fat12,
        AccountEnum.fat13,
        AccountEnum.fat14,
        AccountEnum.fat15,
        AccountEnum.fat16,
        AccountEnum.fat17,
        AccountEnum.fat18,
        AccountEnum.fat19,
        AccountEnum.fat20,
        AccountEnum.fat21,
        AccountEnum.fat22,
        AccountEnum.fat23,
        AccountEnum.fat24,
        AccountEnum.fat25,
    ]
    alliance_r_1_to_25 = OrderedSet(alliance_r_1_to_25)


class CharacterGroupEnum:
    all_characters = get_values(CharacterEnum)

    paladin_protect_retri = [
        CharacterEnum.fat01_AzerothCore_ra,
    ]

    shaman_elemental_resto = [
        CharacterEnum.fat02_AzerothCore_rb,
    ]

    druid_feral_balance = [
        CharacterEnum.fat03_AzerothCore_rc,
    ]

    mage_arcane_fire = [
        CharacterEnum.fat04_AzerothCore_rd,
    ]

    priest_holy_shadow = [
        CharacterEnum.fat05_AzerothCore_re,
    ]

    warlock_demonology_affiliation = [
        CharacterEnum.fat06_AzerothCore_rf,
    ]

    hunter_marksmanship_survival = [
        CharacterEnum.fat07_AzerothCore_rg,
    ]

    druid_balance_resto = [
        CharacterEnum.fat08_AzerothCore_rh,
        CharacterEnum.fat11_AzerothCore_rk,
        CharacterEnum.fat12_AzerothCore_rl,
        CharacterEnum.fat13_AzerothCore_rm,
    ]

    paladin_holy_protect = [
        CharacterEnum.fat09_AzerothCore_ri,
    ]

    dk_blood_tank_unholy_dps = [
        CharacterEnum.fat10_AzerothCore_rj,
    ]

    priest_shadow_disc = [
        CharacterEnum.fat14_AzerothCore_rn,
        CharacterEnum.fat15_AzerothCore_ro,
        CharacterEnum.fat16_AzerothCore_rp,
        CharacterEnum.fat17_AzerothCore_rq,
        CharacterEnum.fat18_AzerothCore_rr,
        CharacterEnum.fat19_AzerothCore_rs,
        CharacterEnum.fat20_AzerothCore_rt,
        CharacterEnum.fat21_AzerothCore_ru,
        CharacterEnum.fat22_AzerothCore_rv,
    ]

    priest_disc_holy = [
        CharacterEnum.fat25_AzerothCore_ry,
    ]

# ==============================================================================
# END of manual editing
# ==============================================================================
