# qwen15b-ours / dev / cut=full

raw 0/112 (0.0%)  ·  fence-stripped 106/112 (94.6%)  ·  schema 106/112 (94.6%)
P 0.0% [0.0% to 0.0%] (percentile)   R 0.0% [0.0% to 0.0%] (percentile)   F1 0.0% [0.0% to 0.0%] (percentile)

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

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

## src/pipe.ts  (tp 0, fp 0, fn 17, unscored 1)
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
  ~ __module__ -> pipe

## src/internal/purryOrderRules.ts  (tp 0, fp 0, fn 13, unscored 2)
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
  ~ __module__ -> purryOrderRules
  ~ __module__ -> purryOrderRulesWithArgument

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

## src/sample.ts  (tp 0, fp 0, fn 8, unscored 1)
  - sample -> purry
  - sample -> sampleImplementation
  - sampleImplementation -> Set
  - sampleImplementation -> add
  - sampleImplementation -> filter
  - sampleImplementation -> has
  - sampleImplementation -> map
  - sampleImplementation -> sort
  ~ __module__ -> sampleImplementation

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

## src/zipWith.ts  (tp 0, fp 0, fn 8, unscored 2)
  - lazyImplementation -> fn
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyDataLastImpl
  - zipWith -> lazyImplementation
  - zipWith -> zipWithImplementation
  - zipWithImplementation -> fn
  - zipWithImplementation -> map
  ~ __module__ -> lazyDataLastImpl
  ~ __module__ -> zipWith

## src/countBy.ts  (tp 0, fp 0, fn 7, unscored 2)
  - countBy -> countByImplementation
  - countBy -> purry
  - countByImplementation -> Map
  - countByImplementation -> categorizationFn
  - countByImplementation -> entries
  - countByImplementation -> get
  - countByImplementation -> set
  ~ __module__ -> countBy
  ~ __module__ -> pipe

## src/dropFirstBy.ts  (tp 0, fp 0, fn 7, unscored 0)
  - dropFirstBy -> dropFirstByImplementation
  - dropFirstBy -> purryOrderRulesWithArgument
  - dropFirstByImplementation -> compareFn
  - dropFirstByImplementation -> heapMaybeInsert
  - dropFirstByImplementation -> heapify
  - dropFirstByImplementation -> push
  - dropFirstByImplementation -> slice

## src/internal/quickSelect.ts  (tp 0, fp 0, fn 7, unscored 0)
  - partition -> compareFn
  - partition -> swapInPlace
  - quickSelect -> compareFn
  - quickSelect -> quickSelectImplementation
  - quickSelectImplementation -> compareFn
  - quickSelectImplementation -> partition
  - quickSelectImplementation -> quickSelectImplementation

## src/internal/withPrecision.ts  (tp 0, fp 0, fn 7, unscored 0)
  - shiftDecimalPoint -> split
  - shiftDecimalPoint -> toString
  - withPrecision -> RangeError
  - withPrecision -> TypeError
  - withPrecision -> roundingFn
  - withPrecision -> shiftDecimalPoint
  - withPrecision -> toString

## src/intersection.ts  (tp 0, fp 0, fn 7, unscored 0)
  - intersection -> lazyImplementation
  - intersection -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> delete
  - lazyImplementation -> get
  - lazyImplementation -> lazyEmptyEvaluator
  - lazyImplementation -> set

## src/difference.ts  (tp 0, fp 0, fn 6, unscored 0)
  - difference -> lazyImplementation
  - difference -> purryFromLazy
  - lazyImplementation -> Map
  - lazyImplementation -> get
  - lazyImplementation -> lazyIdentityEvaluator
  - lazyImplementation -> set

## src/filter.ts  (tp 0, fp 0, fn 6, unscored 1)
  - filter -> filterImplementation
  - filter -> lazyImplementation
  - filter -> purry
  - filterImplementation -> filter
  - filterImplementation -> predicate
  - lazyImplementation -> predicate
  ~ __module__ -> filter

