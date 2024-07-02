# -*- coding: utf-8 -*-

from .acc_dataset import ds


# fmt: off
class AccountEnum:
    admin = ds.accounts["admin"]
    fat01 = ds.accounts["fat01"]
    fat02 = ds.accounts["fat02"]
    fat03 = ds.accounts["fat03"]
    fat04 = ds.accounts["fat04"]
    fat05 = ds.accounts["fat05"]
    fat06 = ds.accounts["fat06"]
    fat07 = ds.accounts["fat07"]
    fat08 = ds.accounts["fat08"]
    fat09 = ds.accounts["fat09"]
    fat10 = ds.accounts["fat10"]


class RealmEnum:
    admin_AzerothCore = ds.accounts["admin"].realms_mapper["AzerothCore"]
    fat01_AzerothCore = ds.accounts["fat01"].realms_mapper["AzerothCore"]
    fat02_AzerothCore = ds.accounts["fat02"].realms_mapper["AzerothCore"]
    fat03_AzerothCore = ds.accounts["fat03"].realms_mapper["AzerothCore"]
    fat04_AzerothCore = ds.accounts["fat04"].realms_mapper["AzerothCore"]
    fat05_AzerothCore = ds.accounts["fat05"].realms_mapper["AzerothCore"]
    fat06_AzerothCore = ds.accounts["fat06"].realms_mapper["AzerothCore"]
    fat07_AzerothCore = ds.accounts["fat07"].realms_mapper["AzerothCore"]
    fat08_AzerothCore = ds.accounts["fat08"].realms_mapper["AzerothCore"]
    fat09_AzerothCore = ds.accounts["fat09"].realms_mapper["AzerothCore"]
    fat10_AzerothCore = ds.accounts["fat10"].realms_mapper["AzerothCore"]


class CharacterEnum:
    admin_AzerothCore_admin = ds.accounts["admin"].realms_mapper["AzerothCore"].characters_mapper["admin"]
    fat01_AzerothCore_ra = ds.accounts["fat01"].realms_mapper["AzerothCore"].characters_mapper["ra"]
    fat02_AzerothCore_rb = ds.accounts["fat02"].realms_mapper["AzerothCore"].characters_mapper["rb"]
    fat03_AzerothCore_rc = ds.accounts["fat03"].realms_mapper["AzerothCore"].characters_mapper["rc"]
    fat04_AzerothCore_rd = ds.accounts["fat04"].realms_mapper["AzerothCore"].characters_mapper["rd"]
    fat05_AzerothCore_re = ds.accounts["fat05"].realms_mapper["AzerothCore"].characters_mapper["re"]
    fat06_AzerothCore_rf = ds.accounts["fat06"].realms_mapper["AzerothCore"].characters_mapper["rf"]
    fat07_AzerothCore_rg = ds.accounts["fat07"].realms_mapper["AzerothCore"].characters_mapper["rg"]
    fat08_AzerothCore_rh = ds.accounts["fat08"].realms_mapper["AzerothCore"].characters_mapper["rh"]
    fat09_AzerothCore_ri = ds.accounts["fat09"].realms_mapper["AzerothCore"].characters_mapper["ri"]
    fat10_AzerothCore_rj = ds.accounts["fat10"].realms_mapper["AzerothCore"].characters_mapper["rj"]
# fmt: on