#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libwebp
Version  : 0.6.0
Release  : 6
URL      : https://github.com/webmproject/libwebp/archive/v0.6.0.tar.gz
Source0  : https://github.com/webmproject/libwebp/archive/v0.6.0.tar.gz
Summary  : Library for the WebP graphics format (decode only)
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
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libpng-dev32
BuildRequires : mesa-dev32
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
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
\____/____/\_____/_____/____/v0.6.0

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
%setup -q -n libwebp-0.6.0
pushd ..
cp -a libwebp-0.6.0 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487353541
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%autogen --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%autogen --disable-static  --disable-gl --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1487353541
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
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cwebp
/usr/bin/dwebp

%files dev
%defattr(-,root,root,-)
/usr/include/webp/decode.h
/usr/include/webp/encode.h
/usr/include/webp/types.h
/usr/lib64/libwebp.so
/usr/lib64/pkgconfig/libwebp.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so
/usr/lib32/pkgconfig/32libwebp.pc
/usr/lib32/pkgconfig/libwebp.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwebp.so.7
/usr/lib64/libwebp.so.7.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libwebp.so.7
/usr/lib32/libwebp.so.7.0.0
