# execute a command
exec { 'pkill killmenow':
  path => '/usr/bin',
}
