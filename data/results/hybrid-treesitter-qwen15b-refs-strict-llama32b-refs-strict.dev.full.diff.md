# hybrid(treesitter+qwen15b-refs-strict & llama32b-refs-strict) / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 96.2% [91.5% to 98.2%]   R 88.8% [85.8% to 91.6%]   F1 92.3% [89.9% to 94.3%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 2)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/internal/purryOrderRules.ts  (tp 10, fp 1, fn 3, unscored 1)
  - orderRuleComparer -> primaryRule
  - purryOrderRules -> compareFn
  - purryOrderRules -> isOrderRule
  + purryOrderRulesWithArgument -> orderRuleComparer
  ~ isOrderRule -> isArray

## src/pipe.ts  (tp 13, fp 0, fn 4, unscored 1)
  - pipe -> lazyOp
  - pipe -> op
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  ~ prepareLazyFunction -> assign

## src/toKebabCase.ts  (tp 4, fp 3, fn 1, unscored 0)
  - toKebabCase -> toKebabCaseImplementation
  + toKebabCase -> join
  + toKebabCase -> toLowerCase
  + toKebabCase -> words

## src/zipWith.ts  (tp 5, fp 0, fn 3, unscored 0)
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation

## src/difference.ts  (tp 5, fp 1, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator
  + difference -> lazyIdentityEvaluator

## src/filter.ts  (tp 4, fp 0, fn 2, unscored 0)
  - filter -> lazyImplementation
  - filterImplementation -> predicate

## src/internal/purryFromLazy.ts  (tp 2, fp 0, fn 2, unscored 1)
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  ~ purryFromLazy -> assign

## src/internal/quickSelect.ts  (tp 5, fp 0, fn 2, unscored 0)
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn

## src/intersection.ts  (tp 6, fp 1, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  + intersection -> lazyEmptyEvaluator

## src/median.ts  (tp 3, fp 1, fn 1, unscored 0)
  - medianImplementation -> numberComparator
  + median -> numberComparator

## src/nthBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - nthBy -> nthByImplementation
  - nthByImplementation -> compareFn

## src/sortBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortBy -> sortByImplementation
  - sortByImplementation -> compareFn

## src/takeFirstBy.ts  (tp 4, fp 0, fn 2, unscored 0)
  - takeFirstBy -> takeFirstByImplementation
  - takeFirstByImplementation -> compareFn

## src/clone.ts  (tp 11, fp 0, fn 1, unscored 3)
  - clone -> cloneImplementation
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/drop.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropFirstBy.ts  (tp 6, fp 0, fn 1, unscored 0)
  - dropFirstByImplementation -> compareFn

## src/findIndex.ts  (tp 3, fp 0, fn 1, unscored 0)
  - findIndexImplementation -> predicate

## src/first.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> firstLazy

## src/flatMap.ts  (tp 5, fp 0, fn 1, unscored 1)
  - flatMapImplementation -> callbackfn
  ~ lazyImplementation -> isArray

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

## src/hasProp.ts  (tp 1, fp 0, fn 1, unscored 1)
  - hasProp -> hasPropImplementation
  ~ hasPropImplementation -> hasOwn

## src/keys.ts  (tp 1, fp 1, fn 0, unscored 0)
  + keys -> keys

## src/map.ts  (tp 5, fp 0, fn 1, unscored 0)
  - mapImplementation -> callbackfn

## src/mapKeys.ts  (tp 2, fp 0, fn 1, unscored 1)
  - mapKeys -> mapKeysImplementation
  ~ mapKeysImplementation -> entries

## src/omit.ts  (tp 2, fp 0, fn 1, unscored 0)
  - omit -> omitImplementation

## src/omitBy.ts  (tp 2, fp 0, fn 1, unscored 1)
  - omitBy -> omitByImplementation
  ~ omitByImplementation -> entries

## src/pathOr.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pathOr -> pathOrImplementation

## src/reduce.ts  (tp 3, fp 0, fn 1, unscored 0)
  - reduceImplementation -> callbackfn

## src/round.ts  (tp 2, fp 1, fn 0, unscored 0)
  + round -> round

## src/sample.ts  (tp 7, fp 0, fn 1, unscored 3)
  - sample -> sampleImplementation
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> min
  ~ sampleImplementation -> random

## src/sort.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortImplementation -> cmp

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

## src/swapIndices.ts  (tp 3, fp 0, fn 1, unscored 1)
  - swapIndices -> swapIndicesImplementation
  ~ swapArray -> isNaN

## src/take.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator

## src/toTitleCase.ts  (tp 8, fp 1, fn 0, unscored 0)
  + toTitleCase -> words

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

## src/countBy.ts  (tp 7, fp 0, fn 0, unscored 1)
  ~ countByImplementation -> fromEntries

## src/dropLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ dropLastImplementation -> max

## src/evolve.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ evolveImplementation -> entries

## src/groupBy.ts  (tp 4, fp 0, fn 0, unscored 2)
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/hasSubObject.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/internal/withPrecision.ts  (tp 7, fp 0, fn 0, unscored 5)
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

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

## src/setPath.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ setPathImplementation -> isArray

## src/stringToPath.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ stringToPath -> Number

## src/takeLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ takeLastImplementation -> max

## src/times.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

69 of 112 files exactly right.
