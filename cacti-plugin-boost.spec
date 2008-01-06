%define		namesrc	boost	
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Boost
Summary(pl.UTF-8):	Wtyczka do Cacti - Boost
Name:		cacti-plugin-boost
Version:	1.7
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	49c5989cc421781fb8e983d70ba2bcac
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Cacti plugin that boosts Cacti performance especially for large sites.

%description -l pl.UTF-8
Wtyczka Cacti zwiększająca jego wydajność, szczególnie w przypadku
dużych serwisów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README 
%{webcactipluginroot}
