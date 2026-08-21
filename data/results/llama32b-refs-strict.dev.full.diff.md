# llama32b-refs-strict / dev / cut=full

raw 111/112 (99.1%)  ·  fence-stripped 111/112 (99.1%)  ·  schema 111/112 (99.1%)
P 70.4% [60.8% to 78.2%]   R 33.0% [28.0% to 37.7%]   F1 45.0% [39.9% to 49.7%]

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

## src/internal/purryOrderRules.ts  (tp 0, fp 1, fn 13, unscored 0)
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
  - purryOrderRulesWithArgument -> isOrderRule
  - purryOrderRulesWithArgument -> purryOrderRules
  + purryOrderRulesWithArgument -> orderRuleComparer

## src/clone.ts  (tp 3, fp 0, fn 9, unscored 0)
  - clone -> purry
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - cloneImplementation -> structuredClone
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push

## src/toKebabCase.ts  (tp 0, fp 4, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + purry -> toKebabCaseImplementation
  + toKebabCase -> join
  + toKebabCase -> toLowerCase
  + toKebabCase -> words

## src/debounce.ts  (tp 0, fp 0, fn 8, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> setTimeout
  - debounce -> toString

## src/dropLastWhile.ts  (tp 3, fp 7, fn 1, unscored 0)
  - dropLastWhileImplementation -> slice
  + dropLastWhile -> for
  + dropLastWhile -> map
  + dropLastWhile -> slice
  + dropLastWhileImplementation -> data
  + dropLastWhileImplementation -> i
  + dropLastWhileImplementation -> i >= 0
  + dropLastWhileImplementation -> length

## src/toTitleCase.ts  (tp 4, fp 4, fn 4, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> test
  - toTitleCaseImplementation -> toUpperCase
  + toTitleCase -> join
  + toTitleCase -> map
  + toTitleCase -> toLowerCase
  + toTitleCase -> words

## src/funnel.ts  (tp 1, fp 0, fn 7, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout

## src/intersection.ts  (tp 2, fp 2, fn 5, unscored 0)
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set
  + intersection -> SKIP_ITEM
  + intersection -> lazyEmptyEvaluator

## src/partialLastBind.ts  (tp 0, fp 6, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> Parameters
  + partialLastBind -> PartialLastBindError
  + partialLastBind -> RemoveSuffix
  + partialLastBind -> ReturnType
  + partialLastBind -> StrictFunction
  + partialLastBind -> TupleSplits

## src/sample.ts  (tp 1, fp 0, fn 7, unscored 0)
  - sample -> purry
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort

## src/countBy.ts  (tp 1, fp 0, fn 6, unscored 0)
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set

## src/difference.ts  (tp 2, fp 2, fn 4, unscored 0)
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set
  + difference -> SKIP_ITEM
  + difference -> lazyIdentityEvaluator

## src/internal/withPrecision.ts  (tp 1, fp 0, fn 6, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> roundingFn
  - withPrecision -> toString

## src/filter.ts  (tp 1, fp 0, fn 5, unscored 0)
  - filter -> lazyImplementation
  - filter -> purry
  - filterImplementation -> filter
  - filterImplementation -> predicate
  - lazyImplementation -> predicate

## src/internal/quickSelect.ts  (tp 2, fp 0, fn 5, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn
  - quickSelectImplementation -> quickSelectImplementation

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 0)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy

## src/isIncludedIn.ts  (tp 0, fp 2, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes
  + isIncludedIn -> container
  + isIncludedIn -> data

## src/stringToPath.ts  (tp 0, fp 1, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test
  + stringToPath -> stringToPathImpl

## src/swapIndices.ts  (tp 0, fp 1, fn 4, unscored 0)
  - swapIndices -> purry
  - swapIndices -> swapIndicesImplementation
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray
  + swapIndices -> swapArrayInternal

## src/takeFirstBy.ts  (tp 1, fp 0, fn 5, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice

