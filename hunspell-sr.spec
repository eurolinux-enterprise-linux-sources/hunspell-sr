Name: hunspell-sr
Summary: Serbian hunspell dictionaries
%define upstreamid 20100920
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://extensions.services.openoffice.org/e-files/1572/6/dict-sr.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/dict-sr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv3
BuildArch: noarch
Requires: hunspell
Provides: hunspell-bs = %{version}-%{release}

%description
Serbian hunspell dictionaries.

%package -n hyphen-sr
Requires: hyphen
Summary: Serbian hyphenation rules
Group: Applications/Text
Provides: hyphen-bs = %{version}-%{release}

%description -n hyphen-sr
Serbian hyphenation rules.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sr.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.dic
cp -p sr.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sr_YU.aff
cp -p sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.dic
cp -p sr-Latn.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sh_YU.aff

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_sr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sr_YU.dic
cp -p hyph_sr-Latn.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_sh_YU.dic

sr_YU_aliases="sr_ME sr_RS"
sh_YU_aliases="sh_ME sh_RS bs_BA"

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
for lang in $sr_YU_aliases; do
	ln -s sr_YU.aff $lang.aff
	ln -s sr_YU.dic $lang.dic
done
for lang in $sh_YU_aliases; do
	ln -s sh_YU.aff $lang.aff
	ln -s sh_YU.dic $lang.dic
done
popd

pushd $RPM_BUILD_ROOT/%{_datadir}/hyphen/
for lang in $sr_YU_aliases; do
	ln -s hyph_sr_YU.dic "hyph_"$lang".dic"
done
for lang in $sh_YU_aliases; do
	ln -s hyph_sh_YU.dic "hyph_"$lang".dic"
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc registration/license*.txt
%{_datadir}/myspell/*

%files -n hyphen-sr
%defattr(-,root,root,-)
%doc registration/license*.txt
%{_datadir}/hyphen/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100920-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 05 2012 Caolán McNamara <caolanm@redhat.com> - 0.20100920-5
- clarify license

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100920-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100920-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100920-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100920-1
- latest version

* Thu Aug 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100818-1
- latest version

* Thu Jul 08 2010 Caolán McNamara <caolanm@redhat.com> - 0.20090511-4
- include licences in all subpackages

* Tue Jan 05 2010 Caolán McNamara <caolanm@redhat.com> - 0.20090511-3
- fix rpmlint warning

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090511-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090511-1
- latest version

* Tue May 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090213-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080711-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 11 2008 Caolán McNamara <caolanm@redhat.com> - 0.20080711-1
- initial version
