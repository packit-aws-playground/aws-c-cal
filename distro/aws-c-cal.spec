Name:           aws-c-cal
Version:        0.5.12
Release:        7%{?dist}
Summary:        AWS Crypto Abstraction Layer

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-cal-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel
BuildRequires:  openssl-devel

Requires:       aws-c-common-libs
Requires:       openssl
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global debug_package %{nil}

%description
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%package libs
Summary:        AWS Crypto Abstraction Layer

%description libs
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%package devel
Summary:        AWS Crypto Abstraction Layer
Requires:       aws-c-common-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives


%prep
%autosetup -p1


%build
echo something

%install
mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/something

%files
%{_bindir}/something

%changelog
* Thu Feb 24 2022 David Duncan <davdunc@amazon.com> - 0.5.12-7
- Include check and ctest section in spec

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.5.12-6
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-4
- Move sha256_profile executable to standard package

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.5.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-1
- Initial package development
