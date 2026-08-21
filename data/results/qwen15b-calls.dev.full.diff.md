# qwen15b-calls / dev / cut=full

raw 108/112 (96.4%)  ·  fence-stripped 108/112 (96.4%)  ·  schema 108/112 (96.4%)
P 50.3% [42.9% to 57.1%]   R 41.0% [33.5% to 46.5%]   F1 45.1% [39.1% to 50.4%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/internal/purryOrderRules.ts  (tp 0, fp 5, fn 13, unscored 0)
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
  + isOrderRule -> primaryRule
  + isProjection -> maybeProjection
  + orderRuleComparer -> compareFn
  + purryOrderRules -> purry
  + purryOrderRulesWithArgument -> purry

## src/internal/quickSelect.ts  (tp 1, fp 12, fn 6, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
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

## src/isDeepEqual.ts  (tp 0, fp 0, fn 18, unscored 0)
  - isDeepEqual -> isDeepEqualImplementation
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

## src/pipe.ts  (tp 0, fp 0, fn 17, unscored 0)
  - pipe -> at
  - pipe -> func
  - pipe -> isIterable
  - pipe -> lazyOp
  - pipe -> map
  - pipe -> op
  - pipe -> prepareLazyFunction
  - pipe -> processItem
  - pipe -> push
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  - prepareLazyFunction -> lazy
  - processItem -> entries
  - processItem -> lazyFn
  - processItem -> processItem
  - processItem -> push
  - processItem -> slice

## src/funnel.ts  (tp 0, fp 4, fn 8, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout
  - funnel -> voidReducer
  + funnel -> call
  + funnel -> cancel
  + funnel -> flush
  + funnel -> isIdle

## src/groupByProp.ts  (tp 1, fp 9, fn 2, unscored 0)
  - groupByProp -> groupByPropImplementation
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

## src/sortedIndexWith.ts  (tp 1, fp 9, fn 1, unscored 0)
  - sortedIndexWith -> binarySearchCutoffIndex
  + binarySearchCutoffIndex -> Error
  + binarySearchCutoffIndex -> filter
  + binarySearchCutoffIndex -> format
  + binarySearchCutoffIndex -> isFinite
  + binarySearchCutoffIndex -> isNaN
  + binarySearchCutoffIndex -> precisionOf
  + binarySearchCutoffIndex -> reduce
  + binarySearchCutoffIndex -> round
  + binarySearchCutoffIndex -> sort

## src/clone.ts  (tp 4, fp 1, fn 8, unscored 2)
  - clone -> cloneImplementation
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

## src/sumBy.ts  (tp 4, fp 8, fn 1, unscored 0)
  - sumBy -> sumByImplementation
  + sumByImplementation -> array
  + sumByImplementation -> done
  + sumByImplementation -> firstEntry
  + sumByImplementation -> index
  + sumByImplementation -> item
  + sumByImplementation -> iter
  + sumByImplementation -> summand
  + sumByImplementation -> value

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

## src/setPath.ts  (tp 0, fp 5, fn 3, unscored 1)
  - setPath -> purry
  - setPath -> setPathImplementation
  - setPathImplementation -> setPathImplementation
  + setPath -> purr
  + setPathImplementation -> assign
  + setPathImplementation -> copyWithin
  + setPathImplementation -> slice
  + setPathImplementation -> splice
  ~ setPathImplementation -> isArray

## src/swapIndices.ts  (tp 2, fp 6, fn 2, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  + swapIndicesImplementation -> data
  + swapIndicesImplementation -> index1
  + swapIndicesImplementation -> index2
  + swapIndicesImplementation -> positiveIndexA
  + swapIndicesImplementation -> positiveIndexB
  + swapIndicesImplementation -> result

## src/toKebabCase.ts  (tp 0, fp 3, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + toKebabCase -> join
  + toKebabCase -> toLowerCase
  + toKebabCase -> words

## src/filter.ts  (tp 1, fp 2, fn 5, unscored 0)
  - filter -> filterImplementation
  - filter -> lazyImplementation
  - filter -> purry
  - filterImplementation -> predicate
  - lazyImplementation -> predicate
  + filter -> filter
  + lazyImplementation -> filter

## src/first.ts  (tp 1, fp 3, fn 4, unscored 0)
  - first -> firstImplementation
  - first -> lazyImplementation
  - first -> toSingle
  - lazyImplementation -> firstLazy
  + firstImplementation -> readonly
  + firstLazy -> next
  + lazyImplementation -> toSingle

## src/dropFirstBy.ts  (tp 5, fp 4, fn 2, unscored 0)
  - dropFirstBy -> dropFirstByImplementation
  - dropFirstByImplementation -> push
  + dropFirstByImplementation -> item
  + dropFirstByImplementation -> n
  + dropFirstByImplementation -> previousHead
  + dropFirstByImplementation -> rest

## src/forEach.ts  (tp 1, fp 1, fn 5, unscored 0)
  - forEach -> forEachImplementation
  - forEach -> lazyImplementation
  - forEach -> purry
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn
  + forEach -> forEach

## src/fromKeys.ts  (tp 1, fp 3, fn 3, unscored 0)
  - fromKeys -> fromKeysImplementation
  - fromKeys -> purry
  - fromKeysImplementation -> mapper
  + fromKeys -> purr
  + fromKeysImplementation -> map
  + fromKeysImplementation -> reduce

## src/groupBy.ts  (tp 3, fp 5, fn 1, unscored 1)
  - groupBy -> groupByImplementation
  + groupByImplementation -> data
  + groupByImplementation -> index
  + groupByImplementation -> item
  + groupByImplementation -> key
  + groupByImplementation -> output
  ~ groupByImplementation -> setPrototypeOf

## src/intersection.ts  (tp 4, fp 3, fn 3, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> lazyEmptyEvaluator
  + intersection -> done
  + intersection -> next
  + lazyImplementation -> remaining

## src/range.ts  (tp 1, fp 3, fn 3, unscored 0)
  - range -> rangeImplementation
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + rangeImplementation -> abs
  + rangeImplementation -> ceil
  + rangeImplementation -> round

## src/zipWith.ts  (tp 3, fp 1, fn 5, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation
  - zipWith -> zipWithImplementation
  + lazyDataLastImpl -> zipWithImplementation

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 5, fn 0, unscored 0)
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/pathOr.ts  (tp 0, fp 3, fn 2, unscored 0)
  - pathOr -> pathOrImplementation
  - pathOr -> purry
  + pathOr -> defaultTo
  + pathOr -> pipe
  + pathOr -> prop

