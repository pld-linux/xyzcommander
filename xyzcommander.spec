%define shortname xyzcmd
%define progrelease beta
Summary:	XYZCommander - Console file manager
Summary(hu.UTF-8):	XYZCommander - konzolos fájlkezelő
Name:		xyzcommander
Version:	0.0.1
Release:	0.1
License:	LGPL
Group:		Applications/Shells
Source0:	http://xyzcmd.googlecode.com/files/%{shortname}-%{version}-%{progrelease}.tar.bz2
# Source0-md5:	2fff6000ba29e146c469fdd6c4d3ebf9
URL:		http://xyzcmd.syhpoon.name
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XYZCommander - Console file manager. Beta version!

%description -l hu.UTF-8
XYZCommander - konzolos fájlkezelő. Béta verzió!

%prep
%setup -q -n %{shortname}-%{version}-%{progrelease}
%{__sed} -i "s,doc\/xyzcmd,doc\/xyzcmd-%{version}-%{progrelease},g" setup.py

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{shortname}
%doc %{_docdir}/%{shortname}-%{version}-%{progrelease}
%{py_sitescriptdir}/libxyz
%{py_sitescriptdir}/*.egg-info
%dir %{_datadir}/xyzcmd
%{_datadir}/xyzcmd/conf
%{_datadir}/xyzcmd/plugins
%{_datadir}/xyzcmd/skins
