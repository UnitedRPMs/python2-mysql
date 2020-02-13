Summary: An interface to MySQL
Name: python2-mysql
Version: 1.4.6
Release: 1%{?dist}
License: GPLv2+
URL: https://github.com/PyMySQL/mysqlclient-python

Source0: %pypi_source mysqlclient

BuildRequires: gcc
BuildRequires: python2-devel 
BuildRequires: python2-setuptools
BuildRequires: mariadb-connector-c-devel 
BuildRequires: openssl-devel zlib-devel
Provides: MySQL-python = %{version}-%{release}

%description
Python2 interface to MySQL

MySQLdb is an interface to the popular MySQL database server for Python.
The design goals are:

-     Compliance with Python database API version 2.0 
-     Thread-safety 
-     Thread-friendliness (threads will not block each other) 

%prep
%autosetup -n mysqlclient-%{version} -p1

%build
%py2_build

%install
%py2_install

%files
%doc README.md doc/*
%license LICENSE

%{python2_sitearch}/MySQLdb/
%{python2_sitearch}/mysqlclient-*-py*.egg-info/


%changelog

* Tue Feb 11 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.4.6-1
- Initial build
