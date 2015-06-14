%bcond_with    nonfree
%bcond_without x264
%bcond_without schroedinger
%bcond_without speex
%bcond_without v4l
%bcond_without openjpeg
%bcond_without libva
%bcond_without frei0r
%bcond_without opencv
%bcond_without libvpx
%bcond_without libass
%bcond_without gnutls
%bcond_without x265


%global libavutil_ver 54
%global libavcodec_ver 56
%global libavformat_ver 56
%global libavdevice_ver 56
%global libavfilter_ver 5
%global libswscale_ver 3
%global libswresample_ver 1
%global libpostproc_ver 53

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name: ffmpeg
Version: 2.7
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Libraries
Source: http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
#Source: http://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
URL: http://ffmpeg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel, bzip2-devel
BuildRequires: a52dec-devel
BuildRequires: libdc1394-devel, libraw1394-devel
%{?with_nonfree:BuildRequires: faac-devel}
BuildRequires: faad2-devel
BuildRequires: gsm-devel
BuildRequires: lame-devel
BuildRequires: libnut-devel
BuildRequires: libtheora-devel, libvorbis-devel
BuildRequires: xvidcore-devel
%{?with_x264:BuildRequires: x264-devel}
%{?with_openjpeg:BuildRequires: openjpeg-devel}
%{?with_schroedinger:BuildRequires: schroedinger-devel}
%{?with_speex:BuildRequires: speex-devel}
BuildRequires: opencore-amr-devel
BuildRequires: libvdpau-devel
BuildRequires: yasm
%{?with_libva:BuildRequires: libva-devel}
%{?with_frei0r:BuildRequires: frei0r-plugins-devel}
%{?with_opencv:BuildRequires: opencv-devel}
BuildRequires: rtmpdump-devel >= 2.2.f, openssl-devel
%{?with_libvpx:BuildRequires: libvpx-devel >= 0.9.6}
BuildRequires: xavs-devel
%{?with_libass:BuildRequires: libass-devel}
%{?with_gnutls:BuildRequires: gnutls-devel}
%{?with_x265:BuildRequires: x265-devel}
Requires: %{name}-libavutil_%{libavutil_ver}
Requires: %{name}-libavcodec_%{libavcodec_ver}
Requires: %{name}-libavformat_%{libavformat_ver}
Requires: %{name}-libavdevice_%{libavdevice_ver}
Requires: %{name}-libavfilter_%{libavfilter_ver}
Requires: %{name}-libswscale_%{libswscale_ver}
Requires: %{name}-libswresample_%{libswresample_ver}
Requires: %{name}-libpostproc_%{libpostproc_ver}

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

%package devel
Summary: FFmpeg shared library development files
Group: Development/Libraries
Requires: %{name}-libavutil_%{libavutil_ver} = %{version}-%{release}
Requires: %{name}-libavcodec_%{libavcodec_ver} = %{version}-%{release}
Requires: %{name}-libavformat_%{libavformat_ver} = %{version}-%{release}
Requires: %{name}-libavdevice_%{libavdevice_ver} = %{version}-%{release}
Requires: %{name}-libavfilter_%{libavfilter_ver} = %{version}-%{release}
Requires: %{name}-libswscale_%{libswscale_ver} = %{version}-%{release}
Requires: %{name}-libswresample_%{libswresample_ver} = %{version}-%{release}
Requires: %{name}-libpostproc_%{libpostproc_ver} = %{version}-%{release}
Requires: zlib-devel, libX11-devel, libXext-devel
Requires: a52dec-devel
Requires: libdc1394-devel, libraw1394-devel
%{?with_nonfree:Requires: faac-devel}
Requires: faad2-devel
Requires: gsm-devel
Requires: lame-devel
Requires: libvorbis-devel, libtheora-devel
Requires: xvidcore-devel
%{?with_x264:Requires: x264-devel}
%{?with_libass:Requires: libass-devel}
%{?with_gnutls:Requires: gnutls-devel}
%{?with_x265:Requires: x265-devel}

%description devel
This package contains the FFmpeg shared library development files

%package libavutil_%{libavutil_ver}
Summary: FFmpeg-libavutil shared library
Group: Development/Libraries

%description libavutil_%{libavutil_ver}
This package contain the FFmpeg-libavutil shared library

%package libavcodec_%{libavcodec_ver}
Summary: FFmpeg-libavcodec shared library
Group: Development/Libraries

%description libavcodec_%{libavcodec_ver}
This package contain the FFmpeg-libavcodec shared library

%package libavformat_%{libavformat_ver}
Summary: FFmpeg-libavformat shared library
Group: Development/Libraries

%description libavformat_%{libavformat_ver}
This package contain the FFmpeg-libavformat shared library

%package libavdevice_%{libavdevice_ver}
Summary: FFmpeg-libavdevice shared library
Group: Development/Libraries

%description libavdevice_%{libavdevice_ver}
This package contain the FFmpeg-libavdevice shared library

%package libavfilter_%{libavfilter_ver}
Summary: FFmpeg-libavfilter shared library
Group: Development/Libraries

%description libavfilter_%{libavfilter_ver}
This package contain the FFmpeg-libavfilter shared library

