# Setup vim syntax


1 Create ~/.vim/after/syntax/jack.vim file with content:
```
syn keyword jackType constructor method function
syn keyword jackType int boolean char void
syn keyword jackType var static field
syn keyword jackStatement let do
syn keyword jackConstant true false null

let b:current_syntax = "jack"
hi def link jackType Type
hi def link jackStatement Statement
hi def link jackConstant Constant
```


2 Create ~.vim/ftdetect/jack.vim file with content:
```
autocmd BufNewFile,BufRead *.jack set filetype=jack
```


3 Create symbolic links into /usr/share/vim/vim74/syntax
from jack to java
```
  $ cd /usr/share/vim/vim74/syntax
  $ ln -s java.vim jack.vim
```
