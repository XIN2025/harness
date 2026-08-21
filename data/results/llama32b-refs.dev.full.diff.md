# llama32b-refs / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 50.7% [43.7% to 57.8%]   R 31.1% [26.5% to 35.5%]   F1 38.5% [34.2% to 42.7%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/isDeepEqual.ts  (tp 1, fp 0, fn 17, unscored 0)
  - isDeepEqual -> purry
  - isDeepEqualArrays -> entries
  - isDeepEqualArrays -> isDeepEqualImplementation
  - isDeepEqualImplementation -> getTime
  - isDeepEqualImplementation -> isComparablePrototype
  - isDeepEqualImplementation -> isDeepEqualArrays
  - isDeepEqualImplementation -> isDeepEqualImplementation
  - isDeepEqualImplementation -> isDeepEqualMaps
  - isDeepEqualImplementation -> isDeepEqualSets
  - isDeepEqualImplementation -> toString
  - isDeepEqualMaps -> entries
  - isDeepEqualMaps -> get
  - isDeepEqualMaps -> has
  - isDeepEqualMaps -> isDeepEqualImplementation
  - isDeepEqualSets -> entries
  - isDeepEqualSets -> isDeepEqualImplementation
  - isDeepEqualSets -> splice

## src/pipe.ts  (tp 2, fp 0, fn 15, unscored 0)
  - pipe -> at
  - pipe -> func
  - pipe -> isIterable
  - pipe -> lazyOp
  - pipe -> map
  - pipe -> op
  - pipe -> push
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  - prepareLazyFunction -> lazy
  - processItem -> entries
  - processItem -> lazyFn
  - processItem -> processItem
  - processItem -> push
  - processItem -> slice

## src/internal/purryOrderRules.ts  (tp 1, fp 2, fn 12, unscored 0)
  - isOrderRule -> isProjection
  - orderRuleComparer -> comparator
  - orderRuleComparer -> nextComparer
  - orderRuleComparer -> orderRuleComparer
  - orderRuleComparer -> primaryRule
  - orderRuleComparer -> projector
  - purryOrderRules -> compareFn
  - purryOrderRules -> func
  - purryOrderRules -> isOrderRule
  - purryOrderRules -> orderRuleComparer
  - purryOrderRulesWithArgument -> func
  - purryOrderRulesWithArgument -> purryOrderRules
  + purryOrderRulesWithArgument -> isProjection
  + purryOrderRulesWithArgument -> orderRuleComparer

## src/internal/withPrecision.ts  (tp 1, fp 8, fn 6, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString
  + parseFloat -> shiftedValueAsString
  + shiftDecimalPoint -> exponent
  + shiftDecimalPoint -> n
  + shiftDecimalPoint -> shift
  + shiftDecimalPoint -> value
  + withPrecision -> MAX_PRECISION
  + withPrecision -> RADIX
  + withPrecision -> precision

## src/randomString.ts  (tp 3, fp 9, fn 1, unscored 2)
  - randomString -> purry
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

## src/takeFirstBy.ts  (tp 1, fp 5, fn 5, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  + takeFirstBy -> compareFn
  + takeFirstBy -> defaultCompare
  + takeFirstBy -> heapMaybeInsert
  + takeFirstBy -> heapify
  + takeFirstBy -> identity

## src/countBy.ts  (tp 0, fp 2, fn 7, unscored 0)
  - countBy -> countByImplementation
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set
  + countBy -> categorizationFn
  + countByImplementation -> PropertyKey

## src/debounce.ts  (tp 0, fp 1, fn 8, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> setTimeout
  - debounce -> toString
  + debounce -> debounce

## src/dropFirstBy.ts  (tp 1, fp 3, fn 6, unscored 0)
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice
  + dropFirstBy -> compareFn
  + dropFirstBy -> heapMaybeInsert
  + dropFirstBy -> heapify

## src/intersection.ts  (tp 1, fp 3, fn 6, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set
  + intersection -> SKIP_ITEM
  + intersection -> lazyEmptyEvaluator
  + intersection -> puryFromLazy

