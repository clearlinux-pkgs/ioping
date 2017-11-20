#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ioping
Version  : 1.0
Release  : 3
URL      : https://github.com/koct9i/ioping/archive/v1.0.tar.gz
Source0  : https://github.com/koct9i/ioping/archive/v1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: ioping-bin
Requires: ioping-doc

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%package bin
Summary: bin components for the ioping package.
Group: Binaries

%description bin
bin components for the ioping package.


%package doc
Summary: doc components for the ioping package.
Group: Documentation

%description doc
doc components for the ioping package.


%prep
%setup -q -n ioping-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511215003
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1511215003
rm -rf %{buildroot}
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ioping

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
