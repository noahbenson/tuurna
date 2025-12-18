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
the {term}`Domain Skill`s. For example, Fitness is a {term}`Fundamental Skill`,
and Strength, Endurance, and Agility are its three {term}`Domain Skill`s.

{term}`Domain Skill`s are the only skills that can be increased directly by
spending experience points during {term}`Ellipsis` (see
[Advancement](/characters/advancement)). The {term}`Level` of a
{term}`Fundamental Skill` is equal to the maximum {term}`Level` that has been
obtained by any two of its {term}`Domain Skill`s, and advancement of a
{term}`Fundamental Skill` occurs automatically when the relevant {term}`Domain
Skill`s advance. For example, if a {term}`Character`'s {term}`Level`s in
Strength, Endurance, and Agility are 2, 3, and 4, respectively, then their
{term}`Level` in Fitness (the {term}`Fundamental Skill` that depends on
Strength, Endurance, and Agility) would be 3 because two of Fitness's
{term}`Domain Skill`s are at least {term}`Level` 3 (but only one is
{term}`Level` 4). If the {term}`Character` then advanced their
[Endurance](skills:core:endurance) to {term}`Level` 4, their
[Fitness](skills:core:fitness) would automatically advance to {term}`Level` 4
as well.


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


## How Do Characters Gain Skills?

{term}`Skill` are categorized into three types based on how they are bestowed
on a {term}`Character`:
1. **{term}`Core Skill`s** are available to all {term}`Character`s. All
   {term}`Player Character`s start with a value of 1 in every {term}`Core
   Skill`.
2. **{term}`Mundane Skill`s** are {term}`Skill`s that can be obtained via a
   {term}`Character`'s {term}`Background` or {term}`Background`s. When a
   {term}`Character` gains access to a
   {term}`Fundamental<Fundamental Skill>` {term}`Mundane Skill`, they
   automatically gain 1 level of all {term}`Domain Skill`s that depend on
   it.
3. **{term}`Path Skill`s** are {term}`Skill`s that provide a {term}`Character`
   with a means of accessing the {term}`Exceptional Skill`s.
   {term}`Player Character`s gain {term}`Path Skill`s during
   [Character Creation](/characters/creation).
3. **{term}`Exceptional Skill`s** are skills that are associated with
   {term}`Character`s, such as the {term}`Player Character`s, that are
   exceptional in some way.

More information on skill advancement can be found in the [Advancement
Section](/characters/advancement) of the [Characters
Chapter](/characters/intro).

