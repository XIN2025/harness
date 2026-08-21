# qwen15b-ours / dev / cut=calls_only

raw 0/112 (0.0%)  ·  fence-stripped 106/112 (94.6%)  ·  schema 106/112 (94.6%)
P 0.0% [0.0% to 0.0%] (percentile)   R 0.0% [0.0% to 0.0%] (percentile)   F1 0.0% [0.0% to 0.0%] (percentile)

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

## src/pipe.ts  (tp 0, fp 0, fn 13, unscored 1)
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
  ~ __module__ -> pipe

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

## src/internal/purryOrderRules.ts  (tp 0, fp 0, fn 11, unscored 2)
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
  ~ __module__ -> purryOrderRules
  ~ __module__ -> purryOrderRulesWithArgument

## src/debounce.ts  (tp 0, fp 0, fn 8, unscored 0)
  - debounce -> Error
  - debounce -> clearTimeout
  - debounce -> func
  - debounce -> handleCoolDownEnd
  - debounce -> handleDebouncedCall
  - debounce -> handleInvoke
  - debounce -> setTimeout
  - debounce -> toString

## src/toTitleCase.ts  (tp 0, fp 0, fn 8, unscored 1)
  - toTitleCase -> toTitleCaseImplementation
  - toTitleCaseImplementation -> join
  - toTitleCaseImplementation -> map
  - toTitleCaseImplementation -> slice
  - toTitleCaseImplementation -> test
  - toTitleCaseImplementation -> toLowerCase
  - toTitleCaseImplementation -> toUpperCase
  - toTitleCaseImplementation -> words
  ~ __module__ -> toTitleCaseImplementation

## src/funnel.ts  (tp 0, fp 0, fn 7, unscored 0)
  - funnel -> callback
  - funnel -> clearTimeout
  - funnel -> handleBurstEnd
  - funnel -> handleIntervalEnd
  - funnel -> invoke
  - funnel -> reducer
  - funnel -> setTimeout

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
  ~ __module__ -> sampleImplementation

## src/countBy.ts  (tp 0, fp 0, fn 6, unscored 2)
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set
  ~ __module__ -> countBy
  ~ __module__ -> pipe

## src/dropFirstBy.ts  (tp 0, fp 0, fn 5, unscored 0)
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice

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

## src/intersection.ts  (tp 0, fp 0, fn 5, unscored 0)
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> set

## src/uniqueBy.ts  (tp 0, fp 0, fn 5, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has
  - uniqueBy -> purryFromLazy

## src/when.ts  (tp 0, fp 0, fn 5, unscored 1)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate
  ~ __module__ -> when

## src/zipWith.ts  (tp 0, fp 0, fn 5, unscored 2)
  - lazyImplementation -> fn
  - zipWith -> lazyDataLastImpl
  - zipWith -> zipWithImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map
  ~ __module__ -> lazyDataLastImpl
  ~ __module__ -> zipWith

## src/difference.ts  (tp 0, fp 0, fn 4, unscored 0)
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> set

## src/dropWhile.ts  (tp 0, fp 0, fn 4, unscored 2)
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice
  ~ __module__ -> dropWhile
  ~ __module__ -> dropWhileImplementation

## src/partition.ts  (tp 0, fp 0, fn 4, unscored 0)
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/pullObject.ts  (tp 0, fp 0, fn 4, unscored 0)
  - pullObject -> purry
  - pullObjectImplementation -> entries
  - pullObjectImplementation -> keyExtractor
  - pullObjectImplementation -> valueExtractor

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/sumBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - sumBy -> purry
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/takeFirstBy.ts  (tp 0, fp 0, fn 4, unscored 1)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  ~ __module__ -> takeFirstByImplementation

## src/takeWhile.ts  (tp 0, fp 0, fn 4, unscored 1)
  - takeWhile -> purry
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push
  ~ __module__ -> takeWhile

## src/toKebabCase.ts  (tp 0, fp 0, fn 4, unscored 0)
  - toKebabCase -> purry
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words

## src/unique.ts  (tp 0, fp 0, fn 4, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> purryFromLazy

## src/capitalize.ts  (tp 0, fp 0, fn 3, unscored 0)
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase

## src/differenceWith.ts  (tp 0, fp 0, fn 3, unscored 0)
  - differenceWith -> purryFromLazy
  - lazyImplementation -> every
  - lazyImplementation -> isEqual

## src/dropLastWhile.ts  (tp 0, fp 0, fn 3, unscored 2)
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  ~ __module__ -> dropLastWhile
  ~ __module__ -> purry

## src/evolve.ts  (tp 0, fp 0, fn 3, unscored 0)
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/filter.ts  (tp 0, fp 0, fn 3, unscored 1)
  - filter -> purry
  - filterImplementation -> filter
  - lazyImplementation -> predicate
  ~ __module__ -> filter

## src/flatMap.ts  (tp 0, fp 0, fn 3, unscored 0)
  - flatMap -> purry
  - flatMapImplementation -> flatMap
  - lazyImplementation -> callbackfn

