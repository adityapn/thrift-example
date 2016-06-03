==========================================================
Thrift example in Python
==========================================================
How to set up Thrift in Mac using brew

brew install thrift
==========================================================
First create hello.thrift with request structure and 
functions

Then Generate the libs for language (in case python)
thrift -r --gen py hello.thrift
==========================================================