## src/flatMap.ts  (tp 0, fp 0, fn 6, unscored 0)
  - flatMap -> flatMapImplementation
  - flatMap -> lazyImplementation
  - flatMap -> purry
  - flatMapImplementation -> callbackfn
  - flatMapImplementation -> flatMap
  - lazyImplementation -> callbackfn

## src/forEach.ts  (tp 0, fp 0, fn 6, unscored 0)
  - forEach -> forEachImplementation
  - forEach -> lazyImplementation
  - forEach -> purry
  - forEachImplementation -> callbackfn
  - forEachImplementation -> forEach
  - lazyImplementation -> callbackfn

## src/map.ts  (tp 0, fp 0, fn 6, unscored 1)
  - lazyImplementation -> callbackfn
  - map -> lazyImplementation
  - map -> mapImplementation
  - map -> purry
  - mapImplementation -> callbackfn
  - mapImplementation -> map
  ~ __module__ -> map

## src/takeFirstBy.ts  (tp 0, fp 0, fn 6, unscored 1)
  - takeFirstBy -> purryOrderRulesWithArgument
  - takeFirstBy -> takeFirstByImplementation
  - takeFirstByImplementation -> compareFn
  - takeFirstByImplementation -> heapMaybeInsert
  - takeFirstByImplementation -> heapify
  - takeFirstByImplementation -> slice
  ~ __module__ -> takeFirstByImplementation

## src/uniqueBy.ts  (tp 0, fp 0, fn 6, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> brandedKeyFunction
  - lazyImplementation -> has
  - uniqueBy -> lazyImplementation
  - uniqueBy -> purryFromLazy

## src/drop.ts  (tp 0, fp 0, fn 5, unscored 1)
  - drop -> dropImplementation
  - drop -> lazyImplementation
  - drop -> purry
  - dropImplementation -> slice
  - lazyImplementation -> lazyIdentityEvaluator
  ~ __module__ -> drop

## src/dropWhile.ts  (tp 0, fp 0, fn 5, unscored 2)
  - dropWhile -> dropWhileImplementation
  - dropWhile -> purry
  - dropWhileImplementation -> entries
  - dropWhileImplementation -> predicate
  - dropWhileImplementation -> slice
  ~ __module__ -> dropWhile
  ~ __module__ -> dropWhileImplementation

## src/first.ts  (tp 0, fp 0, fn 5, unscored 2)
  - first -> firstImplementation
  - first -> lazyImplementation
  - first -> purry
  - first -> toSingle
  - lazyImplementation -> firstLazy
  ~ __module__ -> first
  ~ __module__ -> pipe

## src/internal/words.ts  (tp 0, fp 0, fn 5, unscored 0)
  - words -> flush
  - words -> has
  - words -> push
  - words -> slice
  - words -> test

## src/partition.ts  (tp 0, fp 0, fn 5, unscored 0)
  - partition -> partitionImplementation
  - partition -> purry
  - partitionImplementation -> entries
  - partitionImplementation -> predicate
  - partitionImplementation -> push

## src/pullObject.ts  (tp 0, fp 0, fn 5, unscored 0)
  - pullObject -> pullObjectImplementation
  - pullObject -> purry
  - pullObjectImplementation -> entries
  - pullObjectImplementation -> keyExtractor
  - pullObjectImplementation -> valueExtractor

## src/splitWhen.ts  (tp 0, fp 0, fn 5, unscored 0)
  - splitWhen -> purry
  - splitWhen -> splitWhenImplementation
  - splitWhenImplementation -> findIndex
  - splitWhenImplementation -> predicate
  - splitWhenImplementation -> slice

## src/sumBy.ts  (tp 0, fp 0, fn 5, unscored 0)
  - sumBy -> purry
  - sumBy -> sumByImplementation
  - sumByImplementation -> callbackfn
  - sumByImplementation -> entries
  - sumByImplementation -> next

## src/take.ts  (tp 0, fp 0, fn 5, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> lazyImplementation
  - take -> purry
  - take -> takeImplementation
  - takeImplementation -> slice

