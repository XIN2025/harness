# qwen15b-refs / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 57.4% [50.3% to 64.4%]   R 31.5% [26.5% to 36.1%]   F1 40.7% [35.2% to 45.5%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/isDeepEqual.ts  (tp 1, fp 4, fn 17, unscored 0)
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
  + isDeepEqual -> isComparablePrototype
  + isDeepEqual -> isDeepEqualArrays
  + isDeepEqual -> isDeepEqualMaps
  + isDeepEqual -> isDeepEqualSets

## src/internal/purryOrderRules.ts  (tp 0, fp 3, fn 13, unscored 0)
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
  + sortBy -> sortByImplementation
  + sortByImplementation -> defaultCompare
  + sortByImplementation -> identity

## src/pipe.ts  (tp 2, fp 1, fn 15, unscored 0)
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
  + pipe -> next

## src/clone.ts  (tp 0, fp 2, fn 12, unscored 0)
  - clone -> cloneImplementation
  - clone -> purry
  - cloneImplementation -> deepCloneArray
  - cloneImplementation -> deepCloneObject
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - cloneImplementation -> structuredClone
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push
  + clone -> deepCloneArray
  + clone -> deepCloneObject

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

## src/internal/words.ts  (tp 1, fp 6, fn 4, unscored 0)
  - words -> has
  - words -> push
  - words -> slice
  - words -> test
  + words -> WHITESPACE
  + words -> WORD_SEPARATORS
  + words -> character
  + words -> data
  + words -> word
  + words -> words

## src/debounce.ts  (tp 3, fp 4, fn 5, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> setTimeout
  - debounce -> toString
  + debounce -> coolDownTimeoutId
  + debounce -> latestCallArgs
  + debounce -> maxWaitTimeoutId
  + debounce -> result

## src/internal/quickSelect.ts  (tp 1, fp 3, fn 6, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation
  + quickSelect -> partition
  + quickSelectImplementation -> pivotIndex
  + quickSelectImplementation -> swapInPlace

## src/intersection.ts  (tp 1, fp 3, fn 6, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set
  + lazyImplementation -> other
  + lazyImplementation -> remaining
  + lazyImplementation -> value

## src/internal/withPrecision.ts  (tp 1, fp 2, fn 6, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString
  + withPrecision -> precision
  + withPrecision -> value

## src/difference.ts  (tp 1, fp 2, fn 5, unscored 0)
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set
  + lazyImplementation -> copies
  + lazyImplementation -> remaining

## src/sample.ts  (tp 1, fp 0, fn 7, unscored 0)
  - sample -> purry
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort

## src/toKebabCase.ts  (tp 0, fp 2, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + toKebabCase -> join
  + toKebabCase -> words

## src/setPath.ts  (tp 1, fp 4, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation
  + setPathImplementation -> copy
  + setPathImplementation -> currentValue
  + setPathImplementation -> data
  + setPathImplementation -> remaining

## src/zipWith.ts  (tp 2, fp 0, fn 6, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/countBy.ts  (tp 2, fp 0, fn 5, unscored 0)
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set

## src/evolve.ts  (tp 3, fp 4, fn 1, unscored 0)
  - evolve -> purry
  + evolveImplementation -> data
  + evolveImplementation -> evolver
  + evolveImplementation -> out
  + evolveImplementation -> typeof value === 'function

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 0)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy

## src/nthBy.ts  (tp 0, fp 1, fn 4, unscored 0)
  - nthBy -> nthByImplementation
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> compareFn
  - nthByImplementation -> quickSelect
  + nthBy -> quickSelect

## src/sort.ts  (tp 1, fp 2, fn 3, unscored 0)
  - sort -> purry
  - sortImplementation -> cmp
  - sortImplementation -> sort
  + sortImplementation -> defaultCompare
  + sortImplementation -> identity

## src/sortedIndexBy.ts  (tp 0, fp 1, fn 4, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexBy -> sortedIndexByImplementation
  - sortedIndexByImplementation -> binarySearchCutoffIndex
  - sortedIndexByImplementation -> valueFunction
  + sortedIndexBy -> binarySearchCutoffIndex

## src/sortedLastIndexBy.ts  (tp 0, fp 1, fn 4, unscored 0)
  - sortedLastIndexBy -> purry
  - sortedLastIndexBy -> sortedLastIndexByImplementation
  - sortedLastIndexByImplementation -> binarySearchCutoffIndex
  - sortedLastIndexByImplementation -> valueFunction
  + sortedLastIndexBy -> binarySearchCutoffIndex

## src/stringToPath.ts  (tp 0, fp 1, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test
  + stringToPath -> stringToPathImpl

## src/takeFirstBy.ts  (tp 2, fp 1, fn 4, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  + takeFirstByImplementation -> n

## src/capitalize.ts  (tp 1, fp 1, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase
  + capitalizeImplementation -> data

