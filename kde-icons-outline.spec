#$Revision: 1.2 $, $Date: 2007-02-12 00:48:58 $

%define         _name	outline

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):   Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	040521
Release:	1
License:	GPL
Group:		Themes
Source0:	http://linuxcult.com/crystal/icons/%{_name}.tar.gz
# Source0-md5:	8a8426866fe344041c8140fe5234e952
URL:		http://www.everaldo.com/portfolio/bottons/gui/outline.html
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Outilne is an icon theme based on crystal (the default KDE icon theme), 
which adds black solid outlines to crystal icons.

%description -l pl.UTF-8
Outline to motyw ikon oparty o Crystal (domyślny motyw ikon w KDE),
który dodaje do tych ikon czarną obwódkę.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
