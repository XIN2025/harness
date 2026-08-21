# ts-hexo / dev / cut=full

raw 53/53 (100.0%)  ·  fence-stripped 53/53 (100.0%)  ·  schema 53/53 (100.0%)
P 100.0% [100.0% to 100.0%] (percentile)   R 97.2% [95.4% to 98.4%]   F1 98.6% [97.6% to 99.2%]

`-` missed by the arm (in the oracle, not predicted)
`+` spurious (predicted, not in the oracle)
`~` unscored — this cut excludes the class, so it counts against neither side

## lib/extend/renderer.ts  (tp 8, fp 0, fn 2, unscored 5)
  - getOutput -> renderer
  - register -> fn
  ~ getExtname -> extname
  ~ isRenderable -> Boolean
  ~ isRenderableSync -> Boolean
  ~ register -> method
  ~ register -> promisify

## lib/hexo/render.ts  (tp 28, fp 0, fn 2, unscored 7)
  - render -> renderer
  - renderSync -> renderer
  ~ getExtname -> extname
  ~ render -> readFile
  ~ render -> reject
  ~ render -> resolve
  ~ renderSync -> readFileSync
  ~ toString -> call
  ~ toString -> stringify

## lib/box/index.ts  (tp 68, fp 0, fn 1, unscored 27)
  - addProcessor -> fn
  ~ __module__ -> Pattern
  ~ _checkFileStatus -> join
  ~ _checkFileStatus -> stat
  ~ _processFile -> catch
  ~ _processFile -> finally
  ~ _processFile -> join
  ~ _processFile -> magenta
  ~ _processFile -> method
  ~ _processFile -> reduce
  ~ _processFile -> resolve
  ~ _processFile -> then
  ~ addProcessor -> Pattern
  ~ constructor -> assign
  ~ getHash -> BlueBirdPromise
  ~ getHash -> createReadStream
  ~ getHash -> createSha1Hash
  ~ isIgnoreMatch -> isMatch
  ~ isWatching -> Boolean
  ~ process -> stat
  ~ readDirWalker -> join
  ~ readDirWalker -> map
  ~ readDirWalker -> readdir
  ~ readDirWalker -> resolve
  ~ readDirWalker -> stat
  ~ toRegExp -> makeRe
  ~ watch -> reject
  ~ watch -> watch

## lib/extend/console.ts  (tp 3, fp 0, fn 1, unscored 4)
  - register -> fn
  ~ register -> abbrev
  ~ register -> keys
  ~ register -> method
  ~ register -> promisify

## lib/extend/deployer.ts  (tp 1, fp 0, fn 1, unscored 2)
  - register -> fn
  ~ register -> method
  ~ register -> promisify

## lib/extend/generator.ts  (tp 1, fp 0, fn 1, unscored 2)
  - register -> fn
  ~ register -> method
  ~ register -> promisify

## lib/extend/syntax_highlight.ts  (tp 3, fp 0, fn 1, unscored 0)
  - exec -> fn

## lib/plugins/console/list/page.ts  (tp 5, fp 0, fn 1, unscored 5)
  - listPage -> stringLength
  ~ listPage -> gray
  ~ listPage -> log
  ~ listPage -> magenta
  ~ listPage -> table
  ~ listPage -> underline

## lib/plugins/filter/after_render/external_link.ts  (tp 5, fp 0, fn 1, unscored 1)
  - externalLinkFilter -> addNoopener
  ~ externalLinkFilter -> isExternalLink

## lib/plugins/filter/template_locals/i18n.ts  (tp 8, fp 0, fn 1, unscored 1)
  - i18nLocalsFilter -> Boolean
  ~ i18nLocalsFilter -> Pattern

## lib/plugins/helper/list_tags.ts  (tp 7, fp 0, fn 1, unscored 3)
  - listTagsHelperFactory -> transformArgs
  ~ listTagsHelper -> call
  ~ listTagsHelper -> escapeHTML
  ~ listTagsHelperFactory -> moize

