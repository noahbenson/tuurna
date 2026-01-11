(characters:intro)=
# The Characters of Tu'urna

The cast of {{characters}} of Tu'urna encompasses the spectrum of creatures
(and sometimes entities that are merely creature-like) that one can encounter
in the game world.

The most critical distinction between {{characters}} in the game is that of
{{player_characters}} ({{PCs}}) versus {{nonplayer_characters}} ({{NPCs}}).
{{PCs}} are the {{characters}} whose motivations and intentions are controlled
by the {{players}}; {{NPCs}} are the {{characters}} controlled by the
{{narrator}}.

{{Characters}} can also be categorized as either {{humanoid}} or
{{nonhumanoid}}. All {{PCs}} are {{humanoid}}, as are those {{NPCs}} that are
human or intelligent and sufficiently human-like to use the same rules as the
{{PCs}} for tracking game statistics and capabilities. {{Nonhumanoid}}
{{characters}} use their own game statistics and rules.

This chapter focuses almost exclusively on the rules for {{humanoid}}
{{characters}} (both {{NPCs}} and {{PCs}}, but focusing on the {{PCs}}). The
rules for {{nonhumanoid}} {{characters}} will likely apear in a future
appendix. 

```{note}
This chapter details the core mechanical rules governing {{PCs}} and
{{humanoid}} {{NPCs}} in the game.  However, many implicit rules that apply to
{{humanoids}} are contained in the chapters on [skills](skills:intro) and
[backgrounds](backgrounds:intro) because both the {{backgrounds}} and
{{skills}} can unlock additional rules.
```


(characters:stats)=
## Humanoid Character Statistics

Mechanically, {{humanoids}} consist of a few game statistics:
* Their {{experience}}: the {{levels}} they have attained in all {{skills}}.
* Their {{pools}}: a {{PC}}'s {{luck}}, {{stamina}}, {{sanity}}, and
  {{willpower}}.
* Their {{faculties}}: their physical and mental parts that can be occupied in
  order to perform some task. For example, to swing a sword, one typically must
  occupy at least one {{arm}} and one {{attention}}. Unless a rule grants a
  {{character}} additional {{faculties}}, {{humanoid}} {{characters}} possess
  the following six {{faculties}}:
  * two {{arms}};
  * one pair of {{legs}};
  * one {{breath}};
  * two {{attention}}.
* Their {{status}}: any {{effects}} that are currently affecting them.

The following sections describe the rules for each of these aspects of {{PCs}}.

(characters:stats:experience)=
### Experience: One's Permanent Skills
A {{PC}}'s {{experience}} is described by the collection of all {{levels}} that
the {{character}} has attained in all {{skills}} to which they have access. How
{{PCs}} gain and advance {{skills}} are described in the sections on
[advancement](characters:advancement) and [creation](characters:creation).

(characters:stats:pools)=
### Pools: Exhaustible Resources
A {term}`Pool` is a finite exhaustible resource that can be spent in order to
achieve certain game objectives. If an {term}`Ability` or other rule states
that the {term}`Character` using it spends a point from a {term}`Pool`, then
the {term}`Character` must have at least 1 point in the stated {term}`Pool` or
they are unable to use the ability. Most {term}`Pool`s can also be replenished
in some way, often by spending {term}`Ellipsis Point`s during {term}`Ellipsis`.
{term}`PC`s and {term}`Humanoid`s automatically have four {term}`Pool`s:
{term}`Luck`, {term}`Stamina`, {term}`Sanity`, and {term}`Willpower`.

(characters:luck)=
#### Luck: The Most General Pool
{{Luck}} is the most versatile and important of all the {{pools}}. There are
two uses for {{luck}} during gameplay, neither of which requires any in-game
action by the {{PC}}&mdash;only a decision by the {{player}}:
1. When a {{character}} takes {{damage}}, they may spend any number of {{luck}}
   points that you possess to reduce the {{damage}} by the number of
   {{luck}} spent, to a minimum of 0.
