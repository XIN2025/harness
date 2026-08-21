# treesitter / dev / cut=full

raw 112/112 (100.0%)  ·  fence-stripped 112/112 (100.0%)  ·  schema 112/112 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 72.7% [69.1% to 76.6%]   F1 84.2% [81.8% to 86.7%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/pipe.ts  (tp 13, fp 0, fn 4, unscored 1)
  - pipe -> lazyOp
  - pipe -> op
  - prepareLazyFunction -> fn
  - prepareLazyFunction -> func
  ~ prepareLazyFunction -> assign

## src/drop.ts  (tp 2, fp 0, fn 3, unscored 0)
  - drop -> dropImplementation
  - drop -> lazyImplementation
  - lazyImplementation -> lazyIdentityEvaluator

## src/filter.ts  (tp 3, fp 0, fn 3, unscored 0)
  - filter -> filterImplementation
  - filter -> lazyImplementation
  - filterImplementation -> predicate

## src/first.ts  (tp 2, fp 0, fn 3, unscored 0)
  - first -> firstImplementation
  - first -> lazyImplementation
  - lazyImplementation -> firstLazy

## src/flatMap.ts  (tp 3, fp 0, fn 3, unscored 1)
  - flatMap -> flatMapImplementation
  - flatMap -> lazyImplementation
  - flatMapImplementation -> callbackfn
  ~ lazyImplementation -> isArray

## src/forEach.ts  (tp 3, fp 0, fn 3, unscored 0)
  - forEach -> forEachImplementation
  - forEach -> lazyImplementation
  - forEachImplementation -> callbackfn

## src/internal/purryOrderRules.ts  (tp 10, fp 0, fn 3, unscored 1)
  - orderRuleComparer -> primaryRule
  - purryOrderRules -> compareFn
  - purryOrderRules -> isOrderRule
  ~ isOrderRule -> isArray

## src/map.ts  (tp 3, fp 0, fn 3, unscored 0)
  - map -> lazyImplementation
  - map -> mapImplementation
  - mapImplementation -> callbackfn

## src/take.ts  (tp 2, fp 0, fn 3, unscored 0)
  - lazyImplementation -> lazyEmptyEvaluator
  - take -> lazyImplementation
  - take -> takeImplementation

## src/zipWith.ts  (tp 5, fp 0, fn 3, unscored 0)
  - zipWith -> arg0
  - zipWith -> arg1
  - zipWith -> lazyImplementation

## src/difference.ts  (tp 4, fp 0, fn 2, unscored 0)
  - difference -> lazyImplementation
  - lazyImplementation -> lazyIdentityEvaluator

## src/dropFirstBy.ts  (tp 5, fp 0, fn 2, unscored 0)
  - dropFirstBy -> dropFirstByImplementation
  - dropFirstByImplementation -> compareFn

## src/findIndex.ts  (tp 2, fp 0, fn 2, unscored 0)
  - findIndex -> findIndexImplementation
  - findIndexImplementation -> predicate

## src/internal/purryFromLazy.ts  (tp 2, fp 0, fn 2, unscored 1)
  - purryFromLazy -> dataLast
  - purryFromLazy -> lazy
  ~ purryFromLazy -> assign

## src/internal/quickSelect.ts  (tp 5, fp 0, fn 2, unscored 0)
  - quickSelect -> compareFn
  - quickSelectImplementation -> compareFn

## src/intersection.ts  (tp 5, fp 0, fn 2, unscored 0)
  - intersection -> lazyImplementation
  - lazyImplementation -> lazyEmptyEvaluator

## src/median.ts  (tp 2, fp 0, fn 2, unscored 0)
  - median -> medianImplementation
  - medianImplementation -> numberComparator

## src/nthBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - nthBy -> nthByImplementation
  - nthByImplementation -> compareFn

## src/reduce.ts  (tp 2, fp 0, fn 2, unscored 0)
  - reduce -> reduceImplementation
  - reduceImplementation -> callbackfn

## src/sort.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sort -> sortImplementation
  - sortImplementation -> cmp

## src/sortBy.ts  (tp 2, fp 0, fn 2, unscored 0)
  - sortBy -> sortByImplementation
  - sortByImplementation -> compareFn

## src/splitWhen.ts  (tp 3, fp 0, fn 2, unscored 0)
  - splitWhen -> splitWhenImplementation
  - splitWhenImplementation -> predicate

## src/takeFirstBy.ts  (tp 4, fp 0, fn 2, unscored 0)
  - takeFirstBy -> takeFirstByImplementation
  - takeFirstByImplementation -> compareFn

## src/zip.ts  (tp 2, fp 0, fn 2, unscored 0)
  - zip -> lazyImplementation
  - zip -> zipImplementation

## src/add.ts  (tp 1, fp 0, fn 1, unscored 0)
  - add -> addImplementation

## src/capitalize.ts  (tp 3, fp 0, fn 1, unscored 0)
  - capitalize -> capitalizeImplementation

## src/clone.ts  (tp 11, fp 0, fn 1, unscored 3)
  - clone -> cloneImplementation
  ~ cloneImplementation -> getPrototypeOf
  ~ cloneImplementation -> isArray
  ~ deepCloneObject -> entries

## src/concat.ts  (tp 1, fp 0, fn 1, unscored 0)
  - concat -> concatImplementation

## src/countBy.ts  (tp 6, fp 0, fn 1, unscored 1)
  - countBy -> countByImplementation
  ~ countByImplementation -> fromEntries

## src/defaultTo.ts  (tp 1, fp 0, fn 1, unscored 0)
  - defaultTo -> defaultToImplementation

## src/differenceWith.ts  (tp 3, fp 0, fn 1, unscored 0)
  - differenceWith -> lazyImplementation

## src/divide.ts  (tp 1, fp 0, fn 1, unscored 0)
  - divide -> divideImplementation

## src/dropLast.ts  (tp 2, fp 0, fn 1, unscored 1)
  - dropLast -> dropLastImplementation
  ~ dropLastImplementation -> max

## src/dropLastWhile.ts  (tp 3, fp 0, fn 1, unscored 0)
  - dropLastWhile -> dropLastWhileImplementation

## src/dropWhile.ts  (tp 4, fp 0, fn 1, unscored 0)
  - dropWhile -> dropWhileImplementation

## src/endsWith.ts  (tp 2, fp 0, fn 1, unscored 0)
  - endsWith -> endsWithImplementation

## src/evolve.ts  (tp 3, fp 0, fn 1, unscored 1)
  - evolve -> evolveImplementation
  ~ evolveImplementation -> entries

## src/findLast.ts  (tp 2, fp 0, fn 1, unscored 0)
  - findLast -> findLastImplementation

## src/findLastIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - findLastIndex -> findLastIndexImplementation

## src/fromKeys.ts  (tp 3, fp 0, fn 1, unscored 0)
  - fromKeys -> fromKeysImplementation

## src/funnel.ts  (tp 7, fp 0, fn 1, unscored 4)
  - funnel -> voidReducer
  ~ __module__ -> Symbol
  ~ funnel -> max
  ~ funnel -> min
  ~ funnel -> now

## src/groupBy.ts  (tp 3, fp 0, fn 1, unscored 2)
  - groupBy -> groupByImplementation
  ~ groupByImplementation -> create
  ~ groupByImplementation -> setPrototypeOf

## src/groupByProp.ts  (tp 2, fp 0, fn 1, unscored 2)
  - groupByProp -> groupByPropImplementation
  ~ groupByPropImplementation -> create
  ~ groupByPropImplementation -> setPrototypeOf

## src/hasAtLeast.ts  (tp 1, fp 0, fn 1, unscored 0)
  - hasAtLeast -> hasAtLeastImplementation

## src/hasProp.ts  (tp 1, fp 0, fn 1, unscored 1)
  - hasProp -> hasPropImplementation
  ~ hasPropImplementation -> hasOwn

## src/hasSubObject.ts  (tp 2, fp 0, fn 1, unscored 2)
  - hasSubObject -> hasSubObjectImplementation
  ~ hasSubObjectImplementation -> entries
  ~ hasSubObjectImplementation -> hasOwn

## src/indexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - indexBy -> indexByImplementation

## src/invert.ts  (tp 1, fp 0, fn 1, unscored 1)
  - invert -> invertImplementation
  ~ invertImplementation -> entries

## src/isDeepEqual.ts  (tp 17, fp 0, fn 1, unscored 5)
  - isDeepEqual -> isDeepEqualImplementation
  ~ isComparablePrototype -> getPrototypeOf
  ~ isDeepEqualImplementation -> entries
  ~ isDeepEqualImplementation -> is
  ~ isDeepEqualImplementation -> isArray
  ~ isDeepEqualImplementation -> keys

## src/join.ts  (tp 2, fp 0, fn 1, unscored 0)
  - join -> joinImplementation

## src/last.ts  (tp 2, fp 0, fn 1, unscored 0)
  - last -> lastImplementation

## src/length.ts  (tp 1, fp 0, fn 1, unscored 0)
  - length -> lengthImplementation

## src/mapKeys.ts  (tp 2, fp 0, fn 1, unscored 1)
  - mapKeys -> mapKeysImplementation
  ~ mapKeysImplementation -> entries

## src/mapValues.ts  (tp 2, fp 0, fn 1, unscored 1)
  - mapValues -> mapValuesImplementation
  ~ mapValuesImplementation -> entries

## src/meanBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - meanBy -> meanByImplementation

## src/merge.ts  (tp 1, fp 0, fn 1, unscored 0)
  - merge -> mergeImplementation

## src/objOf.ts  (tp 1, fp 0, fn 1, unscored 0)
  - objOf -> objOfImplementation

## src/omit.ts  (tp 2, fp 0, fn 1, unscored 0)
  - omit -> omitImplementation

## src/omitBy.ts  (tp 2, fp 0, fn 1, unscored 1)
  - omitBy -> omitByImplementation
  ~ omitByImplementation -> entries

## src/only.ts  (tp 1, fp 0, fn 1, unscored 0)
  - only -> onlyImplementation

## src/partition.ts  (tp 4, fp 0, fn 1, unscored 0)
  - partition -> partitionImplementation

## src/pathOr.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pathOr -> pathOrImplementation

## src/pick.ts  (tp 1, fp 0, fn 1, unscored 0)
  - pick -> pickImplementation

## src/product.ts  (tp 1, fp 0, fn 1, unscored 0)
  - product -> productImplementation

## src/pullObject.ts  (tp 4, fp 0, fn 1, unscored 0)
  - pullObject -> pullObjectImplementation

## src/randomString.ts  (tp 3, fp 0, fn 1, unscored 2)
  - randomString -> randomStringImplementation
  ~ randomStringImplementation -> floor
  ~ randomStringImplementation -> random

## src/range.ts  (tp 3, fp 0, fn 1, unscored 4)
  - range -> rangeImplementation
  ~ ceilingWithSnap -> abs
  ~ ceilingWithSnap -> ceil
  ~ ceilingWithSnap -> round
  ~ rangeImplementation -> from

## src/rankBy.ts  (tp 2, fp 0, fn 1, unscored 0)
  - rankBy -> rankByImplementation

## src/sample.ts  (tp 7, fp 0, fn 1, unscored 3)
  - sample -> sampleImplementation
  ~ sampleImplementation -> floor
  ~ sampleImplementation -> min
  ~ sampleImplementation -> random

## src/set.ts  (tp 1, fp 0, fn 1, unscored 0)
  - set -> setImplementation

## src/setPath.ts  (tp 2, fp 0, fn 1, unscored 1)
  - setPath -> setPathImplementation
  ~ setPathImplementation -> isArray

## src/sortedIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedIndex -> sortedIndexImplementation

## src/sortedIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedIndexBy -> sortedIndexByImplementation

## src/sortedIndexWith.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sortedIndexWith -> binarySearchCutoffIndex

## src/sortedLastIndex.ts  (tp 2, fp 0, fn 1, unscored 0)
  - sortedLastIndex -> sortedLastIndexImplementation

## src/sortedLastIndexBy.ts  (tp 3, fp 0, fn 1, unscored 0)
  - sortedLastIndexBy -> sortedLastIndexByImplementation

## src/sum.ts  (tp 1, fp 0, fn 1, unscored 0)
  - sum -> sumImplementation

## src/sumBy.ts  (tp 4, fp 0, fn 1, unscored 0)
  - sumBy -> sumByImplementation

## src/swapIndices.ts  (tp 3, fp 0, fn 1, unscored 1)
  - swapIndices -> swapIndicesImplementation
  ~ swapArray -> isNaN

## src/swapProps.ts  (tp 1, fp 0, fn 1, unscored 0)
  - swapProps -> swapPropsImplementation

## src/takeLast.ts  (tp 2, fp 0, fn 1, unscored 1)
  - takeLast -> takeLastImplementation
  ~ takeLastImplementation -> max

## src/takeLastWhile.ts  (tp 3, fp 0, fn 1, unscored 0)
  - takeLastWhile -> takeLastWhileImplementation

## src/takeWhile.ts  (tp 4, fp 0, fn 1, unscored 0)
  - takeWhile -> takeWhileImplementation

## src/times.ts  (tp 2, fp 0, fn 1, unscored 3)
  - times -> timesImplementation
  ~ timesImplementation -> Array
  ~ timesImplementation -> floor
  ~ timesImplementation -> isInteger

## src/toKebabCase.ts  (tp 4, fp 0, fn 1, unscored 0)
  - toKebabCase -> toKebabCaseImplementation

## src/toUpperCase.ts  (tp 2, fp 0, fn 1, unscored 0)
  - toUpperCase -> toUpperCaseImplementation

## src/uncapitalize.ts  (tp 3, fp 0, fn 1, unscored 0)
  - uncapitalize -> uncapitalizeImplementation

## src/unique.ts  (tp 4, fp 0, fn 1, unscored 0)
  - unique -> lazyImplementation

## src/uniqueBy.ts  (tp 5, fp 0, fn 1, unscored 0)
  - uniqueBy -> lazyImplementation

## src/internal/withPrecision.ts  (tp 7, fp 0, fn 0, unscored 5)
  ~ shiftDecimalPoint -> parseFloat
  ~ shiftDecimalPoint -> parseInt
  ~ withPrecision -> isFinite
  ~ withPrecision -> isInteger
  ~ withPrecision -> isNaN

## src/internal/words.ts  (tp 5, fp 0, fn 0, unscored 1)
  ~ __module__ -> Set

## src/isEmpty.ts  (tp 0, fp 0, fn 0, unscored 2)
  ~ isEmpty -> isArray
  ~ isEmpty -> keys

## src/isPlainObject.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ isPlainObject -> getPrototypeOf

## src/randomInteger.ts  (tp 2, fp 0, fn 0, unscored 3)
  ~ randomInteger -> ceil
  ~ randomInteger -> floor
  ~ randomInteger -> random

## src/stringToPath.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ stringToPath -> Number

23 of 112 files exactly right.
