# qwen15b-theirs / dev / cut=calls_only

raw 0/112 (0.0%)  ·  fence-stripped 110/112 (98.2%)  ·  schema 110/112 (98.2%)
P 13.9% [6.4% to 23.4%]   R 3.0% [1.5% to 5.3%]   F1 5.0% [2.5% to 8.5%]

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

## src/groupByProp.ts  (tp 0, fp 10, fn 2, unscored 0)
  - groupByProp -> purry
  - groupByPropImplementation -> push
  + groupByProp -> ArrayRequiredPrefix
  + groupByProp -> BoundedPartial
  + groupByProp -> CoercedNonEmptyValues
  + groupByProp -> EnsureValuesAreNonEmpty
  + groupByProp -> FixEmptyObject
  + groupByProp -> IsNonEmptyArray
  + groupByProp -> IsNonEmptyFixedTuple
  + groupByProp -> PossiblyEmptyArrayKeys
  + groupByProp -> Simplify
  + groupByProp -> TupleParts

## src/clone.ts  (tp 0, fp 0, fn 11, unscored 0)
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

## src/funnel.ts  (tp 0, fp 3, fn 7, unscored 0)
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

## src/debounce.ts  (tp 0, fp 1, fn 8, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> setTimeout
  - debounce -> toString
  + App -> useState

## src/range.ts  (tp 0, fp 5, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + range -> DEFAULT_STEP
  + range -> SNAP_TOLERANCE
  + range -> end
  + range -> start
  + range -> step

## src/toTitleCase.ts  (tp 0, fp 0, fn 8, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> test
  - toTitleCaseImplementation -> toLowerCase
  - toTitleCaseImplementation -> toUpperCase
  - toTitleCaseImplementation -> words

## src/countBy.ts  (tp 0, fp 1, fn 6, unscored 0)
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set
  + countBy -> toLowerCase

## src/internal/withPrecision.ts  (tp 0, fp 0, fn 7, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> roundingFn
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString

## src/sample.ts  (tp 0, fp 0, fn 7, unscored 1)
  - sample -> purry
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort
  ~ __module__ -> sample

## src/when.ts  (tp 0, fp 2, fn 5, unscored 0)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate
  + when -> constant
  + when -> isNullish

## src/dropFirstBy.ts  (tp 1, fp 2, fn 4, unscored 0)
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice
  + dropFirstBy -> heapMaybeInsert
  + dropFirstBy -> heapify

## src/intersection.ts  (tp 0, fp 1, fn 5, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> set
  + intersection -> intersection

## src/takeFirstBy.ts  (tp 0, fp 2, fn 4, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  + takeFirstBy -> heapMaybeInsert
  + takeFirstBy -> heapify

## src/dropLastWhile.ts  (tp 0, fp 2, fn 3, unscored 0)
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  + dropLastWhile -> data
  + dropLastWhile -> predicate

## src/first.ts  (tp 0, fp 3, fn 2, unscored 0)
  - first -> purry
  - first -> toSingle
  + first -> pipe
  + firstImplementation -> next
  + lazyImplementation -> next

## src/fromKeys.ts  (tp 1, fp 3, fn 2, unscored 0)
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper
  + fromKeys -> BoundedPartial
  + fromKeys -> IterableContainer
  + fromKeys -> Simplify

## src/internal/quickSelect.ts  (tp 0, fp 0, fn 5, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation

## src/internal/words.ts  (tp 0, fp 0, fn 5, unscored 0)
  - words -> flush
  - words -> has
  - words -> push
  - words -> slice
  - words -> test

## src/pullObject.ts  (tp 0, fp 1, fn 4, unscored 0)
  - pullObject -> purry
  - pullObjectImplementation -> entries
  - pullObjectImplementation -> keyExtractor
  - pullObjectImplementation -> valueExtractor
  + pullObject -> prop

## src/sumBy.ts  (tp 0, fp 1, fn 4, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next
  + sumBy -> callbackfn

## src/uniqueBy.ts  (tp 0, fp 0, fn 5, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy

## src/zipWith.ts  (tp 0, fp 0, fn 5, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> lazyDataLastImpl
  - zipWith -> zipWithImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/dropLast.ts  (tp 0, fp 2, fn 2, unscored 0)
  - dropLast -> purry
  - dropLastImplementation -> slice
  + dropLast -> slice
  + purry -> apply

## src/dropWhile.ts  (tp 0, fp 0, fn 4, unscored 0)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

## src/evolve.ts  (tp 0, fp 1, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value
  + evolve -> add

## src/filter.ts  (tp 0, fp 1, fn 3, unscored 0)
  - filter -> purry
  - filterImplementation -> filter
  - lazyImplementation -> predicate
  + App -> useState

## src/meanBy.ts  (tp 0, fp 1, fn 3, unscored 1)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn
  + meanBy -> pipe
  ~ meanBy -> meanByImplementation