## lib/plugins/helper/open_graph.ts  (tp 21, fp 0, fn 1, unscored 14)
  - openGraphHelper -> Boolean
  ~ __module__ -> includes
  ~ __module__ -> shallow
  ~ __module__ -> split
  ~ __module__ -> toLowerCase
  ~ __module__ -> toUpperCase
  ~ meta -> escapeHTML
  ~ og -> escapeHTML
  ~ openGraphHelper -> encodeURL
  ~ openGraphHelper -> escapeHTML
  ~ openGraphHelper -> isArray
  ~ openGraphHelper -> isDate
  ~ openGraphHelper -> isMoment
  ~ openGraphHelper -> prettyUrls
  ~ openGraphHelper -> stripHTML

## lib/plugins/helper/tagcloud.ts  (tp 17, fp 0, fn 1, unscored 4)
  - tagcloudHelperFactory -> transformArgs
  ~ tagcloudHelper -> Color
  ~ tagcloudHelper -> call
  ~ tagcloudHelper -> round
  ~ tagcloudHelperFactory -> moize

## lib/theme/index.ts  (tp 9, fp 0, fn 1, unscored 6)
  - constructor -> Boolean
  ~ constructor -> I18n
  ~ constructor -> isArray
  ~ getView -> extname
  ~ getView -> keys
  ~ removeView -> extname
  ~ setView -> extname

## lib/box/file.ts  (tp 0, fp 0, fn 0, unscored 4)
  ~ read -> readFile
  ~ readSync -> readFileSync
  ~ stat -> stat
  ~ statSync -> statSync

## lib/extend/injector.ts  (tp 14, fp 0, fn 0, unscored 3)
  ~ constructor -> Cache
  ~ get -> from
  ~ getSize -> keys

## lib/extend/processor.ts  (tp 2, fp 0, fn 0, unscored 3)
  ~ register -> Pattern
  ~ register -> method
  ~ register -> promisify

## lib/hexo/load_config.ts  (tp 1, fp 0, fn 0, unscored 21)
  ~ __module__ -> Source
  ~ __module__ -> Theme
  ~ __module__ -> URL
  ~ __module__ -> debug
  ~ __module__ -> deepMerge
  ~ __module__ -> endsWith
  ~ __module__ -> exists
  ~ __module__ -> findConfigPath
  ~ __module__ -> join
  ~ __module__ -> magenta
  ~ __module__ -> render
  ~ __module__ -> replace
  ~ __module__ -> resolve
  ~ __module__ -> tildify
  ~ __module__ -> toString
  ~ __module__ -> validateConfig
  ~ findConfigPath -> basename
  ~ findConfigPath -> extname
  ~ findConfigPath -> join
  ~ findConfigPath -> parse
  ~ findConfigPath -> readdir

## lib/hexo/load_plugins.ts  (tp 21, fp 0, fn 0, unscored 18)
  ~ __module__ -> loadModules
  ~ __module__ -> loadScripts
  ~ __module__ -> then
  ~ displayPath -> magenta
  ~ loadModuleList -> exists
  ~ loadModuleList -> fromEntries
  ~ loadModuleList -> join
  ~ loadModuleList -> keys
  ~ loadModuleList -> parse
  ~ loadModuleList -> readFile
  ~ loadModules -> assign
  ~ loadModules -> entries
  ~ loadModules -> magenta
  ~ loadModules -> map
  ~ loadScripts -> exists
  ~ loadScripts -> filter
  ~ loadScripts -> join
  ~ loadScripts -> listDir

## lib/hexo/load_theme_config.ts  (tp 2, fp 0, fn 0, unscored 15)
  ~ __module__ -> String
  ~ __module__ -> debug
  ~ __module__ -> deepMerge
  ~ __module__ -> exists
  ~ __module__ -> findConfigPath
  ~ __module__ -> join
  ~ __module__ -> magenta
  ~ __module__ -> render
  ~ __module__ -> then
  ~ __module__ -> tildify
  ~ findConfigPath -> basename
  ~ findConfigPath -> extname
  ~ findConfigPath -> join
  ~ findConfigPath -> parse
  ~ findConfigPath -> readdir

