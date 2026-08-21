# ensemble-2of2 / dev / cut=calls_only

raw 105/112 (93.8%)  ·  fence-stripped 105/112 (93.8%)  ·  schema 105/112 (93.8%)
P 76.4% [67.9% to 83.0%]   R 41.1% [32.3% to 49.5%]   F1 53.4% [45.2% to 60.9%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/isDeepEqual.ts  (tp 0, fp 0, fn 17, unscored 0)
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

## src/pipe.ts  (tp 0, fp 0, fn 13, unscored 0)
  - pipe -> at
  - pipe -> func
  - pipe -> isIterable
  - pipe -> map
  - pipe -> prepareLazyFunction
  - pipe -> processItem
  - pipe -> push
  - prepareLazyFunction -> lazy
  - processItem -> entries
  - processItem -> lazyFn
  - processItem -> processItem
  - processItem -> push
  - processItem -> slice

## src/internal/purryOrderRules.ts  (tp 0, fp 0, fn 11, unscored 0)
  - isOrderRule -> isProjection
  - orderRuleComparer -> comparator
  - orderRuleComparer -> nextComparer
  - orderRuleComparer -> orderRuleComparer
  - orderRuleComparer -> projector
  - purryOrderRules -> func
  - purryOrderRules -> isOrderRule
  - purryOrderRules -> orderRuleComparer
  - purryOrderRulesWithArgument -> func
  - purryOrderRulesWithArgument -> isOrderRule
  - purryOrderRulesWithArgument -> purryOrderRules

## src/clone.ts  (tp 4, fp 0, fn 7, unscored 2)
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray

## src/funnel.ts  (tp 0, fp 0, fn 7, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout

## src/internal/quickSelect.ts  (tp 0, fp 2, fn 5, unscored 1)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation
  + quickSelect -> partition
  + quickSelectImplementation -> swapInPlace
  ~ quickSelectImplementation -> compareFn

## src/internal/withPrecision.ts  (tp 0, fp 0, fn 7, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> roundingFn
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString

## src/toTitleCase.ts  (tp 2, fp 1, fn 6, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> toUpperCase
  - toTitleCaseImplementation -> words
  + toTitleCase -> words

## src/debounce.ts  (tp 2, fp 0, fn 6, unscored 0)
  - debounce -> Error
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> toString

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 5, fn 0, unscored 0)
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/intersection.ts  (tp 0, fp 0, fn 5, unscored 1)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> set
  ~ intersection -> lazyImplementation

## src/range.ts  (tp 1, fp 3, fn 2, unscored 0)
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + rangeImplementation -> abs
  + rangeImplementation -> ceil
  + rangeImplementation -> round

## src/when.ts  (tp 0, fp 0, fn 5, unscored 0)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate

## src/difference.ts  (tp 1, fp 1, fn 3, unscored 0)
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> set
  + difference -> SKIP_ITEM

## src/internal/words.ts  (tp 1, fp 0, fn 4, unscored 0)
  - words -> has
  - words -> push
  - words -> slice
  - words -> test

## src/purry.ts  (tp 0, fp 1, fn 3, unscored 0)
  - purry -> Error
  - purry -> fn
  - purry -> lazyDataLastImpl
  + purry -> args

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/toKebabCase.ts  (tp 0, fp 0, fn 4, unscored 0)
  - toKebabCase -> purry
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words

## src/unique.ts  (tp 0, fp 0, fn 4, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy
  ~ unique -> lazyImplementation

## src/uniqueBy.ts  (tp 1, fp 0, fn 4, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy
  ~ uniqueBy -> lazyImplementation

## src/countBy.ts  (tp 3, fp 0, fn 3, unscored 0)
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries

## src/differenceWith.ts  (tp 0, fp 0, fn 3, unscored 1)
  - differenceWith -> purryFromLazy
  - lazyImplementation -> every
  - lazyImplementation -> isEqual
  ~ differenceWith -> lazyImplementation

## src/evolve.ts  (tp 0, fp 0, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/flatMap.ts  (tp 0, fp 0, fn 3, unscored 1)
  - flatMap -> purry
  - flatMapImplementation -> flatMap
  - lazyImplementation -> callbackfn
  ~ flatMap -> flatMapImplementation

## src/forEach.ts  (tp 0, fp 0, fn 3, unscored 1)
  - forEach -> purry
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn
  ~ forEachImplementation -> callbackfn

## src/groupBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/omit.ts  (tp 1, fp 2, fn 1, unscored 0)
  - omit -> purry
  + omitImplementation -> data
  + omitImplementation -> keys

## src/prop.ts  (tp 0, fp 2, fn 1, unscored 0)
  - prop -> propImplementation
  + propImplementation -> data
  + propImplementation -> keys

## src/sample.ts  (tp 4, fp 0, fn 3, unscored 0)
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> has

## src/sumBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/swapIndices.ts  (tp 0, fp 0, fn 3, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray

## src/takeLastWhile.ts  (tp 1, fp 1, fn 2, unscored 0)
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice
  + takeLastWhileImplementation -> for

## src/ceil.ts  (tp 1, fp 1, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil

## src/dropLastWhile.ts  (tp 1, fp 0, fn 2, unscored 0)
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice

## src/dropWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

