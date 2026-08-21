# hybrid(treesitter+llama32b-refs) / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 75.4% [69.8% to 80.5%]   R 92.7% [90.0% to 95.0%]   F1 83.2% [79.6% to 86.3%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/randomString.ts  (tp 4, fp 9, fn 0, unscored 2)
  + randomString -> ALPHABET
  + randomString -> length
  + randomString -> out
  + randomString -> random
  + randomStringImplementation -> !
  + randomStringImplementation -> ALPHABET
  + randomStringImplementation -> iteration
  + randomStringImplementation -> length
  + randomStringImplementation -> out
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 8, fn 0, unscored 0)
  + binarySearchCutoffIndex -> 
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> highIndex = pivotIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> lowIndex = pivotIndex + 1
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/internal/withPrecision.ts  (tp 7, fp 8, fn 0, unscored 5)
  + parseFloat -> shiftedValueAsString
  + shiftDecimalPoint -> exponent
  + shiftDecimalPoint -> n
  + shiftDecimalPoint -> shift
  + shiftDecimalPoint -> value
  + withPrecision -> MAX_PRECISION
  + withPrecision -> RADIX
  + withPrecision -> precision
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

## src/internal/words.ts  (tp 5, fp 6, fn 0, unscored 1)
  + words -> every
  + words -> includes
  + words -> length
  + words -> map
  + words -> some
  + words -> sort
  ~ __module__ -> Set

## src/takeFirstBy.ts  (tp 5, fp 5, fn 1, unscored 0)
  - takeFirstByImplementation -> compareFn
  + takeFirstBy -> compareFn
  + takeFirstBy -> defaultCompare
  + takeFirstBy -> heapMaybeInsert
  + takeFirstBy -> heapify
  + takeFirstBy -> identity

## src/internal/purryOrderRules.ts  (tp 10, fp 2, fn 3, unscored 1)
  - orderRuleComparer -> primaryRule
  - purryOrderRules -> compareFn
  - purryOrderRules -> isOrderRule
  + purryOrderRulesWithArgument -> isProjection
  + purryOrderRulesWithArgument -> orderRuleComparer
  ~ isOrderRule -> isArray

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 2)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/keys.ts  (tp 1, fp 5, fn 0, unscored 0)
  + keys -> EnumerableStringKeyOf
  + keys -> IsNever
  + keys -> IterableContainer
  + keys -> ToString
  + keys -> keys

## src/dropFirstBy.ts  (tp 6, fp 3, fn 1, unscored 0)
  - dropFirstByImplementation -> compareFn
  + dropFirstBy -> compareFn
  + dropFirstBy -> heapMaybeInsert
  + dropFirstBy -> heapify

## src/intersection.ts  (tp 6, fp 3, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  + intersection -> SKIP_ITEM
  + intersection -> lazyEmptyEvaluator
  + intersection -> puryFromLazy

## src/pipe.ts  (tp 13, fp 0, fn 4, unscored 1)
  - pipe -> lazyOp
  - pipe -> op
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  ~ prepareLazyFunction -> assign

## src/purry.ts  (tp 3, fp 4, fn 0, unscored 0)
  + lazyDataLastImpl -> args
  + lazyDataLastImpl -> fn
  + lazyDataLastImpl -> lazy
  + purry -> args

## src/countBy.ts  (tp 6, fp 2, fn 1, unscored 1)
  - countBy -> countByImplementation
  + countBy -> categorizationFn
  + countByImplementation -> PropertyKey
  ~ countByImplementation -> fromEntries

## src/difference.ts  (tp 5, fp 2, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator
  + difference -> SKIP_ITEM
  + difference -> lazyIdentityEvaluator

## src/dropWhile.ts  (tp 5, fp 3, fn 0, unscored 0)
  + dropWhile -> args
  + dropWhile -> data
  + dropWhile -> predicate

## src/endsWith.ts  (tp 3, fp 3, fn 0, unscored 0)
  + endsWith -> defaultCompare
  + endsWith -> identity
  + endsWith -> sliceString

## src/groupByProp.ts  (tp 2, fp 2, fn 1, unscored 2)
  - groupByProp -> groupByPropImplementation
  + groupByProp -> prop
  + groupByPropImplementation -> 
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/meanBy.ts  (tp 4, fp 3, fn 0, unscored 0)
  + meanBy -> defaultCompare
  + meanBy -> fn
  + meanBy -> identity

