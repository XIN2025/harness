# ts-ink / dev / cut=calls_only

raw 26/26 (100.0%)  ·  fence-stripped 26/26 (100.0%)  ·  schema 26/26 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 100.0% [100.0% to 100.0%] (percentile)   F1 100.0% [100.0% to 100.0%] (percentile)

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## src/colorize.ts  (tp 5, fp 0, fn 0, unscored 7)
  ~ colorize -> Number
  ~ colorize -> ansi256
  ~ colorize -> bgAnsi256
  ~ colorize -> bgHex
  ~ colorize -> bgRgb
  ~ colorize -> hex
  ~ colorize -> rgb

## src/components/ErrorOverview.tsx  (tp 10, fp 0, fn 0, unscored 9)
  ~ ErrorOverview -> String
  ~ ErrorOverview -> codeExcerpt
  ~ ErrorOverview -> existsSync
  ~ ErrorOverview -> max
  ~ ErrorOverview -> readFileSync
  ~ __module__ -> StackUtils
  ~ __module__ -> cwd
  ~ __module__ -> nodeInternals
  ~ cleanupPath -> cwd

## src/components/Text.tsx  (tp 1, fp 0, fn 0, unscored 7)
  ~ Text -> bold
  ~ Text -> dim
  ~ Text -> inverse
  ~ Text -> italic
  ~ Text -> strikethrough
  ~ Text -> underline
  ~ Text -> useContext

## src/cursor-helpers.ts  (tp 3, fp 0, fn 0, unscored 4)
  ~ buildCursorSuffix -> cursorTo
  ~ buildCursorSuffix -> cursorUp
  ~ buildReturnToBottom -> cursorDown
  ~ buildReturnToBottom -> cursorTo

## src/devtools.ts  (tp 6, fp 0, fn 0, unscored 6)
  ~ __module__ -> connectToDevTools
  ~ __module__ -> initialize
  ~ __module__ -> isDevToolsReachable
  ~ __module__ -> warn
  ~ isDevToolsReachable -> Promise
  ~ isDevToolsReachable -> WebSocket

## src/dom.ts  (tp 34, fp 0, fn 0, unscored 2)
  ~ createNode -> create
  ~ setTextNodeValue -> String

## src/hooks/use-animation.ts  (tp 4, fp 0, fn 0, unscored 9)
  ~ normalizeAnimationInterval -> isFinite
  ~ normalizeAnimationInterval -> max
  ~ normalizeAnimationInterval -> min
  ~ useAnimation -> floor
  ~ useAnimation -> useCallback
  ~ useAnimation -> useContext
  ~ useAnimation -> useLayoutEffect
  ~ useAnimation -> useRef
  ~ useAnimation -> useState

## src/hooks/use-cursor.ts  (tp 1, fp 0, fn 0, unscored 4)
  ~ useCursor -> useCallback
  ~ useCursor -> useContext
  ~ useCursor -> useInsertionEffect
  ~ useCursor -> useRef

## src/hooks/use-focus-manager.ts  (tp 0, fp 0, fn 0, unscored 1)
  ~ useFocusManager -> useContext

## src/hooks/use-focus.ts  (tp 6, fp 0, fn 0, unscored 7)
  ~ useFocus -> Boolean
  ~ useFocus -> random
  ~ useFocus -> slice
  ~ useFocus -> toString
  ~ useFocus -> useContext
  ~ useFocus -> useEffect
  ~ useFocus -> useMemo

## src/hooks/use-input.ts  (tp 11, fp 0, fn 0, unscored 2)
  ~ useInput -> useEffect
  ~ useInput -> useEffectEvent

## src/hooks/use-paste.ts  (tp 7, fp 0, fn 0, unscored 2)
  ~ usePaste -> useEffect
  ~ usePaste -> useEffectEvent

## src/hooks/use-window-size.ts  (tp 5, fp 0, fn 0, unscored 2)
  ~ useWindowSize -> useEffect
  ~ useWindowSize -> useState

## src/measure-text.ts  (tp 3, fp 0, fn 0, unscored 2)
  ~ __module__ -> Map
  ~ measureText -> widestLine

## src/reconciler.ts  (tp 32, fp 0, fn 0, unscored 10)
  ~ __module__ -> createContext
  ~ __module__ -> createReconciler
  ~ __module__ -> loadPackageJson
  ~ __module__ -> resolve
  ~ __module__ -> warn
  ~ commitUpdate -> entries
  ~ createInstance -> entries
  ~ diff -> hasOwn
  ~ diff -> keys
  ~ loadPackageJson -> parse

## src/render-border.ts  (tp 6, fp 0, fn 0, unscored 1)
  ~ stylePiece -> dim

## src/render-node-to-output.ts  (tp 26, fp 0, fn 0, unscored 3)
  ~ applyPaddingToText -> indentString
  ~ renderNodeToOutput -> widestLine
  ~ renderNodeToScreenReaderOutput -> keys

## src/render-to-string.ts  (tp 12, fp 0, fn 0, unscored 1)
  ~ renderToString -> String

## src/render.ts  (tp 8, fp 0, fn 0, unscored 1)
  ~ getInstance -> write

## src/wrap-text.ts  (tp 1, fp 0, fn 0, unscored 3)
  ~ wrapText -> String
  ~ wrapText -> cliTruncate
  ~ wrapText -> wrapAnsi

26 of 26 files exactly right.
