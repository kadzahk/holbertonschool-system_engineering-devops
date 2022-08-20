# Script that installs a package, here: flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}