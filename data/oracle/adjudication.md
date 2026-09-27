# Oracle adjudication sheet

Mark each row `Y` (a real call or callable reference) or `N`.
Check against the quoted source line; `kind` is the oracle's claim, not a hint.

Selection: the first 60 edges under SHA-256 ranking of the 534 eligible oracle edges.
Public seed: `oracle-adjudication-v1`.
Frozen test-split files excluded: 38.

Adjudicated on 2026-08-24 without consulting arm predictions or test scores.
Result: 60 Y, 0 N, 0 incomplete. Zero-error rule-of-three lower bound: 95.0%.
Scope: precision on this deterministic non-test Remeda edge sample; not oracle recall or cross-repository generalization.

## src/clone.ts  (3 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 42 | `clone` | `purry` | free | `return purry(cloneImplementation, args);` |
| Y | 62 | `cloneImplementation` | `getPrototypeOf` | static | `const prototype = Object.getPrototypeOf(value);` |
| Y | 86 | `cloneImplementation` | `push` | method | `refFrom.push(value);` |

## src/defaultTo.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 62 | `defaultTo` | `defaultToImplementation` | callable_ref | `return purry(defaultToImplementation, args);` |

## src/divide.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 35 | `divide` | `purry` | free | `return purry(divideImplementation, args);` |

## src/dropFirstBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 69 | `dropFirstByImplementation` | `compareFn` | callable_ref | `heapify(heap, compareFn);` |

## src/dropLastWhile.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 49 | `dropLastWhileImplementation` | `predicate` | free | `if (!predicate(data[i], i, data)) {` |

## src/dropWhile.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 41 | `dropWhile` | `dropWhileImplementation` | callable_ref | `return purry(dropWhileImplementation, args);` |

## src/evolve.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 134 | `evolve` | `evolveImplementation` | callable_ref | `return purry(evolveImplementation, args);` |
| Y | 148 | `evolveImplementation` | `value` | free | `? value(out[key])` |

## src/filter.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 101 | `filter` | `purry` | free | `return purry(filterImplementation, args, lazyImplementation);` |

## src/findLast.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 85 | `findLastImplementation` | `predicate` | free | `if (predicate(item, i, data)) {` |

## src/flatMap.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 74 | `lazyImplementation` | `isArray` | static | `return Array.isArray(next)` |

## src/fromKeys.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 87 | `fromKeysImplementation` | `mapper` | free | `result[key] = mapper(key, index, data);` |

## src/funnel.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 289 | `funnel` | `invoke` | free | `invoke();` |

## src/groupBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 74 | `groupBy` | `groupByImplementation` | callable_ref | `return purry(groupByImplementation, args);` |

## src/indexBy.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 56 | `indexBy` | `indexByImplementation` | callable_ref | `return purry(indexByImplementation, args);` |
| Y | 66 | `indexByImplementation` | `mapper` | free | `const key = mapper(item, index, data);` |

## src/internal/lazyDataLastImpl.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 27 | `lazyDataLastImpl` | `assign` | static | `: Object.assign(dataLast, { lazy, lazyArgs: args });` |

## src/internal/purryOrderRules.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 89 | `purryOrderRules` | `orderRuleComparer` | free | `const compareFn = orderRuleComparer(dataOrRule, ...rules);` |
| Y | 152 | `orderRuleComparer` | `nextComparer` | free | `return nextComparer?.(a, b) ?? 0;` |

## src/internal/withPrecision.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 45 | `shiftDecimalPoint` | `split` | method | `const [n, exponent] = asString.split("e");` |

## src/internal/words.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 81 | `words` | `flush` | free | `flush();` |

## src/isDeepEqual.ts  (3 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 151 | `isDeepEqualImplementation` | `isDeepEqualImplementation` | free | `!isDeepEqualImplementation(` |
| Y | 190 | `isDeepEqualArrays` | `isDeepEqualImplementation` | free | `if (!isDeepEqualImplementation(item, other[index])) {` |
| Y | 237 | `isDeepEqualSets` | `isDeepEqualImplementation` | free | `if (isDeepEqualImplementation(dataItem, otherItem)) {` |

## src/isEmpty.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 64 | `isEmpty` | `keys` | static | `return Object.keys(data).length === 0;` |

## src/map.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 53 | `map` | `mapImplementation` | callable_ref | `return purry(mapImplementation, args, lazyImplementation);` |

