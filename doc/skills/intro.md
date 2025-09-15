# The Tu'urna Skill System

{term}`Character`s in Tu'urna, in terms of game mechanics, are defined
primarily by the {term}`Skill`s they have available to them and their skill
levels. Skills describe a character's ability to interact competently with the
world and are the basis for all game {term}`Roll`s.


(skills:hierarchy)=
## Skill Hierarchy

{term}`Skill`s are organized into a shallow hierarchy in which some skills
depend on other skills. Top-level skills that depend on no other skills are
called **{term}`Fundamental Skill`s**. Skills that depend on a Fundamental
Skill are called **{term}`Domain Skill`s**, and skills that depend on Domain
Skills are called **{term}`Practical Skill`s**. A skill cannot depend on a
Practical Skill. Practical Skills are considered dependants of both the Domain
Skill on which they depend directly and the Fundamental Skill on which they
depend by proxy.

Practical Skills are the only skills that can be increased directly by spending
experience points during {term}`Ellipsis` (see
[Advancement](../characters/advancement)). Domain Skill levels are equal to the
sum of the levels of all dependant Practical Skills divided by two, rounded
down. Fundamental Skill levels are equal to the sum of the levels of the four
highest dependant Practical Skills divided by four, rounded down. Both Domain
and Fundamental Skills advance immediately whenever a dependant Practical Skill
advances.


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
    {term}`Difficulty` 1 (trivial) {term}`Challenge`s but only occasionally
    succeeds at {term}`Difficulty` 2 (very easy) {term}`Challenge`s.
* - 2
  - practitioner
  - The character succeeds at {term}`Difficulty` 2 (very easy) {term}`Challenge`s
    about half the time.
* - 3
  - amateur
  - The character succeeds at {term}`Difficulty` 3 (easy) {term}`Challenge`s
    about half the time and occasionally succeeds at {term}`Difficulty` 4 
    (mundane) {term}`Challenge`s.
* - 4
  - proficient
  - The character succeeds about half the time at {term}`Challenge`s of 
    {term}`Difficulty` 4 (mundane) and usually succeeds at easier tasks.
* - 5
  - skilled
  - The character succeeds about half the time at {term}`Challenge`s of 
    {term}`Difficulty` 5 (moderate) and usually succeeds at easier tasks.
* - 6
  - expert
  - The character succeeds slightly less than half the time at {term}`Challenge`s
     of {term}`Difficulty` 6 (challenging) and about one time in four at
     {term}`Diffuclty` 7 (difficult), but typically succeeds on easier tasks.
* - 7
  - virtuoso
  - The character succeeds slightly less than half the time at {term}`Challenge`s
    of {term}`Difficulty` 7 (difficult) and about one time in four at
    {term}`Difficulty` 8 (very difficult).
* - 8
  - master
  - The character succeeds slightly less than half the time at {term}`Challenge`s
    of {term}`Difficulty` 8 (very difficult) and about one time in four at 
    {term}`Difficulty` 9 (nearly impossible).
* - 9
  - grandmaster
  - The height of mortal achievement; the character usually succeeds at 
    {term}`Challenge`s of {term}`Difficulty` 8 (very difficult) and succeeds at
    {term}`Challenge`s of {term}`Difficulty` 10 (impossible) about one time in
    four.
* - 10
  - uncanny
  - The character has an uncanny ability and can succeed at {term}`Challenge`s of
    {term}`Difficulty` 10 (impossible) slightly less than half of the time.
* - 11
  - supernatural
  - The character's abilities are clearly supernatural. They can succeed at 
    {term}`Challenge`s of {term}`Difficulty` 10 (impossible) slightly more than
    half of the time.
* - 12
  - godlike
  - The character's abilities rival those of gods. They can succeed at 
    {term}`Challenge`s of {term}`Difficulty` 10 (impossible) most of the time.
```


## How Do Characters Gain Skills?

{term}`Skill` are categorized into three types based on how they are bestowed
on a {term}`Character`:
1. **{term}`Inherent Skill`s** are available to all characters. All
   {term}`Player Character`s start with a value of 1 in every {term}`Inherent
   Skill`. The {term}`Inherent Skill`s are synonymous with a character's core
   statistics (such as strength or intelligence) in other tabletop RPGs such as
   Dungeons and Dragons. These {term}`Skill`s are {term}`Physique`,
   {term}`Craft`, {term}`Reason`, {term}`Acumen`, and {term}`Harmony`).
2. **{term}`Mundane Skill`s** are {term}`Skill`s that can be obtained via a
   {term}`Character`'s {term}`Background` or {term}`Background`s. When a
   {term}`Character` gains access to a {term}`Mundane Skill`, they
   automatically gain 1 level of all {term}`Practical Skill`s that depend on
   it.
3. **{term}`Exceptional Skill`s** are skills that are associated with
   {term}`Character`s, such as the {term}`Player Character`s, that are
   exceptional in some way.

More information on skill advancement can be found in the [Advancement
Section](/characters/advancement) of the [Characters
Chapter](/characters/intro).


## Derived Skills

{term}`Derived Skill`s are {term}`Skill`s that cannot be advanced and that are
gained automatically by any {term}`Character` eligible for them. For example,
all characters have the [Art skill](skills:derived:art), the level of
which is always equal to the average of a character's {term}`Harmony` and
{term}`Craft`, rounded down.
