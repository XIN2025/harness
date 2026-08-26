# ts-nest / dev / cut=full

raw 43/43 (100.0%)  ·  fence-stripped 43/43 (100.0%)  ·  schema 43/43 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 95.1% [90.6% to 98.0%]   F1 97.5% [95.1% to 99.0%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored, this cut excludes the class, so it counts against neither side

## pipes/validation.pipe.ts  (tp 34, fp 0, fn 6, unscored 8)
  - toValidate -> Array
  - toValidate -> Boolean
  - toValidate -> Date
  - toValidate -> Number
  - toValidate -> Object
  - toValidate -> String
  ~ __module__ -> Injectable
  ~ flattenValidationErrors -> iterate
  ~ flattenValidationErrors -> values
  ~ stripProtoKeys -> isArray
  ~ stripProtoKeys -> isTypedArray
  ~ toValidate -> some
  ~ transform -> keys
  ~ transformPrimitive -> String

## pipes/parse-array.pipe.ts  (tp 19, fp 0, fn 3, unscored 4)
  - isExpectedTypePrimitive -> Boolean
  - isExpectedTypePrimitive -> Number
  - isExpectedTypePrimitive -> String
  ~ __module__ -> Injectable
  ~ transform -> all
  ~ transform -> isArray
  ~ transform -> parse

## decorators/core/exception-filters.decorator.ts  (tp 4, fp 0, fn 1, unscored 0)
  - addExceptionFiltersMetadata -> isFilterValid

## decorators/core/use-interceptors.decorator.ts  (tp 3, fp 0, fn 1, unscored 0)
  - UseInterceptors -> isInterceptorValid

## decorators/core/use-pipes.decorator.ts  (tp 3, fp 0, fn 1, unscored 0)
  - UsePipes -> isPipeValid

## module-utils/utils/get-injection-providers.util.ts  (tp 7, fp 0, fn 1, unscored 0)
  - getInjectionProviders -> mapInjectToTokens

## utils/shared.utils.ts  (tp 9, fp 0, fn 1, unscored 1)
  - isPlainObject -> Object
  ~ isPlainObject -> getPrototypeOf

## decorators/core/controller.decorator.ts  (tp 4, fp 0, fn 0, unscored 2)
  ~ Controller -> from
  ~ Controller -> isArray

## decorators/core/injectable.decorator.ts  (tp 2, fp 0, fn 0, unscored 2)
  ~ mixin -> defineProperty
  ~ mixin -> uid

## decorators/http/request-mapping.decorator.ts  (tp 2, fp 0, fn 0, unscored 1)
  ~ __module__ -> createMappingDecorator

## exceptions/http.exception.ts  (tp 13, fp 0, fn 0, unscored 1)
  ~ createBody -> isArray

## file-stream/streamable-file.ts  (tp 5, fp 0, fn 0, unscored 3)
  ~ __module__ -> Logger
  ~ constructor -> Readable
  ~ constructor -> isUint8Array

## module-utils/configurable-module.builder.ts  (tp 22, fp 0, fn 0, unscored 4)
  ~ __module__ -> Logger
  ~ createConfigurableModuleCls -> filter
  ~ createConfigurableModuleCls -> forEach
  ~ createConfigurableModuleCls -> keys

## pipes/default-value.pipe.ts  (tp 3, fp 0, fn 0, unscored 1)
  ~ __module__ -> Injectable

## pipes/parse-bool.pipe.ts  (tp 5, fp 0, fn 0, unscored 1)
  ~ __module__ -> Injectable

## pipes/parse-date.pipe.ts  (tp 5, fp 0, fn 0, unscored 2)
  ~ __module__ -> Injectable
  ~ transform -> Date

## pipes/parse-float.pipe.ts  (tp 9, fp 0, fn 0, unscored 1)
  ~ __module__ -> Injectable

## pipes/parse-int.pipe.ts  (tp 8, fp 0, fn 0, unscored 1)
  ~ __module__ -> Injectable

## pipes/parse-uuid.pipe.ts  (tp 7, fp 0, fn 0, unscored 1)
  ~ __module__ -> Injectable

## serializer/class-serializer.interceptor.ts  (tp 16, fp 0, fn 0, unscored 3)
  ~ __module__ -> Injectable
  ~ intercept -> map
  ~ serialize -> isArray

## services/logger.service.ts  (tp 26, fp 0, fn 0, unscored 7)
  ~ __module__ -> Array
  ~ __module__ -> ConsoleLogger
  ~ __module__ -> DateTimeFormat
  ~ __module__ -> Injectable
  ~ getTimestamp -> now
  ~ localInstance -> getPrototypeOf
  ~ overrideLogger -> isArray

36 of 43 files exactly right.
