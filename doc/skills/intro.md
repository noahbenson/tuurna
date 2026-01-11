(skills:intro)=
# The Tu'urna Skill System

{{Characters}} in Tu'urna, in terms of game mechanics, are defined
primarily by the {{skills}} they have available to them and their skill
levels. Skills describe a character's ability to interact competently with the
world and are the basis for all game {{rolls}}.


(skills:hierarchy)=
## Skill Hierarchy

{{Skills}} are organized into a shallow hierarchy in which some
{{skills}} are the parents of other skills. If a {{skill}} has any
child {{skills}}, this indicates that the child {{skills}} are specific
subdomains of the parent {{skill}} and are mostly distinct from each
other. In such a case, the parent skill is called the {{fundamental_skill}}
and the child skills on which the {{fundamental_skill}} depends are called
the {{practical_skills}}. For example, Fitness is a {{fundamental_skill}},
and Strength, Endurance, and Agility are its three {{practical_skills}}.

The {{level}} of a {{fundamental_skill}} is equal to the maximum
{{level}} that has been obtained by any two of its 
{{practical_skills}}, and advancement of a {{fundamental_skill}} occurs
automatically when the relevant {{practical_skills}} advance. For example, if
a {{character}}'s {{levels}} in Strength, Endurance, and Agility are 2,
3, and 4, respectively, then their {{level}} in Fitness (the
{{fundamental_skill}} that depends on Strength, Endurance, and Agility)
would be 3 because two of Fitness's {{practical_skills}} are at least
{{level}} 3 (but only one is {{level}} 4). If the {{character}}
then advanced their [Endurance](skills:core:endurance) to {{level}} 4,
their [Fitness](skills:core:fitness) would automatically advance to
{{level}} 4 as well.

{{Fundamental_skills}} can also be advanced using normal methods, but they
can never be advanced to a {{level}} higher than the maximum {{level}}
obtained by their dependant {{practical_skills}}. For example, if a
{{character}} has an [Intuition](skills:path:intuition) {{level}} of 3,
an [Attunement](skills:path:attunement) {{level}} of 4, and a
[Virtue](skills:path:virtue) {{level}} of 0, then they would be able to
increase their [Intuition](skills:path:intuition) to {{level}} 4 because at
least one of its dependant {{practical_skills}} is greater than or equal
to 4. They would then be unable to advance their
[Intuition](skills:path:intuition) to {{level}} 5, however, because neither
of the {{practical_skills}} [Attunement](skills:path:attunement) are high
enough.


(skills:levels)=
## Skill Levels

A {{character}}'s ability at a particular {{skill}} is measured by
their {{level}} in that {{skill}}. Levels must be a non-negative
integer less than 13. Each {{skill}} documents what abilities, if any, are
available to a {{character}} at each {{level}}, and all {{rolls}}
of a {{skill}} are made using a number of dice equal to the {{level}}
(see also, [Rolls](/gameplay/rolls)). The following table explains
approximately how skill levels should be interpreted.

```{list-table} Skill Levels
:header-rows: 1
:name: skill-levels

* - Level
  - Name
  - Description
* - 0
  - unskilled
  - The character cannot attempt the skill.
* - 1
  - novice
  - The character can attempt the skill and usually succeeds at
    {{difficulty}} 1 (trivial) {{checks}} but only occasionally
    succeeds at {{difficulty}} 2 (very easy) {{checks}}.
* - 2
  - practitioner
  - The character succeeds at {{difficulty}} 2 (very easy) {{checks}}
    about half the time.
* - 3
  - amateur
  - The character succeeds at {{difficulty}} 3 (easy) {{checks}}
    about half the time and occasionally succeeds at {{difficulty}} 4 
    (mundane) {{checks}}.
* - 4
  - proficient
  - The character succeeds about half the time at {{checks}} of 
    {{difficulty}} 4 (mundane) and usually succeeds at easier tasks.
* - 5
  - skilled
  - The character succeeds about half the time at {{checks}} of 
    {{difficulty}} 5 (moderate) and usually succeeds at easier tasks.
* - 6
  - expert
  - The character succeeds slightly less than half the time at {{checks}}
     of {{difficulty}} 6 (challenging) and about one time in four at
n     {{difficulty}} 7 (difficult), but typically succeeds on easier tasks.
* - 7
  - virtuoso
  - The character succeeds slightly less than half the time at {{checks}}
    of {{difficulty}} 7 (difficult) and about one time in four at
    {{difficulty}} 8 (very difficult).
* - 8
  - master
  - The character succeeds slightly less than half the time at {{checks}}
    of {{difficulty}} 8 (very difficult) and about one time in four at 
    {{difficulty}} 9 (nearly impossible).
* - 9
  - grandmaster
  - The height of mortal achievement; the character usually succeeds at 
    {{checks}} of {{difficulty}} 8 (very difficult) and succeeds at
    {{checks}} of {{difficulty}} 10 (impossible) about one time in
    four.
* - 10
  - uncanny
  - The character has an uncanny ability and can succeed at {{checks}} of
    {{difficulty}} 10 (impossible) slightly less than half of the time.
* - 11
  - supernatural
  - The character's abilities are clearly supernatural. They can succeed at 
    {{checks}} of {{difficulty}} 10 (impossible) slightly more than
    half of the time.
* - 12
  - godlike
  - The character's abilities rival those of gods. They can succeed at 
    {{checks}} of {{difficulty}} 10 (impossible) most of the time.
```

(skills:levels:abilities)=
### Abilities: the Elements of Skills

