%define prj     Horde_IMAP

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:		horde-imap
Version:	0.0.3
Release:	%mkrel 2
Summary:	Horde Browser package
License:	LGPL
Group:		Networking/Mail
Url:		http://pear.horde.org/index.php?package=%{prj}
Source0:	%{prj}-%{version}.tgz
BuildArch:	noarch
Requires(pre):  php-pear
Requires:	horde-framework
Requires:	horde-cache
Requires:	php-pear-channel-horde
BuildRequires:	php-pear
BuildRequires:	php-pear-channel-horde

%description
The Horde_UI:: class provides an API for getting information about
the current user's userinterface and its capabilities.

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde
%dir %{peardir}/Horde/IMAP/ACL.php
%{peardir}/Horde/IMAP/Admin.php
%{peardir}/Horde/IMAP/Cache.php
%{peardir}/Horde/IMAP/Search.php
%{peardir}/Horde/IMAP/Sort.php
%{peardir}/Horde/IMAP/Thread.php
%{peardir}/Horde/IMAP/Tree.php
%{peardir}/Horde/IMAP/ACL/rfc2086.php
%{peardir}/Horde/IMAP/ACL/rfc4314.php




%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-2mdv2011.0
+ Revision: 564028
- Increased release for rebuild

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.3-1mdv2010.1
+ Revision: 509405
- import horde-imap