## src/forEach.ts  (tp 0, fp 0, fn 3, unscored 0)
  - forEach -> purry
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn

## src/fromKeys.ts  (tp 0, fp 0, fn 3, unscored 1)
  - fromKeys -> purry
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper
  ~ __module__ -> fromKeys

## src/groupBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/indexBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/isIncludedIn.ts  (tp 0, fp 0, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes

## src/last.ts  (tp 0, fp 1, fn 2, unscored 0)
  - last -> purry
  - lastImplementation -> at
  + last -> last

## src/map.ts  (tp 0, fp 0, fn 3, unscored 1)
  - lazyImplementation -> callbackfn
  - map -> purry
  - mapImplementation -> map
  ~ __module__ -> map

## src/meanBy.ts  (tp 0, fp 0, fn 3, unscored 1)
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn
  ~ __module__ -> meanBy

## src/purry.ts  (tp 0, fp 0, fn 3, unscored 0)
  - purry -> Error
  - purry -> fn
  - purry -> lazyDataLastImpl

## src/randomString.ts  (tp 0, fp 0, fn 3, unscored 1)
  - randomString -> purry
  - randomStringImplementation -> join
  - randomStringImplementation -> push
  ~ __module__ -> randomString

## src/range.ts  (tp 0, fp 0, fn 3, unscored 0)
  - range -> purry
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap

## src/sortedIndexBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedIndexBy -> purry
  - sortedIndexByImplementation -> binarySearchCutoffIndex
  - sortedIndexByImplementation -> valueFunction

## src/sortedLastIndexBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedLastIndexBy -> purry
  - sortedLastIndexByImplementation -> binarySearchCutoffIndex
  - sortedLastIndexByImplementation -> valueFunction

## src/splitWhen.ts  (tp 0, fp 0, fn 3, unscored 0)
  - splitWhen -> purry
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> slice

## src/swapIndices.ts  (tp 0, fp 0, fn 3, unscored 0)
  - swapIndices -> purry
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray

## src/takeLastWhile.ts  (tp 0, fp 0, fn 3, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice

## src/uncapitalize.ts  (tp 0, fp 0, fn 3, unscored 0)
  - uncapitalize -> purry
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase

## src/ceil.ts  (tp 0, fp 0, fn 2, unscored 3)
  - ceil -> purry
  - ceil -> withPrecision
  ~ __module__ -> ceil
  ~ __module__ -> purry
  ~ __module__ -> withPrecision

## src/drop.ts  (tp 0, fp 0, fn 2, unscored 1)
  - drop -> purry
  - dropImplementation -> slice
  ~ __module__ -> drop

## src/dropLast.ts  (tp 0, fp 0, fn 2, unscored 0)
  - dropLast -> purry
  - dropLastImplementation -> slice

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

## src/first.ts  (tp 0, fp 0, fn 2, unscored 2)
  - first -> purry
  - first -> toSingle
  ~ __module__ -> first
  ~ __module__ -> pipe

## src/floor.ts  (tp 0, fp 0, fn 2, unscored 1)
  - floor -> purry
  - floor -> withPrecision
  ~ __module__ -> floor

## src/groupByProp.ts  (tp 0, fp 0, fn 2, unscored 1)
  - groupByProp -> purry
  - groupByPropImplementation -> push
  ~ __module__ -> groupByProp

## src/hasSubObject.ts  (tp 0, fp 0, fn 2, unscored 0)
  - hasSubObject -> purry
  - hasSubObjectImplementation -> isDeepEqual

## src/internal/purryFromLazy.ts  (tp 0, fp 0, fn 2, unscored 1)
  - purryFromLazy -> Error
  - purryFromLazy -> pipe
  ~ __module__ -> pipe

## src/join.ts  (tp 0, fp 0, fn 2, unscored 1)
  - join -> purry
  - joinImplementation -> join
  ~ __module__ -> join

## src/mapKeys.ts  (tp 0, fp 0, fn 2, unscored 0)
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper

## src/mapValues.ts  (tp 0, fp 0, fn 2, unscored 1)
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper
  ~ __module__ -> mapValues

## src/median.ts  (tp 0, fp 0, fn 2, unscored 0)
  - median -> purry
  - medianImplementation -> sort

## src/nthBy.ts  (tp 0, fp 0, fn 2, unscored 1)
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> quickSelect
  ~ __module__ -> nthBy

## src/omit.ts  (tp 0, fp 0, fn 2, unscored 0)
  - omit -> purry
  - omitImplementation -> hasAtLeast

## src/omitBy.ts  (tp 0, fp 0, fn 2, unscored 0)
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 1)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ __module__ -> randomInteger

## src/rankBy.ts  (tp 0, fp 0, fn 2, unscored 1)
  - rankBy -> purryOrderRulesWithArgument
  - rankByImplementation -> compareFn
  ~ __module__ -> rankBy

## src/reduce.ts  (tp 0, fp 0, fn 2, unscored 0)
  - reduce -> purry
  - reduceImplementation -> reduce

