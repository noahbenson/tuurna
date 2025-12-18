# Rolls

Frequently during gameplay, a {term}`Character` will attempt to do something
whose outcome is not immediately obvious to the {term}`Narrator`. For example,
a {term}`Character` may attempt to leap across a cavern or to pick a lock. The
outcomes of such actions depend on the skills of the {term}`Character`
performing the action. In such cases, the {term}`Narrator` may use one or more
{term}`Roll`s to help adjudicate the outcome.


(gameplay:rolls)=
## The Rules of a Roll

All {term}`Roll`s are made by a {term}`Character` using a {term}`Skill`. When
the {term}`Narrator` calls for a {term}`Roll`, it is up to them to decide what
{term}`Skill` is appropriate. To execute the {term}`Roll`, the {term}`Player`
rolls a number of 6-sided dice equal to their {term}`PC`'s {term}`Level` in the
{term}`Skill`. Each die whose value is 1 or 2 counts as a *loss*. Each die
whose value is 3 or 4 counts as a *win*. Each die whose value is 5 or 6 both
counts as a *win* and causes an additional die to be rolled and treated
identically. The {term}`Roll`'s {term}`Score` is the total number of *win*
values rolled or 9, whichever is lower. If a rule grants a {term}`Character`
{term}`Supernatural Potential` in a {term}`Skill`, then the {term}`Character`
may achieve a {term}`Score` as high as 12 when making a {term}`Roll` instead of
9.

```{note} 

If a {term}`Player` repeatedly rolls 5s or 6s, the dice continue to
be rerolled, and successes continue to accumulate. It is thus theoretically
possible to achieve an arbitrarily high {term}`Score` on any {term}`Roll`, so
long as the {term}`Character`'s {term}`Level` in the {term}`Skill` is greater
than 0.
```

```{note}

It is up to the {term}`Player` to narrate the course of action of their
{term}`PC`, and in so doing they can suggest the use of a particular
{term}`Skill`; for example, if a {term}`Player` chooses to bash a door down,
they can be reasonably confident that the {term}`Narrator` will call for a
[Strength](skills:core:strength) {term}`Roll` or at least that they won't call
for a [Memory](skills:core:memory) {term}`Roll`. It remains up to the
{term}`Narrator` to determine when a {term}`Roll` is required and which
{term}`Skill` or {term}`Skill`s are relevant to the circumstances.
```

(gameplay:rolls:modifiers)=
### Roll Modifiers: Leverage and Labor
{term}`Roll`s are sometimes modified by contextual circumstances in the game or
by other game rules called {term}`Modifier`s. For example, if one
{term}`Character` uses an {term}`Ability` to injure the wrist of another
{term}`Character`, then the injured {term}`Character` would likely have a
penalty representing the injury's encumbrance applied to any {term}`Roll` made
using their injured wrist. The size of the penalty (the {term}`Modifier`) would
likely depend on the effectiveness of the {term}`Ability`.

There are two kinds of {term}`Modifier`s applied to {term}`Roll`s:
{term}`Leverage`, which adds a flat (potentially negative) value to a
{term}`Roll`'s {term}`Score`, and {term}`Labor`, which causes a certain number
of the dice to be rerolled. (Both of these modifiers are described below.) When
executing a {term}`Roll`, all changes to {term}`Leverage` are integrated, as
are all changes to {term}`Labor`, prior to rolling any dice&mdash;each
{term}`Roll` is executed with a single {term}`Leverage` and a single
{term}`Labor` value.

All {term}`Modifier`s can be applied to a {term}`Roll` by either a game rule or
by the {term}`Narrator`. When a game rule affects a {term}`Roll`, the
{term}`Modifier` is called a {term}`Specific Modifier`. When the
{term}`Narrator` affects a {term}`Roll`, the modifier is called a
{term}`Circumstantial Modifier`. In general, {term}`Circumstantial Modifier`s
are awarded by the {term}`Narrator` due to the contextual setting of a
{term}`Roll` and/or the effectiveness of the strategy being employed by a
{term}`Character`.

A {term}`Modifier` may apply two kinds of changes to a {term}`Roll`:
1. Usually, {term}`Modifier`s update the value. For example, "*You gain +1
   {term}`Leverage` to [Charisma](skills:core:charisma) {term}`Roll`s*" or
   "*You gain -2 {term}`Labor` to [Endurance](skills:core:endurance)
   {term}`Roll`s*".