## lib/hexo/router.ts  (tp 24, fp 0, fn 0, unscored 5)
  ~ _toBuffer -> stringify
  ~ list -> filter
  ~ list -> keys
  ~ set -> method
  ~ set -> promisify

## lib/hexo/scaffold.ts  (tp 16, fp 0, fn 0, unscored 9)
  ~ _listDir -> exists
  ~ _listDir -> extname
  ~ _listDir -> join
  ~ _listDir -> listDir
  ~ get -> readFile
  ~ remove -> unlink
  ~ set -> extname
  ~ set -> join
  ~ set -> writeFile

## lib/hexo/update_package.ts  (tp 1, fp 0, fn 0, unscored 9)
  ~ __module__ -> debug
  ~ __module__ -> join
  ~ __module__ -> readPkg
  ~ __module__ -> stringify
  ~ __module__ -> then
  ~ __module__ -> writeFile
  ~ readPkg -> exists
  ~ readPkg -> parse
  ~ readPkg -> readFile

## lib/models/binary_relation_index.ts  (tp 15, fp 0, fn 0, unscored 4)
  ~ __module__ -> Map
  ~ find -> filter
  ~ find -> from
  ~ find -> map

## lib/models/post.ts  (tp 2, fp 0, fn 0, unscored 34)
  ~ __module__ -> Cache
  ~ __module__ -> Schema
  ~ __module__ -> _showDrafts
  ~ __module__ -> addHierarchy
  ~ __module__ -> apply
  ~ __module__ -> call
  ~ __module__ -> catch
  ~ __module__ -> each
  ~ __module__ -> execFilterSync
  ~ __module__ -> extname
  ~ __module__ -> filter
  ~ __module__ -> find
  ~ __module__ -> findOne
  ~ __module__ -> flush
  ~ __module__ -> get
  ~ __module__ -> includes
  ~ __module__ -> insert
  ~ __module__ -> isArray
  ~ __module__ -> join
  ~ __module__ -> map
  ~ __module__ -> method
  ~ __module__ -> model
  ~ __module__ -> notPublished
  ~ __module__ -> now
  ~ __module__ -> pre
  ~ __module__ -> push
  ~ __module__ -> remove
  ~ __module__ -> removeById
  ~ __module__ -> removeEmptyTag
  ~ __module__ -> resolve
  ~ __module__ -> substring
  ~ __module__ -> then
  ~ __module__ -> valueOf
  ~ __module__ -> virtual

## lib/plugins/console/config.ts  (tp 9, fp 0, fn 0, unscored 8)
  ~ castValue -> Number
  ~ configConsole -> dump
  ~ configConsole -> exists
  ~ configConsole -> extname
  ~ configConsole -> log
  ~ configConsole -> resolve
  ~ configConsole -> stringify
  ~ configConsole -> writeFile

## lib/plugins/console/deploy.ts  (tp 8, fp 0, fn 0, unscored 7)
  ~ deployConsole -> exists
  ~ deployConsole -> isArray
  ~ deployConsole -> join
  ~ deployConsole -> keys
  ~ deployConsole -> log
  ~ deployConsole -> magenta
  ~ deployConsole -> underline

## lib/plugins/console/list/route.ts  (tp 7, fp 0, fn 0, unscored 4)
  ~ buildNodes -> entries
  ~ buildNodes -> keys
  ~ listRoute -> archy
  ~ listRoute -> log