## src/zipWith.ts  (tp 3, fp 0, fn 5, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/dropWhile.ts  (tp 2, fp 1, fn 3, unscored 0)
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice
  + dropWhile -> dropWhile

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

## src/internal/words.ts  (tp 3, fp 2, fn 2, unscored 0)
  - words -> has
  - words -> push
  + words -> map
  + words -> sort

## src/keys.ts  (tp 1, fp 4, fn 0, unscored 0)
  + keys -> EnumerableStringKeyOf
  + keys -> IterableContainer
  + keys -> ToString
  + keys -> keys

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

## src/nthBy.ts  (tp 1, fp 1, fn 3, unscored 0)
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> compareFn
  - nthByImplementation -> quickSelect
  + purryOrderRulesWithArgument -> nthByImplementation

## src/omit.ts  (tp 0, fp 1, fn 3, unscored 0)
  - omit -> omitImplementation
  - omit -> purry
  - omitImplementation -> hasAtLeast
  + omit -> OmitUnboundedRecord

## src/partition.ts  (tp 1, fp 0, fn 4, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/range.ts  (tp 1, fp 1, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + range -> ceilingWithSnap

## src/splitWhen.ts  (tp 1, fp 0, fn 4, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> predicate
  - splitWhenImplementation -> slice

## src/sumBy.ts  (tp 1, fp 0, fn 4, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/takeLastWhile.ts  (tp 2, fp 2, fn 2, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> predicate
  + takeLastWhileImplementation -> map
  + takeLastWhileImplementation -> sort

## src/takeWhile.ts  (tp 1, fp 0, fn 4, unscored 0)
  - takeWhile -> purry
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push

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

## src/capitalize.ts  (tp 1, fp 0, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase

## src/drop.ts  (tp 2, fp 0, fn 3, unscored 0)
  - drop -> purry
  - dropImplementation -> slice
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropFirstBy.ts  (tp 4, fp 0, fn 3, unscored 0)
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice

## src/evolve.ts  (tp 1, fp 0, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/findIndex.ts  (tp 1, fp 0, fn 3, unscored 0)
  - findIndex -> purry
  - findIndexImplementation -> findIndex
  - findIndexImplementation -> predicate

## src/first.ts  (tp 2, fp 0, fn 3, unscored 0)
  - first -> purry
  - first -> toSingle
  - lazyImplementation -> firstLazy

## src/indexBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/internal/purryFromLazy.ts  (tp 1, fp 0, fn 3, unscored 1)
  - purryFromLazy -> Error
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  ~ purryFromLazy -> assign

## src/meanBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn

## src/randomString.ts  (tp 1, fp 0, fn 3, unscored 0)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push

## src/sort.ts  (tp 1, fp 0, fn 3, unscored 0)
  - sort -> purry
  - sortImplementation -> cmp
  - sortImplementation -> sort

## src/sortedLastIndexBy.ts  (tp 2, fp 1, fn 2, unscored 0)
  - sortedLastIndexByImplementation -> binarySearchCutoffIndex
  - sortedLastIndexByImplementation -> valueFunction
  + binarySearchCutoffIndex -> binarySearchCutoffIndex

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> purry
  - takeImplementation -> slice

## src/times.ts  (tp 2, fp 2, fn 1, unscored 2)
  - timesImplementation -> fn
  + timesImplementation -> for
  + timesImplementation -> new Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/unique.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has

## src/differenceWith.ts  (tp 2, fp 0, fn 2, unscored 0)
  - lazyImplementation -> every
  - lazyImplementation -> isEqual

## src/dropLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - dropLast -> purry
  - dropLastImplementation -> slice

## src/endsWith.ts  (tp 1, fp 0, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith

## src/findLastIndex.ts  (tp 1, fp 0, fn 2, unscored 0)
  - findLastIndex -> purry
  - findLastIndexImplementation -> predicate

## src/fromEntries.ts  (tp 0, fp 1, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> fromEntriesArrayWithLiteralKeys

