# -*- coding: utf-8 -*-

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

# -- !! Only for verbosity of code !! -- #

# -- Name generated from winerror.h -- #
EXIT_SUCCESS            = 0

EXIT_FAILURE            = 1
ERROR_FILE_NOT_FOUND    = 1
ERROR_PATH_NOT_FOUND    = 1
ERROR_BAD_ENVIRONMENT   = 1
ERROR_INVALID_PARAMETER = 1
ERROR_BAD_ARGUMENTS     = 1
ERROR_INVALID_FUNCTION  = 1
ERROR_INVALID_DRIVE 	= 1

# -- Name generated manually -- #
ERROR_FILE_EMPTY    = 1

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Error (Exception):
	pass