## lib/plugins/console/render.ts  (tp 4, fp 0, fn 0, unscored 9)
  ~ renderConsole -> cyan
  ~ renderConsole -> hrtime
  ~ renderConsole -> log
  ~ renderConsole -> magenta
  ~ renderConsole -> prettyHrtime
  ~ renderConsole -> resolve
  ~ renderConsole -> stringify
  ~ renderConsole -> tildify
  ~ renderConsole -> writeFile

## lib/plugins/filter/before_post_render/backtick_code_block.ts  (tp 8, fp 0, fn 0, unscored 11)
  ~ __module__ -> RegExp
  ~ __module__ -> escapeSwigTag
  ~ __module__ -> exec
  ~ __module__ -> includes
  ~ __module__ -> parseArgs
  ~ __module__ -> push
  ~ __module__ -> query
  ~ __module__ -> replace
  ~ __module__ -> shift
  ~ __module__ -> split
  ~ parseArgs -> Number

## lib/plugins/filter/new_post_path.ts  (tp 8, fp 0, fn 0, unscored 10)
  ~ newPostPathFilter -> Permalink
  ~ newPostPathFilter -> createSha1Hash
  ~ newPostPathFilter -> ensurePath
  ~ newPostPathFilter -> extname
  ~ newPostPathFilter -> join
  ~ newPostPathFilter -> keys
  ~ newPostPathFilter -> moment
  ~ newPostPathFilter -> now
  ~ newPostPathFilter -> reject
  ~ newPostPathFilter -> resolve

## lib/plugins/generator/asset.ts  (tp 11, fp 0, fn 0, unscored 9)
  ~ assetGenerator -> all
  ~ assetGenerator -> process
  ~ assetGenerator -> then
  ~ process -> createReadStream
  ~ process -> exists
  ~ process -> extname
  ~ process -> filter
  ~ process -> magenta
  ~ process -> map

## lib/plugins/helper/css.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ __module__ -> moize
  ~ cssHelper -> call
  ~ cssHelper -> htmlTag

## lib/plugins/helper/date.ts  (tp 23, fp 0, fn 0, unscored 8)
  ~ __module__ -> shallow
  ~ dateHelper -> format
  ~ fullDateHelper -> format
  ~ getMoment -> Date
  ~ getMoment -> moment
  ~ relativeDateHelper -> fromNow
  ~ timeHelper -> format
  ~ toISOString -> Date

## lib/plugins/helper/feed_tag.ts  (tp 5, fp 0, fn 0, unscored 2)
  ~ feedTagHelper -> deep
  ~ makeFeedTag -> call

## lib/plugins/helper/is.ts  (tp 3, fp 0, fn 0, unscored 9)
  ~ isArchiveHelper -> Boolean
  ~ isCategoryHelper -> Boolean
  ~ isHomeFirstPageHelper -> Boolean
  ~ isHomeHelper -> Boolean
  ~ isMonthHelper -> Boolean
  ~ isPageHelper -> Boolean
  ~ isPostHelper -> Boolean
  ~ isTagHelper -> Boolean
  ~ isYearHelper -> Boolean

## lib/plugins/helper/js.ts  (tp 3, fp 0, fn 0, unscored 3)
  ~ __module__ -> moize
  ~ jsHelper -> call
  ~ jsHelper -> htmlTag

## lib/plugins/helper/link_to.ts  (tp 2, fp 0, fn 0, unscored 4)
  ~ linkToHelper -> assign
  ~ linkToHelper -> call
  ~ linkToHelper -> htmlTag
  ~ linkToHelper -> isArray

## lib/plugins/helper/list_archives.ts  (tp 14, fp 0, fn 0, unscored 2)
  ~ __module__ -> Cache
  ~ listArchivesHelper -> call

## lib/plugins/helper/list_categories.ts  (tp 9, fp 0, fn 0, unscored 2)
  ~ listCategoriesHelper -> String
  ~ listCategoriesHelper -> call

## lib/plugins/helper/list_posts.ts  (tp 4, fp 0, fn 0, unscored 1)
  ~ listPostsHelper -> call