## src/fromKeys.ts  (tp 2, fp 0, fn 2, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> entries

## src/groupBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/groupByProp.ts  (tp 2, fp 1, fn 1, unscored 1)
  - groupByProp -> groupByPropImplementation
  + groupByPropImplementation -> output
  ~ groupByPropImplementation -> create

## src/hasSubObject.ts  (tp 1, fp 0, fn 2, unscored 0)
  - hasSubObject -> purry
  - hasSubObjectImplementation -> isDeepEqual

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 2, fn 0, unscored 0)
  + binarySearchCutoffIndex -> 
  + binarySearchCutoffIndex -> lowIndex

## src/join.ts  (tp 1, fp 0, fn 2, unscored 0)
  - join -> purry
  - joinImplementation -> join

## src/last.ts  (tp 1, fp 0, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at

## src/mapKeys.ts  (tp 1, fp 0, fn 2, unscored 1)
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 1, fp 0, fn 2, unscored 0)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper

## src/omitBy.ts  (tp 1, fp 0, fn 2, unscored 0)
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/purry.ts  (tp 2, fp 1, fn 1, unscored 0)
  - purry -> Error
  + purry -> args

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/rankBy.ts  (tp 1, fp 0, fn 2, unscored 0)
  - rankBy -> purryOrderRulesWithArgument
  - rankByImplementation -> compareFn

## src/reduce.ts  (tp 2, fp 0, fn 2, unscored 0)
  - reduceImplementation -> callbackfn
  - reduceImplementation -> reduce

## src/setPath.ts  (tp 1, fp 0, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation

## src/sortBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortBy -> sortByImplementation
  - sortByImplementation -> sort

## src/sortedIndex.ts  (tp 1, fp 0, fn 2, unscored 0)
  - sortedIndex -> purry
  - sortedIndexImplementation -> binarySearchCutoffIndex

## src/sortedIndexBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexByImplementation -> valueFunction

## src/sortedLastIndex.ts  (tp 1, fp 0, fn 2, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndexImplementation -> binarySearchCutoffIndex

## src/takeLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - takeLast -> purry
  - takeLastImplementation -> slice

## src/toUpperCase.ts  (tp 1, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/zip.ts  (tp 2, fp 0, fn 2, unscored 0)
  - zip -> purry
  - zipImplementation -> map

## src/add.ts  (tp 1, fp 0, fn 1, unscored 0)
  - add -> purry

## src/concat.ts  (tp 1, fp 0, fn 1, unscored 0)
  - concat -> purry

## src/defaultTo.ts  (tp 1, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/divide.ts  (tp 1, fp 0, fn 1, unscored 0)
  - divide -> purry

## src/findLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - findLastImplementation -> predicate

## src/hasAtLeast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/hasProp.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasProp -> purry

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 0)
  + isPlainObject -> typeof data !== "object" || data === null

## src/length.ts  (tp 1, fp 0, fn 1, unscored 0)
  - length -> purry

## src/merge.ts  (tp 1, fp 0, fn 1, unscored 0)
  - merge -> purry

## src/only.ts  (tp 1, fp 0, fn 1, unscored 0)
  - only -> purry

## src/pathOr.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pathOr -> purry

## src/pick.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pick -> purry

## src/pullObject.ts  (tp 4, fp 0, fn 1, unscored 0)
  - pullObject -> purry

## src/round.ts  (tp 2, fp 1, fn 0, unscored 0)
  + round -> round

## src/set.ts  (tp 1, fp 0, fn 1, unscored 0)
  - set -> purry

## src/sliceString.ts  (tp 1, fp 1, fn 0, unscored 0)
  + sliceString -> sliceString

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/split.ts  (tp 1, fp 1, fn 0, unscored 0)
  + pipe -> split

## src/sum.ts  (tp 2, fp 1, fn 0, unscored 0)
  + sum -> sum

## src/swapProps.ts  (tp 1, fp 0, fn 1, unscored 0)
  - swapProps -> purry

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

7 of 112 files exactly right.
