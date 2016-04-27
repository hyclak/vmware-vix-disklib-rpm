%global releasever 6.0.2
%global buildver 3566099

# Disable debug package
%global debug_package %{nil}

# Disable automatic dependency and provides information
%define __find_provides %{nil} 
%define __find_requires %{nil} 
%define _use_internal_dependency_generator 0
Autoprov: 0
Autoreq: 0

Name:           vmware-vix-disklib
Version:        %{releasever}
Release:        1%{?dist}
Summary:        The Virtual Disk Development Kit (VDDK) is a collection of C libraries, code samples, utilities, and documentation to help you create or access VMware virtual disk storage.

License:        Proprietary
URL:            https://developercenter.vmware.com/web/sdk/60/vddk
Source0:        VMware-vix-disklib-%{releasever}-%{buildver}.x86_64.tar.gz
NoSource:	0

BuildRequires:  coreutils
#Requires:

%description
The Virtual Disk Development Kit (VDDK) is a collection of C libraries, code samples, utilities, and documentation to help you create or access VMware virtual disk storage. The kit includes:

* The Virtual Disk and Disk Mount libraries, sets of C function calls to manipulate virtual disk files. C++ code samples that you can build with either Visual Studio or the GNU C compiler
* Documentation about the VDDK libraries and the command-line utilities
* The Disk Mount utility to access files and file systems in offline virtual disks on Windows or Linux guest virtual machines
* The Virtual Disk Manager utility to manipulate offline virtual disk on Windows or Linux (clone, create, relocate, rename, grow, shrink, or defragment)

%prep
%setup -n %{name}-distrib

%build

%install
rm -rf $RPM_BUILD_ROOT
%__mkdir_p %{buildroot}/usr/lib/vmware-vix-disklib
%__cp -r bin64 include lib64 %{buildroot}/usr/lib/%{name}
%__ln_s /usr/lib/vmware-vix-disklib/lib64/libvixDiskLib.so %{buildroot}/usr/lib/libvixDiskLib.so
%__ln_s /usr/lib/vmware-vix-disklib/lib64/libvixDiskLib.so.6 %{buildroot}/usr/lib/libvixDiskLib.so.6

%files
/usr/lib/%{name}/
/usr/lib/libvixDiskLib.so*
%doc doc/*

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%changelog
* Wed Apr 27 2016 Matt Hyclak <matt.hyclak@cbts.net> 6.0.2-1
Initial Build