## src/differenceWith.ts  (tp 1, fp 1, fn 3, unscored 0)
  - differenceWith -> purryFromLazy
  - lazyImplementation -> every
  - lazyImplementation -> isEqual
  + differenceWith -> isEqual

## src/dropFirstBy.ts  (tp 3, fp 0, fn 4, unscored 0)
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice

## src/filter.ts  (tp 2, fp 0, fn 4, unscored 0)
  - filter -> purry
  - filterImplementation -> filter
  - filterImplementation -> predicate
  - lazyImplementation -> predicate

## src/findIndex.ts  (tp 1, fp 1, fn 3, unscored 0)
  - findIndex -> purry
  - findIndexImplementation -> findIndex
  - findIndexImplementation -> predicate
  + findIndex -> predicate

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

## src/map.ts  (tp 2, fp 0, fn 4, unscored 0)
  - lazyImplementation -> callbackfn
  - map -> purry
  - mapImplementation -> callbackfn
  - mapImplementation -> map

## src/meanBy.ts  (tp 1, fp 1, fn 3, unscored 0)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn
  + meanBy -> fn

## src/partition.ts  (tp 2, fp 1, fn 3, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> push
  + partitionImplementation -> data

## src/purry.ts  (tp 1, fp 2, fn 2, unscored 0)
  - purry -> Error
  - purry -> lazyDataLastImpl
  + purry -> args
  + purry -> lazy

## src/sortBy.ts  (tp 1, fp 1, fn 3, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> compareFn
  - sortByImplementation -> sort
  + sortBy -> defaultCompare

## src/sortedIndex.ts  (tp 0, fp 1, fn 3, unscored 0)
  - sortedIndex -> purry
  - sortedIndex -> sortedIndexImplementation
  - sortedIndexImplementation -> binarySearchCutoffIndex
  + sortedIndex -> binarySearchCutoffIndex

## src/toTitleCase.ts  (tp 5, fp 1, fn 3, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> toUpperCase
  + toTitleCaseImplementation -> word

## src/unique.ts  (tp 1, fp 0, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy

## src/uniqueBy.ts  (tp 2, fp 0, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy

## src/when.ts  (tp 1, fp 0, fn 4, unscored 0)
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate

## src/zip.ts  (tp 1, fp 1, fn 3, unscored 0)
  - zip -> lazyImplementation
  - zip -> purry
  - zipImplementation -> map
  + zipImplementation -> lazyImplementation

## src/drop.ts  (tp 2, fp 0, fn 3, unscored 0)
  - drop -> purry
  - dropImplementation -> slice
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropWhile.ts  (tp 2, fp 0, fn 3, unscored 0)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> slice

## src/endsWith.ts  (tp 1, fp 1, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith
  + endsWithImplementation -> suffix

## src/first.ts  (tp 2, fp 0, fn 3, unscored 0)
  - first -> purry
  - first -> toSingle
  - lazyImplementation -> firstLazy

## src/fromKeys.ts  (tp 1, fp 0, fn 3, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper

## src/groupBy.ts  (tp 2, fp 1, fn 2, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> push
  + groupByImplementation -> data

## src/hasAtLeast.ts  (tp 1, fp 2, fn 1, unscored 0)
  - hasAtLeast -> purry
  + hasAtLeastImplementation -> data
  + hasAtLeastImplementation -> minimum

## src/internal/purryFromLazy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - purryFromLazy -> Error
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy

## src/join.ts  (tp 1, fp 1, fn 2, unscored 0)
  - join -> purry
  - joinImplementation -> join
  + joinImplementation -> glue

## src/last.ts  (tp 1, fp 1, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at
  + lastImplementation -> array

## src/merge.ts  (tp 1, fp 2, fn 1, unscored 0)
  - merge -> purry
  + mergeImplementation -> data
  + mergeImplementation -> source

## src/objOf.ts  (tp 1, fp 2, fn 1, unscored 0)
  - objOf -> purry
  + objOfImplementation -> key
  + objOfImplementation -> value

## src/only.ts  (tp 1, fp 2, fn 1, unscored 0)
  - only -> purry
  + onlyImplementation -> defaultCompare
  + onlyImplementation -> identity

## src/partialLastBind.ts  (tp 0, fp 2, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> stringify
  + pipe -> stringify

## src/pathOr.ts  (tp 1, fp 2, fn 1, unscored 0)
  - pathOr -> purry
  + pathOr -> defaultTo
  + pathOr -> prop

## src/pick.ts  (tp 1, fp 2, fn 1, unscored 0)
  - pick -> purry
  + pickImplementation -> keys
  + pickImplementation -> object

## src/product.ts  (tp 1, fp 2, fn 1, unscored 0)
  - product -> purry
  + productImplementation -> data
  + productImplementation -> value

## src/randomString.ts  (tp 1, fp 0, fn 3, unscored 0)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push

## src/range.ts  (tp 1, fp 0, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap

## src/rankBy.ts  (tp 1, fp 1, fn 2, unscored 0)
  - rankBy -> purryOrderRulesWithArgument
  - rankByImplementation -> compareFn
  + rankBy -> compareFn

