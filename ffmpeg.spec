%bcond_with    nonfree
%bcond_without x264
#bcond_without dirac
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


%lib_package avutil 54
%lib_package avcodec 56
%lib_package avformat 56
%lib_package avdevice 56
%lib_package avfilter 5
%lib_package swscale 3
%lib_package swresample 1
%lib_package postproc 53

Summary: Hyper fast MPEG1/MPEG4/H263/RV and AC3/MPEG audio encoder
Name: ffmpeg
Version: 2.5.4
Release: 2%{?dist}
License: GPLv3
Group: System Environment/Libraries
Source: http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
#Source: http://www.ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
URL: http://ffmpeg.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: imlib2-devel, SDL-devel, freetype-devel, zlib-devel, bzip2-devel
BuildRequires: a52dec-devel
BuildRequires: libdc1394-devel, libraw1394-devel
# because pkg-config --libs dirac needs libstdc++
%{?with_dirac:BuildRequires: libstdc++-devel}
%{?with_nonfree:BuildRequires: faac-devel}
BuildRequires: faad2-devel
BuildRequires: gsm-devel
BuildRequires: lame-devel
BuildRequires: libnut-devel
BuildRequires: libtheora-devel, libvorbis-devel
BuildRequires: xvidcore-devel
%{?with_x264:BuildRequires: x264-devel}
%{?with_openjpeg:BuildRequires: openjpeg-devel}
%{?with_dirac:BuildRequires: dirac-devel, schroedinger-devel}
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

Obsoletes: ffmpeg-libs <= %{evr}
%lib_dependencies

%description
FFmpeg is a very fast video and audio converter. It can also grab from a
live audio/video source.
The command line interface is designed to be intuitive, in the sense that
ffmpeg tries to figure out all the parameters, when possible. You have
usually to give only the target bitrate you want. FFmpeg can also convert
from any sample rate to any other, and resize video on the fly with a high
quality polyphase filter.

%devel_extra_Requires zlib-devel, libX11-devel, libXext-devel
%devel_extra_Requires a52dec-devel
%devel_extra_Requires libdc1394-devel, libraw1394-devel
%{?with_nonfree:%devel_extra_Requires faac-devel}
%devel_extra_Requires faad2-devel
%devel_extra_Requires gsm-devel
%devel_extra_Requires lame-devel
%devel_extra_Requires libvorbis-devel, libtheora-devel
%devel_extra_Requires xvidcore-devel
%{?with_x264:%devel_extra_Requires x264-devel}
%{?with_libass:%devel_extra_Requires libass-devel}
%{?with_gnutls:%devel_extra_Requires gnutls-devel}
%{?with_x265:%devel_extra_Requires x265-devel}

%prep
%setup -q
test -f version.h || echo "#define FFMPEG_VERSION \"%{evr}\"" > version.h

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
            --shlibdir=%{_libdir} --mandir=%{_mandir} \
	--enable-shared \
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
	%{?with_dirac:--enable-libdirac} \
	%{?with_nonfree:--enable-libfaac} \
	--enable-libgsm \
	--enable-libmp3lame \
	--enable-libnut \
	--enable-libopencore-amrnb --enable-libopencore-amrwb \
	%{?with_openjpeg:--enable-libopenjpeg} \
	--enable-librtmp \
	%{?with_dirac:--enable-libschroedinger} \
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
	--disable-stripping \
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
#%{_mandir}/man1/lib*.3*


%changelog
* Mon Feb 16 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.5.4-2
- Removed libavresample as it was not built as expected, libswresample should also be a better alternative

* Sat Feb 14 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 2.5.4-1
- Based on ATrpms 2.2.x spec file
- Added libavresample
- Added gnutls and libass support
- Added x265