## src/takeWhile.ts  (tp 0, fp 0, fn 5, unscored 1)
  - takeWhile -> purry
  - takeWhile -> takeWhileImplementation
  - takeWhileImplementation -> entries
  - takeWhileImplementation -> predicate
  - takeWhileImplementation -> push
  ~ __module__ -> takeWhile

## src/toKebabCase.ts  (tp 0, fp 0, fn 5, unscored 0)
  - toKebabCase -> purry
  - toKebabCase -> toKebabCaseImplementation
  - toKebabCaseImplementation -> join
  - toKebabCaseImplementation -> toLowerCase
  - toKebabCaseImplementation -> words

## src/unique.ts  (tp 0, fp 0, fn 5, unscored 0)
  - lazyImplementation -> Set
  - lazyImplementation -> add
  - lazyImplementation -> has
  - unique -> lazyImplementation
  - unique -> purryFromLazy

## src/when.ts  (tp 0, fp 0, fn 5, unscored 1)
  - when -> whenImplementation
  - whenImplementation -> onFalse
  - whenImplementation -> onTrue
  - whenImplementation -> onTrueOrBranches
  - whenImplementation -> predicate
  ~ __module__ -> when

## src/capitalize.ts  (tp 0, fp 0, fn 4, unscored 0)
  - capitalize -> capitalizeImplementation
  - capitalize -> purry
  - capitalizeImplementation -> slice
  - capitalizeImplementation -> toUpperCase

## src/differenceWith.ts  (tp 0, fp 0, fn 4, unscored 0)
  - differenceWith -> lazyImplementation
  - differenceWith -> purryFromLazy
  - lazyImplementation -> every
  - lazyImplementation -> isEqual

## src/dropLastWhile.ts  (tp 0, fp 0, fn 4, unscored 2)
  - dropLastWhile -> dropLastWhileImplementation
  - dropLastWhile -> purry
  - dropLastWhileImplementation -> predicate
  - dropLastWhileImplementation -> slice
  ~ __module__ -> dropLastWhile
  ~ __module__ -> purry

## src/evolve.ts  (tp 0, fp 0, fn 4, unscored 0)
  - evolve -> evolveImplementation
  - evolve -> purry
  - evolveImplementation -> evolveImplementation
  - evolveImplementation -> value

## src/findIndex.ts  (tp 0, fp 0, fn 4, unscored 0)
  - findIndex -> findIndexImplementation
  - findIndex -> purry
  - findIndexImplementation -> findIndex
  - findIndexImplementation -> predicate

## src/fromKeys.ts  (tp 0, fp 0, fn 4, unscored 1)
  - fromKeys -> fromKeysImplementation
  - fromKeys -> purry
  - fromKeysImplementation -> entries
  - fromKeysImplementation -> mapper
  ~ __module__ -> fromKeys

## src/groupBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - groupBy -> groupByImplementation
  - groupBy -> purry
  - groupByImplementation -> callbackfn
  - groupByImplementation -> push

## src/indexBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - indexBy -> indexByImplementation
  - indexBy -> purry
  - indexByImplementation -> entries
  - indexByImplementation -> mapper

## src/internal/purryFromLazy.ts  (tp 0, fp 0, fn 4, unscored 1)
  - purryFromLazy -> Error
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  - purryFromLazy -> pipe
  ~ __module__ -> pipe

## src/last.ts  (tp 0, fp 1, fn 3, unscored 0)
  - last -> lastImplementation
  - last -> purry
  - lastImplementation -> at
  + last -> last

## src/meanBy.ts  (tp 0, fp 0, fn 4, unscored 1)
  - meanBy -> meanByImplementation
  - meanBy -> purry
  - meanByImplementation -> entries
  - meanByImplementation -> fn
  ~ __module__ -> meanBy

## src/median.ts  (tp 0, fp 0, fn 4, unscored 0)
  - median -> medianImplementation
  - median -> purry
  - medianImplementation -> numberComparator
  - medianImplementation -> sort

