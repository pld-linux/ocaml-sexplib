#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Library for serializing OCaml values to and from S-expressions
Summary(pl.UTF-8):	Biblioteka do serializacji wartości OCamlowych do/z S-wyrażeń
Name:		ocaml-sexplib
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/sexplib/tags
Source0:	https://github.com/janestreet/sexplib/archive/v%{version}/sexplib-%{version}.tar.gz
# Source0-md5:	4ad0c908ed9429d91d43381c60a7ff30
URL:		https://github.com/janestreet/sexplib/
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-parsexp-devel >= 0.14
BuildRequires:	ocaml-parsexp-devel < 0.15
BuildRequires:	ocaml-sexplib0-devel >= 0.14
BuildRequires:	ocaml-sexplib0-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
sexplib is a part of Jane Street's Core library. It contains the
functionality for parsing and pretty-printing S-expressions.

This package contains files needed to run bytecode executables using
sexplib library.

%description -l pl.UTF-8
sexplib to część biblioteki podstawowej Jane Street. Zawiera
funkcjonalność analizy i ładnego wypisywania S-wyrażeń.

Ten pakiet zawiera binaria potrzebne do uruchamiania programów
używających biblioteki sexplib.

%package devel
Summary:	Library for serializing OCaml values to and from S-expressions - development part
Summary(pl.UTF-8):	Biblioteka do serializacji wartości OCamlowych do/z S-wyrażeń - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-num-devel
Requires:	ocaml-parsexp-devel >= 0.14
Requires:	ocaml-sexplib0-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
sexplib library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki sexplib.

%prep
%setup -q -n sexplib-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/sexplib/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/sexplib/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/sexplib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md CHANGES.txt COPYRIGHT.txt LICENSE.md LICENSE-Tywith.txt README.org THIRD-PARTY.txt
%dir %{_libdir}/ocaml/sexplib
%{_libdir}/ocaml/sexplib/META
%{_libdir}/ocaml/sexplib/*.cma
%dir %{_libdir}/ocaml/sexplib/num
%{_libdir}/ocaml/sexplib/num/*.cma
%dir %{_libdir}/ocaml/sexplib/unix
%{_libdir}/ocaml/sexplib/unix/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/sexplib/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/sexplib/num/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/sexplib/unix/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/sexplib/*.cmi
%{_libdir}/ocaml/sexplib/*.cmt
%{_libdir}/ocaml/sexplib/*.cmti
%{_libdir}/ocaml/sexplib/*.mli
%{_libdir}/ocaml/sexplib/num/*.cmi
%{_libdir}/ocaml/sexplib/num/*.cmt
%{_libdir}/ocaml/sexplib/num/*.cmti
%{_libdir}/ocaml/sexplib/num/*.mli
%{_libdir}/ocaml/sexplib/unix/*.cmi
%{_libdir}/ocaml/sexplib/unix/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/sexplib/sexplib.a
%{_libdir}/ocaml/sexplib/*.cmx
%{_libdir}/ocaml/sexplib/*.cmxa
%{_libdir}/ocaml/sexplib/num/sexplib_num.a
%{_libdir}/ocaml/sexplib/num/*.cmx
%{_libdir}/ocaml/sexplib/num/*.cmxa
%{_libdir}/ocaml/sexplib/unix/sexplib_unix.a
%{_libdir}/ocaml/sexplib/unix/*.cmx
%{_libdir}/ocaml/sexplib/unix/*.cmxa
%endif
%{_libdir}/ocaml/sexplib/dune-package
%{_libdir}/ocaml/sexplib/opam
