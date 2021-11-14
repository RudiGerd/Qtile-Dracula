call plug#begin('~/.vim/plugged')
Plug 'scrooloose/syntastic'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"Plug 'morhetz/gruvbox'
"Plug 'bundle/ctrlp.vim'
Plug 'preservim/tagbar'
call plug#end()

let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tagbar#enabled = 1
set number relativenumber
set nu rnu
syntax on
set scrolloff=8
set ruler
"colorscheme torte
"colourscheme industry"
set autoindent
set matchpairs+=<:>