## lib/plugins/helper/mail_to.ts  (tp 4, fp 0, fn 0, unscored 4)
  ~ __module__ -> moize
  ~ mailToHelper -> assign
  ~ mailToHelper -> htmlTag
  ~ mailToHelper -> isArray

## lib/plugins/helper/paginator.ts  (tp 16, fp 0, fn 0, unscored 8)
  ~ createLink -> String
  ~ createLink -> call
  ~ createPageTag -> htmlTag
  ~ paginationPartShow -> htmlTag
  ~ paginationPartShow -> max
  ~ paginationPartShow -> min
  ~ paginatorHelper -> assign
  ~ paginatorHelper -> htmlTag

## lib/plugins/processor/asset.ts  (tp 18, fp 0, fn 0, unscored 12)
  ~ __module__ -> Pattern
  ~ __module__ -> isExcludedFile
  ~ __module__ -> isMatch
  ~ __module__ -> isRenderable
  ~ __module__ -> processAsset
  ~ __module__ -> processPage
  ~ processAsset -> relative
  ~ processPage -> all
  ~ processPage -> extname
  ~ processPage -> magenta
  ~ processPage -> spread
  ~ processPage -> yfm

## lib/plugins/processor/post.ts  (tp 51, fp 0, fn 0, unscored 28)
  ~ __module__ -> Pattern
  ~ __module__ -> extname
  ~ __module__ -> isHiddenFile
  ~ __module__ -> isMatch
  ~ __module__ -> isRenderable
  ~ __module__ -> isTmpFile
  ~ __module__ -> processAsset
  ~ __module__ -> processPost
  ~ __module__ -> startsWith
  ~ __module__ -> substring
  ~ markFuturePostDirty -> now
  ~ parseFilename -> Permalink
  ~ parseFilename -> assign
  ~ parseFilename -> extname
  ~ parseFilename -> slugize
  ~ processAsset -> join
  ~ processPost -> Date
  ~ processPost -> all
  ~ processPost -> call
  ~ processPost -> isArray
  ~ processPost -> keys
  ~ processPost -> magenta
  ~ processPost -> spread
  ~ processPost -> then
  ~ processPost -> yfm
  ~ scanAssetDir -> join
  ~ scanAssetDir -> listDir
  ~ scanAssetDir -> stat

## lib/plugins/tag/code.ts  (tp 7, fp 0, fn 0, unscored 12)
  ~ __module__ -> escapeHTML
  ~ __module__ -> exec
  ~ __module__ -> findIndex
  ~ __module__ -> parseArgs
  ~ __module__ -> query
  ~ __module__ -> replace
  ~ __module__ -> slice
  ~ __module__ -> splice
  ~ __module__ -> split
  ~ __module__ -> startsWith
  ~ parseArgs -> Number
  ~ parseArgs -> htmlTag

## lib/plugins/tag/index.ts  (tp 6, fp 0, fn 0, unscored 4)
  ~ __module__ -> WeakMap
  ~ __module__ -> register
  ~ __module__ -> require
  ~ postFindOneFactory -> moize

## lib/plugins/tag/link.ts  (tp 5, fp 0, fn 0, unscored 1)
  ~ linkTag -> htmlTag

## lib/theme/processors/source.ts  (tp 6, fp 0, fn 0, unscored 6)
  ~ __module__ -> Pattern
  ~ __module__ -> includes
  ~ __module__ -> isHiddenFile
  ~ __module__ -> isTmpFile
  ~ __module__ -> startsWith
  ~ __module__ -> substring

## lib/theme/view.ts  (tp 26, fp 0, fn 0, unscored 8)
  ~ _bindHelpers -> keys
  ~ _precompile -> extname
  ~ _precompile -> resolve
  ~ _precompile -> then
  ~ _resolveLayout -> dirname
  ~ _resolveLayout -> join
  ~ constructor -> join
  ~ constructor -> yfm

39 of 53 files exactly right.
