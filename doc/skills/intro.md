(skills:intro)=
# The Tu'urna Skill System

{term}`Character`s in Tu'urna, in terms of game mechanics, are defined
primarily by the {term}`Skill`s they have available to them and their skill
levels. Skills describe a character's ability to interact competently with the
world and are the basis for all game {term}`Roll`s.


(skills:hierarchy)=
## Skill Hierarchy

{term}`Skill`s are organized into a shallow hierarchy in which some
{term}`Skill`s are the parents of other skills. If a {term}`Skill` has any
child {term}`Skill`s, this indicates that the child {term}`Skill`s are specific
subdomains of the parent {term}`Skill` and are mostly distinct from each
other. In such a case, the parent skill is called the {term}`Fundamental Skill`
and the child skills on which the {term}`Fundamental Skill` depends are called
the {term}`Practical Skill`s. For example, Fitness is a {term}`Fundamental Skill`,
and Strength, Endurance, and Agility are its three {term}`Practical Skill`s.

The {term}`Level` of a {term}`Fundamental Skill` is equal to the maximum
{term}`Level` that has been obtained by any two of its 
{term}`Practical Skill`s, and advancement of a {term}`Fundamental Skill` occurs
automatically when the relevant {term}`Practical Skill`s advance. For example, if
a {term}`Character`'s {term}`Level`s in Strength, Endurance, and Agility are 2,
3, and 4, respectively, then their {term}`Level` in Fitness (the
{term}`Fundamental Skill` that depends on Strength, Endurance, and Agility)
would be 3 because two of Fitness's {term}`Practical Skill`s are at least
{term}`Level` 3 (but only one is {term}`Level` 4). If the {term}`Character`
then advanced their [Endurance](skills:core:endurance) to {term}`Level` 4,
their [Fitness](skills:core:fitness) would automatically advance to
{term}`Level` 4 as well.

{term}`Fundamental Skill`s can also be advanced using normal methods, but they
can never be advanced to a {term}`Level` higher than the maximum {term}`Level`
obtained by their dependant {term}`Practical Skill`s. For example, if a
{term}`Character` has an [Intuition](skills:path:intuition) {term}`Level` of 3,
an [Attunement](skills:path:attunement) {term}`Level` of 4, and a
[Virtue](skills:path:virtue) {term}`Level` of 0, then they would be able to
increase their [Intuition](skills:path:intuition) to {term}`Level` 4 because at
least one of its dependant {term}`Practical Skill`s is greater than or equal
to 4. They would then be unable to advance their
[Intuition](skills:path:intuition) to {term}`Level` 5, however, because neither
of the {term}`Practical Skill`s [Attunement](skills:path:attunement) are high
enough.


(skills:levels)=
## Skill Levels

A {term}`Character`'s ability at a particular {term}`Skill` is measured by
their {term}`Level` in that {term}`Skill`. Levels must be a non-negative
integer less than 13. Each {term}`Skill` documents what abilities, if any, are
available to a {term}`Character` at each {term}`Level`, and all {term}`Roll`s
of a {term}`Skill` are made using a number of dice equal to the {term}`Level`
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
    {term}`Difficulty` 1 (trivial) {term}`Check`s but only occasionally
    succeeds at {term}`Difficulty` 2 (very easy) {term}`Check`s.
* - 2
  - practitioner
  - The character succeeds at {term}`Difficulty` 2 (very easy) {term}`Check`s
    about half the time.
* - 3
  - amateur
  - The character succeeds at {term}`Difficulty` 3 (easy) {term}`Check`s
    about half the time and occasionally succeeds at {term}`Difficulty` 4 
    (mundane) {term}`Check`s.
* - 4
  - proficient
  - The character succeeds about half the time at {term}`Check`s of 
    {term}`Difficulty` 4 (mundane) and usually succeeds at easier tasks.
* - 5
  - skilled
  - The character succeeds about half the time at {term}`Check`s of 
    {term}`Difficulty` 5 (moderate) and usually succeeds at easier tasks.
* - 6
  - expert
  - The character succeeds slightly less than half the time at {term}`Check`s
     of {term}`Difficulty` 6 (challenging) and about one time in four at
     {term}`Difficulty` 7 (difficult), but typically succeeds on easier tasks.
* - 7
  - virtuoso
  - The character succeeds slightly less than half the time at {term}`Check`s
    of {term}`Difficulty` 7 (difficult) and about one time in four at
    {term}`Difficulty` 8 (very difficult).
