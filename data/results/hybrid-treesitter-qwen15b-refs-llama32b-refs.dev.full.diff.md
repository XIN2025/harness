# hybrid(treesitter+qwen15b-refs & llama32b-refs) / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 96.0% [91.5% to 97.9%]   R 90.3% [87.4% to 93.0%]   F1 93.1% [90.8% to 94.7%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored, this cut excludes the class, so it counts against neither side

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 2)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/pipe.ts  (tp 13, fp 0, fn 4, unscored 1)
  - pipe -> lazyOp
  - pipe -> op
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  ~ prepareLazyFunction -> assign

## src/internal/purryOrderRules.ts  (tp 10, fp 0, fn 3, unscored 1)
  - orderRuleComparer -> primaryRule
  - purryOrderRules -> compareFn
  - purryOrderRules -> isOrderRule
  ~ isOrderRule -> isArray

## src/zipWith.ts  (tp 5, fp 0, fn 3, unscored 0)
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation

## src/internal/purryFromLazy.ts  (tp 2, fp 0, fn 2, unscored 1)
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  ~ purryFromLazy -> assign

## src/internal/quickSelect.ts  (tp 5, fp 0, fn 2, unscored 0)
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn

## src/nthBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - nthBy -> nthByImplementation
  - nthByImplementation -> compareFn

## src/sort.ts  (tp 3, fp 1, fn 1, unscored 0)
  - sortImplementation -> cmp
  + sortImplementation -> defaultCompare

## src/toKebabCase.ts  (tp 4, fp 1, fn 1, unscored 0)
  - toKebabCase -> toKebabCaseImplementation
  + toKebabCase -> words

## src/ceil.ts  (tp 2, fp 1, fn 0, unscored 0)
  + ceil -> ceil

## src/clone.ts  (tp 11, fp 0, fn 1, unscored 3)
  - clone -> cloneImplementation
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/countBy.ts  (tp 6, fp 0, fn 1, unscored 1)
  - countBy -> countByImplementation
  ~ countByImplementation -> fromEntries

## src/difference.ts  (tp 5, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator

## src/drop.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropFirstBy.ts  (tp 6, fp 0, fn 1, unscored 0)
  - dropFirstByImplementation -> compareFn

## src/filter.ts  (tp 5, fp 0, fn 1, unscored 0)
  - filterImplementation -> predicate

## src/findIndex.ts  (tp 3, fp 0, fn 1, unscored 0)
  - findIndexImplementation -> predicate

## src/first.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> firstLazy

## src/flatMap.ts  (tp 5, fp 0, fn 1, unscored 1)
  - flatMapImplementation -> callbackfn
  ~ lazyImplementation -> isArray

## src/floor.ts  (tp 2, fp 1, fn 0, unscored 0)
  + floor -> floor

## src/forEach.ts  (tp 5, fp 0, fn 1, unscored 0)
  - forEachImplementation -> callbackfn

## src/funnel.ts  (tp 7, fp 0, fn 1, unscored 4)
  - funnel -> voidReducer
  ~ __module__ -> Symbol
  ~ funnel -> max
  ~ funnel -> min
  ~ funnel -> now

## src/groupByProp.ts  (tp 2, fp 0, fn 1, unscored 2)
  - groupByProp -> groupByPropImplementation
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/internal/withPrecision.ts  (tp 7, fp 1, fn 0, unscored 5)
  + withPrecision -> precision
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

## src/intersection.ts  (tp 6, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator

## src/join.ts  (tp 3, fp 1, fn 0, unscored 0)
  + joinImplementation -> glue

## src/keys.ts  (tp 1, fp 1, fn 0, unscored 0)
  + keys -> keys

## src/map.ts  (tp 5, fp 0, fn 1, unscored 0)
  - mapImplementation -> callbackfn

## src/meanBy.ts  (tp 4, fp 1, fn 0, unscored 0)
  + meanBy -> fn

## src/median.ts  (tp 3, fp 0, fn 1, unscored 0)
  - medianImplementation -> numberComparator

## src/omitBy.ts  (tp 2, fp 0, fn 1, unscored 1)
  - omitBy -> omitByImplementation
  ~ omitByImplementation -> entries

## src/purry.ts  (tp 3, fp 1, fn 0, unscored 0)
  + purry -> args

## src/reduce.ts  (tp 3, fp 0, fn 1, unscored 0)
  - reduceImplementation -> callbackfn

## src/round.ts  (tp 2, fp 1, fn 0, unscored 0)
  + round -> round

## src/sortBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortByImplementation -> compareFn

## src/sortedIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedIndex -> sortedIndexImplementation

## src/sortedIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedIndexBy -> sortedIndexByImplementation

## src/sortedLastIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedLastIndex -> sortedLastIndexImplementation

## src/sortedLastIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedLastIndexBy -> sortedLastIndexByImplementation

## src/splitWhen.ts  (tp 4, fp 0, fn 1, unscored 0)
  - splitWhenImplementation -> predicate

## src/take.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator

## src/takeFirstBy.ts  (tp 5, fp 0, fn 1, unscored 0)
  - takeFirstByImplementation -> compareFn

## src/toTitleCase.ts  (tp 8, fp 1, fn 0, unscored 0)
  + toTitleCaseImplementation -> word

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

## src/zip.ts  (tp 3, fp 0, fn 1, unscored 0)
  - zip -> lazyImplementation

## src/dropLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ dropLastImplementation -> max

## src/evolve.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ evolveImplementation -> entries

## src/groupBy.ts  (tp 4, fp 0, fn 0, unscored 2)
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/hasProp.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ hasPropImplementation -> hasOwn

## src/hasSubObject.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/internal/words.ts  (tp 5, fp 0, fn 0, unscored 1)
  ~ __module__ -> Set

## src/invert.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ invertImplementation -> entries

## src/isDeepEqual.ts  (tp 18, fp 0, fn 0, unscored 5)
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries
  ~ isDeepEqualImplementation -> is
  ~ isDeepEqualImplementation -> isArray
  ~ isDeepEqualImplementation -> keys

## src/isPlainObject.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ isPlainObject -> getPrototypeOf

## src/mapKeys.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapValuesImplementation -> entries

## src/randomInteger.ts  (tp 2, fp 0, fn 0, unscored 3)
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/randomString.ts  (tp 4, fp 0, fn 0, unscored 2)
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/range.ts  (tp 4, fp 0, fn 0, unscored 4)
  ~ ceilingWithSnap -> abs
  ~ ceilingWithSnap -> ceil
  ~ ceilingWithSnap -> round
  ~ rangeImplementation -> from

## src/sample.ts  (tp 8, fp 0, fn 0, unscored 3)
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> min
  ~ sampleImplementation -> random

## src/setPath.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ setPathImplementation -> isArray

## src/stringToPath.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ stringToPath -> Number

## src/swapIndices.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ swapArray -> isNaN

## src/takeLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ takeLastImplementation -> max

## src/times.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

67 of 112 files exactly right.
