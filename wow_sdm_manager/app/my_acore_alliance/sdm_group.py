# -*- coding: utf-8 -*-

"""
This module can help you organize your enum into group, made it easier to
construct mappings later.
"""

from ordered_set import OrderedSet
from wow_sdm_manager.vendor.importer import wow_sdm
from wow_sdm_manager.app.my_acore_alliance.sdm_enum import MacroEnum


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

    acc_common_mb_special = [
        MacroEnum.f_00_common__6001_mb_special1,
        MacroEnum.f_00_common__6002_mb_special2,
        MacroEnum.f_00_common__6003_mb_special3,
    ]
    acc_common_mb_special = OrderedSet(acc_common_mb_special)

    # --------------------------------------------------------------------------
    # paladin
    # --------------------------------------------------------------------------
    paladin_common = [
        MacroEnum.f_02_paladin__0_common__11001_clear_debuff_zhTW,
        MacroEnum.f_02_paladin__0_common__11002_raid_divine_sacrifice_zhTW,
        MacroEnum.f_02_paladin__0_common__11151_gm_consumable,
    ]
    paladin_common = OrderedSet(paladin_common)

    paladin_protect_retri = [
        *paladin_common,
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_02_paladin__1_protect_retri__11311_buff_self_alliance_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11301_act1_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11302_act2_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11303_act3_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11304_act4_zhTW,
        MacroEnum.f_02_paladin__1_protect_retri__11305_rotation_zhTW,
    ]
    paladin_protect_retri = OrderedSet(paladin_protect_retri)

    paladin_retri_holy = [
        *paladin_common,
    ]
    paladin_retri_holy = OrderedSet(paladin_retri_holy)

    paladin_holy_protect = [
        *paladin_common,
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_02_paladin__3_holy_protect__11701_act1_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11702_act2_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11703_buff_self_alliance_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11704_rotation_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11731_mb_periodical_beacon_zhTW,
        MacroEnum.f_02_paladin__3_holy_protect__11732_mb_periodical_judgement_zhTW,
        MacroEnum.f_02_paladin__0_common__27171_mb_high_int_heal_rotation_zhTW,
        MacroEnum.f_02_paladin__0_common__27172_mb_high_crt_heal_rotation_zhTW,
    ]
    paladin_holy_protect = OrderedSet(paladin_holy_protect)

    # --------------------------------------------------------------------------
    # dk
    # --------------------------------------------------------------------------
    dk_common = [
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_03_dk__0_common__12151_gm_consumable,
        MacroEnum.f_03_dk__0_common__12111_act1_zhTW,
        MacroEnum.f_03_dk__0_common__12112_act2_zhTW,
        MacroEnum.f_03_dk__0_common__12113_act3_zhTW,
        MacroEnum.f_03_dk__0_common__12114_act4_zhTW,
        MacroEnum.f_03_dk__0_common__12131_tank_rotation_zhTW,
        MacroEnum.f_03_dk__0_common__12132_tank_survival_rotation_zhTW,
    ]
    dk_common = OrderedSet(dk_common)

    dk_blood_tank_unholy_dps = [
        *dk_common,
        MacroEnum.f_03_dk__0_common__12123_frost_buff_self_zhTW,
        MacroEnum.f_03_dk__0_common__12122_unholy_buff_self_zhTW,
    ]
    dk_blood_tank_unholy_dps = OrderedSet(dk_blood_tank_unholy_dps)

    # --------------------------------------------------------------------------
    # shaman
    # --------------------------------------------------------------------------
    shaman_common = [
        MacroEnum.f_05_shaman__0_common__14101_interrupt_zhTW,
        MacroEnum.f_05_shaman__0_common__14131_mb_resto_periodic_earth_shield_zhTW,
        MacroEnum.f_05_shaman__0_common__14151_gm_consumable,
    ]
    shaman_common = OrderedSet(shaman_common)

    shaman_elemental_resto = [
        *shaman_common,
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_05_shaman__1_elemental_resto__14311_buff_self_zhTW,
        MacroEnum.f_05_shaman__1_elemental_resto__14312_burst_zhTW,
        MacroEnum.f_05_shaman__1_elemental_resto__14331_mb_main_rotation_zhTW,
    ]
    shaman_elemental_resto = OrderedSet(shaman_elemental_resto)

    shaman_resto_enhancement = [
        *shaman_common,
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_05_shaman__2_resto_enhancement__14511_buff_self_zhTW,
        MacroEnum.f_05_shaman__2_resto_enhancement__14512_burst_zhTW,
        MacroEnum.f_05_shaman__2_resto_enhancement__14531_mb_main_rotation_zhTW,
    ]
    shaman_resto_enhancement = OrderedSet(shaman_resto_enhancement)

    shaman_enhancement_elemental = [
        *shaman_common,
    ]
    shaman_enhancement_elemental = OrderedSet(shaman_enhancement_elemental)

    # --------------------------------------------------------------------------
    # hunter
    # --------------------------------------------------------------------------
    hunter_common = [
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_04_hunter__0_common__13151_gm_consumable,
        MacroEnum.f_04_hunter__0_common__13102_misdirect_zhTW,
        MacroEnum.f_04_hunter__0_common__13103_tranquil_zhTW,
        MacroEnum.f_04_hunter__0_common__13104_pack_aspect_zhTW,
        MacroEnum.f_04_hunter__0_common__13105_viper_aspect_zhTW,
        MacroEnum.f_04_hunter__0_common__13106_burst_zhTW,
        MacroEnum.f_04_hunter__0_common__13111_act1_zhTW,
    ]
    hunter_common = OrderedSet(hunter_common)

    hunter_marksmanship_survival = [
        *hunter_common,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13301_buff_self_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13312_act2_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13313_act3_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13314_act4_zhTW,
        MacroEnum.f_04_hunter__0_common__13121_marksmanship_rotation_zhTW,
        MacroEnum.f_04_hunter__0_common__13122_survival_rotation_zhTW,
        MacroEnum.f_04_hunter__1_marksmanship_survival__13351_gm_add_debuff_zhTW,
    ]
    hunter_marksmanship_survival = OrderedSet(hunter_marksmanship_survival)

    hunter_survival_beast = [
        *hunter_common,
    ]
    hunter_survival_beast = OrderedSet(hunter_survival_beast)

    hunter_beast_marksmanship = [
        *hunter_common,
    ]
    hunter_beast_marksmanship = OrderedSet(hunter_beast_marksmanship)

    # --------------------------------------------------------------------------
    # druid
    # --------------------------------------------------------------------------
    druid_common = [
        MacroEnum.f_07_druid__0_common__16151_gm_consumable,
        MacroEnum.f_07_druid__0_common__16102_bear_and_stun_zhTW,
        MacroEnum.f_07_druid__0_common__16103_cat_and_dash_zhTW,
        MacroEnum.f_07_druid__0_common__16104_cat_and_prowl_zhTW,
    ]

    druid_feral_balance = [
        *druid_common,
        MacroEnum.f_00_common__2001_buff_physics_dps,
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2003_buff_tank,
        MacroEnum.f_07_druid__3_feral_and_balance__16701_buff_self_bear_zhTW,
        MacroEnum.f_07_druid__3_feral_and_balance__16702_buff_raid_bear_zhTW,
        MacroEnum.f_07_druid__3_feral_and_balance__16731_multibox_main_rotate_bear_zhTW,
    ]
    druid_feral_balance = OrderedSet(druid_feral_balance)

    druid_balance_resto = [
        *druid_common,
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_07_druid__1_balance_resto__16301_buff_self_zhTW,
        MacroEnum.f_07_druid__1_balance_resto__16302_buff_raid_zhTW,
        MacroEnum.f_07_druid__1_balance_resto__16331_main_rotation_zhTW,
        MacroEnum.f_07_druid__1_balance_resto__16332_mb_slow_heal_zhTW,
    ]
    druid_balance_resto = OrderedSet(druid_balance_resto)

    druid_resto_feral = [
        *druid_common,
    ]
    druid_resto_feral = OrderedSet(druid_resto_feral)

    # --------------------------------------------------------------------------
    # warlock
    # --------------------------------------------------------------------------
    warlock_common = [
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_08_warlock__0_common__17101_corruption_zhTW,
        MacroEnum.f_08_warlock__0_common__17102_elemental_curse_zhTW,
        MacroEnum.f_08_warlock__0_common__17103_tongue_curse_zhTW,
        MacroEnum.f_08_warlock__0_common__17151_gm_consumable,
    ]
    warlock_common = OrderedSet(warlock_common)

    warlock_demonology_affiliation = [
        *warlock_common,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17301_burst_zhTW,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17302_buff_self_zhTW,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17331_mb_main_rotate_zhTW,
        MacroEnum.f_08_warlock__1_demonology_affiliation__17351_gm_add_debuff_zhTW,
    ]
    warlock_demonology_affiliation = OrderedSet(warlock_demonology_affiliation)

    warlock_affiliation_destruction = [
        *warlock_common,
    ]
    warlock_affiliation_destruction = OrderedSet(warlock_affiliation_destruction)

    warlock_destruction_demonology = [
        *warlock_common,
    ]
    warlock_destruction_demonology = OrderedSet(warlock_destruction_demonology)

    # --------------------------------------------------------------------------
    # mage
    # --------------------------------------------------------------------------
    mage_common = [
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_09_mage__0_common__18101_interrupt_zhTW,
        MacroEnum.f_09_mage__0_common__18102_buff_self_zhTW,
        MacroEnum.f_09_mage__0_common__18103_buff_team_zhTW,
        MacroEnum.f_09_mage__0_common__18104_act3_zhTW,
        MacroEnum.f_09_mage__0_common__18105_burst_zhTW,
        MacroEnum.f_09_mage__0_common__18151_gm_consumable,
    ]
    mage_common = OrderedSet(mage_common)

    mage_arcane_fire = [
        *mage_common,
        MacroEnum.f_09_mage__1_arcane_fire__18301_act1_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18302_act2_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18331_mb_main_rotation_zhTW,
        MacroEnum.f_09_mage__1_arcane_fire__18351_gm_act1_with_debuff_zhTW,
    ]
    mage_arcane_fire = OrderedSet(mage_arcane_fire)

    mage_fire_frost = [
        *mage_common,
        MacroEnum.f_09_mage__2_fire_frost__18551_gm_act1_with_debuff_zhTW,
    ]
    mage_fire_frost = OrderedSet(mage_fire_frost)

    mage_frost_arcane = [
        *mage_common,
        MacroEnum.f_09_mage__3_frost_arcane__18731_mb_main_rotation_zhTW,
        MacroEnum.f_09_mage__3_frost_arcane__18751_gm_act1_with_debuff_zhTW,
    ]
    mage_frost_arcane = OrderedSet(mage_frost_arcane)

    # --------------------------------------------------------------------------
    # priest
    # --------------------------------------------------------------------------
    priest_common = [
        MacroEnum.f_00_common__2002_buff_caster_dps,
        MacroEnum.f_00_common__2004_buff_healer,
        MacroEnum.f_10_priest__0_common__19101_buff_raid_zhTW,
        MacroEnum.f_10_priest__0_common__19151_gm_consumable,
    ]

    priest_shadow_disc = [
        *priest_common,
        MacroEnum.f_10_priest__1_shadow_disc__19301_buff_self_zhTW,
        MacroEnum.f_10_priest__1_shadow_disc__19302_act1_zhTW,
        MacroEnum.f_10_priest__1_shadow_disc__19303_act2_zhTW,
        MacroEnum.f_10_priest__1_shadow_disc__19331_mb_main_rotate_zhTW,
        MacroEnum.f_10_priest__1_shadow_disc__19332_mb_heal_tank_rotate_zhTW,
    ]
    priest_shadow_disc = OrderedSet(priest_shadow_disc)

    priest_disc_holy = [
        *priest_common,
        MacroEnum.f_10_priest__2_disc_holy__19501_buff_self_zhTW,
        MacroEnum.f_10_priest__2_disc_holy__19531_mb_main_rotate_zhTW,
        MacroEnum.f_10_priest__2_disc_holy__19532_mb_heal_tank_rotate_zhTW,
    ]
    priest_disc_holy = OrderedSet(priest_disc_holy)

    priest_holy_shadow = [
        *priest_common,
        MacroEnum.f_10_priest__3_holy_shadow__19701_buff_self_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19702_act1_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19703_act2_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19731_mb_main_rotate_zhTW,
        MacroEnum.f_10_priest__3_holy_shadow__19732_mb_heal_tank_rotate_zhTW,
    ]
    priest_holy_shadow = OrderedSet(priest_holy_shadow)


# ==============================================================================
# END of manual editing
# ==============================================================================
