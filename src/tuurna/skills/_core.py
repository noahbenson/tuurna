# -*- coding: utf-8 -*-
###############################################################################
# namespace: tuurna.skills._core


# Dependencies ################################################################

from functools import reduce, partial
from collections import namedtuple
from collections.abc import Mapping
import operator as op

import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import icepool as ip


# Types ######################################################################

# Fate -----------------------------------------------------------------------
FateData = namedtuple(
    'FateData',
    ('value', 'name',
     'fail_values', 'pass_values', 'explode_values',
     'mapping'),
    defaults=(None,))
class Fate(FateData):
    """A description of the fate of a skill check.

    Skill checks have a fate, which indicates how much fate is working for or
    against the skill check, abstractly. A fate of 0 is considered a neutral
    fate while positive and negative integers indicate favorable or
    unfavorable fates, respectively.

    A given fate has a name, a set of values that count as failures, a set of
    values that count as passes, and a set of values that explode, meaning
    that they both count as a pass and are rerolled.

    The fate of a roll can be any of the following values:
    * -2. Cursed
    * -1. Disadvantaged
    *  0. Neutral
    * +1. Advantaged
    * +2. Blessed

    Attributes
    ----------
    value : int
        The integer value of the fate.
    name : str
        The name of the fate.
    fail_values : tuple of int
        The D6 values considered a failure.
    pass_values : tuple of int
        The D6 values considered a pass.
    explode_values : tuple of int
        The D6 values considered a pass and that are rerolled.
    mapping : dict
        A mapping of D6 values to outcomes using the ``icepool`` library; this
        mapping is appropriate for the ``icepool.d6.map`` method.
    minimum : int
        (Class Attribute) The minimum value a roll's fate can have,
        representing a highly unfavorable outcome. This value is inclusive.
    neutral : int
        (Class Attribute) The value that represents a neutral fate.
    maximum : int
        (Class Attribute) The minimum value a roll's fate can have,
        representing a highly favorable outcome. This value is inclusive.
    by_values : dict
        (Class Attribute) A dictionary whose keys are the integer fate values
        and whose values are ``Fate`` objects representing those fates.
    by_names : dict
        (Class Attribute) A dictionary whose keys are the fate name strings
        and whose values are ``Fate`` objects representing those fates.

    See Also
    --------
    ``to_fate``
    """
    minimum = -2
    neutral = 0
    maximum = 2
    by_value = {}
    by_name = {}
    __slots__ = ()
    def __new__(cls, *args, **kw):
        narg = len(args)
        obj = super().__new__(cls, *args, **kw)
        if obj.mapping is None:
            m = {}
            for rollval in obj.fail_values:
                m[rollval] = 0
            for rollval in obj.pass_values:
                m[rollval] = 1
            for rollval in obj.explode_values:
                m[rollval] = 1 + ip.Again
            kw['mapping'] = m
            obj = super().__new__(cls, *args, **kw)
        m = obj.mapping
        if len(m) != 6 or not all(k in m for k in range(1,7)):
            raise ValueError("mapping keys are not 1,2,3,4,5,6")
        return obj
Fate.by_value = {
    -2: Fate(-2, 'cursed',        (1,2), (3,4,5,6), ()),
    -1: Fate(-1, 'disadvantaged', (1,2), (3,4,5),   (6,)),
    0:  Fate(0,  'neutral',       (1,2), (3,4),     (5,6)),
    1:  Fate(1,  'advantaged',    (1,),  (2,3,4),   (5,6)),
    2:  Fate(2,  'blessed',       (),    (1,2,3,4), (5,6))}
Fate.by_name = {f.name: f for f in Fate.by_value.values()}

# Level ----------------------------------------------------------------------
LevelData = namedtuple('LevelData', ('value', 'name'))
class Level(LevelData):
    """A description of a skill level.

    Attributes
    ----------
    value : int
        The integer value of the level, between 0 and 12 inclusive.
    name : str
        The uncapitalized name of the skill level; names are always
        appropriate for use as python symbols.
    minimum : int
        (Class Attribute) The minimum value a skill level can take,
        representing a lack of any ability at the skill. This value is
        inclusive.
    maximum : int
        (Class Attribute) The maximum value a skill level can take. This value
        is inclusive.
    by_values : dict
        (Class Attribute) A dictionary whose keys are the integer level values
        and whose values are ``Level`` objects representing those levels.
    by_names : dict
        (Class Attribute) A dictionary whose keys are the level name strings
        and whose values are ``Level`` objects representing those levels.
    """
    minimum = 0
    maximum = 12
    by_values = {}
    by_names = {}
    __slots__ = ()
Level.by_value = {
    0:  Level(0,  'unskilled'),
    1:  Level(1,  'novice'),
    2:  Level(2,  'practitioner'),
    3:  Level(3,  'amateur'),
    4:  Level(4,  'proficient'),
    5:  Level(5,  'skilled'),
    6:  Level(6,  'expert'),
    7:  Level(7,  'virtuoso'),
    8:  Level(8,  'master'),
    9:  Level(9,  'grandmaster'),
    10: Level(10, 'uncanny'),
    11: Level(11, 'supernatural'),
    12: Level(12, 'godlike')}
Level.by_name = {l.name: l for l in Level.by_value.values()}


# Functions ##################################################################

def to_level(obj):
    """Coerces the argument to a skill ``Level`` object and returns it.
    
    If the object cannot be converted into a valid skill level, then a
    ``TypeError`` is raised.

    If the argument is a number or a string representation of a number, then
    it is converted into an integer; if that integer is outside the range of
    a valid skill level, a ``ValueError`` is raised.
    """
    if isinstance(obj, Level):
        return obj
    try:
        return Level.by_name[obj]
    except KeyError:
        pass
    try:
        return Level.by_value[int(obj)]
    except KeyError:
        pass
    raise ValueError(f"cannot find level matching object of type {type(obj)}")
def to_fate(obj):
    """Coerces the argument to a skill ``Fate`` object and returns it.
    
    If the object cannot be converted into a valid fate, then a ``TypeError``
    is raised.

    If the argument is a number or a string representation of a number, then
    it is converted into an integer; if that integer is outside the range of
    a valid fate, a ``ValueError`` is raised.
    """
    if isinstance(obj, Level):
        return obj
    try:
        return Fate.by_name[obj]
    except KeyError:
        pass
    try:
        return Fate.by_value[int(obj)]
    except KeyError:
        pass
    raise ValueError(f"cannot find fate matching object of type {type(obj)}")
