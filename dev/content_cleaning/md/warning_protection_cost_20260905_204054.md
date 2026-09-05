# Warning-Protection Fix — Cost Measurement on the PRE_BUILDLOG Backup (20260905_204054)

Backup: /Users/brunowinter2000/Documents/ai/Meta/ClaudeCode/cli/rag-cli/data/documents/github_issues_PRE_BUILDLOG_STRIP_BACKUP_20260828_230949 · 873 files

## Summary

| Metric | Old (pre-fix) | New (post-fix) |
|---|---|---|
| Files affected | 8 | 8 |
| Blocks removed | 56 | 51 |
| Gross chars removed | 333,184 | 310,370 |

Lines newly kept (were removed by the old detector, now survive): **352**

## Newly Kept Lines (verbatim, by file)

### MinerU__1418.md

L279: `INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.`
L280: `  Downloading https://mirrors.aliyun.com/pypi/packages/93/3d/6127d46701e60b3ab1a9621fe9c99c84f7e46939a8744013b2367651ad27/magic_pdf-0.7.1-py3-none-any.whl (1.1 MB)`
L281: `     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 3.3 MB/s eta 0:00:00`
L282: `WARNING: magic-pdf 0.6.1 does not provide the extra 'full'`

### MinerU__2262.md

L853: `INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.`
L867: `WARNING: magic-pdf 0.6.1 does not provide the extra 'full'`

### MinerU__826.md

L201: `WARNING: magic-pdf 0.6.1 does not provide the extra 'full'`

### curl_cffi__74.md

L1579: `      warning: no files found matching 'include/curl/*'`
L1580: `      adding license file 'LICENSE'`
L1581: `      writing manifest file 'curl_cffi.egg-info/SOURCES.txt'`
L1582: `      copying curl_cffi/py.typed -> build/lib.linux-aarch64-cpython-312/curl_cffi`
L1583: `      running build_ext`
L1584: `      generating cffi module 'build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.c'`
L1585: `      creating build/temp.linux-aarch64-cpython-312`
L1586: `      building 'curl_cffi._wrapper' extension`
L1587: `      creating build/temp.linux-aarch64-cpython-312/build/temp.linux-aarch64-cpython-312`
L1588: `      creating build/temp.linux-aarch64-cpython-312/ffi`
L1589: `      aarch64-linux-android-clang -fno-strict-overflow -Wsign-compare -Wunreachable-code -DNDEBUG -g -O3 -Wall -fstack-protector-strong -O3 -fstack-protector-strong -O3 -fPIC -Iinclude -Iffi -I/data/data/com.termux/files/usr/tmp/tmpmku0rr6s/include -I/data/data/com.termux/files/usr/include/python3.12 -c build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.c -o build/temp.linux-aarch64-cpython-312/build/temp.linux-aarch64-cpython-312/curl_cffi._wrapper.o`

### pyobjc__34.md

