# TODO
# - sync pl
# - init.d processes
%define		plugin boost
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	Large Site Performance Booster for Cacti
Summary(pl.UTF-8):	Wtyczka do Cacti - Boost
Name:		cacti-plugin-%{plugin}
Version:	5.1
Release:	7
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:boost-v%{version}-1.tgz
# Source0-md5:	31bda9b46d933e61bdcd77243928c89c
Patch0:		paths.patch
Patch1:		chmod.patch
URL:		http://docs.cacti.net/plugin:boost
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	cacti >= 0.8.7g-6
Requires:	cacti(pia) >= 2.8
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(date)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}
%define		cachedir		/var/cache/cacti/%{plugin}

%description
Cacti plugin that boosts Cacti performance especially for large sites.

This plugin boost's Cacti performance especially for Large Sites. It
does this by introducing three new features to Cacti.

First, it caches recently viewed images to a public Cache folder for
all users to share.

Second, it introduces an "on demand" RRD update feaure to Cacti. This
feature will only update the RRD files when there is demand on the
system to view a graph. The RRD's will be updated just before the
Graph is rendered by the web server. Then, on a predetermined
schedule, it conducts a batch update's of all remaining RRD's.

Lastly, it introduces an RRD update service to Cacti. This service
allows you to add multiple Cacti servers to your web farm allowing all
the servers to participate in the "on demand" RRD update and viewing
process.

%description -l pl.UTF-8
Wtyczka Cacti zwiększająca jego wydajność, szczególnie w przypadku
dużych serwisów.

%prep
%setup -qc
%undos -f php
cd %{plugin}
%patch0 -p1
%patch1 -p1
cd -

mv %{plugin}/{README,LICENSE,cacti_rrdsvc} .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{cachedir}}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{plugindir}
%attr(770,root,http) %dir %{cachedir}
