---
substitutions:
   Ability: "{term}`Ability`"
   Abilities: "{term}`Abilities<Ability>`"
   ability: "{term}`ability<Ability>`"
   abilities: "{term}`abilities<Ability>`"
   Character: "{term}`Character`"
   Characters: "{term}`Characters<Character>`"
   character: "{term}`character<Character>`"
   characters: "{term}`characters<Character>`"
   Damage: "{term}`Damage`"
   damage: "{term}`damage<Damage>`"
   Damage type: "{term}`Damage type<Damage Type>`"
   Damage types: "{term}`Damage types<Damage Type>`"
   damage type: "{term}`damage type<Damage Type>`"
   damage types: "{term}`damage types<Damage Type>`"
   Faculty: "{term}`Faculty`"
   Faculties: "{term}`faculties<Faculty>`"
   faculty: "{term}`faculty<Faculty>`"
   faculties: "{term}`faculties<Faculty>`"
   Humanoid: "{term}`Humanoid`"
   Humanoids: "{term}`Humanoids<Humanoid>`"
   humanoid: "{term}`humanoid<Humanoid>`"
   humanoids: "{term}`humanoids<Humanoid>`"
   Nonhumanoid: "{term}`Nonhumanoid`"
   Nonhumanoids: "{term}`Nonhumanoids<Nonhumanoid>`"
   nonhumanoid: "{term}`nonhumanoid<Nonhumanoid>`"
   nonhumanoids: "{term}`nonhumanoids<Nonhumanoid>`"
   PC: "{term}`PC`"
   PCs: "{term}`PCs<PC>`"
   Resource: "{term}`Resource`"
   Resources: "{term}`Resources<Resource>`"
   resource: "{term}`resource<Resource>`"
   resources: "{term}`resources<Resource>`"
   Severity: "{term}`Severity`"
   Severities: "{term}`Severities<Severity>`"
   severity: "{term}`severity<Severity>`"
   severities: "{term}`severities<Severity>`"
   Wound: "{term}`Wound`"
   Wounds: "{term}`Wounds<Wound>`"
   wound: "{term}`wound<Wound>`"
   wounds: "{term}`wounds<Wound>`"
---

(characters:effects)=
# Afflictions and Effects


(characters:effects:wounds)=
## Wounds and Damage

Many game rules, especially {{abilities}}, have the potential to result in
{{damage}} to one or more {{characters}}. Similarly, many {{abilities}} allow a
{{character}} to mitigate {{damage}}. Once all mitigations have been applied,
whatever {{damage}} remains becomes a {{wound}}.

{{Wounds}} are the semi-perminent afflictions to a {{character}} that result
from {{damage}}. All {{wounds}} have a {{severity}} value between 1 and 5, a
{{damage type}}, and a {{faculty}}. The rules for all of these data are
descrined below.

```{note}
Multiple rules can apply when similar conditions are met, and conditions like
"when a {{character}} takes {{damage}}" are among the most common conditions.
When multiple rules apply to this kind of situation, the order in which the
rules are resolved is up to the the {{character}} taking the {{damage}}.

For example, suppose a {{humanoid}} {{character}} has an {{ability}} that
allows them, *when they take {{damage}}*, to cut that {{damage}} in half. What
happens if that {{character}} is dealt 6 {{damage}}?

Two rules apply here: (1) when this {{character}} takes more than 5 {{damage}},
hey die, and (2) when this {{character}} takes {{damage}}, they can cut it in
half. If the rules are applied to the {{characger}} in that order, then the
{{character}} would die. If they are applied in the reverse order, the
{{character}} would live. 

Most {{characters}} in this situation choose to halve the damage before they
evaluate whether it will kill them.
```

(characters:effects:wounds:locations)=
### Wound Locations
Each {{wound}} to a {{humanoid}} {{character}} occurs in a specific location
represented by one of the {{character}}'s {{faculties}}. 

(characters:effects:wounds:severity)=
### Wound Severity
Each kind of {{wound}} has five levels of {{severity}}: 1 (trivial) through 5
(critical). When a {{character}} takes {{damage}}, 

