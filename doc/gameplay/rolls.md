# Rolls

Frequently during gameplay, a {{character}} will attempt to do something whose
outcome is not immediately obvious to the {{narrator}}. For example, a
{{character}} may attempt to leap across a cavern or to pick a lock. The
outcomes of such actions depend on the skills of the {{character}} performing
the action. In such cases, the {{narrator}} may use one or more {{rolls}} to
help adjudicate the outcome.


(gameplay:rolls)=
## The Rules of a Roll

All {{rolls}} are made by a {{character}} using a {{skill}}. When the
{{narrator}} calls for a {{roll}}, it is up to them to decide what {{skill}} is
appropriate. To execute the {{roll}}, the {{player}} rolls a number of 6-sided
dice equal to their {{PC}}'s {{level}} in the {{skill}}. Each die whose value
is 1 or 2 counts as a *loss*. Each die whose value is 3 or 4 counts as a
*win*. Each die whose value is 5 or 6 both counts as a *win* and causes an
additional die to be rolled and treated identically. The {{roll}}'s {{score}}
is the total number of *win* values rolled or 9, whichever is lower. If a rule
grants a {{character}} {{supernatural_potential}} in a {{skill}}, then the
{{character}} may achieve a {{score}} as high as 12 when making a {{roll}}
instead of 9.

```{note} 
If a {{player}} repeatedly rolls 5s or 6s, the dice continue to be rerolled,
and successes continue to accumulate. It is thus theoretically possible to
achieve an arbitrarily high {{score}} on any {{roll}}, so long as the
{{character}}'s {{level}} in the {{skill}} is greater than 0.
```

```{note}

It is up to the {{player}} to narrate the course of action of their {{PC}}, and
in so doing they can suggest the use of a particular {{skill}}; for example, if
a {{player}} chooses to bash a door down, they can be reasonably confident that
the {{narrator}} will call for a [Strength](skills:core:strength) {{roll}} or
at least that they won't call for a [Memory](skills:core:memory) {{roll}}. It
remains up to the {{narrator}} to determine when a {{roll}} is required and
which {{skill}} or {{skills}} are relevant to the circumstances.
```

(gameplay:rolls:modifiers)=
### Roll Modifiers: Leverage and Labor
{{Rolls}} are sometimes modified by contextual circumstances in the game or by
other game rules called {{modifiers}}. For example, if one {{character}} uses
an {{ability}} to injure the wrist of another {{character}}, then the injured
{{character}} would likely have a penalty representing the injury's encumbrance
applied to any {{roll}} made using their injured wrist. The size of the penalty
(the {{modifier}}) would likely depend on the effectiveness of the {{ability}}.

There are two kinds of {{modifiers}} applied to {{rolls}}: {{leverage}}, which
adds a flat (potentially negative) value to a {{roll}}'s {{score}}, and
{{labor}}, which causes a certain number of the dice to be rerolled. (Both of
these modifiers are described below.) When executing a {{roll}}, all changes to
{{leverage}} are integrated, as are all changes to {{labor}}, prior to rolling
any dice&mdash;each {{roll}} is executed with a single {{leverage}} and a
single {{labor}} value.

All {{modifiers}} can be applied to a {{roll}} by either a game rule or by the
{{narrator}}. When a game rule affects a {{roll}}, the {{modifier}} is called a
{{specific_modifier}}. When the {{narrator}} affects a {{roll}}, the modifier
is called a {{circumstantial_modifier}}. In general,
{{circumstantial_modifiers}} are awarded by the {{narrator}} due to the
contextual setting of a {{roll}} and/or the effectiveness of the strategy being
employed by a {{character}}.

A {{modifier}} may apply two kinds of changes to a {{roll}}:
1. Usually, {{modifiers}} update the value. For example, "*You gain +1
   {{leverage}} to [Communication](skills:core:communication) {{rolls}}*" or
   "*You gain -2 {{labor}} to [Endurance](skills:core:endurance) {{rolls}}*".
2. Some rules instead set the minimum or maximum value the {{modifier}} can
   take. For example, "*Your minimum {{labor}} for
   [Scholarship](skills:mundane:scholarship) {{rolls}} is 2*" or "*Your maximum
   {{leverage}} for [Tactics](skills:mundane:tactics) {{rolls}} is 3*".

All updates to a {{modifier}} are summed prior to the application of any minima
or maxima. When multiple rules declare different minimum {{modifier}} values
for a {{roll}}, only the rule resulting in the highest minimum {{modifier}}
value is applied; for the maximum, only the rule resulting in the lowest
maximum {{modifier}} value is applied.  When the maximum {{modifier}} value is
less than the minimum {{modifier}} value, the minimum is ignored.

