Summary:	Quake II - demo game data
Summary(pl.UTF-8):	Quake II - dane w wersji demo
Name:		quake2-data-demo
Version:	3.14
Release:	1
License:	free use, limited distribution
Group:		Applications/Games
Source0:	ftp://ftp.idsoftware.com/idstuff/quake2/q2-314-demo-x86.exe
# NoSource0-md5:	4d1cd4618e80a38db59304132ea0856c
NoSource:	0
URL:		http://www.idsoftware.com/games/quake/quake2/
BuildRequires:	unzip
# quake2 or quake2forge
Requires:	%{_datadir}/quake2/baseq2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quake II - demo game data.

%description -l pl.UTF-8
Quake II - dane w wersji demo.

%prep
%setup -q -c -T
unzip -qq %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/quake2/baseq2

install Install/Data/baseq2/pak0.pak $RPM_BUILD_ROOT%{_datadir}/quake2/baseq2
cp -rf Install/Data/baseq2/players $RPM_BUILD_ROOT%{_datadir}/quake2/baseq2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt Install/Data/DOCS
%{_datadir}/quake2/baseq2/pak0.pak
%{_datadir}/quake2/baseq2/players
