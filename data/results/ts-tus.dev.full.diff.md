# ts-tus / dev / cut=full

raw 7/7 (100.0%)  ·  fence-stripped 7/7 (100.0%)  ·  schema 7/7 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 94.2% [89.4% to 97.2%]   F1 97.0% [94.4% to 98.6%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored, this cut excludes the class, so it counts against neither side

## src/lockers/MemoryLocker.ts  (tp 22, fp 0, fn 4, unscored 4)
  - acquireLock -> reject
  - acquireLock -> resolve
  - lock -> onAbort
  - waitTimeout -> abortListener
  ~ __module__ -> Map
  ~ acquireLock -> Promise
  ~ lock -> race
  ~ waitTimeout -> Promise

## src/server.ts  (tp 43, fp 0, fn 3, unscored 6)
  - createContext -> onDelayedAbort
  - get -> handler
  - handler -> onError
  ~ __module__ -> debug
  ~ handle -> NodeRequest
  ~ handle -> sendNodeResponse
  ~ listen -> createServer
  ~ listen -> listen
  ~ write -> String

## src/handlers/BaseHandler.ts  (tp 36, fp 0, fn 2, unscored 8)
  - writeToStore -> onAbort
  - writeToStore -> resolve
  ~ calculateMaxBodySize -> parseInt
  ~ writeToStore -> PassThrough
  ~ writeToStore -> Promise
  ~ writeToStore -> StreamLimiter
  ~ writeToStore -> from
  ~ writeToStore -> fromWeb
  ~ writeToStore -> pipeline
  ~ writeToStore -> throttle

## src/handlers/GetHandler.ts  (tp 19, fp 0, fn 1, unscored 2)
  - registerPath -> handler
  ~ __module__ -> Map
  ~ __module__ -> Set

## src/handlers/HeadHandler.ts  (tp 12, fp 0, fn 0, unscored 2)
  ~ send -> Date
  ~ send -> stringify

## src/handlers/PostHandler.ts  (tp 27, fp 0, fn 0, unscored 7)
  ~ __module__ -> debug
  ~ send -> Date
  ~ send -> Upload
  ~ send -> assign
  ~ send -> fromEntries
  ~ send -> parse
  ~ send -> parseInt

## src/validators/HeaderValidator.ts  (tp 3, fp 0, fn 0, unscored 7)
  ~ __module__ -> Map
  ~ __module__ -> Number
  ~ __module__ -> String
  ~ __module__ -> includes
  ~ __module__ -> isInteger
  ~ __module__ -> parse
  ~ __module__ -> startsWith

3 of 7 files exactly right.
