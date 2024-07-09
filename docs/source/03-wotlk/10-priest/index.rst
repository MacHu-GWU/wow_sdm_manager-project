WotLK Priest
==============================================================================


Common
------------------------------------------------------------------------------


刷团队 Buff
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
一键给团队上团队 Buff. 按顺序上群体耐, 群体精神, 群体暗抗. 接下来的 3 个盾会在第一个盾卡住. 这是有意为之, 使得如果你不断按这个宏的情况下, 大约在 20 秒之内只会生效一次 (刷前三个技能 5 秒, 盾会卡住 15 秒). 这样可以配合骑士给全团刷祝福的周期 (大约也是不到 20 秒)

.. admonition:: 刷团队 Buff

    **zhTW**

    .. code-block:: python

        #showtooltip
        /target player
        /castsequence [nochanneling] reset=target 堅韌禱言,精神禱言,暗影防護禱言,真言術:盾,真言術:盾,真言術:盾

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


Shadow
------------------------------------------------------------------------------


暗牧输出一键宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
暗牧输出一键宏技能循环. 主要思路是以 2 个吸血鬼之触的周期为循环. 由于噬灵瘟疫和吸血鬼之触的持续时间不是整数倍的关系, 所以你无法保证 100% 完美衔接, 只能尽可能保证 DPS 高的吸血鬼之触技能的覆盖. 而中间可能有个几秒钟噬灵瘟疫断档, 但是问题不大.

注意这两个 Dot 技能的持续时间都会受到急速的影响. 急速越高, 周期越短. 所以要根据你的急速来调整宏的重置时间以及技能循环. 另外, 由于精神鞭笞能刷新痛的持续时间, 所以这个宏是建立在你已经上过痛的前提下的. 如果是多开场景下, 你可能会忘记手动上痛 (多开时有一个单独的按键可以一键上这种一场战斗只要丢一次的技能), 所以我们可以技能循环中加入痛. 这样虽然会浪费 一个 GCD, 但是比起忘记上痛浪费的 DPS 这样还是很划算的.

注意一定要加入 ``[nochanneling]`` 来防止在施放重要的引导技能的过程中被打断.

.. admonition:: 6500 GS, 人类操作

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=15 吸血之觸,心靈震爆,噬靈瘟疫,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,吸血之觸,心靈震爆,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


.. admonition:: 6500 GS, MB 多开, 主要是穿插了痛

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=15 吸血之觸,心靈震爆,噬靈瘟疫,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,暗言術:痛,吸血之觸,心靈震爆,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,吸血之觸,心靈震爆,噬靈瘟疫,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,吸血之觸,心靈震爆,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,吸血之觸,心靈震爆,噬靈瘟疫,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞,吸血之觸,心靈震爆,精神鞭笞,精神鞭笞,精神鞭笞,精神鞭笞

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


暗牧 Buff 自己
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
暗牧给自己依次上暗影形态, 吸血鬼的拥抱, 心灵之火, 进入战斗状态.

.. admonition:: 暗牧 Buff 自己

    **zhTW**

    .. code-block:: python

        #showtooltip
        /cast [nostance] 暗影形態
        /castsequence reset=target 吸血鬼的擁抱, 心靈之火

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


暗牧 Act 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
按 1 上痛, 按 Alt 1 丢灭.

.. admonition:: 暗牧 Act 1

    **zhTW**

    .. code-block:: python

        #showtooltip
        /cast [mod:alt] 暗言術:死; 暗言術:痛

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


暗牧 Act 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
按 2 精神鞭笞, 按 Alt 2 噬灵瘟疫.

.. admonition:: 暗牧 Act 2

    **zhTW**

    .. code-block:: python

        #showtooltip
        /cast [nochanneling,mod:alt] 噬靈瘟疫; [nochanneling] 精神鞭笞

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


Disc
------------------------------------------------------------------------------


戒律牧全团套盾一键宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
戒律牧在团队中的主要任务是全团套盾, 所以只要随机选择团队成员并给他们套盾即可.

注意一定要加入 ``[nochanneling]`` 来防止在施放重要的引导技能的过程中被打断.

.. admonition:: 戒律牧全团套盾一键宏

    **zhTW**

    .. code-block:: python

        #showtooltip
        /targetraid
        /cast [nochanneling] 真言術:盾

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


MB 戒律牧刷坦克的血一键宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
在多开的时候戒律牧给掉血了但是血量不危机的坦克刷血. 一般是先上愈合祷言, 然后丢苦修, 然后快速治疗. 之所以不丢盾是因为可能目标身上已经有盾了, 会导致整个技能循环卡住放不出去技能.

注意一定要加入 ``[nochanneling]`` 来防止在施放重要的引导技能的过程中被打断.

.. admonition:: MB 戒律牧刷坦克的血一键宏

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=10 癒合禱言,,懺悟,,快速治療,,快速治療,,快速治療,,

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


Holy
------------------------------------------------------------------------------


神圣牧全团丢恢复一键宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
神牧在团队中的主要任务是全团丢恢复和群刷, 所以只要随机选择团队成员并给他们丢恢复并穿插治疗之环即可.

注意一定要加入 ``[nochanneling]`` 来防止在施放重要的引导技能的过程中被打断.

.. admonition:: 神圣牧全团丢恢复一键宏

    **zhTW**

    .. code-block:: python

        #showtooltip
        /targetraid
        /castsequence [nochanneling] 恢復,恢復,恢復,恢復,恢復,治療之環

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip


MB 神圣牧刷坦克的血一键宏
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
在多开的时候神圣牧给掉血了但是血量不危机的坦克刷血. 一般是先上愈合祷言, 然后丢恢复, 然后丢快速治疗. 之所以不丢盾是因为可能目标身上已经有盾了, 会导致整个技能循环卡住放不出去技能.

注意一定要加入 ``[nochanneling]`` 来防止在施放重要的引导技能的过程中被打断.

.. admonition:: MB 神圣牧刷坦克的血一键宏

    **zhTW**

    .. code-block:: python

        #showtooltip
        /castsequence [nochanneling] reset=10 癒合禱言,,恢復,,快速治療,,快速治療,,快速治療,,

    **zhCN**

    .. code-block:: python

        #showtooltip

    **enUS**

    .. code-block:: python

        #showtooltip
