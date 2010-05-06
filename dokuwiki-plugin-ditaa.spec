# TODO
# - use system ditaa jar
%define		plugin		ditaa
Summary:	Converts ASCII-Flowcharts to png-Graphics using ditaa
Name:		dokuwiki-plugin-%{plugin}
Version:	20100409
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://download.github.com/splitbrain-dokuwiki-plugin-ditaa-596e8bd.zip
# Source0-md5:	07e29cd1987d6fd4808eb1e21145a23b
URL:		http://wiki.splitbrain.org/plugin:ditaa
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20091225
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Ditaa is a tool to convert ASCII-Art flowcharts and diagrams into
their graphical equivalents. This Plugin integrates this feature into
DokuWiki.

You need java installed locally to use local rendering, it defaults to
render via <http://ditaa.org>.

%prep
%setup -qc
# for githug urls:
mv *-%{plugin}-*/* .

version=$(awk '/date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

# ditaa license and history not useful here
rm ditaa/COPYING
rm ditaa/HISTORY

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}


# find locales
%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/conf
%{plugindir}/*.txt
%{plugindir}/*.php

# TODO: system pkg
%dir %{plugindir}/ditaa
%{plugindir}/ditaa/ditaa0_9.jar