* - 8
  - master
  - The character succeeds slightly less than half the time at {term}`Check`s
    of {term}`Difficulty` 8 (very difficult) and about one time in four at 
    {term}`Difficulty` 9 (nearly impossible).
* - 9
  - grandmaster
  - The height of mortal achievement; the character usually succeeds at 
    {term}`Check`s of {term}`Difficulty` 8 (very difficult) and succeeds at
    {term}`Check`s of {term}`Difficulty` 10 (impossible) about one time in
    four.
* - 10
  - uncanny
  - The character has an uncanny ability and can succeed at {term}`Check`s of
    {term}`Difficulty` 10 (impossible) slightly less than half of the time.
* - 11
  - supernatural
  - The character's abilities are clearly supernatural. They can succeed at 
    {term}`Check`s of {term}`Difficulty` 10 (impossible) slightly more than
    half of the time.
* - 12
  - godlike
  - The character's abilities rival those of gods. They can succeed at 
    {term}`Check`s of {term}`Difficulty` 10 (impossible) most of the time.
```

(skills:levels:abilities)=
### Abilities: the Elements of Skills

As a {term}`Character` advances their {term}`Level` in a particular
{term}`Skill`, they may gain subskills called {term}`Abilities<Ability>`. While
not every {term}`Level` of every {term}`Skill` contains distinct
{term}`Abilities<Ability>`, most contain at least one. A {term}`Character` may
attempt to use any {term}`Ability` for which they have attained the
{term}`Ability`'s {term}`Level` in its associated {term}`Skill`.

Most {term}`Abilities<Ability>` can only be used under certain
circumstances. Some {term}`Skill`s place restrictions on their use that are
explained in their descriptions; such restrictions apply to all
{term}`Abilities<Ability>` of the {term}`Skill`. Each {term}`Ability`'s
description can also contains additional rules about when and how it can be
used. In particular, some {term}`Abilities<Ability>` are described as
{term}`Ellipsis Abilities<Ellipsis Ability>`. These abilities can be used
during {term}`Ellipsis`. Similarly, if an {term}`Ability` is described as a
{term}`Scene Ability`, then it can be used during a {term}`Scene`.
{term}`Abilities<Ability>` that can be used during either {term}`Ellipsis` or
{term}`Scene`s are considered both a {term}`Scene Ability` and an
{term}`Ellipsis Ability`, and such a {term}`Ability`'s description will contain
two sections describing their use each {term}`Ability` type.


(skills:access)=
## How Do Characters Gain Access to Skills?

{term}`Skill`s are categorized into four broad types that differ primarily in
how a {term}`Character` gains access to it. A {term}`Character` cannot advance
a {term}`Skill` unless a rule allows them to:
1. **{term}`Core Skill`s** are available to all {term}`Character`s. All
   {term}`Player Character`s start with a value of 1 in every {term}`Core
   Skill`.
2. **{term}`Mundane Skill`s** are {term}`Skill`s that can be obtained via a
   {term}`Character`'s {term}`Background` or {term}`Background`s. When a
   {term}`Character` gains access to a
   {term}`Fundamental<Fundamental Skill>` {term}`Mundane Skill`, they
   automatically gain 1 level of all {term}`Practical Skill`s that depend on
   it.
3. **{term}`Path Skill`s** are {term}`Skill`s that provide a {term}`Character`
   with a means of accessing the {term}`Domain Skill`s.  {term}`Player
   Character`s choose one {term}`Path Skill` during [Character
   Creation](characters:creation), gaining one {term}`Level` of it and its
   {term}`Fundamental Skill`.
3. **{term}`Domain Skill`s** are skills that are associated with
   {term}`Character`s, such as the {term}`Player Character`s, that are
   exceptional in some way. Each {term}`Domain Skill`'s description
   provides a list of {term}`Path Skill`s with which they are compatible along
   with a minimum {term}`Level`. (If no {term}`Level` is listed for a
   {term}`Path Skill`, then the minimum {term}`Level` is 1.) {term}`Character`s can
   advance any {term}`Domain Skill` for which they have obtained the
   required {term}`Level` of any compatible {term}`Path Skill`.

Once a character has gained access to a {term}`Skill`, they can advance it
under the normal rules of advancement. More information on skill advancement
can be found in the [Advancement Section](characters:advancement) of the
[Chapter on Characters](characters:intro).

