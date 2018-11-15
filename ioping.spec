#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ioping
Version  : 1.1
Release  : 6
URL      : https://github.com/koct9i/ioping/archive/v1.1.tar.gz
Source0  : https://github.com/koct9i/ioping/archive/v1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: ioping-bin = %{version}-%{release}
Requires: ioping-license = %{version}-%{release}
Requires: ioping-man = %{version}-%{release}

%description
This tool lets you monitor I/O latency in real time, in a way
similar to how ping(1) does for network latency.

%package bin
Summary: bin components for the ioping package.
Group: Binaries
Requires: ioping-license = %{version}-%{release}
Requires: ioping-man = %{version}-%{release}

%description bin
bin components for the ioping package.


%package license
Summary: license components for the ioping package.
Group: Default

%description license
license components for the ioping package.


%package man
Summary: man components for the ioping package.
Group: Default

%description man
man components for the ioping package.


%prep
%setup -q -n ioping-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542319248
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542319248
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ioping
cp LICENSE %{buildroot}/usr/share/package-licenses/ioping/LICENSE
%make_install PREFIX=/usr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ioping

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ioping/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ioping.1
