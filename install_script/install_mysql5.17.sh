mysql_src_path='/home/chenchao/src/mysql-5.6.36'
boost_src_path='/home/chenchao/src/boost_1_59_0'
mysql_install_path='/home/chenchao/env/mysql-5.6.36'
mysql_data_path=$mysql_install_path'/data'

cd $mysql_src_path

cmake \   
-DCMAKE_INSTALL_PREFIX= $mysql_install_path\   
-DMYSQL_DATADIR= $mysql_data_path\   
-DDEFAULT_CHARSET=utf8 \   
-DDEFAULT_COLLATION=utf8_general_ci \   
-DWITH_INNOBASE_STORAGE_ENGINE=1 \   
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \   
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \   
-DMYSQL_TCP_PORT=3306 \   
-DENABLE_DOWNLOADS=1  

make
make install
make clean