%package libswscale_%{libswscale_ver}
Summary: FFmpeg-libswscale shared library
Group: Development/Libraries

%description libswscale_%{libswscale_ver}
This package contain the FFmpeg-libswscale shared library

%package libswresample_%{libswresample_ver}
Summary: FFmpeg-libswresample shared library
Group: Development/Libraries

%description libswresample_%{libswresample_ver}
This package contain the FFmpeg-libswresample shared library

%package libpostproc_%{libpostproc_ver}
Summary: FFmpeg-libpostproc shared library
Group: Development/Libraries

%description libpostproc_%{libpostproc_ver}
This package contain the FFmpeg-libpostproc shared library

%prep
%setup -q
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
            --shlibdir=%{_libdir} --mandir=%{_mandir} \
	--enable-shared \
	--disable-static \
	--enable-runtime-cpudetect \
	--enable-gpl \
	--enable-version3 \
	%{?with_nonfree:--enable-nonfree} \
	--enable-postproc \
	--enable-avfilter \
	--enable-pthreads \
	--enable-x11grab \
	--enable-vdpau \
	\
	--disable-avisynth \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_opencv:--enable-libopencv} \
	--enable-libdc1394 \
	%{?with_nonfree:--enable-libfaac} \
	--enable-libgsm \
	--enable-libmp3lame \
	--enable-libnut \
	--enable-libopencore-amrnb --enable-libopencore-amrwb \
	%{?with_openjpeg:--enable-libopenjpeg} \
	--enable-librtmp \
	%{?with_schroedinger:--enable-libschroedinger} \
	%{?with_speex:--enable-libspeex} \
	--enable-libtheora \
	--enable-libvorbis \
	%{?with_libvpx:--enable-libvpx} \
	%{?with_x264:--enable-libx264} \
	--enable-libxavs \
	--enable-libxvid \
	%{?with_libass:--enable-libass} \
	%{?with_gnutls:--enable-gnutls} \
	%{?with_x265:--enable-libx265} \
%ifarch %ix86
	--extra-cflags="%{optflags}" \
%else
	--extra-cflags="%{optflags} -fPIC" \
%endif
	--enable-stripping \
	%{!?with_v4l:--disable-demuxer=v4l --disable-demuxer=v4l2 --disable-indev=v4l --disable-indev=v4l2} \

make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} incdir=%{buildroot}%{_includedir}/ffmpeg
#mkdir %{buildroot}%{_includedir}/postproc
#ln %{buildroot}%{_includedir}/ffmpeg/postprocess.h %{buildroot}%{_includedir}/postproc

# Remove from the included docs
rm -f doc/Makefile

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING* CREDITS README.md doc/
%{_bindir}/*
#%{_libdir}/vhook
%{_datadir}/ffmpeg
%{_mandir}/man1/ff*.1*
%{_mandir}/man3/lib*.3*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%files libavutil_%{libavutil_ver}
%defattr(-,root,root,-)
%{_libdir}/libavutil.so.*
%{_mandir}/man3/libavutil.3*

%files libavcodec_%{libavcodec_ver}
%defattr(-,root,root,-)
%{_libdir}/libavcodec.so.*
%{_mandir}/man3/libavcodec.3*

%files libavformat_%{libavformat_ver}
%defattr(-,root,root,-)
%{_libdir}/libavformat.so.*
%{_mandir}/man3/libavformat.3*

%files libavdevice_%{libavdevice_ver}
%defattr(-,root,root,-)
%{_libdir}/libavdevice.so.*
%{_mandir}/man3/libavdevice.3*

%files libavfilter_%{libavfilter_ver}
%defattr(-,root,root,-)
%{_libdir}/libavfilter.so.*
%{_mandir}/man3/libavfilter.3*

%files libswscale_%{libswscale_ver}
%defattr(-,root,root,-)
%{_libdir}/libswscale.so.*
%{_mandir}/man3/libswscale.3*

%files libswresample_%{libswresample_ver}
%defattr(-,root,root,-)
%{_libdir}/libswresample.so.*
%{_mandir}/man3/libswresample.3*

%files libpostproc_%{libpostproc_ver}
%defattr(-,root,root,-)
%{_libdir}/libpostproc.so.*

%changelog
* Sun Jun 14 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.7-1
- New upstream release
- Removed dependency on atrpms scritps to comply with ClearOS policy
- Disabled static build and enabled stripping to reduce size

* Tue May 19 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.3-1
- New upstream release

* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.2-3
- Added buildrequirement atrpms-rpm-config

* Fri May 1 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.2-2
- Enabled schroedinger for support of dirac video

* Mon Apr 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.2-1
- New upstream release

* Mon Apr 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.1-2
- New build to test a new version of x265

* Tue Mar 17 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6.1-1
- New upstream release

* Tue Mar 10 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.6-1
- New upstream release

* Mon Feb 16 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.5.4-2
- Removed libavresample as it was not built as expected, libswresample should also be a better alternative

* Sat Feb 14 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.5.4-1
- Based on ATrpms 2.2.x spec file
- Added libavresample
- Added gnutls and libass support
- Added x265
