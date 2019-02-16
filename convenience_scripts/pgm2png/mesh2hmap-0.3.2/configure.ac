#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_INIT(src/main.c)

PACKAGE=mesh2hmap
VERSION=0.3

AM_INIT_AUTOMAKE(PACKAGE, VERSION)


# Make sure c99 CFLAG is set
CFLAGS="$CFLAGS -std=c99"

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([stdlib.h string.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST
AC_C_INLINE
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([pow strchr])

AC_CONFIG_FILES([Makefile
                 src/Makefile
		 man/Makefile])
AC_OUTPUT
