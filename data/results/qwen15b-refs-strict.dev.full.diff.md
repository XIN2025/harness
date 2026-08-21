# qwen15b-refs-strict / dev / cut=full

raw 111/112 (99.1%)  ·  fence-stripped 111/112 (99.1%)  ·  schema 111/112 (99.1%)
P 67.1% [57.0% to 75.5%]   R 22.0% [18.6% to 25.2%]   F1 33.2% [28.5% to 37.5%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

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

## src/isDeepEqual.ts  (tp 4, fp 1, fn 14, unscored 0)
  - isDeepEqual -> purry
  - isDeepEqualArrays -> entries
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
  - isDeepEqualSets -> entries
  - isDeepEqualSets -> splice
  + isDeepEqual -> isComparablePrototype

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

## src/internal/purryOrderRules.ts  (tp 1, fp 1, fn 12, unscored 0)
  - isOrderRule -> isProjection
  - orderRuleComparer -> comparator
  - orderRuleComparer -> nextComparer
  - orderRuleComparer -> orderRuleComparer
  - orderRuleComparer -> primaryRule
  - orderRuleComparer -> projector
  - purryOrderRules -> compareFn
  - purryOrderRules -> func
  - purryOrderRules -> isOrderRule
  - purryOrderRulesWithArgument -> func
  - purryOrderRulesWithArgument -> isOrderRule
  - purryOrderRulesWithArgument -> purryOrderRules
  + purryOrderRulesWithArgument -> orderRuleComparer

## src/toTitleCase.ts  (tp 1, fp 3, fn 7, unscored 0)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> test
  - toTitleCaseImplementation -> toLowerCase
  - toTitleCaseImplementation -> toUpperCase
  + toTitleCase -> LOWER_CASE_CHARACTER_RE
  + toTitleCase -> words
  + toTitleCaseImplementation -> LOWER_CASE_CHARACTER_RE

## src/dropFirstBy.ts  (tp 1, fp 2, fn 6, unscored 0)
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice
  + dropFirstBy -> heapMaybeInsert
  + dropFirstBy -> heapify

## src/sample.ts  (tp 0, fp 0, fn 8, unscored 0)
  - sample -> purry
  - sample -> sampleImplementation
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort

## src/takeFirstBy.ts  (tp 0, fp 2, fn 6, unscored 0)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstBy -> takeFirstByImplementation
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  + takeFirstBy -> heapMaybeInsert
  + takeFirstBy -> heapify

## src/toKebabCase.ts  (tp 0, fp 3, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words
  + toKebabCase -> join
  + toKebabCase -> toLowerCase
  + toKebabCase -> words

## src/countBy.ts  (tp 1, fp 1, fn 6, unscored 0)
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set
  + countBy -> categorizationFn

## src/internal/quickSelect.ts  (tp 1, fp 1, fn 6, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> compareFn
  - quickSelectImplementation -> quickSelectImplementation
  + quickSelect -> partition

## src/intersection.ts  (tp 1, fp 1, fn 6, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set
  + intersection -> lazyEmptyEvaluator

## src/difference.ts  (tp 1, fp 1, fn 5, unscored 0)
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set
  + difference -> lazyIdentityEvaluator

## src/funnel.ts  (tp 2, fp 0, fn 6, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout
  - funnel -> voidReducer

## src/internal/words.ts  (tp 0, fp 1, fn 5, unscored 0)
  - words -> flush
  - words -> has
  - words -> push
  - words -> slice
  - words -> test
  + words -> words

## src/pullObject.ts  (tp 1, fp 2, fn 4, unscored 0)
  - pullObject -> purry
  - pullObjectImplementation -> entries
  - pullObjectImplementation -> keyExtractor
  - pullObjectImplementation -> valueExtractor
  + pullObject -> keyExtractor
  + pullObject -> valueExtractor

## src/swapIndices.ts  (tp 0, fp 2, fn 4, unscored 0)
  - swapIndices -> purry
  - swapIndices -> swapIndicesImplementation
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray
  + swapIndices -> swapArray
  + swapIndices -> swapArrayImplementation

## src/uniqueBy.ts  (tp 1, fp 1, fn 5, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy
  + uniqueBy -> keyFunction

## src/zipWith.ts  (tp 2, fp 0, fn 6, unscored 0)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map

## src/debounce.ts  (tp 3, fp 0, fn 5, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> setTimeout
  - debounce -> toString

## src/internal/withPrecision.ts  (tp 2, fp 0, fn 5, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> toString

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

## src/dropWhile.ts  (tp 1, fp 0, fn 4, unscored 0)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice

## src/evolve.ts  (tp 1, fp 1, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value
  + evolveImplementation -> evolve

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

## src/purry.ts  (tp 0, fp 1, fn 3, unscored 0)
  - purry -> Error
  - purry -> fn
  - purry -> lazyDataLastImpl
  + purry -> _findIndex

## src/range.ts  (tp 1, fp 1, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap
  + range -> ceilWithSnap

## src/rankBy.ts  (tp 1, fp 2, fn 2, unscored 0)
  - rankBy -> purryOrderRulesWithArgument
  - rankByImplementation -> compareFn
  + rankBy -> compareFn
  + rankBy -> targetItem

## src/sortedIndex.ts  (tp 0, fp 1, fn 3, unscored 0)
  - sortedIndex -> purry
  - sortedIndex -> sortedIndexImplementation
  - sortedIndexImplementation -> binarySearchCutoffIndex
  + sortedIndex -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 0, fp 1, fn 3, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndex -> sortedLastIndexImplementation
  - sortedLastIndexImplementation -> binarySearchCutoffIndex
  + sortedLastIndex -> binarySearchCutoffIndex

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

## src/sumBy.ts  (tp 1, fp 0, fn 4, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next

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

## src/ceil.ts  (tp 0, fp 1, fn 2, unscored 0)
  - ceil -> purry
  - ceil -> withPrecision
  + ceil -> ceil

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

## src/findIndex.ts  (tp 1, fp 0, fn 3, unscored 0)
  - findIndex -> purry
  - findIndexImplementation -> findIndex
  - findIndexImplementation -> predicate

## src/first.ts  (tp 2, fp 0, fn 3, unscored 0)
  - first -> purry
  - first -> toSingle
  - lazyImplementation -> firstLazy

## src/floor.ts  (tp 0, fp 1, fn 2, unscored 0)
  - floor -> purry
  - floor -> withPrecision
  + floor -> floor

## src/fromKeys.ts  (tp 1, fp 0, fn 3, unscored 0)
  - fromKeys -> purry
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper

## src/groupBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/hasProp.ts  (tp 0, fp 1, fn 2, unscored 0)
  - hasProp -> hasPropImplementation
  - hasProp -> purry
  + hasProp -> hasOwn

## src/indexBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/internal/purryFromLazy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - purryFromLazy -> Error
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy

## src/mapKeys.ts  (tp 0, fp 0, fn 3, unscored 0)
  - mapKeys -> mapKeysImplementation
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper

## src/meanBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn

## src/omit.ts  (tp 0, fp 0, fn 3, unscored 0)
  - omit -> omitImplementation
  - omit -> purry
  - omitImplementation -> hasAtLeast

## src/omitBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - omitBy -> omitByImplementation
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/partition.ts  (tp 2, fp 0, fn 3, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> push

## src/randomString.ts  (tp 1, fp 0, fn 3, unscored 0)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push

## src/reduce.ts  (tp 1, fp 0, fn 3, unscored 0)
  - reduce -> purry
  - reduceImplementation -> callbackfn
  - reduceImplementation -> reduce

## src/round.ts  (tp 0, fp 1, fn 2, unscored 0)
  - round -> purry
  - round -> withPrecision
  + round -> round

## src/sort.ts  (tp 1, fp 0, fn 3, unscored 0)
  - sort -> purry
  - sortImplementation -> cmp
  - sortImplementation -> sort

## src/sortBy.ts  (tp 1, fp 0, fn 3, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> compareFn
  - sortByImplementation -> sort

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

## src/fromEntries.ts  (tp 0, fp 1, fn 1, unscored 0)
  - fromEntries -> purry
  + fromEntries -> fromEntries

## src/groupByProp.ts  (tp 1, fp 0, fn 2, unscored 0)
  - groupByProp -> purry
  - groupByPropImplementation -> push

## src/hasSubObject.ts  (tp 1, fp 0, fn 2, unscored 0)
  - hasSubObject -> purry
  - hasSubObjectImplementation -> isDeepEqual

## src/isIncludedIn.ts  (tp 1, fp 0, fn 2, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has

## src/join.ts  (tp 1, fp 0, fn 2, unscored 0)
  - join -> purry
  - joinImplementation -> join

## src/keys.ts  (tp 0, fp 1, fn 1, unscored 0)
  - keys -> purry
  + keys -> keys

## src/last.ts  (tp 1, fp 0, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at

## src/mapValues.ts  (tp 1, fp 0, fn 2, unscored 0)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper

## src/partialLastBind.ts  (tp 0, fp 1, fn 1, unscored 0)
  - partialLastBind -> func
  + partialLastBind -> parseInt

## src/pathOr.ts  (tp 0, fp 0, fn 2, unscored 0)
  - pathOr -> pathOrImplementation
  - pathOr -> purry

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 1)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ randomInteger -> random

## src/setPath.ts  (tp 1, fp 0, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation

## src/takeLast.ts  (tp 1, fp 0, fn 2, unscored 0)
  - takeLast -> purry
  - takeLastImplementation -> slice

## src/toUpperCase.ts  (tp 1, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/values.ts  (tp 0, fp 1, fn 1, unscored 0)
  - values -> purry
  + values -> values

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

## src/hasAtLeast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/invert.ts  (tp 1, fp 0, fn 1, unscored 0)
  - invert -> purry

## src/isPlainObject.ts  (tp 0, fp 1, fn 0, unscored 0)
  + isPlainObject -> typeof

## src/length.ts  (tp 1, fp 0, fn 1, unscored 0)
  - length -> purry

## src/merge.ts  (tp 1, fp 0, fn 1, unscored 0)
  - merge -> purry

## src/objOf.ts  (tp 1, fp 0, fn 1, unscored 0)
  - objOf -> purry

## src/only.ts  (tp 1, fp 0, fn 1, unscored 0)
  - only -> purry

## src/pick.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pick -> purry

## src/product.ts  (tp 1, fp 0, fn 1, unscored 0)
  - product -> purry

## src/prop.ts  (tp 0, fp 0, fn 1, unscored 0)
  - prop -> propImplementation

## src/set.ts  (tp 1, fp 0, fn 1, unscored 0)
  - set -> purry

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/sum.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sum -> purry

## src/swapProps.ts  (tp 1, fp 0, fn 1, unscored 0)
  - swapProps -> purry

## src/times.ts  (tp 2, fp 0, fn 1, unscored 0)
  - times -> purry

4 of 112 files exactly right.
