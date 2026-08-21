# hybrid(treesitter+qwen15b-refs) / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 79.8% [75.4% to 83.3%]   R 92.1% [89.1% to 94.6%]   F1 85.5% [82.8% to 87.8%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/internal/purryOrderRules.ts  (tp 10, fp 3, fn 3, unscored 1)
  - orderRuleComparer -> primaryRule
  - purryOrderRules -> compareFn
  - purryOrderRules -> isOrderRule
  + sortBy -> sortByImplementation
  + sortByImplementation -> defaultCompare
  + sortByImplementation -> identity
  ~ isOrderRule -> isArray

## src/internal/words.ts  (tp 5, fp 6, fn 0, unscored 1)
  + words -> WHITESPACE
  + words -> WORD_SEPARATORS
  + words -> character
  + words -> data
  + words -> word
  + words -> words
  ~ __module__ -> Set

## src/funnel.ts  (tp 7, fp 4, fn 1, unscored 4)
  - funnel -> voidReducer
  + funnel -> call
  + funnel -> cancel
  + funnel -> flush
  + funnel -> isIdle
  ~ __module__ -> Symbol
  ~ funnel -> max
  ~ funnel -> min
  ~ funnel -> now

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 2)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/pipe.ts  (tp 13, fp 1, fn 4, unscored 1)
  - pipe -> lazyOp
  - pipe -> op
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  + pipe -> next
  ~ prepareLazyFunction -> assign

## src/debounce.ts  (tp 8, fp 4, fn 0, unscored 0)
  + debounce -> coolDownTimeoutId
  + debounce -> latestCallArgs
  + debounce -> maxWaitTimeoutId
  + debounce -> result

## src/evolve.ts  (tp 4, fp 4, fn 0, unscored 1)
  + evolveImplementation -> data
  + evolveImplementation -> evolver
  + evolveImplementation -> out
  + evolveImplementation -> typeof value === 'function
  ~ evolveImplementation -> entries

## src/internal/quickSelect.ts  (tp 6, fp 3, fn 1, unscored 0)
  - quickSelect -> compareFn
  + quickSelect -> partition
  + quickSelectImplementation -> pivotIndex
  + quickSelectImplementation -> swapInPlace

## src/intersection.ts  (tp 6, fp 3, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  + lazyImplementation -> other
  + lazyImplementation -> remaining
  + lazyImplementation -> value

## src/isDeepEqual.ts  (tp 18, fp 4, fn 0, unscored 5)
  + isDeepEqual -> isComparablePrototype
  + isDeepEqual -> isDeepEqualArrays
  + isDeepEqual -> isDeepEqualMaps
  + isDeepEqual -> isDeepEqualSets
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries
  ~ isDeepEqualImplementation -> is
  ~ isDeepEqualImplementation -> isArray
  ~ isDeepEqualImplementation -> keys

## src/setPath.ts  (tp 3, fp 4, fn 0, unscored 1)
  + setPathImplementation -> copy
  + setPathImplementation -> currentValue
  + setPathImplementation -> data
  + setPathImplementation -> remaining
  ~ setPathImplementation -> isArray

