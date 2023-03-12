# w3m

w3m is a pager with WWW capability.

## Description

This repository provides Sailfish OS packaging for w3m.

The w3m application is a pager and/or text-based browser. It can handle
table, cookies, authentication, and almost everything except JavaScript.

## Upstream details

Website: https://sourceforge.net/projects/w3m/

Source code: https://github.com/tats/w3m

Licence: MIT licence, see the upstream/COPYING file.

## Building

To build the Sailfish OS version, you'll need a copy of the Sailfish SDK
(sometimes refered to as the Sailfish Application SDK) installed, with a
suitable target. See https://docs.sailfishos.org/Tools/Sailfish_SDK/ for
more information about this.

The steps below will grab a copy of the w3m source and packaging scripts,
then build the application for Sailfish OS.

You'll also need the bdwgc (libgc) development packages. These aren't
available directly from the Jolla repositories, so the instructions also
clone and build a copy of this library too. In the instructions we use an
output directory so that the bdgwc dependencies can be picked up
automatically.

```
git clone --recursive https://github.com/llewelld/bdwgc.git
git clone --recursive https://github.com/llewelld/w3m.git
mkdir RPMS
sfdk config --global output-prefix=$(pwd)RPMS
cd bdwgc
sfdk build -d -p
cd ../w3m
sfdk build -d -p
cd ..
```

The resulting packages can be found in the RPMS directory.

## Info

Packaged by David Llewellyn-Jones

Website: https://www.flypig.co.uk

