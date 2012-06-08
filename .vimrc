set visualbell
set noerrorbells
set nocompatible
syntax on
set autoindent
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set ruler
set incsearch
set virtualedit=all
set nu
set guioptions-=T
set guioptions-=m
set backspace=indent,eol,start
set wildmenu
set wildmode=longest,list
set ic
set scs
set cul
set switchbuf=split,usetab
filetype plugin indent on
if !has("gui_running")
    set t_Co=256
    colorscheme jellybeans
else
    colorscheme jellybeans
endif

set winminheight=0

	map <C-J> <C-W>j<C-W>_
	map <C-K> <C-W>k<C-W>_
	map <C-L> <C-W>l<C-W>_
	map <C-H> <C-W>h<C-W>_
	map <C-K> <C-W>k<C-W>_
    nnoremap j gj
    nnoremap k gk
	map <S-H> gT
	map <S-L> gt


autocmd BufRead *.py set makeprg=python\ -c\ \"import\ py_compile,sys;\ sys.stderr=sys.stdout;\ py_compile.compile(r'%')\"
autocmd BufRead *.py set efm=%C\ %.%#,%A\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m
autocmd FileType python set omnifunc=pythoncomplete#Complete
autocmd BufRead *.java set makeprg=ant
autocmd BufRead *.java set efm=%A\ %#[javac]\ %f:%l:\ %m,%-Z\ %#[javac]\ %p^,%-C%.%#
autocmd BufRead *.java set noexpandtab
autocmd BufRead *.jinc set filetype=jsp
autocmd BufRead *.email set filetype=velocity

" Smart commenting - ,c to comment a line and ,u to uncomment
au FileType haskell,vhdl,ada let b:comment_leader = '-- '
au FileType vim let b:comment_leader = '" '
au FileType c,cpp,java let b:comment_leader = '// '
au FileType sh,make,python let b:comment_leader = '# '
au FileType tex let b:comment_leader = '% '
noremap <silent> ,c :<C-B>sil <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:noh<CR>
noremap <silent> ,u :<C-B>sil <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:noh<CR> 

function! InsertTabWrapper()
      let col = col('.') - 1
      if !col || getline('.')[col - 1] !~ '\k'
          return "\<tab>"
      else
          return "\<c-p>"
      endif
endfunction

inoremap <tab> <c-r>=InsertTabWrapper()<cr>

set foldcolumn=3
set foldmethod=marker
let g:showmarks_enable=0
let g:showmarks_include='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
function! PreviewColor(rgbval)
	exec "hi temp guibg=" . a:rgbval
	echo a:rgbval
	echohl temp | echo "          " | echohl None
	echohl temp | echo "          " | echohl None
	echohl temp | echo "          " | echohl None
	echohl temp | echo "          " | echohl None
	echohl temp | echo "          " | echohl None
	echohl temp | echo "          " | echohl None
endfunction

vmap <F5> "ry :call PreviewColor(@r)<CR>

autocmd Syntax html,vim inoremap < <lt>><Left>

function! SetupScreen(s)
    let g:screen_sessionname = a:s
    let g:screen_windowname = "1"
endfunction

nmap ,t :NERDTree<Enter>

set guifont=Menlo:h12

