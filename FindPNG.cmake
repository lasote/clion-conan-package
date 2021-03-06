
find_path(PNG_INCLUDE_DIR NAMES png.h PATHS ${CONAN_INCLUDE_DIRS_LIBPNG})
find_library(PNG_LIBRARY NAMES ${CONAN_LIBS_LIBPNG} PATHS ${CONAN_LIB_DIRS_LIBPNG})

MESSAGE("** PNG ALREADY FOUND BY CONAN!")
SET(PNG_FOUND TRUE)
MESSAGE("** FOUND PNG:  ${PNG_LIBRARY}")
MESSAGE("** FOUND PNG INCLUDE:  ${PNG_INCLUDE_DIR}")

set(PNG_INCLUDE_DIRS ${PNG_INCLUDE_DIR})
set(PNG_LIBRARIES ${PNG_LIBRARY})

mark_as_advanced(PNG_LIBRARY PNG_INCLUDE_DIR)


set(PNG_MAJOR_VERSION "1")
set(PNG_MINOR_VERSION "6")
set(PNG_PATCH_VERSION "23")
