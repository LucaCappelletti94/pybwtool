apt-get install zlib1g-dev
git clone https://github.com/CRG-Barcelona/libbeato.git
git clone https://github.com/CRG-Barcelona/bwtool.git
cd libbeato/
git checkout 0c30432 
./configure --prefix=$HOME CFLAGS="-g -O0 -I${HOME}/include" LDFLAGS=-L${HOME}/lib
make
make install
cd ../bwtool/
./configure --prefix=$HOME CFLAGS="-g -O0 -I${HOME}/include" LDFLAGS=-L${HOME}/lib
make
make install
cd ..