(gameplay:rolls:modifiers:leverage)=
#### What is Leverage?
{{Leverage}} generally represents the extent to which a course of action
will be effective as a means of achieving its goals. A high {{leverage}}
such as +3 means that a {{character}} is guaranteed to perform the
{{roll}} as if their {{skill}} {{level}} were higher than their
true {{level}} due to natural or circumstantial advantages.

Mechanically, a {{roll}}'s {{leverage}} is added to its
{{score}}. Positive {{leverage}} values increase the {{score}}
while negative {{leverage}} values result in a lower {{score}}.

(gameplay:rolls:modifiers:labor)=
#### What is Labor?
{{Labor}} represents a {{character}}'s advantage or disadvantage on a {{roll}}
that is due to their own effort or influence or the effort or influence of
others working against them. Unlike {{leverage}}, which adds a flat number to
the {{score}} of a {{roll}}, {{labor}} gives the {{character}} performing the
{{roll}} either more or fewer dice to {{roll}}. A {{labor}} of +2, for example,
would allow the {{character}} to {{roll}} two additional dice. If a
{{character}}'s {{labor}} on a {{roll}} reduces the number of dice they
{{roll}} below 1, the {{character}} still rolls 1 die.

```{note}

Note that, although {{leverage}} is statistically identical to
{{labor}}&mdash;in that the expected advantage of rolling 1 additional die is 1
additional {{score}}, which is exactly what is provided by a point of
{{leverage}}&mdash;a point of {{labor}} can potentially provides the
{{character}} with either no additional {{score}} or with a bonus to their
{{score}} that is substantially more than 1.
```

(gameplay:rolls:modifiers:examples)=
#### Leverage and Labor Examples

TODO

In the following examples, we rely on two characters: Ylir and Zejhe. Ylir's
{{level}} in the [Armaments](skills:mundane:armaments) {{skill}} is 5; Zejhe's
{{level}} in the [Instinct](skills:core:instinct) {{skill}} is 4 and in the
[Armaments](skills:mundane:armaments) is 2.


## What kinds of situations call for rolls?

Broadly speaking, there are two types of situations that require {{rolls}} to
adjudicate: {{checks}} and {{contests}}.

(gameplay:rolls:checks)=
### Skill Checks
Some narrative situations that arise in gameplay represent attempts to resolve
a static challenge that exist in the world. In such a situation, the outcome
depends only on whether one can apply one's {{skill}} in the moment with
sufficient grace to overcome a fixed {{difficulty}}. Such {{checks}} are in
contrast to contested rolls ({{contests}}) in which one's skill is set against
that of another.

When the {{narrator}} feels that an outcome is uncertain, they must decide on
the {{skill}} (or {{skills}}) that can resolve the {{check}} and the
{{check}}'s {{difficulty}}. The {{character}} or {{characters}} must then
execute the {{roll}}. The {{narrator}} then compares the character's {{score}}
against the {{difficulty}}

```{list-table} Difficulty Levels
:header-rows: 1
:name: difficulty-levels

* - Difficulty
  - Name
  - Description/Examples
* - 1
  - trivial
  - The challenge can be succeeded by almost anyone: tying a simple knot,
    breaking a twig, reading a sign in a language you understand.
* - 2
  - very easy
  - Minimal skill is required: remembering a word or number, throwing a stone
    10 feet.
* - 3
  - easy
  - Minimal skill is required: remembering a sentence or phrase, jumping over a
    small obstacle.
* - 4
  - mundane
  - Moderate skill is required: overhearing a whispered conversation, picking
    a simple lock, solving an algebra problem.
* - 5
  - moderate
  - Moderate skill is required: knowing specific point of etiquette or history,
    picking a simple lock, solving a difficult algebra problem.
* - 6
  - challenging
  - Substantial skill is required: walking a tightrope, quickly breaking a
    cipher, breaking down a sturdy door.
* - 7
  - difficult
  - The challenge is hard to succeed, even for experts: breaking a difficult
    cipher, cracking a well-built safe, convincing an Outsider to assist you.
* - 8
  - very difficult
  - The greatest mortal practitioners of a skill can succeed at a very
    difficult challenge only slightly more than half of the time: remaining
    unseen in plain daylight, developing new maths, outrunning a tiger.
* - 9
  - nearly impossible
  - The greatest mortal practitioners of a skill can only occasionally succeed
    at neraly impossible challenges: performing a wildly outrageous combat
    maneuver, building an intelligent automaton, magically protecting an entire
    city from disease.
* - 10
  - impossible
  - The task is impossible with mortal means. Even a God would succeed on an
    impossible task only about two out of three times.
```

