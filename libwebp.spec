#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwebp
Version  : 1.0.0
Release  : 21
URL      : https://github.com/webmproject/libwebp/archive/v1.0.0.tar.gz
Source0  : https://github.com/webmproject/libwebp/archive/v1.0.0.tar.gz
Summary  : Library for the WebP graphics format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libwebp-bin
Requires: libwebp-lib
Requires: libwebp-doc
BuildRequires : freeglut-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : go
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : mesa-dev32
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : sed
BuildRequires : setuptools

%description
__   __  ____  ____  ____
/  \\/  \/  _ \/  _ )/  _ \
\       /   __/  _  \   __/
\__\__/\____/\_____/__/ ____  ___
/ _/ /    \    \ /  _ \/ _/
/  \_/   / /   \ \   __/  \__
\____/____/\_____/_____/____/v1.0.0

%package bin
Summary: bin components for the libwebp package.
Group: Binaries

%description bin
bin components for the libwebp package.


%package dev
Summary: dev components for the libwebp package.
Group: Development
Requires: libwebp-lib
Requires: libwebp-bin
Provides: libwebp-devel

%description dev
dev components for the libwebp package.


%package dev32
Summary: dev32 components for the libwebp package.
Group: Default
Requires: libwebp-lib32
Requires: libwebp-bin
Requires: libwebp-dev

%description dev32
dev32 components for the libwebp package.


%package doc
Summary: doc components for the libwebp package.
Group: Documentation

%description doc
doc components for the libwebp package.


%package lib
Summary: lib components for the libwebp package.
Group: Libraries

%description lib
lib components for the libwebp package.


%package lib32
Summary: lib32 components for the libwebp package.
Group: Default

%description lib32
lib32 components for the libwebp package.


%prep
%setup -q -n libwebp-1.0.0
pushd ..
cp -a libwebp-1.0.0 build32
popd
pushd ..
cp -a libwebp-1.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526011056
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
%autogen --disable-static --enable-libwebpdemux
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static --enable-libwebpdemux --disable-gl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell "
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell "
export LDFLAGS="$LDFLAGS -m64 -march=haswell "
%autogen --disable-static --enable-libwebpdemux  --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1526011056
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cwebp
/usr/bin/dwebp
/usr/bin/haswell/cwebp
/usr/bin/haswell/dwebp

%files dev
%defattr(-,root,root,-)
/usr/include/webp/decode.h
/usr/include/webp/demux.h
/usr/include/webp/encode.h
/usr/include/webp/mux_types.h
/usr/include/webp/types.h
/usr/lib64/haswell/libwebp.so
/usr/lib64/haswell/libwebpdemux.so
/usr/lib64/libwebp.so
/usr/lib64/libwebpdemux.so
/usr/lib64/pkgconfig/libwebp.pc
/usr/lib64/pkgconfig/libwebpdemux.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so
/usr/lib32/libwebpdemux.so
/usr/lib32/pkgconfig/32libwebp.pc
/usr/lib32/pkgconfig/32libwebpdemux.pc
/usr/lib32/pkgconfig/libwebp.pc
/usr/lib32/pkgconfig/libwebpdemux.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libwebp.so.7
/usr/lib64/haswell/libwebp.so.7.0.2
/usr/lib64/haswell/libwebpdemux.so.2
/usr/lib64/haswell/libwebpdemux.so.2.0.4
/usr/lib64/libwebp.so.7
/usr/lib64/libwebp.so.7.0.2
/usr/lib64/libwebpdemux.so.2
/usr/lib64/libwebpdemux.so.2.0.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so.7
/usr/lib32/libwebp.so.7.0.2
/usr/lib32/libwebpdemux.so.2
/usr/lib32/libwebpdemux.so.2.0.4
