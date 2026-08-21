# treesitter / dev / cut=calls_only

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 99.7% [98.4% to 100.0%]   F1 99.8% [99.2% to 100.0%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored, this cut excludes the class, so it counts against neither side

## src/internal/purryOrderRules.ts  (tp 10, fp 0, fn 1, unscored 1)
  - purryOrderRules -> isOrderRule
  ~ isOrderRule -> isArray

## src/clone.ts  (tp 11, fp 0, fn 0, unscored 3)
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/countBy.ts  (tp 6, fp 0, fn 0, unscored 1)
  ~ countByImplementation -> fromEntries

## src/dropLast.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ dropLastImplementation -> max

## src/evolve.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ evolveImplementation -> entries

## src/flatMap.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ lazyImplementation -> isArray

## src/funnel.ts  (tp 7, fp 0, fn 0, unscored 4)
  ~ __module__ -> Symbol
  ~ funnel -> max
  ~ funnel -> min
  ~ funnel -> now

## src/groupBy.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/groupByProp.ts  (tp 2, fp 0, fn 0, unscored 2)
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/hasProp.ts  (tp 1, fp 0, fn 0, unscored 1)
  ~ hasPropImplementation -> hasOwn

## src/hasSubObject.ts  (tp 2, fp 0, fn 0, unscored 2)
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/internal/purryFromLazy.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ purryFromLazy -> assign

## src/internal/withPrecision.ts  (tp 7, fp 0, fn 0, unscored 5)
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

## src/internal/words.ts  (tp 5, fp 0, fn 0, unscored 1)
  ~ __module__ -> Set

## src/invert.ts  (tp 1, fp 0, fn 0, unscored 1)
  ~ invertImplementation -> entries

## src/isDeepEqual.ts  (tp 17, fp 0, fn 0, unscored 5)
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries
  ~ isDeepEqualImplementation -> is
  ~ isDeepEqualImplementation -> isArray
  ~ isDeepEqualImplementation -> keys

## src/isEmpty.ts  (tp 0, fp 0, fn 0, unscored 2)
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/isPlainObject.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ isPlainObject -> getPrototypeOf

## src/mapKeys.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ mapValuesImplementation -> entries

## src/omitBy.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ omitByImplementation -> entries

## src/pipe.ts  (tp 13, fp 0, fn 0, unscored 1)
  ~ prepareLazyFunction -> assign

## src/randomInteger.ts  (tp 2, fp 0, fn 0, unscored 3)
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/randomString.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/range.ts  (tp 3, fp 0, fn 0, unscored 4)
  ~ ceilingWithSnap -> abs
  ~ ceilingWithSnap -> ceil
  ~ ceilingWithSnap -> round
  ~ rangeImplementation -> from

## src/sample.ts  (tp 7, fp 0, fn 0, unscored 3)
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> min
  ~ sampleImplementation -> random

## src/setPath.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ setPathImplementation -> isArray

## src/stringToPath.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ stringToPath -> Number

## src/swapIndices.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ swapArray -> isNaN

## src/takeLast.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ takeLastImplementation -> max

## src/times.ts  (tp 2, fp 0, fn 0, unscored 3)
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

111 of 112 files exactly right.
