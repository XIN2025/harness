# ensemble-2of2 / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 85.6% [72.4% to 91.9%]   R 22.2% [18.5% to 25.8%]   F1 35.3% [30.4% to 39.8%]

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

## src/internal/purryOrderRules.ts  (tp 0, fp 0, fn 13, unscored 0)
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

## src/clone.ts  (tp 0, fp 0, fn 12, unscored 0)
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

## src/debounce.ts  (tp 0, fp 0, fn 8, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> setTimeout
  - debounce -> toString

## src/funnel.ts  (tp 0, fp 0, fn 8, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout
  - funnel -> voidReducer

## src/countBy.ts  (tp 0, fp 0, fn 7, unscored 0)
  - countBy -> countByImplementation
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set

## src/internal/quickSelect.ts  (tp 0, fp 0, fn 7, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> compareFn
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation

## src/internal/withPrecision.ts  (tp 1, fp 1, fn 6, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString
  + withPrecision -> precision

## src/sample.ts  (tp 1, fp 0, fn 7, unscored 0)
  - sample -> purry
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort

## src/zipWith.ts  (tp 1, fp 0, fn 7, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyDataLastImpl
  - zipWith -> lazyImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/dropFirstBy.ts  (tp 1, fp 0, fn 6, unscored 0)
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice

## src/intersection.ts  (tp 1, fp 0, fn 6, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set

## src/toKebabCase.ts  (tp 0, fp 1, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + toKebabCase -> words

## src/toTitleCase.ts  (tp 3, fp 1, fn 5, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> toUpperCase
  - toTitleCaseImplementation -> words
  + toTitleCaseImplementation -> word

## src/difference.ts  (tp 1, fp 0, fn 5, unscored 0)
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set

## src/isEmpty.ts  (tp 0, fp 5, fn 0, unscored 0)
  + isEmpty -> hasAtLeast
  + isEmpty -> isEmptyish
  + isEmpty -> isNullish
  + isEmpty -> isStrictEqual
  + isEmpty -> isTruthy

## src/takeFirstBy.ts  (tp 1, fp 0, fn 5, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice

## src/uniqueBy.ts  (tp 1, fp 0, fn 5, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy

## src/dropWhile.ts  (tp 1, fp 0, fn 4, unscored 0)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

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

## src/internal/purryFromLazy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - purryFromLazy -> Error
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  - purryFromLazy -> pipe

## src/internal/words.ts  (tp 1, fp 0, fn 4, unscored 0)
  - words -> has
  - words -> push
  - words -> slice
  - words -> test

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

## src/nthBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - nthBy -> nthByImplementation
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> compareFn
  - nthByImplementation -> quickSelect

## src/partition.ts  (tp 1, fp 0, fn 4, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/sort.ts  (tp 1, fp 1, fn 3, unscored 0)
  - sort -> purry
  - sortImplementation -> cmp
  - sortImplementation -> sort
  + sortImplementation -> defaultCompare

## src/sortedIndexBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexBy -> sortedIndexByImplementation
  - sortedIndexByImplementation -> binarySearchCutoffIndex
  - sortedIndexByImplementation -> valueFunction

## src/sortedLastIndexBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - sortedLastIndexBy -> purry
  - sortedLastIndexBy -> sortedLastIndexByImplementation
  - sortedLastIndexByImplementation -> binarySearchCutoffIndex
  - sortedLastIndexByImplementation -> valueFunction

## src/splitWhen.ts  (tp 1, fp 0, fn 4, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> predicate
  - splitWhenImplementation -> slice

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/takeWhile.ts  (tp 1, fp 0, fn 4, unscored 0)
  - takeWhile -> purry
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push

## src/unique.ts  (tp 1, fp 0, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy

## src/when.ts  (tp 1, fp 0, fn 4, unscored 0)
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate

## src/capitalize.ts  (tp 1, fp 0, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase

## src/differenceWith.ts  (tp 1, fp 0, fn 3, unscored 0)
  - differenceWith -> purryFromLazy
  - lazyImplementation -> every
  - lazyImplementation -> isEqual

## src/drop.ts  (tp 2, fp 0, fn 3, unscored 0)
  - drop -> purry
  - dropImplementation -> slice
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropLastWhile.ts  (tp 1, fp 0, fn 3, unscored 0)
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice

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

## src/fromKeys.ts  (tp 1, fp 0, fn 3, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper

## src/groupBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/groupByProp.ts  (tp 0, fp 0, fn 3, unscored 0)
  - groupByProp -> groupByPropImplementation
  - groupByProp -> purry
  - groupByPropImplementation -> push

## src/indexBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/isIncludedIn.ts  (tp 0, fp 0, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes

## src/join.ts  (tp 1, fp 1, fn 2, unscored 0)
  - join -> purry
  - joinImplementation -> join
  + joinImplementation -> glue

## src/median.ts  (tp 1, fp 0, fn 3, unscored 0)
  - median -> purry
  - medianImplementation -> numberComparator
  - medianImplementation -> sort

