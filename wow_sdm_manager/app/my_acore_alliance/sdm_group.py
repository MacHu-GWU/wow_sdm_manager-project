# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from ordered_set import OrderedSet
from ...vendor.importer import wow_sdm
from .sdm_enum import MacroEnum


# ==============================================================================
# START of manual editing
# ==============================================================================
class MacroGroupEnum:
    all_macros = wow_sdm.get_values(MacroEnum)

    acc_common = [
        # GM command
        MacroEnum.f_00_common__1001_respawn,
        MacroEnum.f_00_common__1002_feigh_death,
        MacroEnum.f_00_common__1003_reset_cooldown,
        MacroEnum.f_00_common__1004_ice_block,
        MacroEnum.f_00_common__1005_resurrection,
        MacroEnum.f_00_common__1006_invisibility,
        MacroEnum.f_00_common__1007_unbind_instance,
        MacroEnum.f_00_common__1008_fly_up,
        MacroEnum.f_00_common__1009_fly_down,
        MacroEnum.f_00_common__1010_x32_speed,
        # Mount
        MacroEnum.f_00_common__1011_MountUp_zhTW,
        MacroEnum.f_00_common__1012_MountDown_zhTW,
        # Multi-box
        MacroEnum.f_00_common__1101_target_party,
        MacroEnum.f_00_common__1102_target_raid,
        MacroEnum.f_00_common__1103_target_focus_target,
        MacroEnum.f_00_common__1104_target_focus_target_target,
        MacroEnum.f_00_common__1105_confirm,
        MacroEnum.f_00_common__1106_set_focus,
        MacroEnum.f_00_common__1107_clear_focus,
        MacroEnum.f_00_common__1108_set_high_fps,
        MacroEnum.f_00_common__1109_set_low_fps,
        MacroEnum.f_00_common__1110_follow_focus,
        # Target specific character
        MacroEnum.f_00_common__1131_target_window_acore_alliance_r_1_to_25_team,
        MacroEnum.f_00_common__1132_target_window_acore_alliance_r_1_to_25_team,
        # Party and Raid
        MacroEnum.f_00_common__1151_invite_raid_acore_alliance_r_1_to_25_team,
        MacroEnum.f_00_common__1152_leave_raid,
        MacroEnum.f_00_common__1153_summon_acore_alliance_r_1_to_25_team,
        # Teleport
        MacroEnum.f_00_common__1171_tele_darnassus,
        MacroEnum.f_00_common__1172_tele_ironforge,
        MacroEnum.f_00_common__1175_tele_shattrath,
        MacroEnum.f_00_common__1176_tele_dalaran,
    ]
    acc_common = OrderedSet(acc_common)

    paladin_protect_retri = [
        # Buff
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_02_paladin__0_common__11101_consumable,
        MacroEnum.f_02_paladin__0_common__11111_clear_debuff_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11311_buff_self_alliance_zhTW,
        # Act
        MacroEnum.f_02_paladin__1_protect_retri__11301_act1_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11302_act2_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11303_act3_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11304_act4_zhTW,
        MacroEnum.f_02_paladin__0_common__11131_protect_rotation_zhTW,
        MacroEnum.f_02_paladin__0_common__11132_retribution_rotation_zhTW,
    ]
    paladin_protect_retri = OrderedSet(paladin_protect_retri)

    shaman_elemental_resto = [
        # Common
        MacroEnum.f_05_shaman__0_common__14102_interrupt_zhTW,
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_05_shaman__0_common__14101_consumable,
        MacroEnum.f_05_shaman__1_elemental_resto__14311_buff_self_zhTW,
        # Act
        MacroEnum.f_05_shaman__0_common__14111_elemental_rotation_zhTW,
        MacroEnum.f_05_shaman__0_common__14112_resto_rotation_zhTW,
        MacroEnum.f_05_shaman__0_common__14114_mb_resto_earth_shield_zhTW,
        MacroEnum.f_05_shaman__1_elemental_resto__14312_burst_zhTW,
    ]
    shaman_elemental_resto = OrderedSet(shaman_elemental_resto)

    druid_feral_balance = [
        # Buff
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_07_druid__0_common__16101_consumable,
        MacroEnum.f_07_druid__3_feral_and_balance__16701_buff_self_bear_zhTW,
        MacroEnum.f_07_druid__3_feral_and_balance__16702_buff_raid_bear_zhTW,
        # Act
        MacroEnum.f_07_druid__3_feral_and_balance__16703_multibox_main_rotate_zhTW,
    ]
    druid_feral_balance = OrderedSet(druid_feral_balance)

    mage_arcane_fire = [
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_09_mage__0_common__18101_consumable,
        MacroEnum.f_09_mage__0_common__18102_interrupt_zhTW,
        MacroEnum.f_09_mage__0_common__18103_buff_self_zhTW,
        MacroEnum.f_09_mage__0_common__18104_buff_team_zhTW,
        # Act
        MacroEnum.f_09_mage__1_arcane_fire__18311_act1_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18312_act2_zhTW,
        MacroEnum.f_09_mage__0_common__18105_act3_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18319_rotation_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18321_burst_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18322_add_debuff_zhTW,
    ]
    mage_arcane_fire = OrderedSet(mage_arcane_fire)

    priest_holy_shadow = [
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_10_priest__0_common__19101_consumable,
        MacroEnum.f_10_priest__3_holy_shadow__19701_buff_self_zhTW,
        MacroEnum.f_10_priest__0_common__19102_buff_raid_zhTW,
        # Act
        MacroEnum.f_10_priest__3_holy_shadow__19702_act1_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19703_act2_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19706_multibox_holy_slow_heal_shadow_main_rotate_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19707_multibox_holy_slow_heal_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19708_multibox_holy_aoe_heal_zhTW,
    ]
    priest_holy_shadow = OrderedSet(priest_holy_shadow)

    warlock_demonology_affiliation = [
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_08_warlock__0_common__17101_consumable,
        # Act
        MacroEnum.f_08_warlock__0_common__17102_elemental_curse_zhTW,
        MacroEnum.f_08_warlock__0_common__17103_tongue_curse_zhTW,
        MacroEnum.f_08_warlock__0_common__17104_corruption_zhTW,
        MacroEnum.f_08_warlock__0_common__17111_demonology_rotation_zhTW,
        MacroEnum.f_08_warlock__0_common__17112_affiliation_rotation_zhTW,
        MacroEnum.f_08_warlock__0_common__17114_spell_stone_zhTW,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17311_burst_zhTW,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17321_add_debuff_zhTW,
    ]
    warlock_demonology_affiliation = OrderedSet(warlock_demonology_affiliation)

    hunter_marksmanship_survival = [
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_04_hunter__0_common__13101_consumable,
        # Act
        MacroEnum.f_04_hunter__0_common__13102_misdirect_zhTW,
        MacroEnum.f_04_hunter__0_common__13103_tranquil_zhTW,
        MacroEnum.f_04_hunter__0_common__13104_pack_aspect_zhTW,
        MacroEnum.f_04_hunter__0_common__13105_viper_aspect_zhTW,
        MacroEnum.f_04_hunter__0_common__13106_burst_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13301_buff_self_zhTW,
        MacroEnum.f_04_hunter__0_common__13111_act1_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13312_act2_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13313_act3_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13314_act4_zhTW,
        MacroEnum.f_04_hunter__0_common__13121_marksmanship_rotation_zhTW,
        MacroEnum.f_04_hunter__0_common__13122_survival_rotation_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13321_add_debuff_zhTW,
    ]
    hunter_marksmanship_survival = OrderedSet(hunter_marksmanship_survival)

    druid_balance_resto = [
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_07_druid__0_common__16101_consumable,
        MacroEnum.f_07_druid__1_balance_resto__16301_buff_self_zhTW,
        MacroEnum.f_07_druid__1_balance_resto__16302_buff_raid_zhTW,
        # Act
        MacroEnum.f_07_druid__1_balance_resto__16303_rotation_zhTW,
        MacroEnum.f_07_druid__1_balance_resto__16304_multibox_slow_heal_zhTW,
    ]
    druid_balance_resto = OrderedSet(druid_balance_resto)

    paladin_holy_protect = [
        # Buff
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_02_paladin__0_common__11101_consumable,
        MacroEnum.f_02_paladin__0_common__11111_clear_debuff_zhTW,
        MacroEnum.f_02_paladin__0_common__11112_raid_divine_sacrifice_zhTW,
        # Act
        MacroEnum.f_02_paladin__0_common__27171_high_int_heal_rotation_zhTW,
        MacroEnum.f_02_paladin__0_common__27172_high_crt_heal_rotation_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11751_mb_periodical_beacon_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11752_mb_periodical_judgement_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11711_act1_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11712_act2_zhTW,
        MacroEnum.f_02_paladin__0_common__11133_holy_rotation_zhTW,
        MacroEnum.f_02_paladin__0_common__11131_protect_rotation_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11731_buff_self_alliance_zhTW,
    ]
    paladin_holy_protect = OrderedSet(paladin_holy_protect)

    dk_blood_tank_unholy_dps = [
        # Buff
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_03_dk__0_common__12101_consumable,
        MacroEnum.f_03_dk__0_common__12123_frost_buff_self_zhTW,
        MacroEnum.f_03_dk__0_common__12122_unholy_buff_self_zhTW,
        # Act
        MacroEnum.f_03_dk__0_common__12111_act1_zhTW,
        MacroEnum.f_03_dk__0_common__12112_act2_zhTW,
        MacroEnum.f_03_dk__0_common__12113_act3_zhTW,
        MacroEnum.f_03_dk__0_common__12114_act4_zhTW,
        MacroEnum.f_03_dk__0_common__12131_tank_rotation_zhTW,
        MacroEnum.f_03_dk__0_common__12132_tank_survival_rotation_zhTW,
    ]
    dk_blood_tank_unholy_dps = OrderedSet(dk_blood_tank_unholy_dps)

    priest_shadow_disco = [
        # Buff
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_10_priest__0_common__19101_consumable,
        MacroEnum.f_10_priest__1_shadow_disco__19301_buff_self_zhTW,
        MacroEnum.f_10_priest__0_common__19102_buff_raid_zhTW,
        # Act
        MacroEnum.f_10_priest__1_shadow_disco__19302_act1_zhTW,
        MacroEnum.f_10_priest__1_shadow_disco__19303_act2_zhTW,
        MacroEnum.f_10_priest__1_shadow_disco__19306_multibox_main_rotate_zhTW,
    ]
    priest_shadow_disco = OrderedSet(priest_shadow_disco)


# ==============================================================================
# END of manual editing
# ==============================================================================