## src/nthBy.ts  (tp 0, fp 0, fn 4, unscored 1)
  - nthBy -> nthByImplementation
  - nthBy -> purryOrderRulesWithArgument
  - nthByImplementation -> compareFn
  - nthByImplementation -> quickSelect
  ~ __module__ -> nthBy

## src/randomString.ts  (tp 0, fp 0, fn 4, unscored 1)
  - randomString -> purry
  - randomString -> randomStringImplementation
  - randomStringImplementation -> join
  - randomStringImplementation -> push
  ~ __module__ -> randomString

## src/range.ts  (tp 0, fp 0, fn 4, unscored 0)
  - range -> purry
  - range -> rangeImplementation
  - rangeImplementation -> RangeError
  - rangeImplementation -> ceilingWithSnap

## src/reduce.ts  (tp 0, fp 0, fn 4, unscored 0)
  - reduce -> purry
  - reduce -> reduceImplementation
  - reduceImplementation -> callbackfn
  - reduceImplementation -> reduce

## src/sort.ts  (tp 0, fp 0, fn 4, unscored 1)
  - sort -> purry
  - sort -> sortImplementation
  - sortImplementation -> cmp
  - sortImplementation -> sort
  ~ __module__ -> sort

## src/sortBy.ts  (tp 0, fp 0, fn 4, unscored 0)
  - sortBy -> purryOrderRules
  - sortBy -> sortByImplementation
  - sortByImplementation -> compareFn
  - sortByImplementation -> sort

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

## src/stringToPath.ts  (tp 0, fp 0, fn 4, unscored 0)
  - stringToPath -> exec
  - stringToPath -> push
  - stringToPath -> stringToPath
  - stringToPath -> test

## src/swapIndices.ts  (tp 0, fp 0, fn 4, unscored 0)
  - swapIndices -> purry
  - swapIndices -> swapIndicesImplementation
  - swapIndicesImplementation -> join
  - swapIndicesImplementation -> swapArray

## src/takeLastWhile.ts  (tp 0, fp 0, fn 4, unscored 0)
  - takeLastWhile -> purry
  - takeLastWhile -> takeLastWhileImplementation
  - takeLastWhileImplementation -> predicate
  - takeLastWhileImplementation -> slice

## src/uncapitalize.ts  (tp 0, fp 0, fn 4, unscored 0)
  - uncapitalize -> purry
  - uncapitalize -> uncapitalizeImplementation
  - uncapitalizeImplementation -> slice
  - uncapitalizeImplementation -> toLowerCase

## src/zip.ts  (tp 0, fp 0, fn 4, unscored 1)
  - zip -> lazyImplementation
  - zip -> purry
  - zip -> zipImplementation
  - zipImplementation -> map
  ~ __module__ -> zip

## src/dropLast.ts  (tp 0, fp 0, fn 3, unscored 0)
  - dropLast -> dropLastImplementation
  - dropLast -> purry
  - dropLastImplementation -> slice

## src/endsWith.ts  (tp 0, fp 0, fn 3, unscored 0)
  - endsWith -> endsWithImplementation
  - endsWith -> purry
  - endsWithImplementation -> endsWith

## src/findLast.ts  (tp 0, fp 0, fn 3, unscored 0)
  - findLast -> findLastImplementation
  - findLast -> purry
  - findLastImplementation -> predicate

## src/findLastIndex.ts  (tp 0, fp 0, fn 3, unscored 0)
  - findLastIndex -> findLastIndexImplementation
  - findLastIndex -> purry
  - findLastIndexImplementation -> predicate

## src/groupByProp.ts  (tp 0, fp 0, fn 3, unscored 1)
  - groupByProp -> groupByPropImplementation
  - groupByProp -> purry
  - groupByPropImplementation -> push
  ~ __module__ -> groupByProp

## src/hasSubObject.ts  (tp 0, fp 0, fn 3, unscored 0)
  - hasSubObject -> hasSubObjectImplementation
  - hasSubObject -> purry
  - hasSubObjectImplementation -> isDeepEqual

