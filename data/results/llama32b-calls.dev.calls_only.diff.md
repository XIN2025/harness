# llama32b-calls / dev / cut=calls_only

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 109/112 (97.3%)
P 36.7% [31.4% to 41.8%]   R 63.1% [53.8% to 71.1%]   F1 46.4% [41.0% to 51.4%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/intersection.ts  (tp 1, fp 14, fn 4, unscored 1)
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> set
  + intersection -> Map
  + intersection -> __module__
  + intersection -> copies === 0
  + intersection -> copies === undefined
  + intersection -> delete
  + intersection -> for
  + intersection -> get
  + intersection -> if copies === 1
  + intersection -> length
  + intersection -> return SKIP_ITEM
  + intersection -> set
  + intersection -> size === 0
  + intersection -> value as S & T
  + intersection -> value of
  ~ intersection -> lazyImplementation

## src/isDeepEqual.ts  (tp 5, fp 4, fn 12, unscored 2)
  - isDeepEqualArrays -> isDeepEqualImplementation
  - isDeepEqualImplementation -> isComparablePrototype
  - isDeepEqualImplementation -> isDeepEqualArrays
  - isDeepEqualImplementation -> isDeepEqualImplementation
  - isDeepEqualImplementation -> isDeepEqualMaps
  - isDeepEqualImplementation -> isDeepEqualSets
  - isDeepEqualImplementation -> toString
  - isDeepEqualMaps -> entries
  - isDeepEqualMaps -> has
  - isDeepEqualMaps -> isDeepEqualImplementation
  - isDeepEqualSets -> entries
  - isDeepEqualSets -> isDeepEqualImplementation
  + isDeepEqualImplementation -> get
  + isDeepEqualImplementation -> getPrototypeOf
  + isDeepEqualImplementation -> has
  + isDeepEqualSets -> includes
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries

## src/difference.ts  (tp 1, fp 12, fn 3, unscored 1)
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> set
  + difference -> Map
  + difference -> SKIP_ITEM
  + difference -> copies
  + difference -> else if
  + difference -> for
  + difference -> get
  + difference -> if
  + difference -> lazyIdentityEvaluator
  + difference -> length
  + difference -> return
  + difference -> set
  + difference -> value of
  ~ difference -> lazyImplementation

## src/when.ts  (tp 0, fp 10, fn 5, unscored 0)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate
  + when -> __module__
  + whenImplementation -> Error
  + whenImplementation -> filter
  + whenImplementation -> format
  + whenImplementation -> isFinite
  + whenImplementation -> isNaN
  + whenImplementation -> precisionOf
  + whenImplementation -> reduce
  + whenImplementation -> round
  + whenImplementation -> sort

## src/omit.ts  (tp 1, fp 12, fn 1, unscored 0)
  - omit -> purry
  + omit -> __module__
  + omitImplementation -> Error
  + omitImplementation -> data
  + omitImplementation -> filter
  + omitImplementation -> format
  + omitImplementation -> isFinite
  + omitImplementation -> isNaN
  + omitImplementation -> keys
  + omitImplementation -> precisionOf
  + omitImplementation -> reduce
  + omitImplementation -> round
  + omitImplementation -> sort

## src/sumBy.ts  (tp 1, fp 10, fn 3, unscored 0)
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next
  + sumBy -> __module__
  + sumImplementation -> array
  + sumImplementation -> callbackfn
  + sumImplementation -> entries
  + sumImplementation -> firstValue
  + sumImplementation -> index
  + sumImplementation -> item
  + sumImplementation -> next
  + sumImplementation -> summand
  + sumImplementation -> value

## src/setPath.ts  (tp 0, fp 10, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation
  + setPath -> __module__
  + setPathImplementation -> Error
  + setPathImplementation -> filter
  + setPathImplementation -> format
  + setPathImplementation -> isFinite
  + setPathImplementation -> isNaN
  + setPathImplementation -> precisionOf
  + setPathImplementation -> reduce
  + setPathImplementation -> round
  + setPathImplementation -> sort

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

## src/partialLastBind.ts  (tp 0, fp 10, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> Parameters
  + partialLastBind -> PartialLastBindError
  + partialLastBind -> RemedaTypeError
  + partialLastBind -> RemoveSuffix
  + partialLastBind -> ReturnType
  + partialLastBind -> StrictFunction
  + partialLastBind -> TupleSplits
  + partialLastBind -> TupleSuffix
  + partialLastBind -> pipe
  + partialLastBind -> stringify

## src/pipe.ts  (tp 3, fp 0, fn 10, unscored 0)
  - pipe -> at
  - pipe -> func
  - pipe -> map
  - pipe -> push
  - prepareLazyFunction -> lazy
  - processItem -> entries
  - processItem -> lazyFn
  - processItem -> processItem
  - processItem -> push
  - processItem -> slice

## src/swapIndices.ts  (tp 2, fp 9, fn 1, unscored 1)
  - swapIndicesImplementation -> swapArray
  + swapArray -> NaN
  + swapArray -> concat
  + swapArray -> includes
  + swapArray -> indexOf
  + swapArray -> length
  + swapArray -> pop
  + swapArray -> push
  + swapArray -> slice
  + swapArray -> toString
  ~ swapArray -> isNaN

## src/clone.ts  (tp 4, fp 2, fn 7, unscored 3)
  - cloneImplementation -> indexOf
  - cloneImplementation -> push
  - deepCloneArray -> cloneImplementation
  - deepCloneArray -> entries
  - deepCloneArray -> push
  - deepCloneObject -> cloneImplementation
  - deepCloneObject -> push
  + cloneImplementation -> entries
  + cloneImplementation -> isPlainObject
  ~ clone -> cloneImplementation
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray

## src/evolve.ts  (tp 3, fp 9, fn 0, unscored 1)
  + evolve -> __module__
  + evolveImplementation -> assign
  + evolveImplementation -> data
  + evolveImplementation -> for
  + evolveImplementation -> function
  + evolveImplementation -> in
  + evolveImplementation -> key
  + evolveImplementation -> out
  + evolveImplementation -> typeof
  ~ evolveImplementation -> entries

## src/median.ts  (tp 2, fp 9, fn 0, unscored 1)
  + medianImplementation -> filter
  + medianImplementation -> format
  + medianImplementation -> isFinite
  + medianImplementation -> isNaN
  + medianImplementation -> reduce
  + medianImplementation -> round
  + medianImplementation -> slice
  + numberComparator -> sort
  + precisionOf -> sort
  ~ median -> medianImplementation

## src/internal/withPrecision.ts  (tp 3, fp 4, fn 4, unscored 1)
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> roundingFn
  - withPrecision -> shiftDecimalPoint
  + shiftDecimalPoint -> e
  + withPrecision -> e
  + withPrecision -> parseInt
  + withPrecision -> split
  ~ shiftDecimalPoint -> parseFloat

## src/range.ts  (tp 2, fp 7, fn 1, unscored 2)
  - rangeImplementation -> RangeError
  + rangeImplementation -> 
  + rangeImplementation -> SNAP_TOLERANCE
  + rangeImplementation -> abs
  + rangeImplementation -> ceil
  + rangeImplementation -> raw
  + rangeImplementation -> raw - rounded
  + rangeImplementation -> round
  ~ range -> rangeImplementation
  ~ rangeImplementation -> from

## src/reduce.ts  (tp 2, fp 8, fn 0, unscored 1)
  + reduceImplementation -> Error
  + reduceImplementation -> filter
  + reduceImplementation -> format
  + reduceImplementation -> isFinite
  + reduceImplementation -> isNaN
  + reduceImplementation -> precisionOf
  + reduceImplementation -> round
  + reduceImplementation -> sort
  ~ reduce -> reduceImplementation

## src/debounce.ts  (tp 2, fp 1, fn 6, unscored 0)
  - debounce -> Error
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> toString
  + debounce -> __module__

## src/meanBy.ts  (tp 3, fp 7, fn 0, unscored 0)
  + meanByImplementation -> array
  + meanByImplementation -> for
  + meanByImplementation -> index
  + meanByImplementation -> item
  + meanByImplementation -> length
  + meanByImplementation -> return
  + meanByImplementation -> sum

## src/prop.ts  (tp 0, fp 6, fn 1, unscored 0)
  - prop -> propImplementation
  + prop -> implementation
  + propImplementation -> data
  + propImplementation -> key
  + propImplementation -> keys
  + propImplementation -> output
  + propImplementation -> undefined

## src/sample.ts  (tp 5, fp 5, fn 2, unscored 0)
  - sampleImplementation -> Set
  - sampleImplementation -> add
  + sampleImplementation -> format
  + sampleImplementation -> isNaN
  + sampleImplementation -> precisionOf
  + sampleImplementation -> reduce
  + sampleImplementation -> round

## src/zipWith.ts  (tp 3, fp 5, fn 2, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> zipWithImplementation
  + lazyDataLastImpl -> done
  + lazyDataLastImpl -> hasNext
  + lazyDataLastImpl -> next
  + zipWithImplementation -> datum
  + zipWithImplementation -> index

## src/fromKeys.ts  (tp 3, fp 6, fn 0, unscored 0)
  + fromKeysImplementation -> Partial
  + fromKeysImplementation -> data
  + fromKeysImplementation -> for
  + fromKeysImplementation -> index
  + fromKeysImplementation -> key
  + fromKeysImplementation -> result

## src/funnel.ts  (tp 5, fp 4, fn 2, unscored 1)
  - funnel -> callback
  - funnel -> reducer
  + funnel -> format
  + funnel -> isNaN
  + funnel -> reduce
  + funnel -> round
  ~ funnel -> voidReducer

## src/internal/binarySearchCutoffIndex.ts  (tp 1, fp 6, fn 0, unscored 0)
  + binarySearchCutoffIndex -> __module__
  + binarySearchCutoffIndex -> array
  + binarySearchCutoffIndex -> highIndex
  + binarySearchCutoffIndex -> lowIndex
  + binarySearchCutoffIndex -> pivot
  + binarySearchCutoffIndex -> pivotIndex

## src/mapValues.ts  (tp 1, fp 5, fn 1, unscored 1)
  - mapValuesImplementation -> valueMapper
  + mapValuesImplementation -> for
  + mapValuesImplementation -> forEach
  + mapValuesImplementation -> mapValuesImplementation
  + mapValuesImplementation -> of
  + mapValuesImplementation -> out
  ~ mapValuesImplementation -> entries

## src/merge.ts  (tp 1, fp 6, fn 0, unscored 1)
  + mergeImplementation -> 
  + mergeImplementation -> Merge
  + mergeImplementation -> Source
  + mergeImplementation -> T
  + mergeImplementation -> data
  + mergeImplementation -> source
  ~ merge -> mergeImplementation

## src/pick.ts  (tp 0, fp 5, fn 1, unscored 1)
  - pick -> purry
  + pickImplementation -> for
  + pickImplementation -> in
  + pickImplementation -> keys
  + pickImplementation -> object
  + pickImplementation -> out
  ~ pick -> pickImplementation

## src/sum.ts  (tp 1, fp 6, fn 0, unscored 0)
  + sumImplementation -> +=
  + sumImplementation -> data
  + sumImplementation -> for
  + sumImplementation -> out
  + sumImplementation -> typeof
  + sumImplementation -> value

## src/uniqueBy.ts  (tp 2, fp 3, fn 3, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  + lazyImplementation -> SKIP_ITEM
  + lazyImplementation -> set
  + uniqueBy -> __module__
  ~ uniqueBy -> lazyImplementation

## src/groupByProp.ts  (tp 2, fp 5, fn 0, unscored 2)
  + groupByPropImplementation -> filter
  + groupByPropImplementation -> item
  + groupByPropImplementation -> items
  + groupByPropImplementation -> key
  + groupByPropImplementation -> undefined
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/indexBy.ts  (tp 3, fp 5, fn 0, unscored 0)
  + indexByImplementation -> BoundedPartial
  + indexByImplementation -> as
  + indexByImplementation -> for
  + indexByImplementation -> key
  + indexByImplementation -> out

## src/internal/purryFromLazy.ts  (tp 1, fp 4, fn 1, unscored 2)
  - purryFromLazy -> Error
  + purryFromLazy -> __module__
  + purryFromLazy -> dataFirst
  + purryFromLazy -> lazyArgs
  + purryFromLazy -> satisfies
  ~ purryFromLazy -> assign
  ~ purryFromLazy -> dataLast

## src/internal/quickSelect.ts  (tp 2, fp 2, fn 3, unscored 1)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelectImplementation -> quickSelectImplementation
  + quickSelect -> partition
  + quickSelectImplementation -> swapInPlace
  ~ quickSelectImplementation -> compareFn

## src/only.ts  (tp 1, fp 5, fn 0, unscored 0)
  + onlyImplementation -> 
  + onlyImplementation -> 0
  + onlyImplementation -> 1
  + onlyImplementation -> data
  + onlyImplementation -> length

## src/pathOr.ts  (tp 1, fp 5, fn 0, unscored 0)
  + pathOrImplementation -> __lookupGetter
  + pathOrImplementation -> getOwnPropertyDescriptor
  + pathOrImplementation -> getPrototypeOf
  + pathOrImplementation -> hasOwnProperty
  + pathOrImplementation -> toString

## src/rankBy.ts  (tp 2, fp 5, fn 0, unscored 0)
  + rankBy -> __module__
  + rankByImplementation -> data
  + rankByImplementation -> for
  + rankByImplementation -> rank
  + rankByImplementation -> targetItem

## src/take.ts  (tp 2, fp 5, fn 0, unscored 1)
  + lazyImplementation -> n
  + lazyImplementation -> remaining
  + lazyImplementation -> value
  + takeImplementation -> array
  + takeImplementation -> n
  ~ take -> lazyImplementation

## src/takeLast.ts  (tp 2, fp 5, fn 0, unscored 2)
  + takeLastImplementation -> 0
  + takeLastImplementation -> Math
  + takeLastImplementation -> array
  + takeLastImplementation -> length
  + takeLastImplementation -> n
  ~ takeLast -> takeLastImplementation
  ~ takeLastImplementation -> max

## src/takeLastWhile.ts  (tp 2, fp 4, fn 1, unscored 0)
  - takeLastWhileImplementation -> predicate
  + takeLastWhileImplementation -> data
  + takeLastWhileImplementation -> for
  + takeLastWhileImplementation -> i
  + takeLastWhileImplementation -> length

## src/zip.ts  (tp 2, fp 5, fn 0, unscored 0)
  + lazyImplementation -> done
  + lazyImplementation -> hasNext
  + lazyImplementation -> next
  + zipImplementation -> IterableContainer
  + zipImplementation -> filter

## src/countBy.ts  (tp 4, fp 2, fn 2, unscored 0)
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  + countByImplementation -> __module__
  + countByImplementation -> undefined

## src/dropLast.ts  (tp 2, fp 4, fn 0, unscored 2)
  + dropLastImplementation -> Math
  + dropLastImplementation -> array
  + dropLastImplementation -> length
  + dropLastImplementation -> n
  ~ dropLast -> dropLastImplementation
  ~ dropLastImplementation -> max

## src/dropLastWhile.ts  (tp 3, fp 4, fn 0, unscored 0)
  + dropLastWhileImplementation -> data
  + dropLastWhileImplementation -> i
  + dropLastWhileImplementation -> index
  + dropLastWhileImplementation -> length

## src/findLastIndex.ts  (tp 2, fp 4, fn 0, unscored 0)
  + findLastIndexImplementation -> data
  + findLastIndexImplementation -> for
  + findLastIndexImplementation -> i
  + findLastIndexImplementation -> return

## src/fromEntries.ts  (tp 0, fp 3, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> as const
  + fromEntries -> fromEntries
  + fromEntries -> pipe

## src/hasAtLeast.ts  (tp 1, fp 4, fn 0, unscored 1)
  + hasAtLeastImplementation -> >=
  + hasAtLeastImplementation -> data
  + hasAtLeastImplementation -> length
  + hasAtLeastImplementation -> minimum
  ~ hasAtLeast -> hasAtLeastImplementation

## src/internal/words.ts  (tp 1, fp 0, fn 4, unscored 0)
  - words -> has
  - words -> push
  - words -> slice
  - words -> test

## src/isPlainObject.ts  (tp 0, fp 4, fn 0, unscored 1)
  + isPlainObject -> Object
  + isPlainObject -> __module__
  + isPlainObject -> data
  + isPlainObject -> typeof
  ~ isPlainObject -> getPrototypeOf

## src/mapKeys.ts  (tp 1, fp 3, fn 1, unscored 1)
  - mapKeys -> purry
  + mapKeys -> __module__
  + mapKeysImplementation -> for
  + mapKeysImplementation -> out
  ~ mapKeysImplementation -> entries

## src/partition.ts  (tp 3, fp 3, fn 1, unscored 0)
  - partitionImplementation -> push
  + partitionImplementation -> data
  + partitionImplementation -> for
  + partitionImplementation -> index

## src/purry.ts  (tp 1, fp 2, fn 2, unscored 1)
  - purry -> Error
  - purry -> lazyDataLastImpl
  + purry -> args
  + purry -> lazy
  ~ __module__ -> Error

## src/randomString.ts  (tp 3, fp 4, fn 0, unscored 2)
  + randomStringImplementation -> ALPHABET
  + randomStringImplementation -> Math
  + randomStringImplementation -> for
  + randomStringImplementation -> length
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/takeFirstBy.ts  (tp 4, fp 4, fn 0, unscored 1)
  + takeFirstBy -> __module__
  + takeFirstByImplementation -> filter
  + takeFirstByImplementation -> reduce
  + takeFirstByImplementation -> sort
  ~ takeFirstByImplementation -> compareFn

## src/add.ts  (tp 1, fp 3, fn 0, unscored 0)
  + addImplementation -> +
  + addImplementation -> addend
  + addImplementation -> value

## src/defaultTo.ts  (tp 1, fp 3, fn 0, unscored 0)
  + defaultToImplementation -> ??
  + defaultToImplementation -> data
  + defaultToImplementation -> fallback

## src/dropFirstBy.ts  (tp 5, fp 3, fn 0, unscored 0)
  + dropFirstByImplementation -> filter
  + dropFirstByImplementation -> reduce
  + dropFirstByImplementation -> sort

## src/first.ts  (tp 1, fp 2, fn 1, unscored 4)
  - first -> toSingle
  + firstImplementation -> item
  + firstLazy -> next
  ~ __module__ -> IterableContainer
  ~ __module__ -> LazyEvaluator
  ~ __module__ -> toSingle
  ~ first -> lazyImplementation

## src/forEach.ts  (tp 2, fp 2, fn 1, unscored 1)
  - lazyImplementation -> callbackfn
  + forEachImplementation -> data
  + lazyImplementation -> forEach
  ~ forEachImplementation -> callbackfn

## src/groupBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/isIncludedIn.ts  (tp 2, fp 2, fn 1, unscored 0)
  - isIncludedIn -> Set
  + pipe -> has
  + pipe -> includes

## src/keys.ts  (tp 0, fp 2, fn 1, unscored 0)
  - keys -> purry
  + keys -> keys
  + keys -> pipe

## src/length.ts  (tp 1, fp 3, fn 0, unscored 1)
  + lengthImplementation -> in
  + lengthImplementation -> length
  + lengthImplementation -> slice
  ~ length -> lengthImplementation

## src/randomInteger.ts  (tp 0, fp 1, fn 2, unscored 3)
  - randomInteger -> RangeError
  - randomInteger -> toString
  + randomInteger -> __module__
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/sort.ts  (tp 2, fp 3, fn 0, unscored 1)
  + sortImplementation -> as
  + sortImplementation -> items
  + sortImplementation -> ret
  ~ sortImplementation -> cmp

## src/split.ts  (tp 1, fp 3, fn 0, unscored 0)
  + split -> dataFirst
  + split -> dataLast
  + split -> pipe

## src/swapProps.ts  (tp 1, fp 3, fn 0, unscored 0)
  + swapPropsImplementation -> assign
  + swapPropsImplementation -> defineProperty
  + swapPropsImplementation -> getOwnPropertyDescriptor

## src/takeWhile.ts  (tp 3, fp 2, fn 1, unscored 0)
  - takeWhileImplementation -> predicate
  + takeWhileImplementation -> break
  + takeWhileImplementation -> for

## src/toTitleCase.ts  (tp 6, fp 1, fn 2, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> words
  + toTitleCase -> words

## src/toUpperCase.ts  (tp 1, fp 2, fn 1, unscored 1)
  - toUpperCaseImplementation -> toUpperCase
  + pipe -> toUpperCase
  + toUpperCase -> toUpperCase
  ~ toUpperCase -> toUpperCaseImplementation

## src/unique.ts  (tp 1, fp 0, fn 3, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  ~ unique -> lazyImplementation

## src/capitalize.ts  (tp 3, fp 2, fn 0, unscored 1)
  + capitalizeImplementation -> ??
  + capitalizeImplementation -> as
  ~ capitalize -> capitalizeImplementation

## src/concat.ts  (tp 1, fp 2, fn 0, unscored 1)
  + concatImplementation -> concat
  + concatImplementation -> push
  ~ concat -> concatImplementation

## src/differenceWith.ts  (tp 1, fp 0, fn 2, unscored 1)
  - lazyImplementation -> every
  - lazyImplementation -> isEqual
  ~ differenceWith -> lazyImplementation

## src/divide.ts  (tp 1, fp 2, fn 0, unscored 1)
  + divideImplementation -> divisor
  + divideImplementation -> value
  ~ divide -> divideImplementation

## src/drop.ts  (tp 2, fp 2, fn 0, unscored 0)
  + drop -> __module__
  + lazyImplementation -> function

## src/dropWhile.ts  (tp 4, fp 2, fn 0, unscored 0)
  + dropWhileImplementation -> data
  + dropWhileImplementation -> index

## src/endsWith.ts  (tp 2, fp 2, fn 0, unscored 1)
  + endsWithImplementation -> data
  + endsWithImplementation -> suffix
  ~ endsWith -> endsWithImplementation

## src/findLast.ts  (tp 1, fp 1, fn 1, unscored 0)
  - findLastImplementation -> predicate
  + findLastImplementation -> for

## src/floor.ts  (tp 2, fp 2, fn 0, unscored 0)
  + floor -> floor
  + floor -> precisionOf

## src/isEmpty.ts  (tp 0, fp 2, fn 0, unscored 2)
  + isEmpty -> __module__
  + isEmpty -> data === undefined
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/join.ts  (tp 2, fp 2, fn 0, unscored 1)
  + joinImplementation -> data
  + joinImplementation -> glue
  ~ join -> joinImplementation

## src/omitBy.ts  (tp 2, fp 2, fn 0, unscored 1)
  + omitByImplementation -> delete
  + omitByImplementation -> for
  ~ omitByImplementation -> entries

## src/pullObject.ts  (tp 4, fp 2, fn 0, unscored 0)
  + pullObjectImplementation -> for
  + pullObjectImplementation -> result

## src/sortedIndex.ts  (tp 2, fp 2, fn 0, unscored 0)
  + sortedIndexImplementation -> item
  + sortedIndexImplementation -> pivot

## src/stringToPath.ts  (tp 2, fp 0, fn 2, unscored 0)
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/times.ts  (tp 2, fp 2, fn 0, unscored 2)
  + timesImplementation -> new Array
  + timesImplementation -> push
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/uncapitalize.ts  (tp 3, fp 2, fn 0, unscored 1)
  + uncapitalizeImplementation -> ??
  + uncapitalizeImplementation -> as
  ~ uncapitalize -> uncapitalizeImplementation

## src/values.ts  (tp 1, fp 2, fn 0, unscored 0)
  + values -> args
  + values -> values

## src/ceil.ts  (tp 2, fp 1, fn 0, unscored 0)
  + ceil -> ceil

## src/flatMap.ts  (tp 2, fp 0, fn 1, unscored 1)
  - flatMapImplementation -> flatMap
  ~ flatMap -> flatMapImplementation

## src/hasSubObject.ts  (tp 2, fp 1, fn 0, unscored 2)
  + hasSubObjectImplementation -> hasOwnProperty
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/invert.ts  (tp 1, fp 1, fn 0, unscored 2)
  + invertImplementation -> for
  ~ invert -> invertImplementation
  ~ invertImplementation -> entries

## src/nthBy.ts  (tp 2, fp 1, fn 0, unscored 0)
  + quickSelect -> compareFn

## src/objOf.ts  (tp 1, fp 1, fn 0, unscored 0)
  + objOfImplementation -> assign

## src/piped.ts  (tp 1, fp 1, fn 0, unscored 0)
  + piped -> map

## src/product.ts  (tp 0, fp 0, fn 1, unscored 0)
  - product -> purry

## src/round.ts  (tp 2, fp 1, fn 0, unscored 0)
  + round -> round

## src/set.ts  (tp 1, fp 1, fn 0, unscored 0)
  + setImplementation -> assign

## src/sliceString.ts  (tp 1, fp 1, fn 0, unscored 0)
  + sliceString -> toString

## src/filter.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ filterImplementation -> predicate

## src/hasProp.ts  (tp 1, fp 0, fn 0, unscored 1)
  ~ hasPropImplementation -> hasOwn

## src/last.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ last -> lastImplementation

## src/map.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ mapImplementation -> callbackfn

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 0, unscored 1)
  ~ sortedIndexWith -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ sortedLastIndex -> sortedLastIndexImplementation

12 of 112 files exactly right.