Each {{character}} can only have one {{wound}} of each {{severity}} at a time; if a {{character}} already has a {{wound}} of the {{severity}} equal to the takes {{damage}} 

If a
{{humanoid}} {{character}} takes more than 5 {{damage}}, they die. Otherwise,
they receive a {{wound}} whose {{severity}} is greater than or equal to the
{{damage}} taken. If the {{character}} has no existing {{wound}} of the
required {{severity}}, then they receive a {{wound}} of that {{severity}}. If
they already have a {{wound}} of that {{severity}} then they instead receive a
{{wound}} of the next highest {{severity}} for which they do not already have a
{{wound}}. If {{humanoid}} {{character}} already has {{wounds}} of all higher
{{severities}}, then they die.


```{list-table} Wound Severities
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - A minor wound such as a scratch, a bruise, or a superficial burn.
    {term}`Severity` 1 {{Wound}} cause no disability.
* - 2
  - A moderate wound such as a deep slash or a badly bruised foot. A
    {term}`Severity` 2 {term}`Wound` causes some minor disability.
* - 3
  - A severe wound such as an impaling sword or a badly broken leg. A
    {term}`Severity` 3 {term}`Wound` causes some significant disability .
* - 4
  - A critical wound such as a severed hamstring or a severed limb. A
    {term}`Severity` 4 {term}`Wound` causes some permanent disability.
* - 5
  - A mortal wound. A {term}`Character` that gains a {term}`Severity` 5
    {term}`Wound` dies at the end of the current {term}`Round`.
```

(characters:effects:wounds:locations)=
### Wound Locations
All {{wounds}} occur in a specific location.

(characters:effects:wounds:damage-types)=
### Damage Types
Each kind of {term}`Wound` is associated with a specific kind of
{term}`Damage`. Whenever a {term}`Humanoid` takes {term}`Damage`, they receive
a {term}`Wound` whose {term}`Severity` is equal to the {term}`Damage`
taken. {{Wound}} occur on specific {{Resources}} such as When a {term}`Character` receives a {term}`Wound`, the 

There are five kinds of {term}`Damage`, each of which is described below.

(characters:effects:wounds:damage:cutting)=
#### Cutting Damage: Stabbing, Slashing, and Piercing
{term}`Cutting Damage` is caused by slashing, piercing, or stabbing weapons
such as swords, spears, and claws.

```{list-table} Cutting Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - A minor cut or gash.
* - 2
  - A 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```

(characters:effects:wounds:damage:crushing)
#### Crushing Damage: Bludgeoning, Pounding, and Slamming
{term}`Crushing Damage` is caused by blunt trauma from bludegoning or smashing
weapons such as fists, mauls, clubs, and falling rocks.

```{list-table} Crushing Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - 
* - 2
  - 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```

(characters:effects:wounds:damage:cold)
#### Cold Damage: Ice, Frost, and Winter
{term}`Cold Damage` is caused by freezing flesh due to exposure to cold.

```{list-table} Cold Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - 
* - 2
  - 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```


(characters:effects:wounds:damage:caustic)
#### Caustic Damage: Fire, Acid, and Friction
{term}`Caustic Damage` is caused by chemical irritants of all forms including
fire, acid, and friction.

```{list-table} Caustic Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - 
* - 2
  - 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```


(characters:effects:wounds:damage:wasting)
#### Wasting Damage: Weakness, Sickness, and Decay
{term}`Wasting Damage` is caused by internal weakness, decay, or loss of
strength such as due to bleeding, sickness, or poison.

```{list-table} Wasting Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - 
* - 2
  - 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```


(characters:effects:wounds:damage:psychic)
#### Psychic Damage: Attacks on Mental Stability, Sanity, and Morale
{term}`Psychic Damage` is caused by telepathic/psionic mental attacks, loss of
morale, and observations that shake one's sanity.

```{list-table} Psychic Wounds
:header-rows: 1

* - Severity Level
  - Description
* - 1
  - 
* - 2
  - 
* - 3
  - 
* - 4
  - 
* - 5
  - 
```