## src/isIncludedIn.ts  (tp 0, fp 0, fn 3, unscored 0)
  - isIncludedIn -> Set
  - isIncludedIn -> has
  - isIncludedIn -> includes

## src/join.ts  (tp 0, fp 0, fn 3, unscored 1)
  - join -> joinImplementation
  - join -> purry
  - joinImplementation -> join
  ~ __module__ -> join

## src/mapKeys.ts  (tp 0, fp 0, fn 3, unscored 0)
  - mapKeys -> mapKeysImplementation
  - mapKeys -> purry
  - mapKeysImplementation -> keyMapper

## src/mapValues.ts  (tp 0, fp 0, fn 3, unscored 1)
  - mapValues -> mapValuesImplementation
  - mapValues -> purry
  - mapValuesImplementation -> valueMapper
  ~ __module__ -> mapValues

## src/omit.ts  (tp 0, fp 0, fn 3, unscored 0)
  - omit -> omitImplementation
  - omit -> purry
  - omitImplementation -> hasAtLeast

## src/omitBy.ts  (tp 0, fp 0, fn 3, unscored 0)
  - omitBy -> omitByImplementation
  - omitBy -> purry
  - omitByImplementation -> predicate

## src/purry.ts  (tp 0, fp 0, fn 3, unscored 0)
  - purry -> Error
  - purry -> fn
  - purry -> lazyDataLastImpl

## src/rankBy.ts  (tp 0, fp 0, fn 3, unscored 1)
  - rankBy -> purryOrderRulesWithArgument
  - rankBy -> rankByImplementation
  - rankByImplementation -> compareFn
  ~ __module__ -> rankBy

## src/setPath.ts  (tp 0, fp 0, fn 3, unscored 0)
  - setPath -> purry
  - setPath -> setPathImplementation
  - setPathImplementation -> setPathImplementation

## src/sortedIndex.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedIndex -> purry
  - sortedIndex -> sortedIndexImplementation
  - sortedIndexImplementation -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 0, fp 0, fn 3, unscored 0)
  - sortedLastIndex -> purry
  - sortedLastIndex -> sortedLastIndexImplementation
  - sortedLastIndexImplementation -> binarySearchCutoffIndex

## src/takeLast.ts  (tp 0, fp 0, fn 3, unscored 0)
  - takeLast -> purry
  - takeLast -> takeLastImplementation
  - takeLastImplementation -> slice

## src/times.ts  (tp 0, fp 0, fn 3, unscored 0)
  - times -> purry
  - times -> timesImplementation
  - timesImplementation -> fn

## src/toUpperCase.ts  (tp 0, fp 0, fn 3, unscored 0)
  - toUpperCase -> purry
  - toUpperCase -> toUpperCaseImplementation
  - toUpperCaseImplementation -> toUpperCase

## src/add.ts  (tp 0, fp 0, fn 2, unscored 0)
  - add -> addImplementation
  - add -> purry

## src/ceil.ts  (tp 0, fp 0, fn 2, unscored 3)
  - ceil -> purry
  - ceil -> withPrecision
  ~ __module__ -> ceil
  ~ __module__ -> purry
  ~ __module__ -> withPrecision

## src/concat.ts  (tp 0, fp 0, fn 2, unscored 1)
  - concat -> concatImplementation
  - concat -> purry
  ~ __module__ -> concat

## src/defaultTo.ts  (tp 0, fp 0, fn 2, unscored 0)
  - defaultTo -> defaultToImplementation
  - defaultTo -> purry

## src/divide.ts  (tp 0, fp 0, fn 2, unscored 3)
  - divide -> divideImplementation
  - divide -> purry
  ~ __module__ -> divide
  ~ __module__ -> map
  ~ __module__ -> reduce

## src/floor.ts  (tp 0, fp 0, fn 2, unscored 1)
  - floor -> purry
  - floor -> withPrecision
  ~ __module__ -> floor