## src/clone.ts  (tp 11, fp 2, fn 1, unscored 3)
  - clone -> cloneImplementation
  + clone -> deepCloneArray
  + clone -> deepCloneObject
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/difference.ts  (tp 5, fp 2, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator
  + lazyImplementation -> copies
  + lazyImplementation -> remaining

## src/nthBy.ts  (tp 2, fp 1, fn 2, unscored 0)
  - nthBy -> nthByImplementation
  - nthByImplementation -> compareFn
  + nthBy -> quickSelect

## src/sort.ts  (tp 3, fp 2, fn 1, unscored 0)
  - sortImplementation -> cmp
  + sortImplementation -> defaultCompare
  + sortImplementation -> identity

## src/toKebabCase.ts  (tp 4, fp 2, fn 1, unscored 0)
  - toKebabCase -> toKebabCaseImplementation
  + toKebabCase -> join
  + toKebabCase -> words

## src/zipWith.ts  (tp 5, fp 0, fn 3, unscored 0)
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation

## src/findIndex.ts  (tp 3, fp 1, fn 1, unscored 0)
  - findIndexImplementation -> predicate
  + findIndex -> predicate

## src/hasAtLeast.ts  (tp 2, fp 2, fn 0, unscored 0)
  + hasAtLeastImplementation -> data
  + hasAtLeastImplementation -> minimum

## src/internal/purryFromLazy.ts  (tp 2, fp 0, fn 2, unscored 1)
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  ~ purryFromLazy -> assign

## src/internal/withPrecision.ts  (tp 7, fp 2, fn 0, unscored 5)
  + withPrecision -> precision
  + withPrecision -> value
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

## src/merge.ts  (tp 2, fp 2, fn 0, unscored 0)
  + mergeImplementation -> data
  + mergeImplementation -> source

## src/objOf.ts  (tp 2, fp 2, fn 0, unscored 0)
  + objOfImplementation -> key
  + objOfImplementation -> value

## src/only.ts  (tp 2, fp 2, fn 0, unscored 0)
  + onlyImplementation -> defaultCompare
  + onlyImplementation -> identity

## src/partialLastBind.ts  (tp 1, fp 2, fn 0, unscored 0)
  + partialLastBind -> stringify
  + pipe -> stringify

## src/pathOr.ts  (tp 2, fp 2, fn 0, unscored 0)
  + pathOr -> defaultTo
  + pathOr -> prop

## src/pick.ts  (tp 2, fp 2, fn 0, unscored 0)
  + pickImplementation -> keys
  + pickImplementation -> object

## src/product.ts  (tp 2, fp 2, fn 0, unscored 0)
  + productImplementation -> data
  + productImplementation -> value

## src/purry.ts  (tp 3, fp 2, fn 0, unscored 0)
  + purry -> args
  + purry -> lazy

## src/sortBy.ts  (tp 3, fp 1, fn 1, unscored 0)
  - sortByImplementation -> compareFn
  + sortBy -> defaultCompare

## src/sortedIndex.ts  (tp 2, fp 1, fn 1, unscored 0)
  - sortedIndex -> sortedIndexImplementation
  + sortedIndex -> binarySearchCutoffIndex

## src/sortedIndexBy.ts  (tp 3, fp 1, fn 1, unscored 0)
  - sortedIndexBy -> sortedIndexByImplementation
  + sortedIndexBy -> binarySearchCutoffIndex

## src/sortedIndexWith.ts  (tp 2, fp 2, fn 0, unscored 0)
  + sortedIndexWith -> defaultCompare
  + sortedIndexWith -> identity

## src/sortedLastIndex.ts  (tp 2, fp 1, fn 1, unscored 0)
  - sortedLastIndex -> sortedLastIndexImplementation
  + sortedLastIndex -> binarySearchCutoffIndex

## src/sortedLastIndexBy.ts  (tp 3, fp 1, fn 1, unscored 0)
  - sortedLastIndexBy -> sortedLastIndexByImplementation
  + sortedLastIndexBy -> binarySearchCutoffIndex

## src/sum.ts  (tp 2, fp 2, fn 0, unscored 0)
  + sumImplementation -> data
  + sumImplementation -> value

## src/zip.ts  (tp 3, fp 1, fn 1, unscored 0)
  - zip -> lazyImplementation
  + zipImplementation -> lazyImplementation

## src/capitalize.ts  (tp 4, fp 1, fn 0, unscored 0)
  + capitalizeImplementation -> data

## src/ceil.ts  (tp 2, fp 1, fn 0, unscored 0)
  + ceil -> ceil

## src/concat.ts  (tp 2, fp 1, fn 0, unscored 0)
  + concatImplementation -> concat

## src/differenceWith.ts  (tp 4, fp 1, fn 0, unscored 0)
  + differenceWith -> isEqual

## src/drop.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropFirstBy.ts  (tp 6, fp 0, fn 1, unscored 0)
  - dropFirstByImplementation -> compareFn

## src/endsWith.ts  (tp 3, fp 1, fn 0, unscored 0)
  + endsWithImplementation -> suffix

## src/filter.ts  (tp 5, fp 0, fn 1, unscored 0)
  - filterImplementation -> predicate

## src/first.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> firstLazy

## src/flatMap.ts  (tp 5, fp 0, fn 1, unscored 1)
  - flatMapImplementation -> callbackfn
  ~ lazyImplementation -> isArray

## src/floor.ts  (tp 2, fp 1, fn 0, unscored 0)
  + floor -> floor

## src/forEach.ts  (tp 5, fp 0, fn 1, unscored 0)
  - forEachImplementation -> callbackfn

## src/fromEntries.ts  (tp 1, fp 1, fn 0, unscored 0)
  + fromEntries -> fromEntries

## src/groupBy.ts  (tp 4, fp 1, fn 0, unscored 2)
  + groupByImplementation -> data
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/hasProp.ts  (tp 2, fp 1, fn 0, unscored 1)
  + hasProp -> hasOwn
  ~ hasPropImplementation -> hasOwn

## src/invert.ts  (tp 2, fp 1, fn 0, unscored 1)
  + invertImplementation -> result
  ~ invertImplementation -> entries

## src/join.ts  (tp 3, fp 1, fn 0, unscored 0)
  + joinImplementation -> glue

## src/keys.ts  (tp 1, fp 1, fn 0, unscored 0)
  + keys -> keys

## src/last.ts  (tp 3, fp 1, fn 0, unscored 0)
  + lastImplementation -> array

## src/map.ts  (tp 5, fp 0, fn 1, unscored 0)
  - mapImplementation -> callbackfn

## src/meanBy.ts  (tp 4, fp 1, fn 0, unscored 0)
  + meanBy -> fn

## src/partition.ts  (tp 5, fp 1, fn 0, unscored 0)
  + partitionImplementation -> data

## src/piped.ts  (tp 1, fp 1, fn 0, unscored 0)
  + pipe -> identity

## src/rankBy.ts  (tp 3, fp 1, fn 0, unscored 0)
  + rankBy -> compareFn

## src/round.ts  (tp 2, fp 1, fn 0, unscored 0)
  + round -> round

## src/stringToPath.ts  (tp 4, fp 1, fn 0, unscored 1)
  + stringToPath -> stringToPathImpl
  ~ stringToPath -> Number

## src/swapProps.ts  (tp 2, fp 1, fn 0, unscored 0)
  + swapPropsImplementation -> obj

## src/take.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator

## src/takeFirstBy.ts  (tp 6, fp 1, fn 0, unscored 0)
  + takeFirstByImplementation -> n

## src/takeLast.ts  (tp 3, fp 1, fn 0, unscored 1)
  + takeLastImplementation -> n
  ~ takeLastImplementation -> max

## src/toTitleCase.ts  (tp 8, fp 1, fn 0, unscored 0)
  + toTitleCaseImplementation -> word

## src/toUpperCase.ts  (tp 3, fp 1, fn 0, unscored 0)
  + toUpperCaseImplementation -> data

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

## src/countBy.ts  (tp 7, fp 0, fn 0, unscored 1)
  ~ countByImplementation -> fromEntries

## src/dropLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ dropLastImplementation -> max

## src/groupByProp.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/hasSubObject.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/isPlainObject.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ isPlainObject -> getPrototypeOf

## src/mapKeys.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapValuesImplementation -> entries

## src/omitBy.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ omitByImplementation -> entries

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

## src/swapIndices.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ swapArray -> isNaN

## src/times.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

42 of 112 files exactly right.