As a {{character}} advances their {{level}} in a particular {{skill}}, they may
gain subskills called {{abilities}}. {{Abilities}} are said to be of a given
{{level}} when they are listed at that {{level}}. While not every {{level}} of
every {{skill}} contains distinct {{abilities}}, most contain at least one.

All {{abilities}} fall into one of three categories, which are listed
immediately after their {{ability}} names in the relevant {{skill}} document:
{{passive}}, {{active}}, and {{ellipsis}}. {{Passive}} {{abilities}} describe
their {{effects}}, and these {{effects}} always apply to any {{character}} who
has attained the {{ability}}'s {{level}} in the relevant {{skill}}.  {{Active}}
{{abilities}} must be explicitly {{activated}} by the {{character}} during a
{{scene}} or {{tension}}, and their description includes any relevant
requirements such as the circumstances under which the {{ability}} can be used
and the {{faculty}} requirements of the {{ability}}'s
{term}`activation<Activate>`.  {{Ellipsis_abilities}} can be used only
during {{ellipsis}}, and their descriptions list their requirements. The cost
of an {{ellipsis}} ability in {{ellipsis_points}} is always provided
immediately after the "{{ellipsis}}" tag that follows the {{ability}}'s name in
the relevant {{skill}} document.

Most {{active}} {{abilities}} can only be used under certain
circumstances. Some {{skills}} place restrictions on their use that are
explained in their descriptions; such restrictions apply to all {{abilities}}
of the {{skill}}. Each {{ability}}'s description can also contains additional
rules about when and how it can be used. Most {{active}} {{abilities}} require
a small amount of activity on the part of the {{player_character}} ({{PC}});
for example, in order to hit a target with a sword, one must first spend a bit
of time swinging the sword. During {{tension}}, these brief activities are
tracked explicitly, usually by requiring one or more of a {{character}}'s
{{faculties}} to be {{occupied}} for a certain number of {{beats}}. The
{{faculty}} requirements of each {{active}} {{ability}} are represented by a
sequence of icons that are explained in the [faculties
section](characters:stats:faculties) of the [characters
chapter](characters:intro).

A {{character}} may attempt to use any {{ability}} for which they have
attained the {{ability}}'s {{level}} in its associated
{{skill}}. Additionally, at the {{narrator}}'s discretion, a
{{character}} may attempt to use an {{ability}} of a {{skill}} for
which they have not attaned the required {{level}}. In such cases, an
additional roll called a {{competency_check}} is required. A
{{competency_check}} for a given {{ability}} is just a {{skill}}
{{check}} whose {{difficulty}} is the {{level}} of the
{{ability}} being attempted.


(skills:access)=
## How Do Characters Gain Access to Skills?

{{Skills}} are categorized into four broad types that differ primarily in
how a {{character}} gains access to it. A {{character}} cannot advance
a {{skill}} unless a rule allows them to:
1. **{{Core_skills}}** are available to all {{characters}}. All
   {{PCs}} start with a value of 1 in every {{core_skill}}.
2. **{{Mundane_skills}}** are {{skills}} that can be obtained via a
   {{character}}'s {{background}} or {{backgrounds}}. When a {{character}}
   gains access to a {{fundamental}} {{mundane_skill}}, they automatically gain
   1 level of all {{practical_skills}} that depend on it.
3. **{{Path_skills}}** are {{skills}} that provide a {{character}} with a means
   of accessing the {{domain_skills}}.  {{PCs}} choose one {{path_skill}}
   during [Character Creation](characters:creation), gaining one {{level}} of
   it and its {{fundamental_skill}}.
3. **{{Domain_skills}}** are skills that are associated with {{characters}},
   such as the {{PCs}}, that are exceptional in some way. Each
   {{domain_skill}}'s description provides a list of {{path_skills}} with which
   they are compatible along with a minimum {{level}}. (If no {{level}} is
   listed for a {{path_skill}}, then the minimum {{level}} is 1.)
   {{characters}} can advance any {{domain_skill}} for which they have obtained
   the required {{level}} of any compatible {{path_skill}}.

Once a character has gained access to a {{skill}}, they can advance it
under the normal rules of advancement. More information on skill advancement
can be found in the [Advancement Section](characters:advancement) of the
[Chapter on Characters](characters:intro).


(skills:natural)=
## Natural Abilities: Abilities without Skills

In addition to the {{abilities}} normally granted by
{{skills}}, there are a handful of {{abilities}} that can be
used by any {{character}} without any {{skill}} requirement. These
{{skills}} are considered innate to the {{character}}, thus they cannot
be failed due to a {{competency_check}}.

The {{natural_abilities}} are:
* **Sleep**. {{Ellipsis}}: 2&ndash;4 {{ellipsis_points}}. You sleep for
  a period, recovering 4 {{stamina}}, 4 {{willpower}}, and 4
  {{sanity}} for each point spent. While sleeping, you are unconscious and
  unaware of your surroundings.
* **Rest**. {{Ellipsis}}: 1 {{ellipsis_point}}. You rest for a short period,
  recovering 2 {{stamina}}, 1 {{willpower}}, and 1 {{sanity}}.
* **Meditate**. {{Ellipsis}}: 1 {{ellipsis_point}}. You spend a short period of
  time performing some ritual that is personally soothing or meaningful to you,
  such as prayer, meditation, or art, recovering 1 {{stamina}}, 1
  {{willpower}}, and 2 {{sanity}}.
* **Relax**. {{Ellipsis}}: 1 {{ellipsis_point}}. You spend a short period of
  time passing time in a way that is relaxing and enjoyable to you, such as
  playing cards, reading, or daydreaming, recovering 1 {{stamina}}, 2
  {{willpower}}, and 1 {{sanity}}.
