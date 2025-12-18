# Wheel Library Bundling - Why and How

---

## The Problem

**torch-ttnn wheels bundle ~43MB of TT-Metal libraries that also exist in the ttnn PyPI package.**

This creates duplication:
- PyPI ttnn package: 43.7 MB (libtt_metal.so, libdevice.so, _ttnncpp.so, libtt_stl.so)
- torch-ttnn wheel: ~43 MB (same libraries bundled)
- **Total installed: ~87 MB**

---

## Why This Is Required

**Critical:** Without bundling, the wheel doesn't work for end-users.

### Issue 1: ttnn PyPI Wheel Missing libtracy.so

```
libtt_metal.so depends on → libtracy-b842b7dc.so.0.10.0
ttnn wheel includes:       libtt_metal.so ✅
ttnn wheel is MISSING:     libtracy*.so ❌

Result: Extension fails to load (library not found)
```

This is a **ttnn PyPI wheel packaging bug** (v0.62.0-dev20250916).

### Issue 2: Hash Suffix Mismatch

ttnn wheel uses hash-suffixed names:
- `libdevice-9738860f.so` (actual file)
- `libtracy-b842b7dc.so` (if it existed)

Our extension expects standard names:
- `libdevice.so`
- `libtracy.so.0.10.0`

**Result:** Even if libraries exist, linker can't find them.

### Issue 3: RUNPATH Doesn't Work Reliably

We set `RUNPATH=$ORIGIN/../../ttnn/build/lib` but:
- Python module loading is complex (not simple dlopen)
- RUNPATH only works for direct dependencies, not transitive
- Dynamic linker doesn't always honor RUNPATH in Python context

**Result:** Libraries exist in ttnn package but extension can't load them.

---

## Current Solution: Bundle Everything

**CMakeLists.txt bundles from submodule build:**
```cmake
install(FILES 
  libtt_metal.so
  libdevice.so
  libtt_stl.so
  libtracy.so + libtracy.so.0.10.0
  _ttnncpp.so
  DESTINATION torch_ttnn_cpp_extension/)
```

**Result:**
- Extension always finds libraries (`$ORIGIN` RPATH)
- No runtime errors
- Works for all end-users
- Wheel size: ~43MB (bundled libraries + extension + Python code)

---

## Trade-offs

| Approach | Size | Works | We Control | Possible |
|----------|------|-------|------------|----------|
| **Clean (RUNPATH only)** | ~500KB | ❌ No | ❌ No | ❌ No |
| **Bundle (current)** | ~43MB | ✅ Yes | ✅ Yes | ✅ Yes |
| **With submodule source** | 237MB | N/A | ✅ Yes | ✅ Avoid |

**Current approach: Reliability over size.**

---

## Possible Solution (Not Achievable Now)

**Would require tt-metal project to:**
1. Fix ttnn wheel: include libtracy.so
2. Remove hash suffixes or provide symlinks
3. Ensure all dependencies are present

**Then we could:**
- Remove bundling from CMakeLists.txt
- Rely on RUNPATH: `$ORIGIN/../../ttnn/build/lib`
- torch-ttnn wheel: ~500KB
- No duplication

**Why not possible:**
- We don't control ttnn PyPI wheel packaging
- Need working wheels now, can't wait for upstream fixes
- Bundling is the only reliable workaround

---

## For End-Users

**When installing:**
```bash
pip install torch-ttnn[pypi]
```

**What gets installed:**
- torch-ttnn wheel: ~43MB (our extension + bundled libraries)
- ttnn package: ~44MB (dependency, has duplicate libraries)
- Total: ~87MB

**Why this is acceptable:**
- **It works** - no library loading errors
- Guaranteed reliability for all users
- Only workaround until tt-metal fixes their wheel
- Self-contained - no dependency on ttnn package library locations
