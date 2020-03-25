git clone https://github.com/CRG-Barcelona/libbeato.git
git clone https://github.com/CRG-Barcelona/bwtool.git
cd libbeato/
git checkout 0c30432
./configure --prefix=$HOME CFLAGS="-g -O0 -I${HOME}/include" LDFLAGS=-L${HOME}/lib > /dev/null 2>&1
make > /dev/null 2>&1
make install > /dev/null 2>&1
cd ../bwtool/
./configure --prefix=$HOME CFLAGS="-g -O0 -I${HOME}/include" LDFLAGS=-L${HOME}/lib > /dev/null 2>&1
make > /dev/null 2>&1
make install > /dev/null 2>&1
cd ..