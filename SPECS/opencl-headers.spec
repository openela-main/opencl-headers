%global commit0 d65bcc5123f93ce7c6b2a3c164fed35c423fc83d
%global date 20201007
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global cl_hpp_ver 2.0.12

Name:           opencl-headers
Version:        3.0
Release:        6%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        OpenCL (Open Computing Language) header files

License:        MIT
URL:            https://www.khronos.org/registry/cl/

Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/%{commit0}/OpenCL-Headers-%{commit0}.tar.gz#/OpenCL-Headers-%{shortcommit0}.tar.gz
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/v%{cl_hpp_ver}.zip#/OpenCL-CLHPP-%{cl_hpp_ver}.zip
# OCL 1.2 compatibility
Source2:        https://www.khronos.org/registry/cl/api/2.1/cl.hpp

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{commit0}

%{uncompress:%{SOURCE1}}
cp -p OpenCL-CLHPP-%{cl_hpp_ver}/include/CL/cl2.hpp %{SOURCE2} .

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 *hpp CL/* -t %{buildroot}%{_includedir}/CL/
# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*

%files
%dir %{_includedir}/CL
%{_includedir}/CL/opencl.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/cl.hpp

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 3.0-6.20201007gitd65bcc5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 3.0-5.20201007gitd65bcc5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Dave Airlie <airlied@redhat.com> - 3.0-2git20201007gitd65bcc5
- Update latest headers

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Karol Herbst <kherbst@redhat.com> - 3.0-1.20200512gitd082d42
- Update to latest upstream, pick up new extensions for OpenCL-CTS build fix
- Rework CLHPP handling as file is not downloadable anymore
- Bump CLHPP version to 2.0.12

* Wed May 20 2020 Karol Herbst <kherbst@redhat.com> - 3.0-0.20200512git5cc337c
- Update to latest upstream, pick up new extensions for OpenCL-CTS build fix
- Bump CLHPP version to 2.0.11

* Fri Feb 28 2020 Karol Herbst <kherbst@redhat.com> - 2.2-7.20200218git96f5bde
- Update to latest upstream, pick up new extensions for OpenCL-CTS build fix

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6.20190205git49f07d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5.20190205git49f07d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Dave Airlie <airlied@redhat.com> - 2.2-4.20190205git49f07d3
- Update to latest upstream, pick up the ppc fix

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3.20180306gite986688
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2.20180306gite986688
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Simone Caronni <negativo17@gmail.com> - 2.2-1.20180306gite986688
- Update to 2.2.
- Use packaging guidelines for snapshots.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1-1
- Update to 2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Dave Airlie <airlied@redhat.com> - 1.2-8
- add cl_egl.h

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 1.2-5
- Pull patch application into pre

* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 1.2-4
- Add patch for cl.hpp to be usable on arm rhbz#1027199

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Dave Airlie <airlied@redhat.com> 1.2-2
- fix missing dir and remove defattr.

* Wed Feb 27 2013 Dave Airlie <airlied@redhat.com> 1.2-1
- OpenCL header files from Khronos for OpenCL 1.2

