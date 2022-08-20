# Script that installs a package, here: puppet-lint

package { 'puppet-lint':
  ensure   => '2.4.2',
  provider => 'gem',
}