2. Some rules instead set the minimum or maximum value the {term}`Modifier` can
   take. For example, "*Your minimum {term}`Labor` for
   [Scholarship](skills:mundane:scholarship) {term}`Roll`s is 2*" or "*Your
   maximum {term}`Leverage` for [Tactics](skills:mundane:tactics) {term}`Roll`s
   is 3*".

All updates to a {term}`Modifier` are summed prior to the application of any
minima or maxima. When multiple rules declare different minimum
{term}`Modifier` values for a {term}`Roll`, only the rule resulting in the
highest minimum {term}`Modifier` value is applied; for the maximum, only the
rule resulting in the lowest maximum {term}`Modifier` value is applied.  When
the maximum {term}`Modifier` value is less than the minimum {term}`Modifier`
value, the minimum is ignored.

(gameplay:rolls:modifiers:leverage)=
#### What is Leverage?
{term}`Leverage` generally represents the extent to which a course of action
will be effective as a means of achieving its goals. A high {term}`Leverage`
such as +3 means that a {term}`Character` is guaranteed to perform the
{term}`Roll` as if their {term}`Skill` {term}`Level` were higher than their
true {term}`Level` due to natural or circumstantial advantages.

Mechanically, a {term}`Roll`'s {term}`Leverage` is added to its
{term}`Score`. Positive {term}`Leverage` values increase the {term}`Score`
while negative {term}`Leverage` values result in a lower {term}`Score`.

(gameplay:rolls:modifiers:labor)=
#### What is Labor?
{term}`Labor` represents a {term}`Character`'s advantage or distadvantage on a
{term}`Roll` that is due to their own effort or influence or the effort or
influence of others working against them. Unlike {term}`Leverage`, which adds a
flat number to the {term}`Score` of a {term}`Roll`, {term}`Labor` gives the
{term}`Character` performing the {term}`Roll` either more or fewer dice to
{term}`Roll`. A {term}`Labor` of +2, for example, would allow the
{term}`Character` to {term}`Roll` two additional dice. If a {term}`Character`'s
{term}`Labor` on a {term}`Roll` reduces the number of dice they {term}`Roll`
below 1, the {term}`Character` still rolls 1 die.

```{note}

Note that, although {term}`Leverage` is statistically identical to
{term}`Labor`&mdash;in that the expected advantage of rolling 1 additional die
is 1 additional {term}`Score`, which is exactly what is provided by a point of
{term}`Leverage`&mdash;a point of {term}`Labor` can potentially provides the
{term}`Character` with either no additional {term}`Score` or with a bonus to
their {term}`Score` that is substantially more than 1.
```

(gameplay:rolls:modifiers:examples)=
#### Leverage and Labor Examples

TODO

In the following examples, we rely on two characters: Ylir and Zejhe. Ylir's
{term}`Level` in the [Armaments](skills:mundane:armaments) {term}`Skill` is 5;
Zejhe's {term}`Level` in the [Instinct](skills:core:instinct)
{term}`Skill` is 4 and in the [Armaments](skills:mundane:armaments) is 2.


## What kinds of situations call for rolls?

Broadly speaking, there are two types of situations that require {term}`Roll`s
to adjudicate: {term}`Check`s and {term}`Contest`s.


(gameplay:rolls:checks)=
### Skill Checks

Some narrative situations that arise in gameplay represent attempts to resolve
a static challenge that exist in the world. In such a situation, the outcome
depends only on whether one can apply one's {term}`Skill` in the moment with
sufficient grace to overcome a fixed {term}`Difficulty`. Such
{term}`Check`s are in contrast to contested rolls ({term}`Contest`s) in
which one's skill is set against that of another.

When the {term}`Narrator` feels that an outcome is uncertain, they must decide
on the {term}`Skill` (or {term}`Skill`s) that can resolve the {term}`Check` and
the {term}`Check`'s {term}`Difficulty`. The {term}`Character` or
{term}`Character`s must then execute the {term}`Roll`. The {term}`Narrator`
then compares the character's {term}`Score` against the {term}`Difficulty`

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

