# qwen15b-calls / dev / cut=calls_only

raw 108/112 (96.4%)  ·  fence-stripped 108/112 (96.4%)  ·  schema 108/112 (96.4%)
P 48.3% [40.7% to 55.3%]   R 52.0% [41.2% to 60.6%]   F1 50.1% [42.7% to 56.6%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored, this cut excludes the class, so it counts against neither side

## src/internal/quickSelect.ts  (tp 0, fp 12, fn 5, unscored 1)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation
  + partition -> data
  + partition -> left
  + partition -> pivot
  + partition -> right
  + quickSelect -> partition
  + quickSelectImplementation -> data
  + quickSelectImplementation -> i
  + quickSelectImplementation -> j
  + quickSelectImplementation -> left
  + quickSelectImplementation -> pivotIndex
  + quickSelectImplementation -> right
  + quickSelectImplementation -> swapInPlace
  ~ quickSelectImplementation -> compareFn

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

## src/internal/purryOrderRules.ts  (tp 0, fp 5, fn 11, unscored 0)
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
  + isOrderRule -> primaryRule
  + isProjection -> maybeProjection
  + orderRuleComparer -> compareFn
  + purryOrderRules -> purry
  + purryOrderRulesWithArgument -> purry

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

## src/funnel.ts  (tp 0, fp 4, fn 7, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout
  + funnel -> call
  + funnel -> cancel
  + funnel -> flush
  + funnel -> isIdle

## src/internal/words.ts  (tp 2, fp 8, fn 3, unscored 0)
  - words -> push
  - words -> slice
  - words -> test
  + words -> /
  + words -> /
  + words -> WHITESPACE
  + words -> WORD_SEPARATORS
  + words -> character
  + words -> data
  + words -> results
  + words -> word

## src/groupByProp.ts  (tp 1, fp 9, fn 1, unscored 0)
  - groupByPropImplementation -> push
  + groupByPropImplementation -> Error
  + groupByPropImplementation -> filter
  + groupByPropImplementation -> format
  + groupByPropImplementation -> isFinite
  + groupByPropImplementation -> isNaN
  + groupByPropImplementation -> precisionOf
  + groupByPropImplementation -> reduce
  + groupByPropImplementation -> round
  + groupByPropImplementation -> sort

## src/internal/withPrecision.ts  (tp 1, fp 4, fn 6, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString
  + shiftDecimalPoint -> shift
  + shiftDecimalPoint -> value
  + withPrecision -> precision
  + withPrecision -> value

## src/sortedIndexWith.ts  (tp 1, fp 9, fn 0, unscored 0)
  + binarySearchCutoffIndex -> Error
  + binarySearchCutoffIndex -> filter
  + binarySearchCutoffIndex -> format
  + binarySearchCutoffIndex -> isFinite
  + binarySearchCutoffIndex -> isNaN
  + binarySearchCutoffIndex -> precisionOf
  + binarySearchCutoffIndex -> reduce
  + binarySearchCutoffIndex -> round
  + binarySearchCutoffIndex -> sort

## src/toTitleCase.ts  (tp 3, fp 4, fn 5, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> toUpperCase
  + toTitleCase -> test
  + toTitleCase -> toLowerCase
  + toTitleCase -> words
  + toTitleCaseImplementation -> preserveConsecutiveUppercase

## src/clone.ts  (tp 4, fp 1, fn 7, unscored 2)
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push
  + cloneImplementation -> typeof
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray

## src/sumBy.ts  (tp 4, fp 8, fn 0, unscored 0)
  + sumByImplementation -> array
  + sumByImplementation -> done
  + sumByImplementation -> firstEntry
  + sumByImplementation -> index
  + sumByImplementation -> item
  + sumByImplementation -> iter
  + sumByImplementation -> summand
  + sumByImplementation -> value

## src/swapIndices.ts  (tp 1, fp 6, fn 2, unscored 1)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  + swapIndicesImplementation -> data
  + swapIndicesImplementation -> index1
  + swapIndicesImplementation -> index2
  + swapIndicesImplementation -> positiveIndexA
  + swapIndicesImplementation -> positiveIndexB
  + swapIndicesImplementation -> result
  ~ swapIndices -> swapIndicesImplementation

## src/setPath.ts  (tp 0, fp 5, fn 2, unscored 1)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation
  + setPath -> purr
  + setPathImplementation -> assign
  + setPathImplementation -> copyWithin
  + setPathImplementation -> slice
  + setPathImplementation -> splice
  ~ setPathImplementation -> isArray

## src/toKebabCase.ts  (tp 0, fp 3, fn 4, unscored 0)
  - toKebabCase -> purry
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + toKebabCase -> join
  + toKebabCase -> toLowerCase
  + toKebabCase -> words

## src/dropFirstBy.ts  (tp 4, fp 4, fn 1, unscored 1)
  - dropFirstByImplementation -> push
  + dropFirstByImplementation -> item
  + dropFirstByImplementation -> n
  + dropFirstByImplementation -> previousHead
  + dropFirstByImplementation -> rest
  ~ dropFirstByImplementation -> compareFn

## src/fromKeys.ts  (tp 1, fp 3, fn 2, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> mapper
  + fromKeys -> purr
  + fromKeysImplementation -> map
  + fromKeysImplementation -> reduce

## src/groupBy.ts  (tp 3, fp 5, fn 0, unscored 1)
  + groupByImplementation -> data
  + groupByImplementation -> index
  + groupByImplementation -> item
  + groupByImplementation -> key
  + groupByImplementation -> output
  ~ groupByImplementation -> setPrototypeOf

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 5, fn 0, unscored 0)
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/intersection.ts  (tp 3, fp 3, fn 2, unscored 1)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  + intersection -> done
  + intersection -> next
  + lazyImplementation -> remaining
  ~ intersection -> lazyImplementation