When a {{check}} occurs, the {{narrator}} will narrate the challenge and
request that one or more {{characters}} make a {{roll}} in a particular
{{skill}}. Generally speaking, the {{check}} is succeeded if the {{score}} of
the {{roll}} is greater than or equal to the {{difficulty}}, though, in some
cases, there may be multiple levels of success. For example, when trying to
remember a point of history, a {{character}} who {{rolls}} 6
[Scholarship](skills:mundane:scholarship) would likely remember more details
than a {{character}} who {{rolls}} 5 but fewer than one who {{rolls}} 7.

When a group {{check}} is required, the {{narrator}} will decide whether the
{{difficulty}} must be met by the maximum, the minimum, or the average value
rolled. The maximum value should typically be used when any {{character}}'s
success would yield success, such as when trying to spot something hidden. The
minimum value should typically be used when any {{character}}'s failure would
yield failure, such as when attempting to sneak past guards. The average should
typically be used when all {{characters}} have equal opportunity to contribute
to success, such as when trying to lift something heavy.

(gameplay:rolls:contests)=
### Contests of Skill
{{Contests}} occur when two or more {{characters}} act in conflict. In such a
case the {{narrator}} must decide which {{skill}} each character is must
{{roll}} and whether there is {{leverage}} inherent in the contest.
{{Leverage}} occurs when one {{character}} has an advantage or is using a
strategy that is inherently more advantageous in the {{contest}}. For example,
if one {{character}} were channeling fire at another {{character}} who was
countering with an origami shield, the character using the fire would have
substantial {{leverage}} due to paper's inherent weakness to fire. The
{{narrator}} might award five points of {{leverage}} to the fire sorcerer in
such a case.

```{note}

In some cases, the {{narrator}} may choose to award {{leverage}} to multiple
{{characters}} in a {{contest}}, for example if each of the {{characters}}
employs a different strategy that is nonetheless effective.
```

```{note}

The {{narrator}} may choose to award negative {{leverage}} in some cases to
indicate that a strategy is especially poor.
```

Once both {{characters}} have {{rolled}} their respective {{skills}}, the
outcome is determined by the sum of each {{character}}'s {{score}} and
{{leverage}}. Typically, the {{character}} with the highest sum wins the
{{contest}}, but it is up to the {{narrator}} to compares these values and
narrates the outcome. The {{narrator}} may choose to narrate a different
outcome if, for example, the sum of {{score}} and {{leverage}} for one
{{character}} is substantially higher than that of the other. If a tie occurs
when a tie is not possible, then the {{contest}} is rerolled.


(gameplay:rolls:fate)=
## The Fate of a Roll

Occasionally, a rule may declare, or the {{narrator}} may decide, that the
circumstances of a {{roll}} are especially favored or unfavored. In such cases,
the formula for accumulating successes, failures, and rerolls is slightly
changed to favor our disfavor the resulting {{score}}. The {{fates}} are
described in the following table.

```{list-table} Fates
:header-rows: 1
:name: fates

* - Name
  - Description
* - Cursed
  - Dice that show 5 or 6 still count as a *win* but are no longer rerolled.
* - Unlucky
  - Dice that show 5 still count as a *win* but are no longer rerolled.
* - Neutral
  - No changes to the rules.
* - Lucky
  - Dice that show 2 count as a *win* instead of as a *loss*.
* - Blessed
  - Dice that show 1 or 2 count as a *win* instead of as a *loss*.
```

A {{fate}} applies to a single {{character}}'s roll, so in a {{contest}}, some
characters may make {{rolls}} with different {{fates}}.


(gamplay:rolls:mutliskill)=
## Rolls with Multiple Skills

Occasionally, a rule or the {{narrator}} will require that a {{roll}} be
performed using multiple {{skills}}. In such a case, the {{character}} executes
both {{rolls}} and uses the sum of both {{scores}}.  If the the {{roll}} is a
{{check}}, then the {{difficulty}} is doubled. If the {{roll}} is a
{{contest}}, then both players must execute {{rolls}} for the same number of
{{skills}}.  If two {{skills}} are required of only one of the {{characters}},
then the other {{character}} should roll their single {{skill}} twice.

For example, if one {{character}} is using art to try to effect an emotion in
another {{character}} who does not wish to experience that emotion, then the
{{narrator}} might call for a {{contest}} of the former's
[Craft](skills:mundane:craft) and [Communication](skills:core:communication)
against the latter's [Communication](skills:core:communication), reasoning that
the production of a work of art is both communication
([Communication](skills:core:communication)) and
[Craft](skills:mundane:craft). The former {{character}} would roll both
{{skills}} while the latter {{character}} would roll
[Communication](skills:core:communication) twice.

