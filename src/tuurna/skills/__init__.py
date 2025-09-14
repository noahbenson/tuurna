# -*- coding: utf-8 -*-
###############################################################################
# namespace: tuurna.skills

"""The skill system of Tu'urna.

Skills represent a character's abilities to interact with the world; they do
not need to be active, but they must represent a capacity of some kind.
Intuitively, PCs have skills from the PC skill graph, but other characters may
have individual skills; for example, a plant might have a skill related to its
ability to produce energy from sunlight.

More information can be found in the documentation for the ``skills.Fate``,
``skills.Skill``, ``skills.Difficulty``, and ``skills.Level`` classes.
"""

from ._core import (
    Fate,
    Level,
    Skill,
    Difficulty,
    skills,
    to_level,
    to_skill,
    to_fate,
    to_difficulty)

Fate.__module__ = __name__
Level.__module__ = __name__
Skill.__module__ = __name__
Difficulty.__module__ = __name__
to_level.__module__ = __name__
to_skill.__module__ = __name__
to_fate.__module__ = __name__
to_difficulty.__module__ = __name__

