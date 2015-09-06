%bcond_with    nonfree
%bcond_without avisynth
%bcond_without stripping
%bcond_with    dcadec
%bcond_without filecompress
%bcond_without fontconfig
%bcond_without freetype
%bcond_with    gme
%bcond_without gnutls
%bcond_without gsm
%bcond_without ladspa
%bcond_without lame
%bcond_without libass
%bcond_without libbluray
%bcond_without libbs2b
%bcond_without libcaca
%bcond_without libdc1394
%bcond_with    libiconv
%bcond_with    libilbc
%bcond_without libmodplug
%bcond_without libtheora
%bcond_without libv4l
%bcond_without libva
%bcond_without libvdpau
%bcond_without libvorbis
%bcond_without libvpx
%bcond_with    libwebp
%bcond_without opencore
%bcond_without openal
%bcond_with    opencl
%bcond_without opencv
%bcond_without openjpeg
%bcond_without opus
%bcond_without pulseaudio
%bcond_without rtmpdump
%bcond_without schroedinger
%bcond_without speex
%bcond_with    twolame
%bcond_without visualon
%bcond_without x264
%bcond_without x265
%bcond_without xavs
%bcond_without xvid
%bcond_without vidstab

#**********************************************************
# The following libs works in ClearOS 7 but not in ClearOS 6
# Build in ClearOS 6 using: rpmbuild -ba ffmpeg.spec --without frei0r --without libcdio --without soxr --without wavpack
#**********************************************************
%bcond_without frei0r
%bcond_without libcdio
%bcond_without soxr
%bcond_without wavpack


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
Version: 2.7.2
Release: 1%{?dist}
License: GPLv3
Group: System Environment/Libraries
Source: http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
#Source: http://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
URL: http://ffmpeg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: SDL-devel, yasm
%{?with_nonfree:BuildRequires: faac-devel}
%{?with_dcadec:BuildRequires: dcadec-devel}
%{?with_filecompress:BuildRequires: zlib-devel, bzip2-devel, xz-devel}
%{?with_fontconfig:BuildRequires: fontconfig-devel}
%{?with_freetype:BuildRequires: freetype-devel}
%{?with_frei0r:BuildRequires: frei0r-plugins-devel}
%{?with_gme:BuildRequires: gme-devel}
%{?with_gnutls:BuildRequires: gnutls-devel}
%{?with_gsm:BuildRequires: gsm-devel}
%{?with_ladspa:BuildRequires: ladspa-devel}
%{?with_lame:BuildRequires: lame-devel}
%{?with_libass:BuildRequires: libass-devel}
%{?with_libbluray:BuildRequires: libbluray-devel}
%{?with_libbs2b:BuildRequires: libbs2b-devel}
%{?with_libcaca:BuildRequires: libcaca-devel}
%{?with_libcdio:BuildRequires: libcdio-paranoia-devel}
%{?with_libdc1394:BuildRequires: libdc1394-devel, libraw1394-devel}
%{?with_libiconve:BuildRequires: libiconv-devel}
%{?with_libilbc:BuildRequires: libilbc-devel}
%{?with_libmodplug:BuildRequires: libmodplug-devel}
%{?with_libtheora:BuildRequires: libtheora-devel}
%{?with_libv4l:BuildRequires: libv4l-devel}
%{?with_libva:BuildRequires: libva-devel}
%{?with_libvdpau:BuildRequires: libvdpau-devel}
%{?with_libvorbis:BuildRequires: libvorbis-devel}
%{?with_libvpx:BuildRequires: libvpx-devel >= 0.9.6}
%{?with_libwebp:BuildRequires: libwebp-devel}
%{?with_opencore:BuildRequires: opencore-amr-devel}
%{?with_openal:BuildRequires: openal-soft-devel}
%{?with_opencl:BuildRequires: opencl-devel}
%{?with_opencv:BuildRequires: opencv-devel}
%{?with_openjpeg:BuildRequires: openjpeg-devel}
%{?with_opus:BuildRequires: opus-devel}
%{?with_pulseaudio:BuildRequires: pulseaudio-libs-devel}
%{?with_rtmpdump:BuildRequires: rtmpdump-devel >= 2.2.f}
%{?with_schroedinger:BuildRequires: schroedinger-devel}
%{?with_soxr:BuildRequires: soxr-devel}
%{?with_speex:BuildRequires: speex-devel}
%{?with_twolame:BuildRequires: twolame-devel}
%{?with_visualon:BuildRequires: vo-amrwbenc-devel}
%{?with_visualon:%{!?with_nonfree:BuildRequires: vo-aacenc-devel}}
%{?with_wavpack:BuildRequires: wavpack-devel}
%{?with_x264:BuildRequires: x264-devel}
%{?with_x265:BuildRequires: x265-devel}
%{?with_xavs:BuildRequires: xavs-devel}
%{?with_xvid:BuildRequires: xvidcore-devel}
%{?with_vidstab:BuildRequires: vid.stab}
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
Requires: libX11-devel, libXext-devel
%{?with_nonfree:Requires: faac-devel}
%{?with_dcadec:Requires: dcadec-devel}
%{?with_filecompress:Requires: zlib-devel, bzip2-devel, xz-devel}
%{?with_fontconfig:Requires: fontconfig-devel}
%{?with_freetype:Requires: freetype-devel}
%{?with_frei0r:Requires: frei0r-plugins-devel}
%{?with_gme:Requires: gme-devel}
%{?with_gnutls:Requires: gnutls-devel}
%{?with_gsm:Requires: gsm-devel}
%{?with_ladspa:Requires: ladspa-devel}
%{?with_lame:Requires: lame-devel}
%{?with_libass:Requires: libass-devel}
%{?with_libbluray:Requires: libbluray-devel}
%{?with_libbs2b:Requires: libbs2b-devel}
%{?with_libcaca:Requires: libcaca-devel}
%{?with_libcdio:Requires: libcdio-paranoia-devel}
%{?with_libdc1394:Requires: libdc1394-devel, libraw1394-devel}
%{?with_libiconve:Requires: libiconv-devel}
%{?with_libilbc:Requires: libilbc-devel}
%{?with_libmodplug:Requires: libmodplug-devel}
%{?with_libtheora:Requires: libtheora-devel}
%{?with_libv4l:Requires: libv4l-devel}
%{?with_libva:Requires: libva-devel}
%{?with_libvdpau:Requires: libvdpau-devel}
%{?with_libvorbis:Requires: libvorbis-devel}
%{?with_libvpx:Requires: libvpx-devel >= 0.9.6}
%{?with_libwebp:Requires: libwebp-devel}
%{?with_opencore:Requires: opencore-amr-devel}
%{?with_openal:Requires: openal-soft-devel}
%{?with_opencl:Requires: opencl-devel}
%{?with_opencv:Requires: opencv-devel}
%{?with_openjpeg:Requires: openjpeg-devel}
%{?with_opus:Requires: opus-devel}
%{?with_pulseaudio:Requires: pulseaudio-libs-devel}
%{?with_rtmpdump:Requires: rtmpdump-devel >= 2.2.f}
%{?with_schroedinger:Requires: schroedinger-devel}
%{?with_soxr:Requires: soxr-devel}
%{?with_speex:Requires: speex-devel}
%{?with_twolame:Requires: twolame-devel}
%{?with_visualon:Requires: vo-amrwbenc-devel}
%{?with_visualon:%{!?with_nonfree:Requires: vo-aacenc-devel}}
%{?with_wavpack:Requires: wavpack-devel}
%{?with_x264:Requires: x264-devel}
%{?with_x265:Requires: x265-devel}
%{?with_xavs:Requires: xavs-devel}
%{?with_xvid:Requires: xvidcore-devel}
%{?with_vidstab:Requires: vid.stab-devel}

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
%{?with_opus:Requires: opus}

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
%{?with_libcaca:Requires: libcaca}
%{?with_openal:Requires: openal-soft}

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
        %{?with_avisynth:--enable-avisynth} \
	%{?with_nonfree:--enable-libfaac} \
	%{?with_dcadec:--enable-libdcadec} \
	%{?with_filecompress:--enable-zlib --enable-bzlib --enable-lzma} \
	%{?with_fontconfig:--enable-fontconfig} \
	%{?with_freetype:--enable-libfreetype} \
	%{?with_frei0r:--enable-frei0r} \
	%{?with_gme:--enable-libgme} \
	%{?with_gnutls:--enable-gnutls} \
	%{?with_gsm:--enable-libgsm} \
	%{?with_ladspa:--enable-ladspa} \
	%{?with_lame:--enable-libmp3lame} \
	%{?with_libass:--enable-libass} \
	%{?with_libbluray:--enable-libbluray} \
	%{?with_libbs2b:--enable-libbs2b} \
	%{?with_libcaca:--enable-libcaca} \
	%{?with_libcdio:--enable-libcdio} \
	%{?with_libdc1394:--enable-libdc1394} \
	%{?with_libiconve:--enable-libiconv} \
	%{?with_libilbc:--enable-libilbc} \
	%{?with_libmodplug:--enable-libmodplug} \
	%{?with_libtheora:--enable-libtheora} \
	%{?with_libv4l:--enable-libv4l2} \
	%{?with_libvdpau:--enable-vdpau} \
	%{?with_libvorbis:--enable-libvorbis} \
	%{?with_libvpx:--enable-libvpx} \
	%{?with_libwebp:--enable-libwebp} \
	%{?with_opencore:--enable-libopencore-amrnb --enable-libopencore-amrwb} \
	%{?with_openal:--enable-openal} \
	%{?with_opencl:--enable-opencl} \
	%{?with_opencv:--enable-libopencv} \
	%{?with_openjpeg:--enable-libopenjpeg} \
	%{?with_opus:--enable-libopus} \
	%{?with_pulseaudio:--enable-libpulse} \
	%{?with_rtmpdump:--enable-librtmp} \
	%{?with_schroedinger:--enable-libschroedinger} \
	%{?with_soxr:--enable-libsoxr} \
	%{?with_speex:--enable-libspeex} \
	%{?with_twolame:--enable-twolame} \
	%{?with_visualon:--enable-libvo-amrwbenc} \
        %{?with_visualon:%{!?with_nonfree:--enable-libvo-aacenc}} \
	%{?with_wavpack:--enable-libwavpack} \
	%{?with_x264:--enable-libx264} \
	%{?with_x265:--enable-libx265} \
	%{?with_xavs:--enable-libxavs} \
	%{?with_xvid:--enable-libxvid} \
	%{?with_vidstab:--enable-libvidstab} \
%ifarch %ix86
	--extra-cflags="%{optflags}" \
%else
	--extra-cflags="%{optflags} -fPIC" \
%endif
	%{?with_stripping:--enable-stripping} \
	%{!?with_libv4l:--disable-demuxer=v4l --disable-demuxer=v4l2 --disable-indev=v4l --disable-indev=v4l2} \

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
* Tue Jul 21 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.7.2-1
- New upstream release

* Sat Jun 20 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.7.1-1
- New upstream release
- Structured spec file for better readability and prepared for future libs
- Removed obsolete BuildReq imlib2, faad2, a52dec and libnut (xmms not needed anymore)
- Added vid.stab, libbluray, fontconfig, libbs2b, ladspa, libcdio
- Added openal, opus, pulseaudio, soxr, libv4l, vo-amrwbenc, vo-aacenc
- Added libcaca, libwavpack, lzma, zlib

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