## src/set.ts  (tp 1, fp 4, fn 1, unscored 0)
  - set -> setImplementation
  + setImplementation -> UpsertProp
  + setImplementation -> addProp
  + setImplementation -> pipe
  + setImplementation -> setPath

## src/when.ts  (tp 2, fp 2, fn 3, unscored 2)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  + whenImplementation -> data
  + whenImplementation -> extraArgs
  ~ __module__ -> when
  ~ __module__ -> whenImplementation

## src/countBy.ts  (tp 4, fp 1, fn 3, unscored 0)
  - countBy -> countByImplementation
  - countByImplementation -> Map
  - countByImplementation -> entries
  + countByImplementation -> forEach

## src/difference.ts  (tp 4, fp 2, fn 2, unscored 0)
  - difference -> lazyImplementation
  - lazyImplementation -> lazyIdentityEvaluator
  + difference -> SKIP_ITEM
  + lazyImplementation -> next

## src/drop.ts  (tp 2, fp 1, fn 3, unscored 0)
  - drop -> dropImplementation
  - drop -> lazyImplementation
  - lazyImplementation -> lazyIdentityEvaluator
  + lazyImplementation -> next

## src/dropLastWhile.ts  (tp 1, fp 1, fn 3, unscored 0)
  - dropLastWhile -> dropLastWhileImplementation
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  + dropLastWhileImplementation -> for

## src/evolve.ts  (tp 0, fp 0, fn 4, unscored 0)
  - evolve -> evolveImplementation
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/flatMap.ts  (tp 3, fp 1, fn 3, unscored 0)
  - flatMap -> lazyImplementation
  - flatMap -> purry
  - lazyImplementation -> callbackfn
  + flatMap -> callbackfn

## src/isEmpty.ts  (tp 0, fp 4, fn 0, unscored 0)
  + isEmpty -> IterableContainer
  + isEmpty -> Record
  + isEmpty -> string
  + isEmpty -> undefined

## src/median.ts  (tp 2, fp 2, fn 2, unscored 0)
  - median -> medianImplementation
  - medianImplementation -> numberComparator
  + medianImplementation -> ceil
  + medianImplementation -> floor

## src/product.ts  (tp 1, fp 3, fn 1, unscored 0)
  - product -> productImplementation
  + productImplementation -> *
  + productImplementation -> of
  + productImplementation -> typeof

## src/purry.ts  (tp 1, fp 2, fn 2, unscored 0)
  - purry -> Error
  - purry -> fn
  + purry -> args
  + purry -> strictFunction

## src/randomString.ts  (tp 2, fp 2, fn 2, unscored 2)
  - randomString -> purry
  - randomString -> randomStringImplementation
  + randomString -> ALPHABET
  + randomStringImplementation -> length
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/sample.ts  (tp 5, fp 1, fn 3, unscored 2)
  - sample -> sampleImplementation
  - sampleImplementation -> Set
  - sampleImplementation -> has
  + sampleImplementation -> slice
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> random

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/sum.ts  (tp 1, fp 3, fn 1, unscored 0)
  - sum -> sumImplementation
  + sumImplementation -> of
  + sumImplementation -> typeof
  + sumImplementation -> value

