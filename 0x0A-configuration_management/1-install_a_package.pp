# install a package
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  before   => Package['flask'],
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