## src/hasAtLeast.ts  (tp 0, fp 0, fn 2, unscored 0)
  - hasAtLeast -> hasAtLeastImplementation
  - hasAtLeast -> purry

## src/hasProp.ts  (tp 0, fp 0, fn 2, unscored 0)
  - hasProp -> hasPropImplementation
  - hasProp -> purry

## src/invert.ts  (tp 0, fp 0, fn 2, unscored 0)
  - invert -> invertImplementation
  - invert -> purry

## src/length.ts  (tp 0, fp 0, fn 2, unscored 0)
  - length -> lengthImplementation
  - length -> purry

## src/merge.ts  (tp 0, fp 0, fn 2, unscored 1)
  - merge -> mergeImplementation
  - merge -> purry
  ~ __module__ -> merge

## src/objOf.ts  (tp 0, fp 0, fn 2, unscored 0)
  - objOf -> objOfImplementation
  - objOf -> purry

## src/only.ts  (tp 0, fp 0, fn 2, unscored 0)
  - only -> onlyImplementation
  - only -> purry

## src/pathOr.ts  (tp 0, fp 0, fn 2, unscored 1)
  - pathOr -> pathOrImplementation
  - pathOr -> purry
  ~ __module__ -> pathOr

## src/pick.ts  (tp 0, fp 0, fn 2, unscored 1)
  - pick -> pickImplementation
  - pick -> purry
  ~ __module__ -> pick

## src/product.ts  (tp 0, fp 0, fn 2, unscored 1)
  - product -> productImplementation
  - product -> purry
  ~ __module__ -> product

## src/randomInteger.ts  (tp 0, fp 0, fn 2, unscored 1)
  - randomInteger -> RangeError
  - randomInteger -> toString
  ~ __module__ -> randomInteger

## src/round.ts  (tp 0, fp 0, fn 2, unscored 3)
  - round -> purry
  - round -> withPrecision
  ~ __module__ -> purry
  ~ __module__ -> round
  ~ __module__ -> withPrecision

## src/set.ts  (tp 0, fp 0, fn 2, unscored 2)
  - set -> purry
  - set -> setImplementation
  ~ __module__ -> pipe
  ~ __module__ -> set

## src/sortedIndexWith.ts  (tp 0, fp 0, fn 2, unscored 0)
  - sortedIndexWith -> binarySearchCutoffIndex
  - sortedIndexWith -> purry

## src/sum.ts  (tp 0, fp 0, fn 2, unscored 1)
  - sum -> purry
  - sum -> sumImplementation
  ~ __module__ -> sum

## src/swapProps.ts  (tp 0, fp 0, fn 2, unscored 1)
  - swapProps -> purry
  - swapProps -> swapPropsImplementation
  ~ __module__ -> swapProps

## src/fromEntries.ts  (tp 0, fp 0, fn 1, unscored 1)
  - fromEntries -> purry
  ~ __module__ -> fromEntries

## src/internal/binarySearchCutoffIndex.ts  (tp 0, fp 0, fn 1, unscored 1)
  - binarySearchCutoffIndex -> predicate
  ~ __module__ -> binarySearchCutoffIndex

## src/keys.ts  (tp 0, fp 0, fn 1, unscored 0)
  - keys -> purry

## src/partialLastBind.ts  (tp 0, fp 0, fn 1, unscored 0)
  - partialLastBind -> func

## src/piped.ts  (tp 0, fp 0, fn 1, unscored 0)
  - piped -> pipe

## src/prop.ts  (tp 0, fp 0, fn 1, unscored 1)
  - prop -> propImplementation
  ~ __module__ -> prop

## src/sliceString.ts  (tp 0, fp 0, fn 1, unscored 0)
  - sliceString -> slice

## src/split.ts  (tp 0, fp 0, fn 1, unscored 1)
  - split -> split
  ~ __module__ -> split

## src/values.ts  (tp 0, fp 0, fn 1, unscored 0)
  - values -> purry

## src/isEmpty.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ __module__ -> isEmpty

2 of 112 files exactly right.
