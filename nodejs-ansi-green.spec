%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name ansi-green

Summary:       The color green, in ansi
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.1.1
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/ansi-green
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
The color green, in ansi.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-4
- Fix runtime dependency to use macro

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.1-3
- rebuilt

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.1-2
- Enable scl macros, fix license macro for el6

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 0.1.1-1
- Initial package