## src/nthBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 53 | `nthBy` | `nthByImplementation` | callable_ref | `return purryOrderRulesWithArgument(nthByImplementation, args);` |

## src/omit.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 143 | `omitImplementation` | `hasAtLeast` | free | `if (!hasAtLeast(keys, 2)) {` |

## src/omitBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 175 | `omitByImplementation` | `entries` | static | `for (const [key, value] of Object.entries(out)) {` |

## src/only.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 44 | `only` | `purry` | free | `return purry(onlyImplementation, args);` |

## src/pipe.ts  (4 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 290 | `pipe` | `map` | method | `const lazyFunctions = functions.map((op) =>` |
| Y | 291 | `pipe` | `prepareLazyFunction` | free | `"lazy" in op ? prepareLazyFunction(op) : undefined,` |
| Y | 357 | `processItem` | `processItem` | free | `const subResult = processItem(` |
| Y | 388 | `prepareLazyFunction` | `assign` | static | `return Object.assign(fn, {` |

## src/randomInteger.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 56 | `randomInteger` | `toString` | method | ``randomInteger: The range [${from.toString()},${to.toString()}] contains no inte` |

## src/rankBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 65 | `rankByImplementation` | `compareFn` | free | `if (compareFn(targetItem, item) > 0) {` |

## src/setPath.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 97 | `setPathImplementation` | `isArray` | static | `if (Array.isArray(data)) {` |

## src/sortedIndexBy.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 88 | `sortedIndexBy` | `sortedIndexByImplementation` | callable_ref | `return purry(sortedIndexByImplementation, args);` |
| Y | 101 | `sortedIndexByImplementation` | `binarySearchCutoffIndex` | free | `return binarySearchCutoffIndex(` |

## src/split.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 111 | `split` | `split` | method | `(dataOrSeparator as string).split(separatorOrLimit, limit);` |

## src/splitWhen.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 36 | `splitWhen` | `purry` | free | `return purry(splitWhenImplementation, args);` |
| Y | 43 | `splitWhenImplementation` | `findIndex` | method | `const index = data.findIndex(predicate);` |

## src/sum.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 69 | `sum` | `purry` | free | `return purry(sumImplementation, args);` |

## src/sumBy.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 91 | `sumByImplementation` | `entries` | method | `const iter = array.entries();` |

## src/swapIndices.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 148 | `swapIndices` | `purry` | free | `return purry(swapIndicesImplementation, args);` |

## src/swapProps.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 47 | `swapProps` | `purry` | free | `return purry(swapPropsImplementation, args);` |

## src/take.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 61 | `lazyImplementation` | `lazyEmptyEvaluator` | callable_ref | `return lazyEmptyEvaluator;` |

## src/takeFirstBy.ts  (2 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 52 | `takeFirstBy` | `takeFirstByImplementation` | callable_ref | `return purryOrderRulesWithArgument(takeFirstByImplementation, args);` |
| Y | 69 | `takeFirstByImplementation` | `heapify` | free | `heapify(heap, compareFn);` |

## src/takeWhile.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 52 | `takeWhileImplementation` | `entries` | method | `for (const [index, item] of data.entries()) {` |

## src/toKebabCase.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 73 | `toKebabCaseImplementation` | `toLowerCase` | method | `words(data).join("-").toLowerCase();` |

## src/toTitleCase.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 139 | `toTitleCaseImplementation` | `test` | static | `LOWER_CASE_CHARACTER_RE.test(data)` |

## src/toUpperCase.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 53 | `toUpperCase` | `toUpperCaseImplementation` | callable_ref | `return purry(toUpperCaseImplementation, args);` |

## src/uncapitalize.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 53 | `uncapitalize` | `purry` | free | `return purry(uncapitalizeImplementation, args);` |

## src/unique.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 50 | `lazyImplementation` | `add` | method | `set.add(value);` |

## src/values.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 42 | `values` | `purry` | free | `return purry(Object.values, args);` |

## src/when.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 148 | `when` | `whenImplementation` | free | `whenImplementation(...args);` |

## src/zipWith.ts  (1 edges)

| Y/N | line | caller | callee | kind | source line |
|---|---|---|---|---|---|
| Y | 96 | `zipWith` | `zipWithImplementation` | free | `return zipWithImplementation(arg0, arg1!, arg2!);` |