## src/partition.ts  (tp 0, fp 0, fn 4, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/swapIndices.ts  (tp 0, fp 1, fn 3, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray
  + swapIndices -> swapArray

## src/takeLastWhile.ts  (tp 0, fp 1, fn 3, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice
  + takeLastWhile -> pipe

## src/takeWhile.ts  (tp 1, fp 1, fn 3, unscored 0)
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push
  + takeWhile -> pipe

## src/toKebabCase.ts  (tp 0, fp 0, fn 4, unscored 1)
  - toKebabCase -> purry
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  ~ __module__ -> toKebabCase

## src/unique.ts  (tp 0, fp 0, fn 4, unscored 1)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy
  ~ unique -> lazyImplementation

## src/capitalize.ts  (tp 0, fp 0, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase

## src/difference.ts  (tp 1, fp 0, fn 3, unscored 1)
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> set
  ~ difference -> lazyImplementation

## src/drop.ts  (tp 0, fp 1, fn 2, unscored 0)
  - drop -> purry
  - dropImplementation -> slice
  + drop -> drop

## src/flatMap.ts  (tp 0, fp 0, fn 3, unscored 0)
  - flatMap -> purry
  - flatMapImplementation -> flatMap
  - lazyImplementation -> callbackfn

## src/forEach.ts  (tp 0, fp 0, fn 3, unscored 0)
  - forEach -> purry
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn

## src/groupBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/hasProp.ts  (tp 0, fp 2, fn 1, unscored 0)
  - hasProp -> purry
  + hasAtLeast -> pipe
  + hasProp -> hasOwn

## src/indexBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/isIncludedIn.ts  (tp 0, fp 0, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes

## src/join.ts  (tp 0, fp 1, fn 2, unscored 1)
  - join -> purry
  - joinImplementation -> join
  + pipe -> join
  ~ join -> joinImplementation

## src/last.ts  (tp 0, fp 1, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at
  + last -> at

## src/map.ts  (tp 0, fp 0, fn 3, unscored 0)
  - lazyImplementation -> callbackfn
  - map -> purry
  - mapImplementation -> map

## src/omit.ts  (tp 0, fp 1, fn 2, unscored 0)
  - omit -> purry
  - omitImplementation -> hasAtLeast
  + omit -> pipe

## src/pick.ts  (tp 0, fp 2, fn 1, unscored 0)
  - pick -> purry
  + pick -> pipe
  + pick -> purr

## src/purry.ts  (tp 0, fp 0, fn 3, unscored 0)
  - purry -> Error
  - purry -> fn
  - purry -> lazyDataLastImpl

## src/randomString.ts  (tp 0, fp 0, fn 3, unscored 0)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push

## src/sortBy.ts  (tp 0, fp 1, fn 2, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> sort
  + sortBy -> prop

## src/sortedLastIndex.ts  (tp 0, fp 1, fn 2, unscored 1)
  - sortedLastIndex -> purry
  - sortedLastIndexImplementation -> binarySearchCutoffIndex
  + sortedLastIndex -> binarySearchCutoffIndex
  ~ sortedLastIndex -> sortedLastIndexImplementation

## src/sortedLastIndexBy.ts  (tp 1, fp 1, fn 2, unscored 0)
  - sortedLastIndexByImplementation -> binarySearchCutoffIndex
  - sortedLastIndexByImplementation -> valueFunction
  + sortedLastIndexBy -> binarySearchCutoffIndex

## src/splitWhen.ts  (tp 0, fp 0, fn 3, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> slice

## src/times.ts  (tp 0, fp 1, fn 2, unscored 0)
  - times -> purry
  - timesImplementation -> fn
  + times -> identity

## src/uncapitalize.ts  (tp 0, fp 0, fn 3, unscored 0)
  - uncapitalize -> purry
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase

## src/ceil.ts  (tp 0, fp 0, fn 2, unscored 0)
  - ceil -> purry
  - ceil -> withPrecision

## src/differenceWith.ts  (tp 1, fp 0, fn 2, unscored 0)
  - lazyImplementation -> every
  - lazyImplementation -> isEqual

## src/endsWith.ts  (tp 0, fp 0, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith

## src/findIndex.ts  (tp 0, fp 0, fn 2, unscored 0)
  - findIndex -> purry
  - findIndexImplementation -> findIndex

## src/findLast.ts  (tp 0, fp 0, fn 2, unscored 0)
  - findLast -> purry
  - findLastImplementation -> predicate

## src/findLastIndex.ts  (tp 0, fp 0, fn 2, unscored 0)
  - findLastIndex -> purry
  - findLastIndexImplementation -> predicate

## src/floor.ts  (tp 0, fp 0, fn 2, unscored 0)
  - floor -> purry
  - floor -> withPrecision