## src/endsWith.ts  (tp 0, fp 0, fn 2, unscored 1)
  - endsWith -> purry
  - endsWithImplementation -> endsWith
  ~ endsWith -> endsWithImplementation

## src/filter.ts  (tp 1, fp 0, fn 2, unscored 0)
  - filter -> purry
  - lazyImplementation -> predicate

## src/first.ts  (tp 1, fp 1, fn 1, unscored 0)
  - first -> toSingle
  + firstLazy -> next

## src/floor.ts  (tp 1, fp 1, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor

## src/fromEntries.ts  (tp 0, fp 1, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> fromEntries

## src/fromKeys.ts  (tp 1, fp 0, fn 2, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> mapper

## src/groupByProp.ts  (tp 1, fp 1, fn 1, unscored 0)
  - groupByPropImplementation -> push
  + groupByPropImplementation -> filter

## src/internal/purryFromLazy.ts  (tp 1, fp 1, fn 1, unscored 1)
  - purryFromLazy -> Error
  + purryFromLazy -> lazyArgs
  ~ purryFromLazy -> dataLast

## src/keys.ts  (tp 0, fp 1, fn 1, unscored 0)
  - keys -> purry
  + keys -> keys

## src/mapValues.ts  (tp 1, fp 1, fn 1, unscored 1)
  - mapValuesImplementation -> valueMapper
  + mapValuesImplementation -> of
  ~ mapValuesImplementation -> entries

## src/meanBy.ts  (tp 3, fp 2, fn 0, unscored 0)
  + meanByImplementation -> length
  + meanByImplementation -> sum

## src/partition.ts  (tp 2, fp 0, fn 2, unscored 0)
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/randomString.ts  (tp 2, fp 1, fn 1, unscored 2)
  - randomString -> purry
  + randomStringImplementation -> length
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/round.ts  (tp 1, fp 1, fn 1, unscored 0)
  - round -> purry
  + round -> round

## src/setPath.ts  (tp 0, fp 0, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation

## src/sum.ts  (tp 1, fp 2, fn 0, unscored 0)
  + sumImplementation -> typeof
  + sumImplementation -> value

## src/takeWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push

## src/zipWith.ts  (tp 3, fp 0, fn 2, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> zipWithImplementation

## src/concat.ts  (tp 1, fp 1, fn 0, unscored 0)
  + concatImplementation -> concat

## src/defaultTo.ts  (tp 1, fp 1, fn 0, unscored 0)
  + defaultToImplementation -> ??

## src/dropFirstBy.ts  (tp 4, fp 0, fn 1, unscored 0)
  - dropFirstByImplementation -> push

## src/findLast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - findLastImplementation -> predicate

## src/findLastIndex.ts  (tp 1, fp 0, fn 1, unscored 0)
  - findLastIndexImplementation -> predicate

## src/hasAtLeast.ts  (tp 1, fp 1, fn 0, unscored 0)
  + hasAtLeastImplementation -> length

## src/hasProp.ts  (tp 0, fp 0, fn 1, unscored 1)
  - hasProp -> purry
  ~ hasPropImplementation -> hasOwn

## src/indexBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - indexByImplementation -> mapper

## src/isIncludedIn.ts  (tp 2, fp 0, fn 1, unscored 0)
  - isIncludedIn -> Set

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 1)
  + isPlainObject -> typeof
  ~ isPlainObject -> getPrototypeOf

## src/length.ts  (tp 1, fp 1, fn 0, unscored 0)
  + lengthImplementation -> length

## src/mapKeys.ts  (tp 1, fp 0, fn 1, unscored 0)
  - mapKeys -> purry

## src/only.ts  (tp 1, fp 1, fn 0, unscored 0)
  + onlyImplementation -> length

## src/partialLastBind.ts  (tp 0, fp 0, fn 1, unscored 0)
  - partialLastBind -> func

## src/pathOr.ts  (tp 0, fp 0, fn 1, unscored 0)
  - pathOr -> purry

## src/pick.ts  (tp 0, fp 0, fn 1, unscored 0)
  - pick -> purry

## src/piped.ts  (tp 1, fp 1, fn 0, unscored 0)
  + piped -> map

## src/product.ts  (tp 0, fp 0, fn 1, unscored 0)
  - product -> purry

## src/sortBy.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortByImplementation -> sort

## src/sortedLastIndexBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedLastIndexByImplementation -> valueFunction

## src/splitWhen.ts  (tp 2, fp 0, fn 1, unscored 0)
  - splitWhenImplementation -> slice

## src/takeFirstBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - takeFirstByImplementation -> slice

## src/times.ts  (tp 2, fp 1, fn 0, unscored 2)
  + timesImplementation -> new Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/toUpperCase.ts  (tp 1, fp 0, fn 1, unscored 0)
  - toUpperCaseImplementation -> toUpperCase

## src/uncapitalize.ts  (tp 2, fp 0, fn 1, unscored 0)
  - uncapitalizeImplementation -> slice

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

## src/zip.ts  (tp 2, fp 1, fn 0, unscored 0)
  + lazyImplementation -> next

## src/hasSubObject.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ hasSubObjectImplementation -> entries

## src/invert.ts  (tp 1, fp 0, fn 0, unscored 1)
  ~ invertImplementation -> entries

## src/omitBy.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ omitByImplementation -> entries

31 of 112 files exactly right.