## src/clone.ts  (tp 4, fp 0, fn 8, unscored 0)
  - clone -> purry
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 8, fn 0, unscored 0)
  + binarySearchCutoffIndex -> 
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> highIndex = pivotIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> lowIndex = pivotIndex + 1
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/toTitleCase.ts  (tp 3, fp 3, fn 5, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> toUpperCase
  - toTitleCaseImplementation -> words
  + toTitleCase -> words
  + toTitleCaseImplementation -> preserveConsecutiveUppercase
  + toTitleCaseImplementation -> word

## src/difference.ts  (tp 1, fp 2, fn 5, unscored 0)
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set
  + difference -> SKIP_ITEM
  + difference -> lazyIdentityEvaluator

## src/dropWhile.ts  (tp 1, fp 3, fn 4, unscored 0)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice
  + dropWhile -> args
  + dropWhile -> data
  + dropWhile -> predicate

## src/funnel.ts  (tp 1, fp 0, fn 7, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout

## src/sample.ts  (tp 1, fp 0, fn 7, unscored 0)
  - sample -> purry
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort

## src/internal/words.ts  (tp 5, fp 6, fn 0, unscored 0)
  + words -> every
  + words -> includes
  + words -> length
  + words -> map
  + words -> some
  + words -> sort

## src/meanBy.ts  (tp 1, fp 3, fn 3, unscored 0)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn
  + meanBy -> defaultCompare
  + meanBy -> fn
  + meanBy -> identity

## src/partition.ts  (tp 1, fp 2, fn 4, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push
  + partitionImplementation -> defaultCompare
  + partitionImplementation -> identity

## src/purry.ts  (tp 1, fp 4, fn 2, unscored 0)
  - purry -> Error
  - purry -> lazyDataLastImpl
  + lazyDataLastImpl -> args
  + lazyDataLastImpl -> fn
  + lazyDataLastImpl -> lazy
  + purry -> args

## src/zipWith.ts  (tp 2, fp 0, fn 6, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyDataLastImpl
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/dropLastWhile.ts  (tp 1, fp 2, fn 3, unscored 0)
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  + dropLastWhile -> data
  + dropLastWhile -> predicate

## src/endsWith.ts  (tp 1, fp 3, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith
  + endsWith -> defaultCompare
  + endsWith -> identity
  + endsWith -> sliceString

## src/evolve.ts  (tp 1, fp 2, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value
  + evolveImplementation -> add
  + evolveImplementation -> pipe

## src/groupByProp.ts  (tp 0, fp 2, fn 3, unscored 0)
  - groupByProp -> groupByPropImplementation
  - groupByProp -> purry
  - groupByPropImplementation -> push
  + groupByProp -> prop
  + groupByPropImplementation -> 

## src/internal/quickSelect.ts  (tp 2, fp 0, fn 5, unscored 0)
  - partition -> compareFn
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 0)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy

## src/keys.ts  (tp 1, fp 5, fn 0, unscored 0)
  + keys -> EnumerableStringKeyOf
  + keys -> IsNever
  + keys -> IterableContainer
  + keys -> ToString
  + keys -> keys

## src/sortBy.ts  (tp 1, fp 2, fn 3, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> compareFn
  - sortByImplementation -> sort
  + sortByImplementation -> defaultCompare
  + sortByImplementation -> identity

## src/sortedIndexBy.ts  (tp 1, fp 2, fn 3, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexBy -> sortedIndexByImplementation
  - sortedIndexByImplementation -> binarySearchCutoffIndex
  + binarySearchCutoffIndex -> pivot
  + sortedIndexBy -> valueFunction

## src/splitWhen.ts  (tp 1, fp 1, fn 4, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> predicate
  - splitWhenImplementation -> slice
  + splitWhen -> predicate

## src/stringToPath.ts  (tp 0, fp 1, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test
  + stringToPath -> NONNEGATIVEINTEGER_RE

## src/takeWhile.ts  (tp 1, fp 1, fn 4, unscored 0)
  - takeWhile -> purry
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push
  + takeWhile -> predicate

## src/toKebabCase.ts  (tp 1, fp 1, fn 4, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> words
  + toKebabCase -> words

## src/unique.ts  (tp 1, fp 1, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy
  + unique -> SKIP_ITEM

## src/capitalize.ts  (tp 1, fp 1, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase
  + capitalize -> capitalize

## src/filter.ts  (tp 2, fp 0, fn 4, unscored 0)
  - filter -> purry
  - filterImplementation -> filter
  - filterImplementation -> predicate
  - lazyImplementation -> predicate

## src/flatMap.ts  (tp 2, fp 0, fn 4, unscored 0)
  - flatMap -> purry
  - flatMapImplementation -> callbackfn
  - flatMapImplementation -> flatMap
  - lazyImplementation -> callbackfn