2. Immediately after you make a {{roll}}, you may spend up to 2 {{luck}} to
   increase the {{roll}}'s {{leverage}} by the number of {{luck}} points
   spent. You may choose to do this after you see the outcome of the {{roll}}
   but before you know whether it succeeds or fails.

A {{character}}'s {{luck}} resets at the beginning of every {{scene}}. In each
{{scene}}, each {{PC}} gains an amount of {{luck}} equal to the roll of a
6-sided die. However, the {{player}} does not roll this die until the first
time they elect to use a {{luck}} point. Accordingly, all {{players}} are
initially blind to how lucky their {{PCs}} are in each {{scene}}.

(characters:stamina)=
#### Stamina: Physical Energy
{{Stamina}} represents a {{character}}'s potential energy that can be used to
perform physically difficult tasks. A variety of {{abilities}} that involve
physical activity, such as combat or movement {{abilities}}, require the
expenditure of {{stamina}} to use.

A {{humanoid}} {{character}}'s maximum {{stamina}} is determined by the sum of
their {{level}} in the [fitness](skills:core:fitness) and
[combat](skills:mundane:combat) {{skills}}, and the minimum {{stamina}} is
zero. If a rule would result in a {{character}}'s {{stamina}} exceeding their
maximum, their {{stamina}} instead becomes their maximum.

{{Stamina}} recovers when a {{character}} rests; both the [Sleep and
Rest](skills:natural) {{natural_abilities}} recover {{stamina}}
efficiently. There is no penalty for exhausting one's {{stamina}}, but a
{{character}} with zero {{stamina}} cannot {{activate}} {{abilities}} that
require {{stamina}} nor voluntarily take an action that would result in losing
{{stamina}}. If a rule causes a {{character}} who has zero {{stamina}} to lose
any {{stamina}}, they instead take 1 {{wasting}} {{damage}} for each
{{stamina}} they would have lost.

(characters:sanity)=
#### Sanity: One's Grasp of Reality
{{Sanity}} represents a {{character}}'s grasp of reality and protection from
psychosis. {{Sanity}} can sometimes be spent to empower mental {{abilities}}
or to avoid {{psychic_damage}}.

A {{humanoid}} {{character}}'s maximum {{sanity}} is determined by the sum of
their {{level}} in the [harmony](skills:core:harmony) and
[craft](skills:mundane:craft) {{skills}}, and the minimum {{sanity}} is
zero. If a rule would result in a {{character}}'s {{sanity}} exceeding their
maximum, their {{sanity}} instead becomes their maximum.

{{Sanity}} generally recovers slowly; both the [Sleep and
Meditate](skills:natural) {{natural_abilities}} recover {{sanity}} efficiently,
and the [Relax and Rest](skills:natural) {{natural_abilities}} each recover one
{{sanity}}. When a {{character}}'s {{sanity}} becomes zero, they gain the
[insane](effect:insane) {{effect}}. A {{character}} with zero {{sanity}} cannot
{{activate}} {{abilities}} that require {{sanity}} nor voluntarily take an
action that would result in losing {{sanity}}; however, there is no penalty for
involuntarily losing {{sanity}} when one's {{sanity}} is already zero.

(characters:willpower)=
#### Willpower: One's Mental Potential
{{Willpower}} represents a {{character}}'s mental strength and ability to force
their mind into action. Many mental abilities require the expenditure of
{{willpower}} either to be used or to be empowered.

A {{humanoid}} {{character}}'s maximum {{willpower}} is determined by the sum
of their {{level}} in the [acumen](skills:core:acumen) and
[reason](skills:mundane:reason) {{skills}}, and the minimum {{willpower}} is
zero. If a rule would result in a {{character}}'s {{willpower}} exceeding their
maximum, their {{willpower}} instead becomes their maximum.