## src/sortBy.ts  (tp 3, fp 2, fn 1, unscored 0)
  - sortByImplementation -> compareFn
  + sortByImplementation -> defaultCompare
  + sortByImplementation -> identity

## src/sortedIndexBy.ts  (tp 3, fp 2, fn 1, unscored 0)
  - sortedIndexBy -> sortedIndexByImplementation
  + binarySearchCutoffIndex -> pivot
  + sortedIndexBy -> valueFunction

## src/toTitleCase.ts  (tp 8, fp 3, fn 0, unscored 0)
  + toTitleCase -> words
  + toTitleCaseImplementation -> preserveConsecutiveUppercase
  + toTitleCaseImplementation -> word

## src/ceil.ts  (tp 2, fp 2, fn 0, unscored 0)
  + ceil -> ceil
  + ceil -> precision

## src/dropLastWhile.ts  (tp 4, fp 2, fn 0, unscored 0)
  + dropLastWhile -> data
  + dropLastWhile -> predicate

## src/evolve.ts  (tp 4, fp 2, fn 0, unscored 1)
  + evolveImplementation -> add
  + evolveImplementation -> pipe
  ~ evolveImplementation -> entries

## src/floor.ts  (tp 2, fp 2, fn 0, unscored 0)
  + floor -> floor
  + floor -> precision

## src/internal/quickSelect.ts  (tp 5, fp 0, fn 2, unscored 0)
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn

## src/median.ts  (tp 3, fp 1, fn 1, unscored 0)
  - medianImplementation -> numberComparator
  + median -> numberComparator

## src/nthBy.ts  (tp 3, fp 1, fn 1, unscored 0)
  - nthByImplementation -> compareFn
  + nthByImplementation -> CompareFunction

## src/objOf.ts  (tp 2, fp 2, fn 0, unscored 0)
  + objOf -> key
  + objOf -> value

## src/omitBy.ts  (tp 2, fp 1, fn 1, unscored 1)
  - omitBy -> omitByImplementation
  + omitBy -> predicate
  ~ omitByImplementation -> entries

## src/partition.ts  (tp 5, fp 2, fn 0, unscored 0)
  + partitionImplementation -> defaultCompare
  + partitionImplementation -> identity

## src/randomInteger.ts  (tp 2, fp 2, fn 0, unscored 3)
  + randomInteger -> fromCeiled
  + randomInteger -> toFloored
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/round.ts  (tp 2, fp 2, fn 0, unscored 0)
  + round -> precision
  + round -> round

## src/set.ts  (tp 2, fp 2, fn 0, unscored 0)
  + setImplementation -> defaultCompare
  + setImplementation -> identity

## src/split.ts  (tp 1, fp 2, fn 0, unscored 0)
  + split -> SplitBase
  + split -> string

## src/splitWhen.ts  (tp 4, fp 1, fn 1, unscored 0)
  - splitWhenImplementation -> predicate
  + splitWhen -> predicate

## src/swapProps.ts  (tp 2, fp 2, fn 0, unscored 0)
  + swapPropsImplementation -> defaultCompare
  + swapPropsImplementation -> identity

## src/toKebabCase.ts  (tp 4, fp 1, fn 1, unscored 0)
  - toKebabCase -> toKebabCaseImplementation
  + toKebabCase -> words

## src/values.ts  (tp 1, fp 2, fn 0, unscored 0)
  + values -> args
  + values -> values

## src/zipWith.ts  (tp 6, fp 0, fn 2, unscored 0)
  - zipWith -> arg0
  - zipWith -> arg1

## src/add.ts  (tp 2, fp 1, fn 0, unscored 0)
  + add -> add

## src/capitalize.ts  (tp 4, fp 1, fn 0, unscored 0)
  + capitalize -> capitalize

## src/debounce.ts  (tp 8, fp 1, fn 0, unscored 0)
  + debounce -> debounce

## src/differenceWith.ts  (tp 4, fp 1, fn 0, unscored 0)
  + differenceWith -> SKIP_ITEM

## src/divide.ts  (tp 2, fp 1, fn 0, unscored 0)
  + divide -> divide

## src/drop.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyIdentityEvaluator

## src/filter.ts  (tp 5, fp 0, fn 1, unscored 0)
  - filterImplementation -> predicate

## src/findIndex.ts  (tp 3, fp 0, fn 1, unscored 0)
  - findIndexImplementation -> predicate