## src/range.ts  (tp 1, fp 3, fn 2, unscored 0)
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + rangeImplementation -> abs
  + rangeImplementation -> ceil
  + rangeImplementation -> round

## src/when.ts  (tp 2, fp 2, fn 3, unscored 2)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  + whenImplementation -> data
  + whenImplementation -> extraArgs
  ~ __module__ -> when
  ~ __module__ -> whenImplementation

## src/filter.ts  (tp 1, fp 2, fn 2, unscored 0)
  - filter -> purry
  - lazyImplementation -> predicate
  + filter -> filter
  + lazyImplementation -> filter

## src/first.ts  (tp 1, fp 3, fn 1, unscored 0)
  - first -> toSingle
  + firstImplementation -> readonly
  + firstLazy -> next
  + lazyImplementation -> toSingle

## src/forEach.ts  (tp 0, fp 1, fn 3, unscored 1)
  - forEach -> purry
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn
  + forEach -> forEach
  ~ forEachImplementation -> callbackfn

## src/isEmpty.ts  (tp 0, fp 4, fn 0, unscored 0)
  + isEmpty -> IterableContainer
  + isEmpty -> Record
  + isEmpty -> string
  + isEmpty -> undefined

## src/pathOr.ts  (tp 0, fp 3, fn 1, unscored 0)
  - pathOr -> purry
  + pathOr -> defaultTo
  + pathOr -> pipe
  + pathOr -> prop

## src/purry.ts  (tp 1, fp 2, fn 2, unscored 0)
  - purry -> Error
  - purry -> fn
  + purry -> args
  + purry -> strictFunction

## src/set.ts  (tp 1, fp 4, fn 0, unscored 0)
  + setImplementation -> UpsertProp
  + setImplementation -> addProp
  + setImplementation -> pipe
  + setImplementation -> setPath

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/countBy.ts  (tp 4, fp 1, fn 2, unscored 0)
  - countByImplementation -> Map
  - countByImplementation -> entries
  + countByImplementation -> forEach