## src/forEach.ts  (tp 2, fp 0, fn 4, unscored 0)
  - forEach -> purry
  - forEachImplementation -> callbackfn
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn

## src/groupBy.ts  (tp 1, fp 1, fn 3, unscored 1)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push
  + groupByImplementation -> output
  ~ groupByImplementation -> create

## src/isIncludedIn.ts  (tp 0, fp 1, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes
  + isIncludedIn -> container

## src/map.ts  (tp 2, fp 0, fn 4, unscored 0)
  - lazyImplementation -> callbackfn
  - map -> purry
  - mapImplementation -> callbackfn
  - mapImplementation -> map

## src/median.ts  (tp 1, fp 1, fn 3, unscored 0)
  - median -> purry
  - medianImplementation -> numberComparator
  - medianImplementation -> sort
  + median -> numberComparator

## src/omitBy.ts  (tp 0, fp 1, fn 3, unscored 0)
  - omitBy -> omitByImplementation
  - omitBy -> purry
  - omitByImplementation -> predicate
  + omitBy -> predicate

## src/randomInteger.ts  (tp 0, fp 2, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  + randomInteger -> fromCeiled
  + randomInteger -> toFloored
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/takeLastWhile.ts  (tp 1, fp 1, fn 3, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice
  + takeLastWhile -> predicate

## src/uncapitalize.ts  (tp 1, fp 1, fn 3, unscored 0)
  - uncapitalize -> purry
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase
  + uncapitalize -> uncapitalize

## src/uniqueBy.ts  (tp 2, fp 0, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has

## src/when.ts  (tp 1, fp 0, fn 4, unscored 0)
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate

## src/ceil.ts  (tp 1, fp 2, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil
  + ceil -> precision

## src/differenceWith.ts  (tp 2, fp 1, fn 2, unscored 0)
  - lazyImplementation -> every
  - lazyImplementation -> isEqual
  + differenceWith -> SKIP_ITEM

## src/drop.ts  (tp 2, fp 0, fn 3, unscored 0)
  - drop -> purry
  - dropImplementation -> slice
  - lazyImplementation -> lazyIdentityEvaluator

## src/findIndex.ts  (tp 1, fp 0, fn 3, unscored 0)
  - findIndex -> purry
  - findIndexImplementation -> findIndex
  - findIndexImplementation -> predicate

## src/first.ts  (tp 2, fp 0, fn 3, unscored 0)
  - first -> purry
  - first -> toSingle
  - lazyImplementation -> firstLazy

## src/floor.ts  (tp 1, fp 2, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor
  + floor -> precision

## src/indexBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/internal/purryFromLazy.ts  (tp 2, fp 1, fn 2, unscored 0)
  - purryFromLazy -> Error
  - purryFromLazy -> pipe
  + purryFromLazy -> args

## src/last.ts  (tp 1, fp 1, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at
  + last -> undefined

## src/nthBy.ts  (tp 2, fp 1, fn 2, unscored 0)
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> compareFn
  + nthByImplementation -> CompareFunction

## src/objOf.ts  (tp 1, fp 2, fn 1, unscored 0)
  - objOf -> purry
  + objOf -> key
  + objOf -> value

## src/reduce.ts  (tp 1, fp 0, fn 3, unscored 0)
  - reduce -> purry
  - reduceImplementation -> callbackfn
  - reduceImplementation -> reduce

## src/round.ts  (tp 1, fp 2, fn 1, unscored 0)
  - round -> purry
  + round -> precision
  + round -> round

## src/set.ts  (tp 1, fp 2, fn 1, unscored 0)
  - set -> purry
  + setImplementation -> defaultCompare
  + setImplementation -> identity

## src/setPath.ts  (tp 1, fp 1, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation
  + setPathImplementation -> push

## src/sort.ts  (tp 2, fp 1, fn 2, unscored 0)
  - sort -> purry
  - sortImplementation -> sort
  + sortImplementation -> defaultCompare

## src/sortedLastIndex.ts  (tp 1, fp 1, fn 2, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndexImplementation -> binarySearchCutoffIndex
  + binarySearchCutoffIndex -> item

## src/split.ts  (tp 0, fp 2, fn 1, unscored 0)
  - split -> split
  + split -> SplitBase
  + split -> string

## src/swapIndices.ts  (tp 1, fp 0, fn 3, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray

## src/swapProps.ts  (tp 1, fp 2, fn 1, unscored 0)
  - swapProps -> purry
  + swapPropsImplementation -> defaultCompare
  + swapPropsImplementation -> identity

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> purry
  - takeImplementation -> slice

## src/add.ts  (tp 1, fp 1, fn 1, unscored 0)
  - add -> purry
  + add -> add

## src/divide.ts  (tp 1, fp 1, fn 1, unscored 0)
  - divide -> purry
  + divide -> divide

## src/findLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - findLast -> purry
  - findLastImplementation -> predicate

## src/findLastIndex.ts  (tp 1, fp 0, fn 2, unscored 0)
  - findLastIndex -> purry
  - findLastIndexImplementation -> predicate

## src/fromEntries.ts  (tp 0, fp 1, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> entries

## src/fromKeys.ts  (tp 2, fp 0, fn 2, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> entries

## src/join.ts  (tp 2, fp 1, fn 1, unscored 0)
  - join -> purry
  + joinImplementation -> glue

## src/length.ts  (tp 1, fp 1, fn 1, unscored 0)
  - length -> purry
  + lengthImplementation -> length

## src/mapKeys.ts  (tp 1, fp 0, fn 2, unscored 1)
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 1, fp 0, fn 2, unscored 0)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper

## src/omit.ts  (tp 1, fp 0, fn 2, unscored 0)
  - omit -> purry
  - omitImplementation -> hasAtLeast

## src/product.ts  (tp 1, fp 1, fn 1, unscored 0)
  - product -> purry
  + product -> product

## src/pullObject.ts  (tp 3, fp 0, fn 2, unscored 0)
  - pullObject -> purry
  - pullObjectImplementation -> entries

## src/range.ts  (tp 2, fp 0, fn 2, unscored 1)
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  ~ ceilingWithSnap -> ceil

## src/rankBy.ts  (tp 2, fp 1, fn 1, unscored 0)
  - rankBy -> purryOrderRulesWithArgument
  + rankByImplementation -> targetItem

## src/sliceString.ts  (tp 0, fp 1, fn 1, unscored 0)
  - sliceString -> slice
  + sliceString -> sliceString

## src/sortedIndex.ts  (tp 2, fp 1, fn 1, unscored 0)
  - sortedIndex -> purry
  + sortedIndexImplementation -> item

## src/sum.ts  (tp 1, fp 1, fn 1, unscored 0)
  - sum -> purry
  + sum -> sum

## src/sumBy.ts  (tp 3, fp 0, fn 2, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> entries

## src/times.ts  (tp 1, fp 0, fn 2, unscored 2)
  - times -> purry
  - timesImplementation -> fn
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/toUpperCase.ts  (tp 1, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/values.ts  (tp 1, fp 2, fn 0, unscored 0)
  + values -> args
  + values -> values

## src/zip.ts  (tp 2, fp 0, fn 2, unscored 0)
  - zip -> purry
  - zipImplementation -> map

## src/concat.ts  (tp 1, fp 0, fn 1, unscored 0)
  - concat -> purry

## src/defaultTo.ts  (tp 1, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/dropLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - dropLastImplementation -> slice

## src/hasAtLeast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/hasProp.ts  (tp 1, fp 0, fn 1, unscored 1)
  - hasProp -> purry
  ~ hasPropImplementation -> hasOwn

## src/hasSubObject.ts  (tp 2, fp 0, fn 1, unscored 0)
  - hasSubObject -> purry

## src/invert.ts  (tp 1, fp 0, fn 1, unscored 1)
  - invert -> purry
  ~ invertImplementation -> entries

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 0)
  + isPlainObject -> typeof data

## src/merge.ts  (tp 1, fp 0, fn 1, unscored 0)
  - merge -> purry

## src/only.ts  (tp 1, fp 0, fn 1, unscored 0)
  - only -> purry

## src/partialLastBind.ts  (tp 1, fp 1, fn 0, unscored 0)
  + partialLastBind -> partial

## src/pathOr.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pathOr -> purry

## src/pick.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pick -> purry

## src/prop.ts  (tp 1, fp 1, fn 0, unscored 0)
  + prop -> prop

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/sortedLastIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedLastIndexBy -> purry

## src/takeLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - takeLastImplementation -> slice

1 of 112 files exactly right.
