#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : compat-SDL2-soname1
Version  : 2.0.5
Release  : 10
URL      : https://www.libsdl.org/release/SDL2-2.0.5.tar.gz
Source0  : https://www.libsdl.org/release/SDL2-2.0.5.tar.gz
Source99 : https://www.libsdl.org/release/SDL2-2.0.5.tar.gz.sig
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : CPL-1.0 Zlib
Requires: compat-SDL2-soname1-bin
Requires: compat-SDL2-soname1-lib
BuildRequires : cmake
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-dev32
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32libpulse-simple)
BuildRequires : pkgconfig(32libusb-1.0)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xcursor)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xi)
BuildRequires : pkgconfig(32xinerama)
BuildRequires : pkgconfig(32xkbcommon)
BuildRequires : pkgconfig(32xrandr)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the compat-SDL2-soname1 package.
Group: Binaries

%description bin
bin components for the compat-SDL2-soname1 package.


%package dev
Summary: dev components for the compat-SDL2-soname1 package.
Group: Development
Requires: compat-SDL2-soname1-lib
Requires: compat-SDL2-soname1-bin
Provides: compat-SDL2-soname1-devel

%description dev
dev components for the compat-SDL2-soname1 package.


%package dev32
Summary: dev32 components for the compat-SDL2-soname1 package.
Group: Default
Requires: compat-SDL2-soname1-lib32
Requires: compat-SDL2-soname1-bin
Requires: compat-SDL2-soname1-dev

%description dev32
dev32 components for the compat-SDL2-soname1 package.


%package lib
Summary: lib components for the compat-SDL2-soname1 package.
Group: Libraries

%description lib
lib components for the compat-SDL2-soname1 package.


%package lib32
Summary: lib32 components for the compat-SDL2-soname1 package.
Group: Default

%description lib32
lib32 components for the compat-SDL2-soname1 package.