## src/debounce.ts  (tp 5, fp 0, fn 3, unscored 0)
  - debounce -> Error
  - debounce -> func
  - debounce -> toString

## src/dropLastWhile.ts  (tp 1, fp 1, fn 2, unscored 0)
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  + dropLastWhileImplementation -> for

## src/endsWith.ts  (tp 0, fp 1, fn 2, unscored 1)
  - endsWith -> purry
  - endsWithImplementation -> endsWith
  + endsWith -> endsWith
  ~ endsWith -> endsWithImplementation

## src/evolve.ts  (tp 0, fp 0, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/flatMap.ts  (tp 1, fp 1, fn 2, unscored 2)
  - flatMap -> purry
  - lazyImplementation -> callbackfn
  + flatMap -> callbackfn
  ~ flatMap -> flatMapImplementation
  ~ flatMapImplementation -> callbackfn

## src/fromEntries.ts  (tp 0, fp 2, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> fromEntries
  + fromEntries -> purr

## src/partialLastBind.ts  (tp 0, fp 2, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> parseInt
  + pipe -> stringify

## src/piped.ts  (tp 1, fp 3, fn 0, unscored 0)
  + piped -> add
  + piped -> map
  + piped -> prop

## src/product.ts  (tp 1, fp 3, fn 0, unscored 0)
  + productImplementation -> *
  + productImplementation -> of
  + productImplementation -> typeof

## src/prop.ts  (tp 1, fp 3, fn 0, unscored 0)
  + propImplementation -> data
  + propImplementation -> keys
  + propImplementation -> maybeData

## src/randomString.ts  (tp 2, fp 2, fn 1, unscored 2)
  - randomString -> purry
  + randomString -> ALPHABET
  + randomStringImplementation -> length
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/sample.ts  (tp 5, fp 1, fn 2, unscored 2)
  - sampleImplementation -> Set
  - sampleImplementation -> has
  + sampleImplementation -> slice
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> random

## src/sum.ts  (tp 1, fp 3, fn 0, unscored 0)
  + sumImplementation -> of
  + sumImplementation -> typeof
  + sumImplementation -> value

## src/takeLastWhile.ts  (tp 1, fp 1, fn 2, unscored 0)
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice
  + takeLastWhileImplementation -> for

## src/unique.ts  (tp 1, fp 0, fn 3, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> has
  - unique -> purryFromLazy
  ~ unique -> lazyImplementation

## src/uniqueBy.ts  (tp 2, fp 0, fn 3, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy
  ~ uniqueBy -> lazyImplementation

## src/zipWith.ts  (tp 3, fp 1, fn 2, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> zipWithImplementation
  + lazyDataLastImpl -> zipWithImplementation

## src/ceil.ts  (tp 1, fp 1, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil

## src/difference.ts  (tp 4, fp 2, fn 0, unscored 0)
  + difference -> SKIP_ITEM
  + lazyImplementation -> next

## src/dropWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

## src/findLast.ts  (tp 1, fp 1, fn 1, unscored 0)
  - findLastImplementation -> predicate
  + findLastImplementation -> findLast

## src/findLastIndex.ts  (tp 1, fp 1, fn 1, unscored 0)
  - findLastIndexImplementation -> predicate
  + findLastIndexImplementation -> findLastIndex

## src/floor.ts  (tp 1, fp 1, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor

## src/hasProp.ts  (tp 0, fp 1, fn 1, unscored 1)
  - hasProp -> purry
  + hasProp -> hasOwn
  ~ hasPropImplementation -> hasOwn

## src/internal/purryFromLazy.ts  (tp 1, fp 1, fn 1, unscored 2)
  - purryFromLazy -> Error
  + purryFromLazy -> lazyArgs
  ~ purryFromLazy -> dataLast
  ~ purryFromLazy -> lazy

