%define upstream_name    Devel-TraceUse
%define upstream_version 2.02

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Hack around calling UNIVERSAL::can() as a function
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/UNIVERSAL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Test::More)
BuildRequires:  perl(Module::Build)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
The UNIVERSAL class provides a few default methods so that all objects can use
them. Object orientation allows programmers to override these methods in
subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants as
functions, bypassing any possible overriding. This is wrong and you should not
do it. Unfortunately, not everyone heeds this warning and their bad code can
break your good code.

Fortunately, this upstream_name replaces UNIVERSAL::can() with a method that checks to
see if the first argument is a valid invocant (whether an object -- a blessed
referent -- or the name of a class). If so, and if the invocant's class has its
own can() method, it calls that as a method. Otherwise, everything works as you
might expect.

If someone attempts to call UNIVERSAL::can() as a function, this upstream_name will
emit a lexical warning (see perllexwarn) to that effect. You can disable it
with no warnings; or no warnings 'UNIVERSAL::isa';, but don't do that; fix the
code instead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*
%{_mandir}/*/*
