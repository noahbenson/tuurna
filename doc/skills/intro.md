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
experience points during [ellipsis](../gameplay/ellipsis) (see
[Advancement](../characters/advancement)). Domain Skill levels are equal to the
sum of the levels of all dependant Practical Skills divided by two, rounded
down. Fundamental Skill levels are equal to the sum of the levels of all
dependant Practical Skills divided by four, rounded down. Both Domain and
Fundamental Skills advance immediately whenever a dependant Practical Skill
advances.


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

(skills:derived)=
## Derived Skills

{term}`Derived Skill`s are skills that cannot be advanced and that are gained
automatically by any character eligible for them. For example, the all
characters have the [Art skill](/skills/derived/art), the level of which is
always equal to the average of a character's {term}`Harmony` and {term}`Craft`,
rounded down.