## src/round.ts  (tp 0, fp 0, fn 2, unscored 3)
  - round -> purry
  - round -> withPrecision
  ~ __module__ -> purry
  ~ __module__ -> round
  ~ __module__ -> withPrecision

## src/setPath.ts  (tp 0, fp 0, fn 2, unscored 0)
  - setPath -> purry
  - setPathImplementation -> setPathImplementation

## src/sort.ts  (tp 0, fp 0, fn 2, unscored 1)
  - sort -> purry
  - sortImplementation -> sort
  ~ __module__ -> sort

## src/sortBy.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sortBy -> purryOrderRules
  - sortByImplementation -> sort

## src/sortedIndex.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sortedIndex -> purry
  - sortedIndexImplementation -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndexImplementation -> binarySearchCutoffIndex

## src/take.ts  (tp 0, fp 0, fn 2, unscored 0)
  - take -> purry
  - takeImplementation -> slice

## src/takeLast.ts  (tp 0, fp 0, fn 2, unscored 0)
  - takeLast -> purry
  - takeLastImplementation -> slice

## src/times.ts  (tp 0, fp 0, fn 2, unscored 0)
  - times -> purry
  - timesImplementation -> fn

## src/toUpperCase.ts  (tp 0, fp 0, fn 2, unscored 0)
  - toUpperCase -> purry
  - toUpperCaseImplementation -> toUpperCase

## src/zip.ts  (tp 0, fp 0, fn 2, unscored 1)
  - zip -> purry
  - zipImplementation -> map
  ~ __module__ -> zip

## src/add.ts  (tp 0, fp 0, fn 1, unscored 0)
  - add -> purry

## src/concat.ts  (tp 0, fp 0, fn 1, unscored 1)
  - concat -> purry
  ~ __module__ -> concat

## src/defaultTo.ts  (tp 0, fp 0, fn 1, unscored 0)
  - defaultTo -> purry

## src/divide.ts  (tp 0, fp 0, fn 1, unscored 3)
  - divide -> purry
  ~ __module__ -> divide
  ~ __module__ -> map
  ~ __module__ -> reduce

## src/fromEntries.ts  (tp 0, fp 0, fn 1, unscored 1)
  - fromEntries -> purry
  ~ __module__ -> fromEntries

## src/hasAtLeast.ts  (tp 0, fp 0, fn 1, unscored 0)
  - hasAtLeast -> purry

## src/hasProp.ts  (tp 0, fp 0, fn 1, unscored 0)
  - hasProp -> purry

## src/internal/binarySearchCutoffIndex.ts  (tp 0, fp 0, fn 1, unscored 1)
  - binarySearchCutoffIndex -> predicate
  ~ __module__ -> binarySearchCutoffIndex

## src/invert.ts  (tp 0, fp 0, fn 1, unscored 0)
  - invert -> purry

## src/keys.ts  (tp 0, fp 0, fn 1, unscored 0)
  - keys -> purry

## src/length.ts  (tp 0, fp 0, fn 1, unscored 0)
  - length -> purry

## src/merge.ts  (tp 0, fp 0, fn 1, unscored 1)
  - merge -> purry
  ~ __module__ -> merge

## src/objOf.ts  (tp 0, fp 0, fn 1, unscored 0)
  - objOf -> purry

## src/only.ts  (tp 0, fp 0, fn 1, unscored 0)
  - only -> purry

## src/partialLastBind.ts  (tp 0, fp 0, fn 1, unscored 0)
  - partialLastBind -> func

## src/pathOr.ts  (tp 0, fp 0, fn 1, unscored 1)
  - pathOr -> purry
  ~ __module__ -> pathOr

## src/pick.ts  (tp 0, fp 0, fn 1, unscored 1)
  - pick -> purry
  ~ __module__ -> pick

## src/piped.ts  (tp 0, fp 0, fn 1, unscored 0)
  - piped -> pipe

## src/product.ts  (tp 0, fp 0, fn 1, unscored 1)
  - product -> purry
  ~ __module__ -> product

## src/prop.ts  (tp 0, fp 0, fn 1, unscored 1)
  - prop -> propImplementation
  ~ __module__ -> prop

## src/set.ts  (tp 0, fp 0, fn 1, unscored 2)
  - set -> purry
  ~ __module__ -> pipe
  ~ __module__ -> set

## src/sliceString.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sliceString -> slice

## src/sortedIndexWith.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> purry

## src/split.ts  (tp 0, fp 0, fn 1, unscored 1)
  - split -> split
  ~ __module__ -> split

## src/sum.ts  (tp 0, fp 0, fn 1, unscored 1)
  - sum -> purry
  ~ __module__ -> sum

## src/swapProps.ts  (tp 0, fp 0, fn 1, unscored 1)
  - swapProps -> purry
  ~ __module__ -> swapProps

## src/values.ts  (tp 0, fp 0, fn 1, unscored 0)
  - values -> purry

## src/isEmpty.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ __module__ -> isEmpty

2 of 112 files exactly right.
