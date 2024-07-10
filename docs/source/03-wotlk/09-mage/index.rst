WotLK Mage
==============================================================================


Common
------------------------------------------------------------------------------


刷团队 Buff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一键给团队上团队 Buff. 按顺序上群体智慧. 接下来的 3 个防护冰霜结界会在第一个技能卡住. 这是有意为之, 使得如果你不断按这个宏的情况下, 大约在 30 秒之内只会生效一次 (防护冰霜结界会卡住 30 秒). 这样可以配合骑士给全团刷祝福的周期 (大约也是不到 20 秒).

.. admonition:: 刷团队 Buff

    **zhTW**

    .. code-block:: python

        #showtooltip
        /target player
        /castsequence [nochanneling] reset=target 秘法光輝,防護冰霜結界,防護冰霜結界,防護冰霜結界

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


法师 Buff 自己
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
给自己上 Buff. 先给自己上熔火护甲, 然后给特定法系 DPS 上专注魔法. 这个 /target 的目标就是其他法系 DPS 的名字. 熔火护甲在目标是别人的情况下依然会自动给自己上.

.. admonition:: 法师 Buff 自己

    **zhTW**

    .. code-block:: python

        #showtooltip
        /target rc # 鸟德
        /castsequence reset=target 熔火護甲,魔法凝聚

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


打断施法
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
取消当前施法并智能打断目标施法. 如果焦点存在且是敌人则打断它的施法, 如果焦点的目标存在且是敌人则打断它的施法.

.. admonition:: 打断施法

    **zhTW**

    .. code-block:: python

        #showtooltip
        /stopcasting
        /cast [target=focus,harm] 法術反制; [target=focustarget,harm] 法術反制; [] 法術反制

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


火焰冲击, 灼烧, 魔法增效, 魔法抑制
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
把所有天赋都有的 4 个技能 火焰冲击, 灼烧, 魔法增效, 魔法抑制 绑定到一个键位上以节约动作条. 所有天赋的法师的 3 号键位通常都是这个.

.. admonition:: 打断施法

    **zhTW**

    .. code-block:: python

        #showtooltip
        /cast [mod:alt,help] 魔法增效; [mod:alt,harm] 灼燒; [help] 魔法抑制; [harm] 火焰衝擊; [mod:alt] 魔法增效; [] 魔法抑制

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


法师一键开所有爆发技能
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
法师的爆发技能除了幻象有 GCD, 冰脉, 奥强, 燃烧都没有 GCD, 可以一起开. 没有 GCD 的技能可以放在一个宏里, 不会出现上面的技能放不出来导致下面的技能也放不出来的情况. 例如就算你是火法, 没有冰脉技能, 你依然可以放出下面的燃烧技能.

.. admonition:: 法师一键开所有爆发技能

    **zhTW**

    .. code-block:: python

        #showtooltip
        /stopcasting
        /cast 幻鏡之像
        /cast 冰寒脈動
        /cast 秘法強化
        /cast 燃烧

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


给敌人添加法师有益的 DeBuff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
给法师的中频输出循环技能添加给敌人上 Debuff 的功能. 只能用于单机 GM, 用来模拟团队 Debuff. 这些技能都是在输出循环中 15 秒内肯定会用到的触发类技能, 使得整体按这个键的频率不会太高, 避免一直按的时候造成异常.

Spell ID::

    .aura 54499 # 十字军之心 +3% 被暴击几率
    .aura 47865 # 元素诅咒 +13% 受到的法术伤害, -165 所有抗性
    .aura 22959 # 强化灼烧 +5% 被法术暴击的几率
    .aura 33198 # 苦难 +3% 被法术命中的几率
    .aura 31589 # 减速 移动速度 -60%, 远程攻击间隔 +60%, 施法速度 -30% (用于触发奥系 "折磨弱小" 天赋)

.. admonition:: 给敌人添加法师有益的 DeBuff

    **zhTW**

    .. code-block:: python

        #showtooltip
        /cast [nochanneling] 秘法飛彈 # 奥法用这个
        /cast [nochanneling] 炎爆术 # 火法用这个
        /cast [nochanneling] 霜火箭 # 冰法用这个
        /stopmacro [noharm]
        .aura 54499
        .aura 47865
        .aura 22959
        .aura 33198
        .aura 31589

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


Arcane
------------------------------------------------------------------------------


MB 奥法一键输出宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
奥法的输出主打一个无脑粗暴, 基本就是 3 个或 4 个奥冲一个飞弹. 追求高续航就 3+1, 追求高输出就 4+1.

.. admonition:: 追求高续航

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=15 秘法衝擊,秘法衝擊,秘法衝擊,秘法飛彈

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


.. admonition:: 追求高输出

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=15 秘法衝擊,秘法衝擊,秘法衝擊,秘法衝擊,秘法飛彈

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


Fire
------------------------------------------------------------------------------



Frost
------------------------------------------------------------------------------