## src/hasSubObject.ts  (tp 0, fp 0, fn 2, unscored 1)
  - hasSubObject -> purry
  - hasSubObjectImplementation -> isDeepEqual
  ~ hasSubObject -> hasSubObjectImplementation

## src/internal/purryFromLazy.ts  (tp 0, fp 0, fn 2, unscored 0)
  - purryFromLazy -> Error
  - purryFromLazy -> pipe

## src/mapKeys.ts  (tp 0, fp 0, fn 2, unscored 0)
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper

## src/mapValues.ts  (tp 0, fp 0, fn 2, unscored 0)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper

## src/median.ts  (tp 0, fp 0, fn 2, unscored 1)
  - median -> purry
  - medianImplementation -> sort
  ~ median -> medianImplementation

## src/nthBy.ts  (tp 0, fp 0, fn 2, unscored 1)
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> quickSelect
  ~ nthBy -> nthByImplementation

## src/omitBy.ts  (tp 0, fp 0, fn 2, unscored 0)
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/only.ts  (tp 0, fp 1, fn 1, unscored 1)
  - only -> purry
  + only -> pipe
  ~ only -> onlyImplementation

## src/partialLastBind.ts  (tp 0, fp 1, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> parseInt

## src/pathOr.ts  (tp 0, fp 1, fn 1, unscored 0)
  - pathOr -> purry
  + pathOr -> prop

## src/product.ts  (tp 0, fp 1, fn 1, unscored 0)
  - product -> purry
  + product -> pipe

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 0)
  - randomInteger -> RangeError
  - randomInteger -> toString

## src/reduce.ts  (tp 0, fp 0, fn 2, unscored 0)
  - reduce -> purry
  - reduceImplementation -> reduce

## src/round.ts  (tp 0, fp 0, fn 2, unscored 0)
  - round -> purry
  - round -> withPrecision

## src/setPath.ts  (tp 0, fp 0, fn 2, unscored 1)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation
  ~ setPath -> setPathImplementation

## src/sort.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sort -> purry
  - sortImplementation -> sort

## src/sortedIndex.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sortedIndex -> purry
  - sortedIndexImplementation -> binarySearchCutoffIndex

## src/sortedIndexBy.ts  (tp 1, fp 0, fn 2, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexByImplementation -> binarySearchCutoffIndex

## src/take.ts  (tp 0, fp 0, fn 2, unscored 0)
  - take -> purry
  - takeImplementation -> slice

## src/takeLast.ts  (tp 1, fp 1, fn 1, unscored 0)
  - takeLastImplementation -> slice
  + takeLast -> slice

## src/toUpperCase.ts  (tp 0, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/zip.ts  (tp 0, fp 0, fn 2, unscored 1)
  - zip -> purry
  - zipImplementation -> map
  ~ __module__ -> zip

## src/add.ts  (tp 0, fp 0, fn 1, unscored 1)
  - add -> purry
  ~ add -> addImplementation

## src/concat.ts  (tp 0, fp 0, fn 1, unscored 0)
  - concat -> purry

## src/defaultTo.ts  (tp 0, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/divide.ts  (tp 0, fp 0, fn 1, unscored 1)
  - divide -> purry
  ~ divide -> divideImplementation

## src/fromEntries.ts  (tp 0, fp 0, fn 1, unscored 0)
  - fromEntries -> purry

## src/hasAtLeast.ts  (tp 0, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/internal/binarySearchCutoffIndex.ts  (tp 0, fp 0, fn 1, unscored 0)
  - binarySearchCutoffIndex -> predicate

## src/invert.ts  (tp 0, fp 0, fn 1, unscored 0)
  - invert -> purry

## src/keys.ts  (tp 0, fp 0, fn 1, unscored 0)
  - keys -> purry

## src/length.ts  (tp 0, fp 0, fn 1, unscored 0)
  - length -> purry

## src/merge.ts  (tp 0, fp 0, fn 1, unscored 0)
  - merge -> purry

## src/objOf.ts  (tp 0, fp 0, fn 1, unscored 0)
  - objOf -> purry

## src/piped.ts  (tp 0, fp 0, fn 1, unscored 0)
  - piped -> pipe

## src/prop.ts  (tp 0, fp 0, fn 1, unscored 0)
  - prop -> propImplementation

## src/rankBy.ts  (tp 1, fp 0, fn 1, unscored 0)
  - rankByImplementation -> compareFn

## src/set.ts  (tp 0, fp 0, fn 1, unscored 0)
  - set -> purry

## src/sliceString.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sliceString -> slice

## src/sortedIndexWith.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/sum.ts  (tp 0, fp 0, fn 1, unscored 1)
  - sum -> purry
  ~ sum -> sumImplementation

## src/swapProps.ts  (tp 0, fp 0, fn 1, unscored 0)
  - swapProps -> purry

## src/values.ts  (tp 0, fp 0, fn 1, unscored 0)
  - values -> purry

3 of 112 files exactly right.