## src/omitBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - omitBy -> omitByImplementation
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/purry.ts  (tp 1, fp 1, fn 2, unscored 0)
  - purry -> Error
  - purry -> lazyDataLastImpl
  + purry -> args

## src/randomString.ts  (tp 1, fp 0, fn 3, unscored 0)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push

## src/range.ts  (tp 1, fp 0, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap

## src/reduce.ts  (tp 1, fp 0, fn 3, unscored 0)
  - reduce -> purry
  - reduceImplementation -> callbackfn
  - reduceImplementation -> reduce

## src/sortBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> compareFn
  - sortByImplementation -> sort

## src/sortedIndex.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedIndex -> purry
  - sortedIndex -> sortedIndexImplementation
  - sortedIndexImplementation -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndex -> sortedLastIndexImplementation
  - sortedLastIndexImplementation -> binarySearchCutoffIndex

## src/sumBy.ts  (tp 2, fp 0, fn 3, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/swapIndices.ts  (tp 1, fp 0, fn 3, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> purry
  - takeImplementation -> slice

## src/takeLastWhile.ts  (tp 1, fp 0, fn 3, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice

## src/uncapitalize.ts  (tp 1, fp 0, fn 3, unscored 0)
  - uncapitalize -> purry
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase

## src/zip.ts  (tp 1, fp 0, fn 3, unscored 0)
  - zip -> lazyImplementation
  - zip -> purry
  - zipImplementation -> map

## src/ceil.ts  (tp 1, fp 1, fn 1, unscored 0)
  - ceil -> purry
  + ceil -> ceil

## src/dropLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - dropLast -> purry
  - dropLastImplementation -> slice

## src/endsWith.ts  (tp 1, fp 0, fn 2, unscored 0)
  - endsWith -> purry
  - endsWithImplementation -> endsWith

## src/findLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - findLast -> purry
  - findLastImplementation -> predicate

## src/findLastIndex.ts  (tp 1, fp 0, fn 2, unscored 0)
  - findLastIndex -> purry
  - findLastIndexImplementation -> predicate

## src/floor.ts  (tp 1, fp 1, fn 1, unscored 0)
  - floor -> purry
  + floor -> floor

## src/keys.ts  (tp 0, fp 1, fn 1, unscored 0)
  - keys -> purry
  + keys -> keys

## src/last.ts  (tp 1, fp 0, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at

## src/mapKeys.ts  (tp 1, fp 0, fn 2, unscored 0)
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper

## src/mapValues.ts  (tp 1, fp 0, fn 2, unscored 0)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper

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

## src/rankBy.ts  (tp 1, fp 0, fn 2, unscored 0)
  - rankBy -> purryOrderRulesWithArgument
  - rankByImplementation -> compareFn

## src/round.ts  (tp 1, fp 1, fn 1, unscored 0)
  - round -> purry
  + round -> round

## src/setPath.ts  (tp 1, fp 0, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation

## src/takeLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - takeLast -> purry
  - takeLastImplementation -> slice

## src/times.ts  (tp 1, fp 0, fn 2, unscored 0)
  - times -> purry
  - timesImplementation -> fn

## src/toUpperCase.ts  (tp 1, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/add.ts  (tp 1, fp 0, fn 1, unscored 0)
  - add -> purry

## src/concat.ts  (tp 1, fp 0, fn 1, unscored 0)
  - concat -> purry

## src/defaultTo.ts  (tp 1, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/divide.ts  (tp 1, fp 0, fn 1, unscored 0)
  - divide -> purry

## src/fromEntries.ts  (tp 0, fp 0, fn 1, unscored 0)
  - fromEntries -> purry

## src/hasAtLeast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/hasProp.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasProp -> purry

## src/hasSubObject.ts  (tp 2, fp 0, fn 1, unscored 0)
  - hasSubObject -> purry

## src/invert.ts  (tp 1, fp 0, fn 1, unscored 1)
  - invert -> purry
  ~ invertImplementation -> entries

## src/length.ts  (tp 1, fp 0, fn 1, unscored 0)
  - length -> purry

## src/merge.ts  (tp 1, fp 0, fn 1, unscored 0)
  - merge -> purry

## src/objOf.ts  (tp 1, fp 0, fn 1, unscored 0)
  - objOf -> purry

## src/only.ts  (tp 1, fp 0, fn 1, unscored 0)
  - only -> purry

## src/partialLastBind.ts  (tp 0, fp 0, fn 1, unscored 0)
  - partialLastBind -> func

## src/pathOr.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pathOr -> purry

## src/pick.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pick -> purry

## src/product.ts  (tp 1, fp 0, fn 1, unscored 0)
  - product -> purry

## src/set.ts  (tp 1, fp 0, fn 1, unscored 0)
  - set -> purry

## src/sliceString.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sliceString -> slice

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/split.ts  (tp 0, fp 0, fn 1, unscored 0)
  - split -> split

## src/sum.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sum -> purry

## src/swapProps.ts  (tp 1, fp 0, fn 1, unscored 0)
  - swapProps -> purry

## src/values.ts  (tp 1, fp 1, fn 0, unscored 0)
  + values -> values

4 of 112 files exactly right.