{{Willpower}} generally recovers slowly; both the [Sleep and
Relax](skills:natural) {{natural_abilities}} recover two {{willpower}}, and the
[Meditate and Rest](skills:natural) {{natural_abilities}} each recover one
{{willpower}}. There is no penalty for a {{character}} whose {{willpower}} is
zero, but such a {{character}} cannot {{activate}} {{abilities}} that require
{{willpower}} nor voluntarily take an action that would result in losing
{{willpower}}. If something causes a {{character}} with zero {{willpower}} to
lose additional {{willpower}}, they instead take one {{psychic_damage}} per
point of {{willpower}} that would have been lost.

(character:stats:faculties)=
### Faculties: One's Mind and Body
A {{character}}'s {{faculties}} represent their physical and mental parts of
their body and mind that they can engage to perform actions in the world. Each
{{faculty}} is a permanent component of the {{character}} that can be
{{occupied}} to accomplish something or {term}`wounded<Wound>` by {{damage}}.

Many {{abilities}} require the use of one or more {{faculties}} for some amount
of time. For example, swinging a sword typically requires one to {{occupy}} at
least one of their {{arms}}; singing typically requires one to {{occupy}} one's
{{breath}}. Each {{faculty}} can be occupied by at most one
{term}`activity<Activate>` at a time. These requirements are indicated in the
{{ability}} description using the following icons:
* {{arm_icon}}: one {{arm}} is required;
* {{arms_icon}}: two {{arms}} are required;
* {{eye_icon}}: one {{attention}} is required;
* {{eyes_icon}}: two {{attention}} are required;
* {{breath_icon}}: one {{breath}} is required;
* {{legs_icon}}: one pair of {{legs}} is required.

Additionally the icon {{link_icon}} is used to indicate that one's {{link}}
must be {{occupied}}; see the [chapter](skills:path) on {{path_skills}} for
more information.

If multiple {{faculties}} are required, they are listed as a sequence; for
example, "{{arm_icon}}{{eye_icon}}" would indicate that one {{arm}} and one
{{attention}} must be occupied. If an icon is duplicated, then two of that
{{faculty}} are required.

{{Faculties}} must be {{occupied}} for a certain number of {{beats}} for an
{{ability}} to finish {term}`activation<Activate>`, and the {{ability}} is
executed at the end of the final {{beat}} for which it specifies a required
{{faculty}}. An {{ability}} that requires multiple {{beats}} of {{occupied}}
{{faculties}} will use the following formatting rules:
* If one or more {{faculties}} are each required simultaneously for a number of
  {{beats}}, this is written as `FxN` where `F` is the {{faculty}} icon and `N`
  is the number of {{beats}} required. For example {{breath_icon}}{{x}}3
  indicates that one's {{breath}} must be {{occupied}} for 3 simultanous
  {{beats}}; {{breath_icon}}{{legs_icon}}{{x}}2 indicates that one's {{breath}}
  and {{legs}} must both be {{occupied}} for 2 {{beats}}.
* If different {{faculties}} are required on different {{beats}}, this is
  written as `A|B` where `A` is the requirements of the first {{beat}} or
  sequence of {{beats}} and `B` is the requirements of the second {{beat}} or
  sequence of {{beats}}. For example,
  {{arm_icon}}{{eye_icon}}{{x}}2|{{breath_icon}} indicates for two sequential
  {{beats}} both one {{arm}} and one {{attention}} are required followed by one
  {{beat}} on which one's {{breath}} alone is required.
* If an amount of time not measured in {{beats}} is required (such as minutes
  or hours), then that amount of time immediately follows an {{x}} symbol and
  includes one of the units: s, m, h, or d for seconds, minutes, hours, or
  days, respectively. For example, {{breath_icon}}{{x}}1m indicates that one
  must {{occupy}} one's {{breath}} for 1 minute in order to {{activate}} the
  relevant {{ability}}.

(characters:stats:status)=
### Status: One's Afflictions and Effects
A {{character}}'s {{status}} is their current condition, represented by a set
of {{effects}}, each of which causes a specific affliction or advantage to
affect the {{character}}. {{Effects}} are described in detail in the chapter
[](characters:effects).

