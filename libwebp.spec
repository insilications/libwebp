#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libwebp
Version  : 1.1.0
Release  : 33
URL      : file:///insilications/build/clearlinux/packages/libwebp/libwebp-v1.1.0.zip
Source0  : file:///insilications/build/clearlinux/packages/libwebp/libwebp-v1.1.0.zip
Summary  : Library for the WebP graphics format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: libwebp-bin = %{version}-%{release}
Requires: libwebp-lib = %{version}-%{release}
Requires: libwebp-man = %{version}-%{release}
BuildRequires : SDL-dev
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : freeglut-dev
BuildRequires : giflib-dev
BuildRequires : glu-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(sdl)
BuildRequires : sed
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
__   __  ____  ____  ____
/  \\/  \/  _ \/  _ )/  _ \
\       /   __/  _  \   __/
\__\__/\____/\_____/__/ ____  ___
/ _/ /    \    \ /  _ \/ _/
/  \_/   / /   \ \   __/  \__
\____/____/\_____/_____/____/v1.1.0

%package bin
Summary: bin components for the libwebp package.
Group: Binaries

%description bin
bin components for the libwebp package.


%package dev
Summary: dev components for the libwebp package.
Group: Development
Requires: libwebp-lib = %{version}-%{release}
Requires: libwebp-bin = %{version}-%{release}
Provides: libwebp-devel = %{version}-%{release}
Requires: libwebp = %{version}-%{release}

%description dev
dev components for the libwebp package.


%package lib
Summary: lib components for the libwebp package.
Group: Libraries

%description lib
lib components for the libwebp package.


%package man
Summary: man components for the libwebp package.
Group: Default

%description man
man components for the libwebp package.


%package staticdev
Summary: staticdev components for the libwebp package.
Group: Default
Requires: libwebp-dev = %{version}-%{release}

%description staticdev
staticdev components for the libwebp package.


%prep
%setup -q -n libwebp-v1.1.0
cd %{_builddir}/libwebp-v1.1.0

%build
## build_prepend content
find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
find . -type f -name 'config.status' -exec touch {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595072143
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-common -Wno-error -Wp,-D_REENTRANT
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -fno-common -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags1 end
%autogen  --enable-libwebpdemux --enable-libwebpmux --enable-static --enable-shared --enable-libwebpdecoder --enable-libwebpextras --enable-gl --enable-sdl --disable-maintainer-mode
## make_prepend content
find . -type f -name 'Makefile*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#
find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1595072143
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cwebp
/usr/bin/dwebp
/usr/bin/gif2webp
/usr/bin/img2webp
/usr/bin/vwebp
/usr/bin/webpinfo
/usr/bin/webpmux

%files dev
%defattr(-,root,root,-)
/usr/include/webp/decode.h
/usr/include/webp/demux.h
/usr/include/webp/encode.h
/usr/include/webp/mux.h
/usr/include/webp/mux_types.h
/usr/include/webp/types.h
/usr/lib64/libwebp.so
/usr/lib64/libwebpdecoder.so
/usr/lib64/libwebpdemux.so
/usr/lib64/libwebpmux.so
/usr/lib64/pkgconfig/libwebp.pc
/usr/lib64/pkgconfig/libwebpdecoder.pc
/usr/lib64/pkgconfig/libwebpdemux.pc
/usr/lib64/pkgconfig/libwebpmux.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libwebp.so.7
/usr/lib64/libwebp.so.7.1.0
/usr/lib64/libwebpdecoder.so.3
/usr/lib64/libwebpdecoder.so.3.1.0
/usr/lib64/libwebpdemux.so.2
/usr/lib64/libwebpdemux.so.2.0.6
/usr/lib64/libwebpmux.so.3
/usr/lib64/libwebpmux.so.3.0.5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cwebp.1
/usr/share/man/man1/dwebp.1
/usr/share/man/man1/gif2webp.1
/usr/share/man/man1/img2webp.1
/usr/share/man/man1/vwebp.1
/usr/share/man/man1/webpinfo.1
/usr/share/man/man1/webpmux.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libwebp.a
/usr/lib64/libwebpdecoder.a
/usr/lib64/libwebpdemux.a
/usr/lib64/libwebpmux.a