## src/takeLastWhile.ts  (tp 1, fp 1, fn 3, unscored 0)
  - takeLastWhile -> takeLastWhileImplementation
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice
  + takeLastWhileImplementation -> for

## src/debounce.ts  (tp 5, fp 0, fn 3, unscored 0)
  - debounce -> Error
  - debounce -> func
  - debounce -> toString

## src/dropWhile.ts  (tp 2, fp 0, fn 3, unscored 0)
  - dropWhile -> dropWhileImplementation
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

## src/endsWith.ts  (tp 1, fp 1, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith
  + endsWith -> endsWith

## src/findLast.ts  (tp 1, fp 1, fn 2, unscored 0)
  - findLast -> findLastImplementation
  - findLastImplementation -> predicate
  + findLastImplementation -> findLast

## src/findLastIndex.ts  (tp 1, fp 1, fn 2, unscored 0)
  - findLastIndex -> findLastIndexImplementation
  - findLastIndexImplementation -> predicate
  + findLastIndexImplementation -> findLastIndex

## src/fromEntries.ts  (tp 0, fp 2, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> fromEntries
  + fromEntries -> purr

## src/hasProp.ts  (tp 0, fp 1, fn 2, unscored 1)
  - hasProp -> hasPropImplementation
  - hasProp -> purry
  + hasProp -> hasOwn
  ~ hasPropImplementation -> hasOwn

## src/map.ts  (tp 3, fp 0, fn 3, unscored 0)
  - map -> lazyImplementation
  - map -> mapImplementation
  - mapImplementation -> callbackfn

## src/mapKeys.ts  (tp 1, fp 1, fn 2, unscored 0)
  - mapKeys -> mapKeysImplementation
  - mapKeys -> purry
  + mapKeys -> entries

## src/meanBy.ts  (tp 3, fp 2, fn 1, unscored 0)
  - meanBy -> meanByImplementation
  + meanByImplementation -> length
  + meanByImplementation -> sum

## src/omit.ts  (tp 2, fp 2, fn 1, unscored 0)
  - omit -> omitImplementation
  + omitImplementation -> data
  + omitImplementation -> keys

## src/partialLastBind.ts  (tp 0, fp 2, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> parseInt
  + pipe -> stringify

## src/partition.ts  (tp 2, fp 0, fn 3, unscored 0)
  - partition -> partitionImplementation
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/piped.ts  (tp 1, fp 3, fn 0, unscored 0)
  + piped -> add
  + piped -> map
  + piped -> prop

## src/prop.ts  (tp 1, fp 3, fn 0, unscored 0)
  + propImplementation -> data
  + propImplementation -> keys
  + propImplementation -> maybeData

## src/sort.ts  (tp 2, fp 1, fn 2, unscored 0)
  - sort -> sortImplementation
  - sortImplementation -> cmp
  + sortImplementation -> slice

## src/splitWhen.ts  (tp 2, fp 0, fn 3, unscored 0)
  - splitWhen -> splitWhenImplementation
  - splitWhenImplementation -> predicate
  - splitWhenImplementation -> slice

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> lazyImplementation
  - take -> takeImplementation

## src/takeFirstBy.ts  (tp 3, fp 0, fn 3, unscored 0)
  - takeFirstBy -> takeFirstByImplementation
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> slice

## src/takeWhile.ts  (tp 2, fp 0, fn 3, unscored 0)
  - takeWhile -> takeWhileImplementation
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push

## src/unique.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> has
  - unique -> purryFromLazy

## src/uniqueBy.ts  (tp 3, fp 0, fn 3, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy

## src/zip.ts  (tp 2, fp 1, fn 2, unscored 0)
  - zip -> lazyImplementation
  - zip -> zipImplementation
  + lazyImplementation -> next

## src/add.ts  (tp 1, fp 1, fn 1, unscored 0)
  - add -> addImplementation
  + addImplementation -> number

## src/capitalize.ts  (tp 3, fp 1, fn 1, unscored 0)
  - capitalize -> capitalizeImplementation
  + capitalizeImplementation -> charAt

## src/ceil.ts  (tp 1, fp 1, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil

## src/concat.ts  (tp 1, fp 1, fn 1, unscored 0)
  - concat -> concatImplementation
  + concatImplementation -> concat

## src/defaultTo.ts  (tp 1, fp 1, fn 1, unscored 0)
  - defaultTo -> defaultToImplementation
  + defaultToImplementation -> ??

## src/divide.ts  (tp 1, fp 1, fn 1, unscored 0)
  - divide -> divideImplementation
  + divideImplementation -> number