## src/mapKeys.ts  (tp 1, fp 1, fn 1, unscored 0)
  - mapKeys -> purry
  + mapKeys -> entries

## src/meanBy.ts  (tp 3, fp 2, fn 0, unscored 0)
  + meanByImplementation -> length
  + meanByImplementation -> sum

## src/median.ts  (tp 2, fp 2, fn 0, unscored 0)
  + medianImplementation -> ceil
  + medianImplementation -> floor

## src/omit.ts  (tp 2, fp 2, fn 0, unscored 0)
  + omitImplementation -> data
  + omitImplementation -> keys

## src/partition.ts  (tp 2, fp 0, fn 2, unscored 0)
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/round.ts  (tp 1, fp 1, fn 1, unscored 0)
  - round -> purry
  + round -> round

## src/takeWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push

## src/add.ts  (tp 1, fp 1, fn 0, unscored 0)
  + addImplementation -> number

## src/capitalize.ts  (tp 3, fp 1, fn 0, unscored 0)
  + capitalizeImplementation -> charAt

## src/concat.ts  (tp 1, fp 1, fn 0, unscored 0)
  + concatImplementation -> concat

## src/defaultTo.ts  (tp 1, fp 1, fn 0, unscored 0)
  + defaultToImplementation -> ??

## src/differenceWith.ts  (tp 2, fp 0, fn 1, unscored 1)
  - differenceWith -> purryFromLazy
  ~ differenceWith -> lazyImplementation

## src/divide.ts  (tp 1, fp 1, fn 0, unscored 0)
  + divideImplementation -> number

## src/drop.ts  (tp 2, fp 1, fn 0, unscored 0)
  + lazyImplementation -> next

## src/hasAtLeast.ts  (tp 1, fp 1, fn 0, unscored 0)
  + hasAtLeastImplementation -> length

## src/indexBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - indexByImplementation -> mapper

## src/isIncludedIn.ts  (tp 2, fp 0, fn 1, unscored 0)
  - isIncludedIn -> Set

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 1)
  + isPlainObject -> typeof
  ~ isPlainObject -> getPrototypeOf

## src/keys.ts  (tp 1, fp 1, fn 0, unscored 0)
  + keys -> keys

## src/length.ts  (tp 1, fp 1, fn 0, unscored 0)
  + lengthImplementation -> length

## src/mapValues.ts  (tp 2, fp 1, fn 0, unscored 1)
  + mapValuesImplementation -> of
  ~ mapValuesImplementation -> entries

## src/merge.ts  (tp 1, fp 1, fn 0, unscored 0)
  + mergeImplementation -> spread

## src/objOf.ts  (tp 1, fp 1, fn 0, unscored 0)
  + objOfImplementation -> Record

## src/omitBy.ts  (tp 2, fp 1, fn 0, unscored 1)
  + omitByImplementation -> of
  ~ omitByImplementation -> entries

## src/only.ts  (tp 1, fp 1, fn 0, unscored 0)
  + onlyImplementation -> length

## src/pick.ts  (tp 1, fp 1, fn 0, unscored 0)
  + pickImplementation -> PickFromArray

## src/sort.ts  (tp 2, fp 1, fn 0, unscored 0)
  + sortImplementation -> slice

## src/sortBy.ts  (tp 1, fp 0, fn 1, unscored 1)
  - sortByImplementation -> sort
  ~ sortByImplementation -> compareFn

## src/sortedLastIndexBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedLastIndexByImplementation -> valueFunction

## src/splitWhen.ts  (tp 2, fp 0, fn 1, unscored 0)
  - splitWhenImplementation -> slice

## src/swapProps.ts  (tp 1, fp 1, fn 0, unscored 0)
  + swapPropsImplementation -> destructuring

## src/takeFirstBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - takeFirstByImplementation -> slice

## src/times.ts  (tp 2, fp 1, fn 0, unscored 2)
  + timesImplementation -> new Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

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

19 of 112 files exactly right.
