(characters:effects)=
# Afflictions and Effects

During gameplay, {{characters}} will inevitably be affected by various
events. Some of these events may give the {{character}} a beneficial condition
such as having confidence or increased dexterity while others will be negative
or neutral, such as being injured or seated.

{{Effects}} can be broadly categorized into two kinds: {{wounds}} and
{{conditions}}. {{Wounds}} are the result of {{damage}} and are subject to
special rules described in the next section. {{Conditions}} are other temporary
changes to a {{character}}'s {{status}} that each follow their own rules.


(characters:effects:wounds)=
## Wounds and Damage

Many game rules, especially {{abilities}}, have the potential to result in
{{damage}} to one or more {{characters}}. Similarly, many {{abilities}} allow a
{{character}} to mitigate {{damage}}. Once all mitigations have been applied,
whatever {{damage}} remains becomes a {{wound}}.

{{Wounds}} are the semi-perminent afflictions to a {{character}} that result
from {{damage}}. All {{wounds}} have a {{severity}} value between 1 and 5, a
{{damage_type}}, and a {{faculty}}. The rules for all of these data are
described below.

```{note}
Multiple rules can simultaneously apply when similar conditions are met, and
many rules usually apply "when a {{character}} takes {{damage}}".  When
multiple rules apply to this kind of situation, the order in which the rules
are resolved is up to the the {{character}} taking the {{damage}}.

For example, suppose a {{humanoid}} {{character}} has an {{ability}} that
allows them, *when they take {{damage}}*, to cut that {{damage}} in half. What
happens if that {{character}} is dealt 6 {{damage}}?

Two rules apply here: (1) when this {{character}} takes more than 5 {{damage}},
they die, and (2) when this {{character}} takes {{damage}}, they can cut it in
half. If the rules are applied to the {{character}} in that order, then the
{{character}} would die. If they are applied in the reverse order, the
{{character}} would live. 

Most {{characters}} in this situation choose to halve the damage before they
evaluate whether it will kill them.
```

(characters:effects:wounds:locations)=
### Wound Locations
Each {{wound}} to a {{humanoid}} {{character}} occurs in a specific location
represented by one of the {{character}}'s {{faculties}}. When a {{character}}
receives a {{wound}}, roll a d6 and assign the {{wound}} to one of the
{{character}}'s {{faculties}} according to the table below. A {{character}} may
have multiple {{wounds}} on the same {{faculty}}, but they cannot have multiple
{{wounds}} of the same {{severity}}.

```{list-table} Wound Locations
:header-rows: 1

* - Die Roll
  - {{Wound}} Location
* - 1
  - {{Attention}} ({{eye_icon}})
* - 2
  - {{Attention}} ({{eye_icon}})
* - 3
  - {{Breath}} ({{lungs_icon}})
* - 4
  - {{Arm}} ({{arm_icon}})
* - 5
  - {{Arm}} ({{arm_icon}})
* - 6
  - {{Legs}} ({{legs_icon}})
```

(characters:effects:wounds:severity)=
### Wound Severity
Each {{wound}} has a {{severity}} rating: 1 (trivial) through 5 (critical). When a
{{character}} takes {{damage}}, they gain a {{wound}} whose severity is equal
to the amount of {{damage}} taken. If a {{character}} ever takes more than 5
{{damage}} at once, they die.

Each {{character}} can only have one {{wound}} of each {{severity}} at a time;
if a {{character}} already has a {{wound}} of the {{severity}} equal to the
taken {{damage}}, then they instead receive a {{wound}} of the next highest
{{severity}} for which they do not aleady have a {{wound}}. If a {{character}}
every takes more than 5 {{damage}}, or if they take 1&ndash;5 {{damage}} but
already have {{wounds}} of that {{severity}} and every higher {{severity}},
then the {{character}} dies.

Each {{wound}} whose {{severity}} is greater than 1 causes the {{character}}
some kind of disadvantage when they {{occupy}} the injured {{faculty}}. Those
disadvantages are detailed in the following table.


```{list-table} Wound Severities
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - A trivial wound such as a scratch, a bruise, or a superficial burn.
    A {{severity}} 1 {{wound}} cause no disability.
* - 2
  - A minor wound such as a slashed arm or a bruised foot.
    Whenever a {{character}} {{occupies}} a {{faculty}} with a {{severity}} 2
    {{wound}}, they must make a {{competency_check}} at the end of the first
    {{beat}} on which the {{faculty}} is occupied. On failure, the 
    {{character}} fails immediately to {{activate}} the {{ability}}. The
    {{competency_check}} is not made on subsequent beats of the
    {term}`activation<Activate>`.
* - 3
  - A moderate wound such as an deep cut or a sprained ankle. At the end of
    every {{beat}} during which a {{faculty}} with a {{severity}} 3 {{wound}}
    is {{occupied}}, the {{character}} must make a {{competency_check}}. On
    failure, the {{character}} fails immediately to {{activate}} the
    {{ability}}.
* - 4
  - A severe wound such as large third degree burns or a badly broken arm. At
    the end of every {{beat}} during which a {{faculty}} with a {{severity}} 4
    {{wound}} is {{occupied}}, the {{character}} must make a
    {{competency_check}} with a {{leverage}} of -1. On failure, the
    {{character}} fails immediately to {{activate}} the {{ability}}.
* - 5
  - A critical wound. A {{character}} with a {{severity}} 5 {{wound}} cannot
    {{occupy}} the wounded {{faculty}}.
```

(characters:effects:wounds:damage-types)=
### Types of Damage
Each kind of {{wound}} is associated with the kind of {{damage}} that caused
it. There are {{damage_types}} that {{damage}} and {{wounds}} can take, each of
which is described below. The {{damage_type}} does not have an effect on any
disability caused by the {{wound}}, but 

(characters:effects:wounds:damage:cutting)=
#### Cutting Damage: Stabbing, Slashing, and Piercing
{term}`Cutting Damage` is caused by slashing, piercing, or stabbing weapons
such as swords, spears, claws, and teeth.

(characters:effects:wounds:damage:crushing)=
#### Crushing Damage: Bludgeoning, Pounding, and Slamming
{term}`Crushing Damage` is caused by blunt trauma from bludegoning or smashing
weapons such as fists, mauls, clubs, and falling rocks.

(characters:effects:wounds:damage:caustic)=
#### Caustic Damage: Fire, Acid, and Friction
{term}`Caustic Damage` is caused by chemical irritants of all forms including
fire, acid, freezing, and friction.

(characters:effects:wounds:damage:wasting)=
#### Wasting Damage: Weakness, Sickness, and Decay
{term}`Wasting Damage` is caused by internal weakness, decay, or loss of
strength such as due to bleeding, sickness, or poison.

(characters:effects:wounds:damage:psychic)=
#### Psychic Damage: Attacks on Mental Stability, Sanity, and Morale
{{Psychic_damage}} is caused by telepathic/psionic mental attacks, loss of
morale, and observations that shake one's sanity. A {{psychic}} {{wound}} might
represent a character's loss of coordination with a particular {{faculty}} or
loss of ability to control it.