## src/findIndex.ts  (tp 2, fp 0, fn 2, unscored 0)
  - findIndex -> findIndexImplementation
  - findIndexImplementation -> predicate

## src/floor.ts  (tp 1, fp 1, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor

## src/hasAtLeast.ts  (tp 1, fp 1, fn 1, unscored 0)
  - hasAtLeast -> hasAtLeastImplementation
  + hasAtLeastImplementation -> length

## src/indexBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - indexBy -> indexByImplementation
  - indexByImplementation -> mapper

## src/internal/purryFromLazy.ts  (tp 3, fp 1, fn 1, unscored 0)
  - purryFromLazy -> Error
  + purryFromLazy -> lazyArgs

## src/length.ts  (tp 1, fp 1, fn 1, unscored 0)
  - length -> lengthImplementation
  + lengthImplementation -> length

## src/mapValues.ts  (tp 2, fp 1, fn 1, unscored 1)
  - mapValues -> mapValuesImplementation
  + mapValuesImplementation -> of
  ~ mapValuesImplementation -> entries

## src/merge.ts  (tp 1, fp 1, fn 1, unscored 0)
  - merge -> mergeImplementation
  + mergeImplementation -> spread

## src/nthBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - nthBy -> nthByImplementation
  - nthByImplementation -> compareFn

## src/objOf.ts  (tp 1, fp 1, fn 1, unscored 0)
  - objOf -> objOfImplementation
  + objOfImplementation -> Record

## src/omitBy.ts  (tp 2, fp 1, fn 1, unscored 1)
  - omitBy -> omitByImplementation
  + omitByImplementation -> of
  ~ omitByImplementation -> entries

## src/only.ts  (tp 1, fp 1, fn 1, unscored 0)
  - only -> onlyImplementation
  + onlyImplementation -> length

## src/pick.ts  (tp 1, fp 1, fn 1, unscored 0)
  - pick -> pickImplementation
  + pickImplementation -> PickFromArray

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/reduce.ts  (tp 2, fp 0, fn 2, unscored 0)
  - reduce -> reduceImplementation
  - reduceImplementation -> callbackfn

## src/round.ts  (tp 1, fp 1, fn 1, unscored 0)
  - round -> purry
  + round -> round

## src/sortBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortBy -> sortByImplementation
  - sortByImplementation -> sort

## src/sortedLastIndexBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortedLastIndexBy -> sortedLastIndexByImplementation
  - sortedLastIndexByImplementation -> valueFunction

## src/swapProps.ts  (tp 1, fp 1, fn 1, unscored 0)
  - swapProps -> swapPropsImplementation
  + swapPropsImplementation -> destructuring

## src/times.ts  (tp 2, fp 1, fn 1, unscored 2)
  - times -> timesImplementation
  + timesImplementation -> new Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/uncapitalize.ts  (tp 2, fp 0, fn 2, unscored 0)
  - uncapitalize -> uncapitalizeImplementation
  - uncapitalizeImplementation -> slice

## src/differenceWith.ts  (tp 3, fp 0, fn 1, unscored 0)
  - differenceWith -> purryFromLazy

## src/dropLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - dropLast -> dropLastImplementation

## src/hasSubObject.ts  (tp 2, fp 0, fn 1, unscored 1)
  - hasSubObject -> hasSubObjectImplementation
  ~ hasSubObjectImplementation -> entries

## src/invert.ts  (tp 1, fp 0, fn 1, unscored 1)
  - invert -> invertImplementation
  ~ invertImplementation -> entries

## src/isIncludedIn.ts  (tp 2, fp 0, fn 1, unscored 0)
  - isIncludedIn -> Set

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 1)
  + isPlainObject -> typeof
  ~ isPlainObject -> getPrototypeOf

## src/join.ts  (tp 2, fp 0, fn 1, unscored 0)
  - join -> joinImplementation

## src/keys.ts  (tp 1, fp 1, fn 0, unscored 0)
  + keys -> keys

## src/last.ts  (tp 2, fp 0, fn 1, unscored 0)
  - last -> lastImplementation

## src/pullObject.ts  (tp 4, fp 0, fn 1, unscored 0)
  - pullObject -> pullObjectImplementation

## src/rankBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - rankBy -> rankByImplementation

## src/sortedIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedIndex -> sortedIndexImplementation

## src/sortedIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedIndexBy -> sortedIndexByImplementation

## src/sortedLastIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedLastIndex -> sortedLastIndexImplementation

## src/takeLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - takeLast -> takeLastImplementation

## src/toUpperCase.ts  (tp 2, fp 0, fn 1, unscored 0)
  - toUpperCase -> toUpperCaseImplementation

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

2 of 112 files exactly right.