%prep
%setup -q -n SDL2-2.0.5
pushd ..
cp -a SDL2-2.0.5 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506264585
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DVIDEO_WAYLAND=off -DWAYLAND_SHARED=off
make VERBOSE=1  %{?_smp_mflags}
popd
mkdir clr-build32
pushd clr-build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=32 -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DVIDEO_WAYLAND=off -DWAYLAND_SHARED=off
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1506264585
rm -rf %{buildroot}
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/sdl2-config

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/SDL2/SDL.h
%exclude /usr/include/SDL2/SDL_assert.h
%exclude /usr/include/SDL2/SDL_atomic.h
%exclude /usr/include/SDL2/SDL_audio.h
%exclude /usr/include/SDL2/SDL_bits.h
%exclude /usr/include/SDL2/SDL_blendmode.h
%exclude /usr/include/SDL2/SDL_clipboard.h
%exclude /usr/include/SDL2/SDL_config.h
%exclude /usr/include/SDL2/SDL_config_android.h
%exclude /usr/include/SDL2/SDL_config_iphoneos.h
%exclude /usr/include/SDL2/SDL_config_macosx.h
%exclude /usr/include/SDL2/SDL_config_minimal.h
%exclude /usr/include/SDL2/SDL_config_pandora.h
%exclude /usr/include/SDL2/SDL_config_psp.h
%exclude /usr/include/SDL2/SDL_config_windows.h
%exclude /usr/include/SDL2/SDL_config_winrt.h
%exclude /usr/include/SDL2/SDL_config_wiz.h
%exclude /usr/include/SDL2/SDL_copying.h
%exclude /usr/include/SDL2/SDL_cpuinfo.h
%exclude /usr/include/SDL2/SDL_egl.h
%exclude /usr/include/SDL2/SDL_endian.h
%exclude /usr/include/SDL2/SDL_error.h
%exclude /usr/include/SDL2/SDL_events.h
%exclude /usr/include/SDL2/SDL_filesystem.h
%exclude /usr/include/SDL2/SDL_gamecontroller.h
%exclude /usr/include/SDL2/SDL_gesture.h
%exclude /usr/include/SDL2/SDL_haptic.h
%exclude /usr/include/SDL2/SDL_hints.h
%exclude /usr/include/SDL2/SDL_joystick.h
%exclude /usr/include/SDL2/SDL_keyboard.h
%exclude /usr/include/SDL2/SDL_keycode.h
%exclude /usr/include/SDL2/SDL_loadso.h
%exclude /usr/include/SDL2/SDL_log.h
%exclude /usr/include/SDL2/SDL_main.h
%exclude /usr/include/SDL2/SDL_messagebox.h
%exclude /usr/include/SDL2/SDL_mouse.h
%exclude /usr/include/SDL2/SDL_mutex.h
%exclude /usr/include/SDL2/SDL_name.h
%exclude /usr/include/SDL2/SDL_opengl.h
%exclude /usr/include/SDL2/SDL_opengl_glext.h
%exclude /usr/include/SDL2/SDL_opengles.h
%exclude /usr/include/SDL2/SDL_opengles2.h
%exclude /usr/include/SDL2/SDL_opengles2_gl2.h
%exclude /usr/include/SDL2/SDL_opengles2_gl2ext.h
%exclude /usr/include/SDL2/SDL_opengles2_gl2platform.h
%exclude /usr/include/SDL2/SDL_opengles2_khrplatform.h
%exclude /usr/include/SDL2/SDL_pixels.h
%exclude /usr/include/SDL2/SDL_platform.h
%exclude /usr/include/SDL2/SDL_power.h
%exclude /usr/include/SDL2/SDL_quit.h
%exclude /usr/include/SDL2/SDL_rect.h
%exclude /usr/include/SDL2/SDL_render.h
%exclude /usr/include/SDL2/SDL_revision.h
%exclude /usr/include/SDL2/SDL_rwops.h
%exclude /usr/include/SDL2/SDL_scancode.h
%exclude /usr/include/SDL2/SDL_shape.h
%exclude /usr/include/SDL2/SDL_stdinc.h
%exclude /usr/include/SDL2/SDL_surface.h
%exclude /usr/include/SDL2/SDL_system.h
%exclude /usr/include/SDL2/SDL_syswm.h
%exclude /usr/include/SDL2/SDL_test.h
%exclude /usr/include/SDL2/SDL_test_assert.h
%exclude /usr/include/SDL2/SDL_test_common.h
%exclude /usr/include/SDL2/SDL_test_compare.h
%exclude /usr/include/SDL2/SDL_test_crc32.h
%exclude /usr/include/SDL2/SDL_test_font.h
%exclude /usr/include/SDL2/SDL_test_fuzzer.h
%exclude /usr/include/SDL2/SDL_test_harness.h
%exclude /usr/include/SDL2/SDL_test_images.h
%exclude /usr/include/SDL2/SDL_test_log.h
%exclude /usr/include/SDL2/SDL_test_md5.h
%exclude /usr/include/SDL2/SDL_test_random.h
%exclude /usr/include/SDL2/SDL_thread.h
%exclude /usr/include/SDL2/SDL_timer.h
%exclude /usr/include/SDL2/SDL_touch.h
%exclude /usr/include/SDL2/SDL_types.h
%exclude /usr/include/SDL2/SDL_version.h
%exclude /usr/include/SDL2/SDL_video.h
%exclude /usr/include/SDL2/begin_code.h
%exclude /usr/include/SDL2/close_code.h
%exclude /usr/lib64/libSDL2-2.0.so
%exclude /usr/lib64/libSDL2.so
%exclude /usr/lib64/pkgconfig/sdl2.pc
%exclude /usr/share/aclocal/sdl2.m4

%files dev32
%defattr(-,root,root,-)
%exclude /usr/lib32/libSDL2-2.0.so
%exclude /usr/lib32/libSDL2.so
%exclude /usr/lib32/pkgconfig/32sdl2.pc
%exclude /usr/lib32/pkgconfig/sdl2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2-2.0.so.0.4.1
/usr/lib64/libSDL2-2.0.so.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL2-2.0.so.0.4.1
/usr/lib32/libSDL2-2.0.so.1
