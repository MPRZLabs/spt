# Maintainer: Michał Sidor <michcioperz@autistici.org>
pkgname=python-mprisfy
pkgver=1.5
pkgrel=1
pkgdesc="Commandline tool for controlling Spotify"
arch=('any')
url="http://github.com/michcioperz/spt"
license=('MIT')
groups=()
depends=('python')
makedepends=('git')
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=('git://github.com/michcioperz/spt.git')
md5sums=('SKIP')

package() {
  cd "$srcdir/spt"
  python setup.py install --root="$pkgdir/" --optimize=1
}