When a {term}`Check` occurs, the {term}`Narrator` will narrate the challenge
and request that one or more {term}`Character`s make a {term}`Roll` in a
particular {term}`Skill`. Generally speaking, the {term}`Check` is succeeded if
the {term}`Score` of the {term}`Roll` is greater than or equal to the
{term}`Difficulty`, though, in some cases, there may be multiple levels of
success. For example, when trying to remember a point of history, a
{term}`Character` who {term}`Roll`s 6 [Scholarship](skills:mundane:scholarship)
would likely remember more details than a {term}`Character` who {term}`Roll`s 5
but fewer than one who {term}`Roll`s 7.

When a group {term}`Check` is required, the {term}`Narrator` will decide
whether the {term}`Difficulty` must be met by the maximum, the minimum, or the
average value rolled. The maximum value should typically be used when any
{term}`Character`'s success would yield success, such as when trying to spot
something hidden. The minimum value should typically be used when any
{term}`Character`'s failure would yield failure, such as when attempting to
sneak past guards. The average should typically be used when all
{term}`Character`s have equal opportunity to contribute to success, such as
when trying to lift something heavy.

(gameplay:rolls:contests)=
### Contests of Skill

{term}`Contest`s occur when two or more {term}`Character`s act in conflict. In
such a case the {term}`Narrator` must decide which {term}`Skill` each character
is must {term}`Roll` and whether there is {term}`Leverage` inherent in the
contest.  {term}`Leverage` occurs when one {term}`Character` has an advantage
or is using a strategy that is inherently more advantageous in the
{term}`Contest`. For example, if one {term}`Character` were channeling fire at
another {term}`Character` who was countering with an origami shield, the
character using the fire would have substantial {term}`Leverage` due to paper's
inherent weakness to fire. The {term}`Narrator` might award five points of
{term}`Leverage` to the fire sorcerer in such a case.

```{note}

In some cases, the {term}`Narrator` may choose to award {term}`Leverage`
to multiple {term}`Character`s in a {term}`Contest`, for example if each
of the {term}`Character`s employs a different strategy that is nonetheless
effective.
```

```{note}

The {term}`Narrator` may choose to award negative {term}`Leverage` in some
cases to indicate that a strategy is especially poor.
```

Once both {term}`Character`s have {term}`Roll`ed their respective
{term}`Skill`s, the outcome is determined by the sum of each
{term}`Character`'s {term}`Score` and {term}`Leverage`. Typically, the
{term}`Character` with the highest sum wins the {term}`Contest`, but it is up
to the {term}`Narrator` to compares these values and narrates the outcome. The
{term}`Narrator` may choose to narrate a different outcome if, for example, the
sum of {term}`Score` and {term}`Leverage` for one {term}`Character` is
substantially higher than that of the other. If a tie occurs when a tie is not
possible, then the {term}`Contest` is rerolled.


(gameplay:rolls:fate)=
## The Fate of a Roll

Occasionally, a rule may declare, or the {term}`Narrator` may decide, that the
circumstances of a {term}`Roll` are especially favored or unfavored. In such
cases, the formula for accumulating successes, failures, and rerolls is
slightly changed to favor our disfavor the resulting {term}`Score`. The
{term}`Fate`s are described in the following table.

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

A {term}`Fate` applies to a single {term}`Character`'s roll, so in a
{term}`Contest`, some characters may make {term}`Roll`s with different 
{term}`Fate`s.


(gamplay:rolls:mutliskill)=
## Rolls with Multiple Skills

Occasionally, a rule or the {term}`Narrator` will require that a {term}`Roll`
be performed using multiple {term}`Skill`s. In such a case, the
{term}`Character` executes both {term}`Roll`s and uses the sum of both
{term}`Score`s.  If the the {term}`Roll` is a {term}`Check`, then the
{term}`Difficulty` is doubled. If the {term}`Roll` is a {term}`Contest`, then
both players must execute {term}`Roll`s for the same number of {term}`Skill`s.
If two {term}`Skill`s are required of only one of the {term}`Character`s, then
the other {term}`Character` should roll their single {term}`Skill` twice.

For example, if one {term}`Character` is using art to try to effect an emotion
in another {term}`Character` who does not wish to experience that emotion, then
the {term}`Narrator` might call for a {term}`Contest` of the former's
[Craft](skills:mundane:craft) and [Communication](skills:core:communication)
against the latter's [Communication](skills:core:communication), reasoning that
the production of a work of art is both communication
([Communication](skills:core:communication)) and
[Craft](skills:mundane:craft). The former {term}`Character` would roll both
{term}`Skill`s while the latter {term}`Character` would roll
[Communication](skills:core:communication) twice.

