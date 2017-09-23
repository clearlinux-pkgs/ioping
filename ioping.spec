#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ioping
Version  : 1.0
Release  : 1
URL      : https://github.com/koct9i/ioping/archive/v1.0.tar.gz
Source0  : https://github.com/koct9i/ioping/archive/v1.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%prep
%setup -q -n ioping-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506185760
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1506185760
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/local/bin/ioping
/usr/local/share/man/man1/ioping.1