## src/sortedIndexWith.ts  (tp 1, fp 2, fn 1, unscored 0)
  - sortedIndexWith -> purry
  + sortedIndexWith -> defaultCompare
  + sortedIndexWith -> identity

## src/sortedLastIndex.ts  (tp 1, fp 1, fn 2, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndex -> sortedLastIndexImplementation
  + sortedLastIndex -> binarySearchCutoffIndex

## src/splitWhen.ts  (tp 2, fp 0, fn 3, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> slice

## src/sum.ts  (tp 1, fp 2, fn 1, unscored 0)
  - sum -> purry
  + sumImplementation -> data
  + sumImplementation -> value

## src/sumBy.ts  (tp 2, fp 0, fn 3, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> purry
  - takeImplementation -> slice

## src/takeWhile.ts  (tp 2, fp 0, fn 3, unscored 0)
  - takeWhile -> purry
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> push

## src/toUpperCase.ts  (tp 1, fp 1, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase
  + toUpperCaseImplementation -> data

## src/uncapitalize.ts  (tp 1, fp 0, fn 3, unscored 0)
  - uncapitalize -> purry
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase

## src/ceil.ts  (tp 1, fp 1, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil

## src/concat.ts  (tp 1, fp 1, fn 1, unscored 0)
  - concat -> purry
  + concatImplementation -> concat

## src/dropLastWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> slice

## src/floor.ts  (tp 1, fp 1, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor

## src/groupByProp.ts  (tp 1, fp 0, fn 2, unscored 0)
  - groupByProp -> purry
  - groupByPropImplementation -> push

## src/hasProp.ts  (tp 1, fp 1, fn 1, unscored 0)
  - hasProp -> purry
  + hasProp -> hasOwn

## src/indexBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries

## src/invert.ts  (tp 1, fp 1, fn 1, unscored 1)
  - invert -> purry
  + invertImplementation -> result
  ~ invertImplementation -> entries

## src/isIncludedIn.ts  (tp 1, fp 0, fn 2, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has

## src/keys.ts  (tp 0, fp 1, fn 1, unscored 0)
  - keys -> purry
  + keys -> keys

## src/median.ts  (tp 2, fp 0, fn 2, unscored 0)
  - median -> purry
  - medianImplementation -> sort

## src/omit.ts  (tp 1, fp 0, fn 2, unscored 0)
  - omit -> purry
  - omitImplementation -> hasAtLeast

## src/pullObject.ts  (tp 3, fp 0, fn 2, unscored 0)
  - pullObject -> purry
  - pullObjectImplementation -> entries

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/reduce.ts  (tp 2, fp 0, fn 2, unscored 0)
  - reduce -> purry
  - reduceImplementation -> reduce

## src/round.ts  (tp 1, fp 1, fn 1, unscored 0)
  - round -> purry
  + round -> round

## src/swapIndices.ts  (tp 2, fp 0, fn 2, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join

## src/swapProps.ts  (tp 1, fp 1, fn 1, unscored 0)
  - swapProps -> purry
  + swapPropsImplementation -> obj

## src/takeLast.ts  (tp 2, fp 1, fn 1, unscored 1)
  - takeLast -> purry
  + takeLastImplementation -> n
  ~ takeLastImplementation -> max

## src/takeLastWhile.ts  (tp 2, fp 0, fn 2, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> slice

## src/add.ts  (tp 1, fp 0, fn 1, unscored 0)
  - add -> purry

## src/defaultTo.ts  (tp 1, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/divide.ts  (tp 1, fp 0, fn 1, unscored 0)
  - divide -> purry

## src/dropLast.ts  (tp 2, fp 0, fn 1, unscored 1)
  - dropLast -> purry
  ~ dropLastImplementation -> max

## src/findLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - findLast -> purry

## src/findLastIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - findLastIndex -> purry

## src/fromEntries.ts  (tp 1, fp 1, fn 0, unscored 0)
  + fromEntries -> fromEntries

## src/hasSubObject.ts  (tp 2, fp 0, fn 1, unscored 0)
  - hasSubObject -> purry

## src/length.ts  (tp 1, fp 0, fn 1, unscored 0)
  - length -> purry

## src/mapKeys.ts  (tp 2, fp 0, fn 1, unscored 0)
  - mapKeys -> purry

## src/mapValues.ts  (tp 2, fp 0, fn 1, unscored 0)
  - mapValues -> purry

## src/omitBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - omitBy -> purry

## src/piped.ts  (tp 1, fp 1, fn 0, unscored 0)
  + pipe -> identity

## src/set.ts  (tp 1, fp 0, fn 1, unscored 0)
  - set -> purry

## src/times.ts  (tp 2, fp 0, fn 1, unscored 0)
  - times -> purry

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

## src/isPlainObject.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ isPlainObject -> getPrototypeOf

5 of 112 files exactly right.