## src/first.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> firstLazy

## src/flatMap.ts  (tp 5, fp 0, fn 1, unscored 1)
  - flatMapImplementation -> callbackfn
  ~ lazyImplementation -> isArray

## src/forEach.ts  (tp 5, fp 0, fn 1, unscored 0)
  - forEachImplementation -> callbackfn

## src/fromEntries.ts  (tp 1, fp 1, fn 0, unscored 0)
  + fromEntries -> entries

## src/groupBy.ts  (tp 4, fp 1, fn 0, unscored 2)
  + groupByImplementation -> output
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/internal/purryFromLazy.ts  (tp 4, fp 1, fn 0, unscored 1)
  + purryFromLazy -> args
  ~ purryFromLazy -> assign

## src/isIncludedIn.ts  (tp 3, fp 1, fn 0, unscored 0)
  + isIncludedIn -> container

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 1)
  + isPlainObject -> typeof data
  ~ isPlainObject -> getPrototypeOf

## src/join.ts  (tp 3, fp 1, fn 0, unscored 0)
  + joinImplementation -> glue

## src/last.ts  (tp 3, fp 1, fn 0, unscored 0)
  + last -> undefined

## src/length.ts  (tp 2, fp 1, fn 0, unscored 0)
  + lengthImplementation -> length

## src/map.ts  (tp 5, fp 0, fn 1, unscored 0)
  - mapImplementation -> callbackfn

## src/partialLastBind.ts  (tp 1, fp 1, fn 0, unscored 0)
  + partialLastBind -> partial

## src/product.ts  (tp 2, fp 1, fn 0, unscored 0)
  + product -> product

## src/prop.ts  (tp 1, fp 1, fn 0, unscored 0)
  + prop -> prop

## src/rankBy.ts  (tp 3, fp 1, fn 0, unscored 0)
  + rankByImplementation -> targetItem

## src/reduce.ts  (tp 3, fp 0, fn 1, unscored 0)
  - reduceImplementation -> callbackfn

## src/setPath.ts  (tp 3, fp 1, fn 0, unscored 1)
  + setPathImplementation -> push
  ~ setPathImplementation -> isArray

## src/sliceString.ts  (tp 1, fp 1, fn 0, unscored 0)
  + sliceString -> sliceString

## src/sort.ts  (tp 4, fp 1, fn 0, unscored 0)
  + sortImplementation -> defaultCompare

## src/sortedIndex.ts  (tp 3, fp 1, fn 0, unscored 0)
  + sortedIndexImplementation -> item

## src/sortedLastIndex.ts  (tp 3, fp 1, fn 0, unscored 0)
  + binarySearchCutoffIndex -> item

## src/stringToPath.ts  (tp 4, fp 1, fn 0, unscored 1)
  + stringToPath -> NONNEGATIVEINTEGER_RE
  ~ stringToPath -> Number

## src/sum.ts  (tp 2, fp 1, fn 0, unscored 0)
  + sum -> sum

## src/take.ts  (tp 4, fp 0, fn 1, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator

## src/takeLastWhile.ts  (tp 4, fp 1, fn 0, unscored 0)
  + takeLastWhile -> predicate

## src/takeWhile.ts  (tp 5, fp 1, fn 0, unscored 0)
  + takeWhile -> predicate

## src/uncapitalize.ts  (tp 4, fp 1, fn 0, unscored 0)
  + uncapitalize -> uncapitalize

## src/unique.ts  (tp 5, fp 1, fn 0, unscored 0)
  + unique -> SKIP_ITEM

## src/clone.ts  (tp 12, fp 0, fn 0, unscored 3)
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/dropLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ dropLastImplementation -> max

## src/funnel.ts  (tp 8, fp 0, fn 0, unscored 4)
  ~ __module__ -> Symbol
  ~ funnel -> max
  ~ funnel -> min
  ~ funnel -> now

## src/hasProp.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ hasPropImplementation -> hasOwn

## src/hasSubObject.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/invert.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ invertImplementation -> entries

## src/isDeepEqual.ts  (tp 18, fp 0, fn 0, unscored 5)
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries
  ~ isDeepEqualImplementation -> is
  ~ isDeepEqualImplementation -> isArray
  ~ isDeepEqualImplementation -> keys

## src/mapKeys.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapValuesImplementation -> entries

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

## src/takeLast.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ takeLastImplementation -> max

## src/times.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

35 of 112 files exactly right.