L46: `warning: no directories found matching 'Scripts'`
L47: `warning: no directories found matching 'setup-lib'`
L48: `warning: no directories found matching 'source-deps'`
L49: `warning: no previously-included files matching '.DS_Store' found anywhere in distribution`
L50: `warning: no previously-included files matching '*.pyc' found anywhere in distribution`
L51: `warning: no previously-included files matching '*.so' found anywhere in distribution`
L211: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L212: `libffi-src/x86/x86-ffi64.c:164:27: warning: implicit conversion loses integer`
L213: `      precision: 'unsigned long' to 'int' [-Wshorten-64-to-32]`
L214: `                        int size = byte_offset + type->size;`
L215: `                            ~~~~   ~~~~~~~~~~~~^~~~~~~~~~~~`
L216: `libffi-src/x86/x86-ffi64.c:216:39: warning: implicit conversion loses integer`
L217: `      precision: 'unsigned long' to 'int' [-Wshorten-64-to-32]`
L218: `  ...(type->size + UNITS_PER_WORD - 1) / UNITS_PER_WORD;`
L219: `     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~`
L220: `libffi-src/x86/x86-ffi64.c:423:15: warning: implicit conversion loses integer`
L238: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L239: `Modules/objc/block_support.m:260:47: warning: implicit conversion loses integer`
L240: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L241: `  ...if (PyObjCFFI_AllocByRef(Py_SIZE(signature) + PyTuple_Size(args), ...`
L242: `         ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~`
L243: `Modules/objc/block_support.m:264:28: warning: implicit conversion loses integer`
L244: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L245: `                if (PyObjCFFI_AllocByRef(Py_SIZE(signature), &byref, ...`
L246: `                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~`
L247: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L248: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L249: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L250: `Modules/objc/block_support.m:301:45: warning: implicit conversion loses integer`
L251: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L252: `  ...if (PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args), byref, ...`
L253: `         ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L254: `Modules/objc/block_support.m:306:27: warning: implicit conversion loses integer`
L255: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L256: `                if (PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, ...`
L257: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~`
L258: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L259: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L260: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L261: `Modules/objc/block_support.m:316:41: warning: implicit conversion loses integer`
L262: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L263: `                PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args)...`
L264: `                ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L265: `Modules/objc/block_support.m:318:23: warning: implicit conversion loses integer`
L266: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L267: `                PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr);`
L268: `                ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~`
L269: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L270: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L271: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L272: `6 warnings generated.`
L292: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L293: `Modules/objc/function.m:189:51: warning: implicit conversion loses integer`
L294: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L295: `  ...if (PyObjCFFI_AllocByRef(Py_SIZE(self->methinfo)+PyTuple_Size(args), ...`
L296: `         ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L297: `Modules/objc/function.m:193:28: warning: implicit conversion loses integer`
L298: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L299: `                if (PyObjCFFI_AllocByRef(Py_SIZE(self->methinfo), ...`
L300: `                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~`
L301: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L302: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L303: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L304: `Modules/objc/function.m:234:50: warning: implicit conversion loses integer`
L305: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L306: `  ...if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo)+PyTuple_Size(args), ...`
L307: `         ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L308: `Modules/objc/function.m:239:27: warning: implicit conversion loses integer`
L309: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L310: `                if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, ...`
L311: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~`
L312: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L313: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L314: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L315: `Modules/objc/function.m:249:27: warning: implicit conversion loses integer`
L316: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L317: `                if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, ...`
L318: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~`
L319: `Modules/objc/function.m:254:27: warning: implicit conversion loses integer`
L320: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L321: `                if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, ...`
L322: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~~~~~~`
L323: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L324: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L325: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L326: `6 warnings generated.`
L370: `Modules/objc/objc-object.h:41:90: note: expanded from macro`
L371: `      'PyObjCObject_SET_BLOCK'`
L372: `  ...value) (((PyObjCBlockObject*)(object))->signature = (value))`
L373: `                                                       ^ ~~~~~~~`
L374: `7 warnings generated.`
L375: `Modules/objc/libffi_support.m:936:9: warning: implicit conversion loses integer`
L376: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L377: `        return curarg;`
L378: `        ~~~~~~ ^~~~~~`
L379: `Modules/objc/libffi_support.m:988:15: warning: implicit conversion loses integer`
L380: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L381: `        return curarg+1;`
L382: `        ~~~~~~ ~~~~~~^~`
L383: `Modules/objc/libffi_support.m:1823:30: warning: implicit conversion loses`
L384: `      integer precision: 'long' to 'int' [-Wshorten-64-to-32]`
L385: `                 int result = Py_SIZE(sig) - 1;`
L386: `                     ~~~~~~   ~~~~~~~~~~~~~^~~`
L387: `Modules/objc/libffi_support.m:3143:9: warning: implicit conversion loses integer`
L388: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L389: `        return Py_SIZE(methinfo);`
L390: `        ~~~~~~ ^~~~~~~~~~~~~~~~~`
L391: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L392: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L393: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L394: `Modules/objc/libffi_support.m:3326:13: warning: initializing 'char *' with an`
L411: `Modules/objc/objc-object.h:41:90: note: expanded from macro`
L412: `      'PyObjCObject_SET_BLOCK'`
L413: `  ...value) (((PyObjCBlockObject*)(object))->signature = (value))`
L414: `                                                       ^ ~~~~~~~`
L415: `Modules/objc/libffi_support.m:3732:45: warning: implicit conversion loses`
L416: `      integer precision: 'long' to 'int' [-Wshorten-64-to-32]`
L417: `                if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo)+PyTuple_Size(args), `
L418: `                    ~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L419: `Modules/objc/libffi_support.m:3737:28: warning: implicit conversion loses`
L420: `      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L421: `                if (PyObjCFFI_AllocByRef(Py_SIZE(methinfo), &byref, ...`
L422: `                    ~~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~`
L423: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L424: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L425: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L426: `Modules/objc/libffi_support.m:3905:44: warning: implicit conversion loses`
L427: `      integer precision: 'long' to 'int' [-Wshorten-64-to-32]`
L428: `                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo)+PyTuple_Size(args)...`
L429: `                    ~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~`
L430: `Modules/objc/libffi_support.m:3910:27: warning: implicit conversion loses`
L431: `      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L432: `                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, ...`
L433: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~`
L434: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L435: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L436: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L437: `Modules/objc/libffi_support.m:3931:27: warning: implicit conversion loses`
L438: `      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L439: `                if (PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, ...`
L440: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~~`
L441: `Modules/objc/libffi_support.m:3936:27: warning: implicit conversion loses`
L442: `      integer precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L443: `                if (PyObjCFFI_FreeByRef(Py_SIZE(methinfo), byref, ...`
L444: `                    ~~~~~~~~~~~~~~~~~~~ ^~~~~~~~~~~~~~~~~`
L445: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L446: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L447: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L448: `Modules/objc/libffi_support.m:3997:42: warning: implicit conversion loses`
L480: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L481: `Modules/objc/objc-class.m:49:6: warning: implicit conversion loses integer`
L482: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L483: `        n = PyTuple_GET_SIZE(mro);`
L484: `          ~ ^~~~~~~~~~~~~~~~~~~~~`
L485: `/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/tupleobject.h:51:33: note: `
L486: `      expanded from macro 'PyTuple_GET_SIZE'`
L487: `#define PyTuple_GET_SIZE(op)    Py_SIZE(op)`
L488: `                                ^`
L489: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L490: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L491: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L492: `Modules/objc/objc-class.m:983:23: warning: implicit conversion loses integer`
L493: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L494: `        info->method_magic = PyObjC_methodlist_magic(objc_class);`
L495: `                           ~ ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
L496: `Modules/objc/objc-class.m:1085:14: warning: implicit conversion loses integer`
L497: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L498: `  ...(magic = PyObjC_methodlist_magic(info->class))) || (info->generation != ...`
L499: `            ~ ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
L500: `Modules/objc/objc-class.m:1100:23: warning: implicit conversion loses integer`
L501: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L502: `                        info->generation = PyObjC_MappingCount;`
L503: `                                         ~ ^~~~~~~~~~~~~~~~~~~`
L504: `Modules/objc/objc-class.m:2634:50: warning: implicit conversion loses integer`
L524: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L525: `Modules/objc/objc_support.m:2119:19: warning: implicit conversion loses integer`
L526: `      precision: 'long long' to 'int' [-Wshorten-64-to-32]`
L527: `                        *(int*)datum = temp;`
L528: `                                     ~ ^~~~`
L529: `Modules/objc/objc_support.m:2154:19: warning: implicit conversion loses integer`
L530: `      precision: 'long long' to 'int' [-Wshorten-64-to-32]`
L531: `                        *(int*)datum = temp;`
L532: `                                     ~ ^~~~`
L533: `Modules/objc/objc_support.m:2190:28: warning: implicit conversion loses integer`
L534: `      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]`
L535: `                        *(unsigned int*)datum = utemp;`
L536: `                                              ~ ^~~~~`
L537: `Modules/objc/objc_support.m:2198:19: warning: implicit conversion loses integer`
L538: `      precision: 'long long' to 'int' [-Wshorten-64-to-32]`
L539: `                        *(int*)datum = temp;`
L540: `                                     ~ ^~~~`
L541: `Modules/objc/objc_support.m:2206:28: warning: implicit conversion loses integer`
L542: `      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]`
L543: `                        *(unsigned int*)datum = utemp;`
L544: `                                              ~ ^~~~~`
L545: `Modules/objc/objc_support.m:2434:19: warning: implicit conversion loses integer`
L546: `      precision: 'long long' to 'int' [-Wshorten-64-to-32]`
L547: `                        *(int*)datum = temp;`
L548: `                                     ~ ^~~~`
L549: `Modules/objc/objc_support.m:2442:28: warning: implicit conversion loses integer`
L550: `      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]`
L551: `                        *(unsigned int*)datum = utemp;`
L552: `                                              ~ ^~~~~`
L553: `Modules/objc/objc_support.m:2450:20: warning: implicit conversion loses integer`
L554: `      precision: 'long long' to 'long' [-Wshorten-64-to-32]`
L555: `                        *(long*)datum = temp;`
L556: `                                      ~ ^~~~`
L557: `Modules/objc/objc_support.m:2458:29: warning: implicit conversion loses integer`
L558: `      precision: 'unsigned long long' to 'unsigned long' [-Wshorten-64-to-32]`
L559: `                        *(unsigned long*)datum = utemp;`
L560: `                                               ~ ^~~~~`
L561: `9 warnings generated.`
L562: `Modules/objc/objc_support.m:722:21: warning: implicit conversion loses integer`
L563: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L564: `                        int item_align = PyObjCRT_AlignOfType(type);`
L565: `                            ~~~~~~~~~~   ^~~~~~~~~~~~~~~~~~~~~~~~~~`
L566: `Modules/objc/objc_support.m:901:12: warning: implicit conversion loses integer`
L567: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L568: `                        int i = strtol(type+1, NULL, 10);`
L569: `                            ~   ^~~~~~~~~~~~~~~~~~~~~~~~`
L570: `Modules/objc/objc_support.m:2434:19: warning: implicit conversion loses integer`
L571: `      precision: 'long long' to 'int' [-Wshorten-64-to-32]`
L572: `                        *(int*)datum = temp;`
L573: `                                     ~ ^~~~`
L574: `Modules/objc/objc_support.m:2442:28: warning: implicit conversion loses integer`
L575: `      precision: 'unsigned long long' to 'unsigned int' [-Wshorten-64-to-32]`
L576: `                        *(unsigned int*)datum = utemp;`
L577: `                                              ~ ^~~~~`
L578: `4 warnings generated.`
L629: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L630: `Modules/objc/pointer-support.m:59:16: warning: implicit conversion loses integer`
L631: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L632: `                        return end1 - signature;`
L633: `                        ~~~~~~ ~~~~~^~~~~~~~~~~`
L634: `Modules/objc/pointer-support.m:61:16: warning: implicit conversion loses integer`
L635: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L636: `                        return end2 - signature;`
L637: `                        ~~~~~~ ~~~~~^~~~~~~~~~~`
L638: `Modules/objc/pointer-support.m:72:16: warning: implicit conversion loses integer`
L639: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L640: `                        return end1 - signature;`
L641: `                        ~~~~~~ ~~~~~^~~~~~~~~~~`
L642: `Modules/objc/pointer-support.m:74:16: warning: implicit conversion loses integer`
L643: `      precision: 'long' to 'int' [-Wshorten-64-to-32]`
L644: `                        return end2 - signature;`
L645: `                        ~~~~~~ ~~~~~^~~~~~~~~~~`
L646: `Modules/objc/pointer-support.m:77:9: warning: implicit conversion loses integer`
L647: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L648: `        return strlen(signature);`
L649: `        ~~~~~~ ^~~~~~~~~~~~~~~~~`
L650: `5 warnings generated.`
L669: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L670: `Modules/objc/struct-wrapper.m:748:9: warning: implicit conversion loses integer`
L671: `      precision: 'Py_ssize_t' (aka 'long') to 'int' [-Wshorten-64-to-32]`
L672: `                len = PyList_GET_SIZE(keys);`
L673: `                    ~ ^~~~~~~~~~~~~~~~~~~~~`
L674: `/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/listobject.h:63:32: note: `
L675: `      expanded from macro 'PyList_GET_SIZE'`
L676: `#define PyList_GET_SIZE(op)    Py_SIZE(op)`
L677: `                               ^`
L678: `Modules/objc/pyobjc-compat.h:153:56: note: expanded from macro 'Py_SIZE'`
L679: `#define Py_SIZE(ob)             (((PyVarObject*)(ob))->ob_size)`
L680: `                                 ~~~~~~~~~~~~~~~~~~~~~~^~~~~~~`
L681: `1 warning generated.`
L767: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L768: `Modules/objc/test/properties.m:24:9: warning: Ignore warnings about properties`
L769: `      in this file. [-W#pragma-messages]`
L770: `#pragma message "Ignore warnings about properties in this file."`
L771: `        ^`
L772: `Modules/objc/test/properties.m:28:1: warning: no 'assign', 'retain', or 'copy'`
L773: `      attribute is specified - 'assign' is assumed`
L774: `@property id prop4;`
L775: `^`
L776: `Modules/objc/test/properties.m:28:1: warning: default property attribute`
L777: `      'assign' not appropriate for non-gc object`
L778: `Modules/objc/test/properties.m:30:1: warning: no 'assign', 'retain', or 'copy'`
L779: `      attribute is specified - 'assign' is assumed`
L780: `@property(readwrite) id prop6;`
L781: `^`
L782: `Modules/objc/test/properties.m:30:1: warning: default property attribute`
L783: `      'assign' not appropriate for non-gc object`
L784: `Modules/objc/test/properties.m:35:1: warning: no 'assign', 'retain', or 'copy'`
L785: `      attribute is specified - 'assign' is assumed`
L786: `@property(getter=propGetter,setter=propSetter:) id prop11;`
L787: `^`
L788: `Modules/objc/test/properties.m:35:1: warning: default property attribute`
L789: `      'assign' not appropriate for non-gc object`
L790: `7 warnings generated.`
L791: `Modules/objc/test/properties.m:24:9: warning: Ignore warnings about properties`
L792: `      in this file. [-W#pragma-messages]`
L793: `#pragma message "Ignore warnings about properties in this file."`
L794: `        ^`
L795: `Modules/objc/test/properties.m:28:1: warning: no 'assign', 'retain', or 'copy'`
L796: `      attribute is specified - 'assign' is assumed`
L797: `@property id prop4;`
L798: `^`
L799: `Modules/objc/test/properties.m:28:1: warning: default property attribute`
L800: `      'assign' not appropriate for non-gc object`
L801: `Modules/objc/test/properties.m:30:1: warning: no 'assign', 'retain', or 'copy'`
L802: `      attribute is specified - 'assign' is assumed`
L803: `@property(readwrite) id prop6;`
L804: `^`
L805: `Modules/objc/test/properties.m:30:1: warning: default property attribute`
L806: `      'assign' not appropriate for non-gc object`
L807: `Modules/objc/test/properties.m:35:1: warning: no 'assign', 'retain', or 'copy'`
L808: `      attribute is specified - 'assign' is assumed`
L809: `@property(getter=propGetter,setter=propSetter:) id prop11;`
L810: `^`
L811: `Modules/objc/test/properties.m:35:1: warning: default property attribute`
L812: `      'assign' not appropriate for non-gc object`
L813: `7 warnings generated.`
L814: `/usr/bin/clang -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.8-intel-2.7/Modules/objc/test/properties.o -o build/lib.macosx-10.8-intel-2.7/PyObjCTest/properties.so -framework CoreFoundation -framework Foundation -framework Carbon -isysroot /`
L815: `building 'PyObjCTest.protected' extension`
L857: `clang: warning: argument unused during compilation: '-mno-fused-madd'`
L858: `Modules/objc/test/testbndl.m:521:12: warning: implicit conversion loses integer`
L859: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L860: `        int len = strlen(arg);`
L861: `            ~~~   ^~~~~~~~~~~`
L862: `Modules/objc/test/testbndl.m:761:12: warning: implicit conversion loses integer`
L863: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L864: `        int len = strlen(*arg);`
L865: `            ~~~   ^~~~~~~~~~~~`
L866: `Modules/objc/test/testbndl.m:783:12: warning: implicit conversion loses integer`
L867: `      precision: 'size_t' (aka 'unsigned long') to 'int' [-Wshorten-64-to-32]`
L868: `        int len = strlen(*arg);`
L869: `            ~~~   ^~~~~~~~~~~~`
L870: `3 warnings generated.`
L871: `/usr/bin/clang -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.8-intel-2.7/Modules/objc/test/testbndl.o -o build/lib.macosx-10.8-intel-2.7/PyObjCTest/testbndl.so -framework CoreFoundation -framework Foundation -framework Carbon -isysroot /`
L872: `building 'PyObjCTest.testbndl2' extension`
L1137: `warning: no directories found matching 'source-deps'`
L1138: `warning: no previously-included files matching '.DS_Store' found anywhere in distribution`
L1139: `warning: no previously-included files matching '*.pyc' found anywhere in distribution`
L1140: `warning: no previously-included files matching '*.so' found anywhere in distribution`
L1541: `clang: warning: argument unused during compilation: '-mno-fused-madd'`

