ngx_path='/home/chenchao/src/nginx-1.11.2'
ndk_path='/home/chenchao/src/ngx_devel_kit-0.3.0'
luangx_path='/home/chenchao/src/lua-nginx-module-0.10.8'

pcre_path='/home/chenchao/src/pcre2-10.23'
pcre_path='/home/chenchao/env/lib/pcre-8.40'
zlib_path='/home/chenchao/env/lib/zlib-1.2.11'
openssl_path='/home/chenchao/env/lib/openssl-1.1.0e'
openssl_path='/home/chenchao/src/openssl-1.1.0e'

instal_path='/home/chenchao/env/nginx-1.11.2'

export LUAJIT_LIB=/home/chenchao/env/lib/luajit2.0.5/lib
export LUAJIT_INC=/home/chenchao/env/lib/luajit2.0.5/include/luajit-2.0

cd $ngx_path
./configure --prefix=$instal_path \
	--with-ld-opt="-Wl,-rpath,/home/chenchao/env/lib/luajit2.0.5/lib" \
	--add-module=$ndk_path \
	--add-module=$luangx_path \
	--with-http_ssl_module \
#	--with-pcre=$pcre_path\
	--with-zlib=$zlib_path 
#	--with-openssl=$openssl_path

make -j2
make install


